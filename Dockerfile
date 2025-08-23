FROM python:3.9.6-slim

WORKDIR /app

ENV TRANSFORMERS_OFFLINE=1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "ner:app", "--host", "0.0.0.0", "--port", "8000"]