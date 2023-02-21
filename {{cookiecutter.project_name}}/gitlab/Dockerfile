ARG PYTHON_FLAVOR=alpine
# TODO: there is an issue with dependencies installation in the alpine flavor
#FROM python:3.8-${PYTHON_FLAVOR}
FROM python:3.8

COPY requirements_dev.txt requirements_dev.txt
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements_dev.txt
