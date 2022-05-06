FROM python:3.9.6

WORKDIR /Service_4

COPY . /app/

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
