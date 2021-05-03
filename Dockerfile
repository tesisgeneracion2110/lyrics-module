FROM python:3.7.10-slim


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /sample/requirements.txt

WORKDIR /sample

RUN pip3 install -r requirements.txt
    sudo apt update
    sudo apt install python3-dev python3-pip python3-venv
    python3 -m venv --system-site-packages ./venv
    source ./venv/bin/activate
    pip3 install --upgrade pip
    pip3 install --user --upgrade tensorflow

COPY . /sample

ENTRYPOINT [ "python" ]

CMD [ "__init__.py" ]