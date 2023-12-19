FROM python:3.8

WORKDIR /app

COPY client.py /app/client.py

RUN pip install websockets

CMD ["python", "client.py"]
