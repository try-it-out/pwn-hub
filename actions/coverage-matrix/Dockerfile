FROM python:3.7-alpine

RUN apk add --no-cache git build-base python3-dev
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY run.py /run.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]