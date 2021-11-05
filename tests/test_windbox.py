from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models.models_windbox import Windbox


@pytest.fixture()
def create_windbox(db: Session) -> Generator[Windbox, None, None]:
    windbox = Windbox(
        hostname="windbox01.windreserve.de"
    )
    db.begin()
    db.add(windbox)
    db.commit()
    yield windbox
    db.rollback()


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


def test_list(app_client: TestClient, create_windbox: Windbox) -> None:
    rv = app_client.get("/windbox")
    response = rv.json()
    assert rv.status_code == 200
    assert len(response) == 1
    assert response[0]["id"] == create_windbox.id
    assert response[0]["hostname"] == create_windbox.hostname


def test_get(app_client: TestClient, create_windbox: Windbox, db: Session) -> None:
    rv = app_client.get(
        f"/windbox/{create_windbox.id}",
        headers={'accept': 'application/json'}
    )
    windbox = rv.json()

    assert rv.status_code == 200
    assert windbox["hostname"] == create_windbox.hostname


def test_update(app_client: TestClient, create_windbox: Windbox) -> None:
    response = app_client.put(
        f"/windbox/{create_windbox.id}",
        json={
            "hostname": "windbox03.windreserve.de"})
    assert response.status_code == 200
    data = response.json()
    assert data["hostname"] == "windbox03.windreserve.de"
    assert data["id"] == create_windbox.id

    response = app_client.get(
        f"/windbox/{create_windbox.id}",
        headers={
            'accept': 'application/json'})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == create_windbox.id
    assert data["hostname"] == "windbox03.windreserve.de"


def test_delete(app_client: TestClient, create_windbox: Windbox) -> None:
    response = app_client.delete(f"/windbox/{create_windbox.id}")
    assert response.status_code == 204

    response = app_client.get(f"/windbox/{create_windbox.id}")
    assert response.status_code == 404

    response = app_client.get("/windbox")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 0
