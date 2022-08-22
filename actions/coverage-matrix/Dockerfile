FROM python:3.8

RUN apt update
RUN apt install -y git

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY run.py /run.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]