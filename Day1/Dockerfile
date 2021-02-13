FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y vim git python3 python3-pip python3-dev sqlite3

RUN git clone https://github.com/SotaMatsuzawa/MLOps_tutorial.git /home/MLOps_tutoraial

WORKDIR /home/MLOps_tutorial
RUN pip3 install -r requirments.txt


