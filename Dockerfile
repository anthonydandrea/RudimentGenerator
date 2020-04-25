FROM golang:1.13

WORKDIR /go/src/app
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...

RUN apt-get update && apt-get install -y \
    vim \
    cron \
    python3 \
    python3-pip \
    lilypond && \
    pip3 install -r requirements.txt && \
    alias python=python3


# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Setup cron job
RUN (crontab -l ; echo "0 */6 * * * rm static/rudiments/ >> /var/log/cron.log") | crontab

ADD docker_start.sh /
RUN chmod +x /docker_start.sh

# CMD ["./docker_start.sh"]
CMD ["go", "run", "server/src/server.go"]