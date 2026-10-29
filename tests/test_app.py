from app import app
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_get_home_page():
    client=app.test_client()
    response=client.get("/")
    assert response.status_code == 200

def test_get_about_page():
    client=app.test_client()
    response=client.get("/about")
    assert response.status_code == 200