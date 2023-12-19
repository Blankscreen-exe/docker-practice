FROM python:3.8

WORKDIR /app

COPY server.py /app/server.py

RUN pip install websockets

CMD ["python", "server.py"]
