FROM python:3.10.9-slim-bullseye

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

CMD python3 /app/webserv.py

