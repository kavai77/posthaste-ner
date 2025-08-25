from fastapi import FastAPI
from gliner import GLiNER
from pydantic import BaseModel

model = GLiNER.from_pretrained("urchade/gliner_large-v2.1", cache_dir="./.models")

app = FastAPI()

labels = ["postcode", "city", "country", "state", "address", "date", "service", "weight", "dimensions", "item", "sender", "recipient"]

class TextRequest(BaseModel):
    text: str

@app.post("/extract")
async def extract_entities(request: TextRequest):
    entities = model.predict_entities(request.text, labels)
    result = {entity["label"]: entity["text"] for entity in entities}
    return result
