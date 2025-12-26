FROM ubuntu:22.04
MAINTAINER hellojuntae

RUN apt update
RUN apt install -y xinetd
ENV TERM=linux

RUN useradd getsputs

ADD xinetd /etc/xinetd.d/
ADD share /home/getsputs

RUN chmod 460 /home/getsputs/*

RUN chown getsputs:root /home/getsputs/*
RUN chmod +x /home/getsputs/getsputs
RUN chmod +x /home/getsputs/run.sh

CMD ["/usr/sbin/xinetd","-dontfork"]