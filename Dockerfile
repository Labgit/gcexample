FROM python:3.8

CMD mkdir /gcexample/gcexample /gcexample/tests
WORKDIR /gcexample

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY gcexample gcexample
COPY tests tests
COPY boot.sh ./

RUN chmod +x boot.sh

WORKDIR /gcexample/gcexample
EXPOSE 5000
ENTRYPOINT ["../boot.sh"]