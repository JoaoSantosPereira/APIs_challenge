FROM python:3.9-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

EXPOSE 5000

CMD ["python", "app.py"]