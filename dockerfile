#DockerFile.base

FROM ubuntu:16.04
MAINTAINER dbwodud34@gmail.com

RUN apt-get -y update
RUN apt-get -y dist-upgrade
RUN apt-get install -y python-pip git vim

#도커 설치
RUN apt-get install docker

#장고 설치
CMD pip install django