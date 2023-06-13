from datetime import datetime, timedelta
from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/health_check")
async def health_check():
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    requests.get(url="https://fastapi.tiangolo.com/lo/")
    return {"message": "health_check"}

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=8000, reload=True)