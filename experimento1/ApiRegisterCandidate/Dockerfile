FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /service
COPY ApiRegisterCandidate/ /service/ApiRegisterCandidate/
WORKDIR /service/ApiRegisterCandidate
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 5001
ENV FLASK_APP=app.py
ENTRYPOINT [ "flask", "run", "-p 5001", "--host=0.0.0.0"]