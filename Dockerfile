FROM python:3
ADD . /moe
WORKDIR /moe
RUN pip install -r requirements.txt
