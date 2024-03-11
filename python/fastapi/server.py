import os
import logging
import hashlib
from datetime import datetime, timedelta
from loguru import logger as loguru_logger
from fastapi import FastAPI, HTTPException, Request
import uvicorn
import requests
from starlette.responses import HTMLResponse
from models import Result
import csv

logging_logger = logging.getLogger()
logging_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logging_logger.addHandler(stream_handler)

app = FastAPI(title="whatap-fastapi")

@app.get("/health_check", tags=["trace"])
async def health_check():
    logging_logger.info("this is logging_logger_message")
    loguru_logger.info(f"this is loguru_logger_message")
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    requests.get(url="https://fastapi.tiangolo.com/lo/")
    return {"message": "health_check"}

@app.get("/whatap_test")
async def whatap_test(req:Request):
    logging_logger.info("start:health_test")
    message = str(dict(req.headers))
    message = message.replace('{', '')
    message = message.replace('}', '')
    message = message.replace("'", '')

    logging_logger.info(f"message:{message}")
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    res = requests.get(url="https://www.naver.com")
    return {"test": "test"}

@app.get("/error_check", tags=["trace"])
async def error_check():
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    requests.get(url="https://www.naver.com")
    raise HTTPException(status_code=400)

@app.get("/use_memory", tags=["trace"])
def use_memory():
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    test_list = []
    for i in range(0, 10000000):
        test_list.append(i)
    return HTMLResponse(status_code=200)

@app.get("/log", tags=["trace"])
def log():
    for i in range(0, 10000):
        print(f"10000_WHATAP_JYKIM_LOGTEST:{i}")
    return HTMLResponse(status_code=200)

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=8000, reload=True)