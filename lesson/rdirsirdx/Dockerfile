FROM ubuntu:22.04
MAINTAINER hellojuntae

RUN apt update
RUN apt install -y xinetd
ENV TERM=linux

RUN useradd rdirsirdx

ADD xinetd /etc/xinetd.d/
ADD share /home/rdirsirdx

RUN chmod 460 /home/rdirsirdx/*

RUN chown rdirsirdx:root /home/rdirsirdx/*
RUN chmod +x /home/rdirsirdx/rdirsirdx
RUN chmod +x /home/rdirsirdx/run.sh

CMD ["/usr/sbin/xinetd","-dontfork"]