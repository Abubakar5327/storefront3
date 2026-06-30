FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update \
  && apt-get install python3-dev default-libmysqlclient-dev gcc -y

RUN pip install --upgrade pip 
RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --dev

COPY . /app/

RUN chmod +x docker-entrypoint.sh

EXPOSE 8000

CMD ["./docker-entrypoint.sh"]