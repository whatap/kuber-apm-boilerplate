from flask import Flask
import logging
import requests
logging_logger = logging.getLogger()
logging_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logging_logger.addHandler(stream_handler)

app = Flask(__name__)

@app.route("/health_check")
def hello_world():
    logging_logger.info("hey I am your favourite log message")
    return "<p>Hello, World!</p>"

@app.route("/f5/system")
def f5_topology_system():
    url = "http://www.naver.com"
    requests.get(url=url)
    return {"message": "/f5/system"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)