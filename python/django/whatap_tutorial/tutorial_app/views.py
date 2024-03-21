import os
import time

from django.shortcuts import render
import requests
from django.http import HttpResponse
import logging
from loguru import logger as loguru_logger
# Create your views here.

logging_logger = logging.getLogger()
logging_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logging_logger.addHandler(stream_handler)

def home(request):
    logging_logger.info("home")
    loguru_logger.info(f"home")
    print(f"test:home:{os.environ}")
    return HttpResponse(f"home")

def health_check(request):
    logging_logger.info("health_check-logging-test")
    loguru_logger.info(f"health_check-loguru-test")
    url = "https://www.naver.com"
    requests.get(url=url)
    return HttpResponse(f"health_check")

def active_stack_check(request):
    logging_logger.info("active_stack_check-logging-test")
    loguru_logger.info(f"active_stack_check-loguru-test")
    time.sleep(8)
    url = "https://www.naver.com"
    requests.get(url=url)
    return HttpResponse(f"health_check")

def error_check(request):
    logging_logger.info("error-check-logging-test")
    loguru_logger.info(f"error-check-loguru-test")
    url = "https://www.naver.com"
    requests.get(url=url)
    return HttpResponse(status=400)

