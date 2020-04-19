FROM golang:1.13

WORKDIR /go/src/app
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...

RUN apt-get update && apt-get install -y \
    vim \
    python3 \
    python3-pip \
    lilypond && \
    pip3 install -r requirements.txt && \
    alias python=python3


CMD ["go","run","server/src/server.go"]