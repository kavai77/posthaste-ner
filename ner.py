from fastapi import FastAPI
from gliner import GLiNER
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import re

model = GLiNER.from_pretrained("urchade/gliner_large-v2.1", cache_dir="./.models")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

labels = ["postcode", "city", "country", "state", "address", "phone", "email", "weight", "dimensions", "item", "recipient"]
numeric_labels = ["number"]
dimension_labels = ["length", "width", "height"]

class TextRequest(BaseModel):
    text: str

@app.post("/extract")
async def extract_entities(request: TextRequest):
    entities = model.predict_entities(request.text, labels)
    result = {entity["label"]: entity["text"] for entity in entities}
    if "dimensions" in result:
        dimension_entities = model.predict_entities(result.get("dimensions"), numeric_labels)
        for label, entity in zip(dimension_labels, dimension_entities):
            result[label] = extract_first_number(entity["text"])
        del result["dimensions"]
    if "weight" in result:
        result["weight"] = extract_first_number(result["weight"])
    return result

def extract_first_number(text: str):
    match = re.search(r"\d+(\.\d+)?", text)
    if match:
        return float(match.group())
    return None
