FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y vim git python3 python3-pip python3-dev sqlite3