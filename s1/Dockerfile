FROM python:latest

RUN mkdir /opt/pgn/

COPY . /opt/pgn/

WORKDIR /opt/pgn/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
