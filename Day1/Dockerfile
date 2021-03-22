FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y vim git python3 python3-pip python3-dev sqlite3

RUN git clone https://github.com/SotaMatsuzawa/MLOps_tutorial.git /home/MLops_tutorial

WORKDIR /home
RUN pip3 install -r MLops_tutorial/Day1/requirments.txt