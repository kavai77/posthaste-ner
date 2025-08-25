# 🚢 Posthaste NER

Named entity recognition for Posthaste with [GLiNER](https://github.com/urchade/GLiNER) model.

## 🛠 Running locally with Docker

```bash
docker pull ghcr.io/kavai77/posthaste-ner:main
```
```bash
docker run -p 8000:8000 ghcr.io/kavai77/posthaste-ner:main
```

## 🕹️ Making an example request
```bash
curl -s -X POST http://localhost:8000/extract -H 'Content-Type: application/json' \
--data '{"text": " '\
'Please create a shipment to 1101 Budapest, Lajos út 12/A 2/4, Hungary, '\
'with Fedex International Economy. The shipment weight is 2.5 kg, and the '\
'dimensions are 30 cm x 20 cm x 10 cm. The shipment contains a laptop and a charger. '\
'The sender is John Doe, and the recipient is Jane Smith. '\
'The shipment is scheduled for delivery on 2025-08-15."}' | jq
```
Expected response:
```json
{
  "postcode": "1101",
  "city": "Budapest",
  "address": "Lajos út 12/A 2/4",
  "country": "Hungary",
  "service": "Fedex International Economy",
  "weight": "2.5 kg",
  "dimensions": "30 cm x 20 cm x 10 cm",
  "item": "charger",
  "sender": "John Doe",
  "recipient": "Jane Smith",
  "date": "2025-08-15"
}
```

## 🧑‍💻 Development
Clone the project
```bash
git clone git@github.com:kavai77/posthaste-ner.git
```
Create a virtual environment and activate it
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Install the dependencies
```bash
pip install -r requirements.txt
```
Run the application
```bash 
TRANSFORMERS_OFFLINE=1 uvicorn ner:app
```
Run the tests
```bash
TRANSFORMERS_OFFLINE=1 pytest
```