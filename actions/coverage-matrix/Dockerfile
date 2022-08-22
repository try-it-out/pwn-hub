FROM centos:centos7

RUN yum -y install epel-release && yum clean all
RUN yum -y install python-pip && yum clean all
RUN yum install -y git && yum clean all

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY run.py /run.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]