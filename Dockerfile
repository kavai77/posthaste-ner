FROM huggingface/transformers-pytorch-cpu:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV TRANSFORMERS_OFFLINE=1
RUN pytest
CMD ["uvicorn", "ner:app", "--host", "0.0.0.0", "--port", "8000"]
