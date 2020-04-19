FROM ubuntu:18.04

MAINTAINER Anthony Mendez "anthonymendez9@gmail.com"

RUN apt-get update -y && \
    apt-get install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get install python3.8 -y && \
    apt-get install python3.8-dev -y && \
    apt-get install build-essential -y && \
    apt-get install libssl-dev -y && \
    apt-get install libffi-dev -y && \
    apt-get install libxml2-dev -y && \
    apt-get install libxslt1-dev -y && \
    apt-get install zlib1g-dev -y
RUN apt-get install python3-pip -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN python3.8 -m pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3.8" ]

CMD [ "debug.py" ]