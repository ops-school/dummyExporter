FROM alpine:latest

RUN apk update && \
    apk add python3 

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /dummyExporter/requirements.txt

WORKDIR /dummyExporter

RUN pip3 install -r requirements.txt

COPY . /dummyExporter

ENTRYPOINT [ "python3" ]

CMD [ "dummyExporter.py" ]
