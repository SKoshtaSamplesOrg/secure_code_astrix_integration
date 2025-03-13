FROM python:3.14.0a5-slim
LABEL authors="shubhrakoshta"

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV USER_NAME test_user
ENV PASSWORD "vS7xQj^2m0L@i90"

CMD["python", "main.py"]