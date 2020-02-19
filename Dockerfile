FROM python:3.8-slim

COPY . .

RUN pip install --no-cache-dir Flask && \
    pip install --no-cache-dir mysql-connector

EXPOSE 5000

CMD ["python3", "server.py"]

