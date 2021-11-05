import json
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.config import Settings
from app.models.models_windbox import Windbox

# @pytest.fixture()
# def create_windbox(db: Session) -> Generator[Windbox, None, None]:
#     windbox = Windbox(
#         hostname="windbox01.windreserve.de"
#     )
    
#     db.add(windbox)
#     db.flush()
#     yield windbox
#     db.rollback()


# def test_db_settings(app_client: TestClient) -> None:
#     rv = app_client.get("/info")
#     response = rv.json()
#     assert response["db"] == "sqlite:///./config.test.db"


def test_create(app_client: TestClient) -> None:
    response = app_client.post(
        "/windbox/",
        json={"hostname": "windbox02"}
        )
    assert response.status_code == 200
    data = response.json()
    assert data["hostname"] == "windbox02"
    assert "id" in data
    windbox_id = data["id"]

    response = app_client.get(f"/windbox/{windbox_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["hostname"] == "windbox02"
    assert data["id"] == windbox_id


# def test_list(app_client: TestClient, create_windbox: Windbox) -> None:
#     rv = app_client.get("/windbox")
#     response = rv.json()
#     assert rv.status_code == 200
#     assert response[0]["id"] == create_windbox.id
#     #assert response[0]


# def test_get(app_client: TestClient, create_windbox: Windbox) -> None:
#     rv = app_client.get(f"/windbox/{create_windbox.id}", headers={'accept': 'application/json'})
#     windbox = rv.json()
#     #assert windbox['detail'][0]['loc'] == "yes"
#     assert rv.status_code == 200
#     assert windbox["hostname"] == "windbox01.windreserve.de"
