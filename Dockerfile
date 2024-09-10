FROM python:3.12-slim

RUN mkdir -p /app/logs

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "main.py" ]
