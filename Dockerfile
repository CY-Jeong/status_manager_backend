FROM python:3.10-slim

WORKDIR /usr/src/app/

COPY . .
 
RUN apt-get update && \
    python -m pip install --upgrade pip && \
    pip install -r requirements.txt

ENV TZ=Asia/Seoul
ENV PORT="8080"


