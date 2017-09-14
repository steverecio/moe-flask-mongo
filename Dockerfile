FROM python:2.7
ADD . /moe
WORKDIR /moe
RUN pip install -r requirements.txt
