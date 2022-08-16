FROM python:3.8

RUN mkdir -p /home/bybit-profit-loss
WORKDIR /home/bybit-profit-loss

COPY requirements.txt /home/bybit-profit-loss

RUN pip install -r /home/bybit-profit-loss/requirements.txt

COPY . /home/bybit-profit-loss