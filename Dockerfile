FROM python:3.8-slim-buster
LABEL mantainer="Agustin Rodriguez <gus990@gmail.com>"

COPY . /app
WORKDIR /app

RUN apt-get update && \
    apt-get -y install gcc && \
    rm -rf /var/lib/apt/lists/*

RUN pip install \
    fastapi \
    uvicorn \
    requests \
    email-validator \
    python-dateutil

CMD ["uvicorn", "ecoapi.main:app", "--host", "0.0.0.0", "--port", "8000"]