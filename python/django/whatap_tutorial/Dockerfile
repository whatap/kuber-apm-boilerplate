FROM python:3.10
WORKDIR /app

ADD . /app/
RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh
CMD ["./entrypoint.sh"]
