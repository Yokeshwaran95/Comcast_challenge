FROM golang:1.16-alpine
ARG environ
RUN cd golang 
WORKDIR /app


COPY file.txt ./
COPY file-${environ}.txt ./
COPY *.go ./

RUN go build server.go

EXPOSE 8080

CMD [ "/server " ]