FROM python:3.11.5

WORKDIR /app
COPY ./requirements.txt /app

RUN pip install -U pip
RUN pip install -r requirements.txt

ENV PORT=8089 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1

EXPOSE 8089