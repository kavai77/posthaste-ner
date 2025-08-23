# Posthaste NER

Named entity recognition for Posthaste with ... model

## Running locally with Docker

```bash
docker pull ghcr.io/kavai77/posthaste-ner:main
docker run -p 8000:8000 ghcr.io/kavai77/posthaste-ner:main
```

## Making an example request
```bash
curl http://127.0.0.1:8000/extract -H 'Content-Type: application/json' \
   --data '{"text": "Create a shipment to Budapest, Hungary, 1101, Lajos street 12. with Fedex International Priority"}'
```
Response:
```json
{
  "city": "Budapest",
  "country": "Hungary",
  "postcode": "1101",
  "address": "Lajos street 12.",
  "service": "Fedex International Priority"
}
```