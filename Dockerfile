FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install wget

RUN apt-get update
RUN apt-get install -y nano
RUN apt install python3
RUN apt install -y python3-pip

RUN git clone https://github.com/tesisgeneracion2110/lyrics-module.git
RUN cd lyrics-module
RUN git checkout feature/WebService

RUN pip3 install -r requirements.txt
RUN apt update
RUN python3 setup.py develop
RUN apt install python3-venv
RUN python3 -m venv --system-site-packages ./venv
RUN source ./venv/bin/activate
RUN pip3 install --upgrade pip
RUN pip3 install --user --upgrade tensorflow

ENTRYPOINT [ "python3" ]
