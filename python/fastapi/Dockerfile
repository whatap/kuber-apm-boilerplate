FROM python:3.10
EXPOSE 80
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh
RUN ls -l
RUN chmod -R 777 /app
CMD ["./entrypoint.sh"]
