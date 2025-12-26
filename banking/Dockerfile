FROM ubuntu:22.04
MAINTAINER hellojuntae

RUN apt update
RUN apt install -y xinetd
ENV TERM=linux

RUN useradd banking

ADD xinetd /etc/xinetd.d/
ADD share /home/banking

RUN chmod 460 /home/banking/*

RUN chown banking:root /home/banking/*
RUN chmod +x /home/banking/banking
RUN chmod +x /home/banking/run.sh

CMD ["/usr/sbin/xinetd","-dontfork"]