FROM python:2.7.13-wheezy

Add . /pillbox
WORKDIR /pillbox

RUN pip install -r requirements.txt

