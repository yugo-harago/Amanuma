# /api/Dockerfile
FROM python:3.9

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SECRET_KEY=ghjv5wa9UQBfUHatHXDRabu2Dj4BaxRqpAFMD5Ndd3E4M
ENV DEBUG=TRUE
ENV YOUTUBE_API_KEY=AIzaSyAG6Ovrn6TEDrweO5BNJDzR1CZLsBiqlTA
ENV DEVELOPMENT_MODE=False
ENV DJANGO_ALLOWED_HOSTS=*

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt


# COPY . /app/

# CMD [ "python", "manage.py", "runserver", "8100" ]

EXPOSE 8100
EXPOSE 3000
