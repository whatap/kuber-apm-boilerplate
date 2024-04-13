import logging
from datetime import datetime, timedelta
from pydantic import BaseModel
from enum import Enum
import uvicorn
import requests
from config import config
from fastapi import FastAPI, Query, HTTPException, Path
from fastapi.responses import JSONResponse
import pymysql
import pymysql.cursors

logging_logger = logging.getLogger()
logging_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logging_logger.addHandler(stream_handler)

DATABASE_CONFIG = {
    'host': config.MysqlConfig().host,
    'user': config.MysqlConfig().user,
    'password': config.MysqlConfig().password,
    'database': config.MysqlConfig().database
}

# Connect to the MySQL database
class Owner(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: str
    city: str
    telephone: str

# Enum for allowed page sizes
class PageSize(Enum):
    ten = 10
    twenty = 20
    thirty = 30

# Pydantic model for the veterinarian data
class Vet(BaseModel):
    id: int
    first_name: str
    last_name: str
    specialties: str  # Concatenated string of specialties


# Connect to the MySQL database
def get_database_connection():
    try:
        connection = pymysql.connect(**DATABASE_CONFIG)
        return connection
    except Exception as e:
        print("Error while connecting to MySQL", e)
        raise HTTPException(status_code=500, detail="Database connection failed")


app = FastAPI(title="whatap-fastapi")
print(f"config.project_dir={config.project_dir}")

@app.get("/health_check", tags=["trace"])
async def health_check():
    logging_logger.info("this is logging_logger_message")
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    requests.get(url="https://fastapi.tiangolo.com/lo/")
    return {"message": "health_check"}

# Get the list of owners with pagination
def valid_page_size(page_size: int = 10):
    if page_size not in (10, 20, 30):
        raise ValueError("page_size must be 10, 20, or 30")
    return page_size

# Get the list of owners with pagination
@app.get("/petclinic/owners", tags=["owner"], response_model=dict)
def get_owners(page: int = Query(1, alias='page'), page_size: int = Query(default=10, alias='page_size', ge=10, le=30, description="Must be 10, 20, or 30")):
    try:
        valid_page_size(page_size)  # Custom validation function call
    except Exception as e:
        return JSONResponse(status_code=404, content={"success": False, "message": str(e)})
    connection = get_database_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    offset = (page - 1) * page_size
    query = f"SELECT id, first_name, last_name, address, city, telephone FROM owners LIMIT {page_size} OFFSET {offset}"
    try:
        cursor.execute(query)
        owners = cursor.fetchall()
        return {"success": True, "items": owners}
    except Exception as e:
        print("Failed to read data from MySQL table", e)
        return JSONResponse(status_code=404, content={"success": False, "message": "Owner not found"})
    finally:
        cursor.close()
        connection.close()

@app.get("/petclinic/owners/{id}", tags=["owner"], response_model=dict)
def get_owner(id: int = Path(..., description="The ID of the owner to retrieve", gt=0)):
    connection = get_database_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    query = f"SELECT id, first_name, last_name, address, city, telephone FROM owners WHERE id = {id}"
    try:
        cursor.execute(query)
        owner = cursor.fetchone()
        if owner:
            return {"success": True, "item": owner}
        else:
            return {"success": False, "message": "Owner not found"}
    except Exception as e:
        print("Failed to read data from MySQL table", e)
        return JSONResponse(status_code=404, content={"success": False, "message": str(e)})
        #raise HTTPException(status_code=500, detail="Failed to fetch data")
    finally:
        cursor.close()
        connection.close()

# Endpoint to get list of veterinarians with their specialties
@app.get("/petclinic/vets", tags=["vet"], response_model=dict)
def get_vets(page: int = Query(1, alias='page'), page_size: int = Query(default=10, alias='page_size', ge=10, le=30, description="Must be 10, 20, or 30")):
    try:
        valid_page_size(page_size)  # Custom validation function call
    except Exception as e:
        return {"failed":False, "message": str(e)}
    connection = get_database_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    offset = (page - 1) * page_size
    query = f"""
    SELECT v.id AS id, v.first_name, v.last_name, 
           GROUP_CONCAT(s.name ORDER BY s.name SEPARATOR ', ') AS specialties
    FROM vets v
    LEFT JOIN vet_specialties vs ON v.id = vs.vet_id
    LEFT JOIN specialties s ON vs.specialty_id = s.id
    GROUP BY v.id, v.first_name, v.last_name
    LIMIT {page_size} OFFSET {offset};
    """
    try:
        cursor.execute(query)
        vets = cursor.fetchall()
        return {"success": True, "items": vets}
    except Exception as e:
        print("Failed to read data from MySQL table", e)
        return JSONResponse(status_code=404, content={"success": False, "message": str(e)})
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=8000, reload=True)