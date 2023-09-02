import os
import logging
import hashlib
from datetime import datetime, timedelta
from loguru import logger as loguru_logger
from fastapi import FastAPI, HTTPException
import uvicorn
import requests
from starlette.responses import HTMLResponse
from kubernetes import client, config, watch

logging_logger = logging.getLogger()
logging_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logging_logger.addHandler(stream_handler)

config.load_kube_config()
batch_v1 = client.BatchV1Api()

app = FastAPI()
@app.get("/health_check")
async def health_check():
    logging_logger.info("this is logging_logger_message")
    loguru_logger.info(f"this is loguru_logger_message")
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    requests.get(url="https://fastapi.tiangolo.com/lo/")
    return {"message": "health_check"}

@app.get("/error_check")
async def error_check():
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    requests.get(url="https://www.naver.com")
    raise HTTPException(status_code=400)

@app.get("/use_memory")
def use_memory():
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    test_list = []
    for i in range(0, 10000000):
        test_list.append(i)
    return HTMLResponse(status_code=200)

@app.post("/k8s/job/{hashtag}")
def k8s_trigger_job(hashtag):
    try:
        job_hash = int(hashlib.sha256(hashtag.encode('utf-8')).hexdigest(), 16) % 10**8
    except Exception as e:
        job_hash = 00000000
    stime = int(datetime.now().timestamp())
    JOB_NAME = f"job-{job_hash}-{stime}"
    WHATAP_SERVER_HOST = os.getenv("WHATAP_SERVER_HOST")
    WHATAP_LICENSE = os.getenv("WHATAP_LICENSE")
    WHATAP_APP_NAME = f"HASHTAG_SEARCH_{hashtag}"
    WHATAP_LOGGING_ENABLED = os.getenv("WHATAP_LOGGING_ENABLED")

    NODE_IP = client.V1EnvVarSource(field_ref=client.V1ObjectFieldSelector(field_path="status.hostIP"))
    NODE_NAME = client.V1EnvVarSource(field_ref=client.V1ObjectFieldSelector(field_path="spec.nodeName"))
    POD_NAME = client.V1EnvVarSource(field_ref=client.V1ObjectFieldSelector(field_path="metadata.name"))
    def create_job_object():
        # Configurate Pod template container
        container = client.V1Container(
            name='agent-python-method',
            image='whatap/agent-python-method:latest',
            env=[
                client.V1EnvVar(name="WHATAP_SERVER_HOST", value=WHATAP_SERVER_HOST),
                client.V1EnvVar(name="WHATAP_LICENSE", value=WHATAP_LICENSE),
                client.V1EnvVar(name="WHATAP_LOGGING_ENABLED", value=WHATAP_LOGGING_ENABLED),
                client.V1EnvVar(name="HASHTAG", value=hashtag),
                client.V1EnvVar(name="WHATAP_APP_NAME", value=WHATAP_APP_NAME),
                client.V1EnvVar(name="NODE_IP", value_from=NODE_IP),
                client.V1EnvVar(name="NODE_NAME", value_from=NODE_NAME),
                client.V1EnvVar(name="POD_NAME", value_from=POD_NAME)
                ]
        )

        # Create and configurate a spec section
        template = client.V1PodTemplateSpec(
            spec=client.V1PodSpec(restart_policy='Never', containers=[container]))
        # Create the specification of deployment
        spec = client.V1JobSpec(template=template)
        # Instantiate the job object
        job = client.V1Job(
            api_version='batch/v1',
            kind='Job',
            metadata=client.V1ObjectMeta(name=JOB_NAME),
            spec=spec)
        return job
    def create_job(api_instance, job):
        api_response = api_instance.create_namespaced_job(
            body=job,
            namespace='jobs')
        print("Job created. status='%s'" % str(api_response.status))
    def delete_job(api_instance):
        api_response = api_instance.delete_namespaced_job(
            name=JOB_NAME,
            namespace='jobs',
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=0))
        print("Job deleted. status='%s'" % str(api_response.status))

    job = create_job_object()
    create_job(api_instance=batch_v1, job=job)


if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=8000, reload=True)