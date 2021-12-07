FROM python:3.8-slim

RUN pip install "fastapi[all]"

COPY . /app

CMD tail -f /dev/null
