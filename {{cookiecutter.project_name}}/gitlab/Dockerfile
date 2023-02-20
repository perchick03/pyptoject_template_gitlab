ARG PYTHON_FLAVOR=alpine
FROM python:3.8-${PYTHON_FLAVOR}

COPY requirements_dev.txt requirements_dev.txt
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements_dev.txt
