FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Asia/Tokyo
RUN apt-get update && \
  apt-get install -y --no-install-recommends tzdata

RUN apt-get update && apt-get install -y \
        vim \
        git \
        lsof \
        python3 \
        python3-pip \
        python3-dev \
        sqlite3 \
        expect

WORKDIR home/

COPY . .

RUN pip3 install -r requirments.txt
