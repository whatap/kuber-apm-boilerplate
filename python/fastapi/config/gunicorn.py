"""gunicorn ASGI server configuration."""
import os
from src.utils import get_project_dir
from log import logger
from multiprocessing import cpu_count

# 서버 시작 시 단 한번만 작동
def on_starting(server):
    master_pid = str(os.getpid())
    with open(f"{get_project_dir()}/run/gunicorn.pid", mode="a+") as f:
        # 파일의 시작점으로 간다.
        f.seek(0)

        # 이전 내용을 모두 삭제한다.
        f.truncate(0)

        # 운영환경의 pid 를 입력한다.
        f.write(f"{master_pid}")
        logger.debug(f"master_pid:{master_pid}")

# 워커 생성될 시기에 작동
def post_worker_init(worker):
    logger.debug("post_worker_init")
    worker_pid = str(os.getpid())
    with open(f"{get_project_dir()}/run/gunicorn.pid", mode="a") as f:
        # 마스터 pid 가 파일에 써지고 호출되기 때문에 운영환경의 pid 를 추가로 입력하면 된다.
        f.write(f" {worker_pid}")
        logger.debug(f"worker_pid:{worker_pid}")

#서버 종료 시 작동
def on_exit(server):
    with open(f"{get_project_dir()}/run/gunicorn.pid", mode="a+") as f:
        # 파일의 시작점으로 간다.
        f.seek(0)

        # 이전 내용을 모두 삭제한다.
        f.truncate(0)

def max_workers():
    return 2*cpu_count()+1
    # return 1
    # return 10


def min_workers():
    return 1

bind = '0.0.0.0:9000'
max_requests = 1000
worker_class = 'uvicorn.workers.UvicornWorker'
workers = max_workers()
timeout = 60
accesslog = 'run/gunicorn.access.log'
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%(D)s"'
access_log_format = '%(h)s %(l)s %(t)s "%(r)s" %(s)s %(b)s "%(a)s" "%(M)s ms"'
errorlog = 'run/gunicorn.error.log'
pidfile = 'run/gunicorn.pid'
daemon = False
reload = False
