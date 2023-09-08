FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /service
COPY APIGateway/ /service/APIGateway/
WORKDIR /service/APIGateway
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=app.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]