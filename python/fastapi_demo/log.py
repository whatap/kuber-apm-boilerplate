import logging
from src.utils import get_project_dir

project_dir = get_project_dir()
FORMAT = '%(module)s.%(funcName)s - %(message)s - %(levelname)s - %(asctime)s %(lineno)s'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False

# 로그를 콘솔에 출력하는 Handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
STREAM_FORMAT = FORMAT
stream_log_formatter = logging.Formatter(STREAM_FORMAT)
stream_handler.setFormatter(stream_log_formatter)
logger.addHandler(stream_handler)


##File handler
filename = f"{project_dir}/app_logs/app.log"
file_handler = logging.FileHandler(filename=filename, mode="a")
file_handler.setLevel(logging.INFO)
FORMAT = FORMAT
file_log_formatter = logging.Formatter(FORMAT)
file_handler.setFormatter(file_log_formatter)
logger.addHandler(file_handler)