FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install wget

RUN apt-get update
RUN apt-get install -y nano
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-venv

RUN git clone https://github.com/tesisgeneracion2110/lyrics-module.git
RUN cd lyrics-module &&\
    pip3 install -r requirements.txt &&\
#    python3 setup.py develop
    python3 -m venv --system-site-packages ./venv
#    source ./venv/bin/activate
#RUN pip3 install -y --upgrade pip
#RUN pip3 install -y --user --upgrade tensorflow

#ENTRYPOINT [ "python3" ]

