FROM python:3.9.5-alpine3.13

WORKDIR /app

COPY . .

ENTRYPOINT [ "python3", "-u", "tuto_680.py" ]

