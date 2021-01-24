FROM python:3.6
ADD . /app
WORKDIR /app
RUN pip install -r package.txt