FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# running the tests will make sure, it will download the models from huggingface and build the image with the downloaded models already
RUN pytest
CMD ["uvicorn", "ner:app", "--host", "0.0.0.0", "--port", "8000"]
