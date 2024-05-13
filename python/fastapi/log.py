import logging

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