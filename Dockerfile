FROM python:3

RUN pip install flask
RUN pip install flask_restful
RUN pip install pystrich

ADD app.py /

EXPOSE 5000

ENTRYPOINT [ "python", "./app.py" ]