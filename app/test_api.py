from .app import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_post_request():
    data = {
        "field_name1": "+7 999 855 37 10",
        "field_name2": "bogdan",
        "field_name3": "bodga@yandex.ru",
        "field_name4": "11.12.2017"
    }
    response = client.post('/forms/', json=data)
    assert response.status_code == 200
    assert response.json() == ["phone_reg_form", "auth_form", "full_auth_form", "author_form", "business_card_form"]