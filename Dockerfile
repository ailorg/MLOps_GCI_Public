FROM ubuntu:latest
 
RUN apt-get update && apt-get install -y \
        vim \
        git \
        lsof \
        python3 \
        python3-pip \
        python3-dev \
        sqlite3
 
WORKDIR home/
 
COPY . .
 
RUN pip3 install -r requirments.txt
