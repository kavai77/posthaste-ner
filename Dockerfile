FROM python:3.12.3-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV TRANSFORMERS_OFFLINE=1
RUN pytest -disable-warnings
CMD ["uvicorn", "ner:app", "--host", "0.0.0.0", "--port", "8000"]