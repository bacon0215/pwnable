FROM ubuntu:22.04
MAINTAINER hellojuntae

RUN apt update
RUN apt install -y xinetd
ENV TERM=linux

RUN useradd shellcode

ADD xinetd /etc/xinetd.d/
ADD share /home/shellcode

RUN chmod 460 /home/shellcode/*

RUN chown shellcode:root /home/shellcode/*
RUN chmod +x /home/shellcode/shellcode
RUN chmod +x /home/shellcode/run.sh

CMD ["/usr/sbin/xinetd","-dontfork"]