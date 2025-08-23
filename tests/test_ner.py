import pytest
from fastapi.testclient import TestClient
from ner import app

client = TestClient(app)

def test_extract_entities():
    text = """
        Please create a shipment to 1101 Budapest, Lajos út 12/A 2/4, Hungary, with Fedex International Economy. 
        The shipment weight is 2.5 kg, and the dimensions are 30 cm x 20 cm x 10 cm.
        The shipment contains a laptop and a charger.
        The sender is John Doe, and the recipient is Jane Smith.
        The shipment is scheduled for delivery on 2025-08-15.
        """
    payload = {"text": text}
    response = client.post("/extract", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["postcode"] == "1101"
    assert data["city"] == "Budapest"
    assert data["country"] == "Hungary"
    assert "state" not in data
    assert data["address"] == "Lajos út 12/A 2/4"
    assert data["service"] == "Fedex International Economy"
    assert data["weight"] == "2.5 kg"
    assert data["dimensions"] == "30 cm x 20 cm x 10 cm"
    assert data["item"] == "charger"
    assert data["sender"] == "John Doe"
    assert data["recipient"] == "Jane Smith"
    assert data["date"] == "2025-08-15"
