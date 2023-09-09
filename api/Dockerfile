# /api/Dockerfile
FROM python:3.9

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SECRET_KEY=ghjv5wa9UQBfUHatHXDRabu2Dj4BaxRqpAFMD5Ndd3E4M
ENV DEBUG=False
ENV DEVELOPMENT_MODE=False

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


# COPY . /app/

# CMD [ "python", "manage.py", "runserver", "8100" ]

EXPOSE 8100
EXPOSE 3000
