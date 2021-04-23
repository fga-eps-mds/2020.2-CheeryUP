FROM python:3

EXPOSE 8000

RUN mkdir /src

WORKDIR /src


COPY src /src

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED 1

