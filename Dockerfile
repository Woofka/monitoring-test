FROM python:3.8.5

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -q -r /app/requirements.txt

ENTRYPOINT ["python3"]
