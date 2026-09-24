FROM python:3.12-slim

WORKDIR /app

COPY processor.py .

RUN mkdir -p /app/data

CMD ["python", "-u", "processor.py"]