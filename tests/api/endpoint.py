

from typing import Any, Dict

import pytest
from fastapi.testclient import TestClient

from app.dependencies import get_settings
from app.main import app as fa_app


@pytest.mark.usefixtures("get_settings_override", "db")
class BaseTestEndpoint():

    create_obj_cls: Any
    create_data: Dict
    update_data: Dict
    endpoint: str

    @pytest.fixture
    def client(self, get_settings_override):
        fa_app.dependency_overrides[get_settings] = lambda: get_settings_override
        yield TestClient(fa_app)

    @pytest.fixture
    def create_obj(self, db):
        obj = self.create_obj_cls(
            **self.create_data
        )
        db.begin()
        db.add(obj)
        db.commit()
        yield obj
        db.rollback()

    def test__create(self, client):
        response = client.post(f"{self.endpoint}/", json=self.create_data)

        assert response.status_code == 200
        data = response.json()

        for key in self.create_data.keys():
            assert data[key] == self.create_data[key]

        assert "id" in data
        obj_id = data["id"]

        response = client.get(f"{self.endpoint}/{obj_id}")
        assert response.status_code == 200, response.text
        data = response.json()
        for key in self.create_data.keys():
            assert data[key] == self.create_data[key]

        assert data["id"] == obj_id

    def test__list(self, client, create_obj):
        response = client.get(self.endpoint)

        assert response.status_code == 200

        data = response.json()
        assert len(data) == 1

        # TODO: create fixture to compare data to create_obj
        for key in self.create_obj_cls.__table__.columns.keys():
            assert data[0][key] == getattr(create_obj, key)

    def test__read(self, client, create_obj):
        response = client.get(f"{self.endpoint}/{create_obj.id}")
        assert response.status_code == 200

        data = response.json()

        # TODO: use same fixture as in test__list
        for key in self.create_obj_cls.__table__.columns.keys():
            assert data[key] == getattr(create_obj, key)

    def test__update(self, client, create_obj):
        response = client.put(
            f"{self.endpoint}/{create_obj.id}",
            json=self.update_data)

        assert response.status_code == 200

        data = response.json()

        assert data["id"] == create_obj.id

        for key in self.update_data.keys():
            assert data[key] == self.update_data[key]

        response = client.get(f"{self.endpoint}/{create_obj.id}")

        assert response.status_code == 200

        data = response.json()

        assert data["id"] == create_obj.id

        for key in self.update_data.keys():
            assert data[key] == self.update_data[key]

    def test__delete(self, client, create_obj):
        response = client.delete(f"{self.endpoint}/{create_obj.id}")
        assert response.status_code == 204

        response = client.get(f"{self.endpoint}/{create_obj.id}")
        assert response.status_code == 404

        response = client.get(self.endpoint)
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 0
