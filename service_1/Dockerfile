FROM python:3.6.9
WORKDIR /service_1
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]

