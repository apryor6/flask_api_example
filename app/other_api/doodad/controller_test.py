from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import DoodadService
from .schema import DoodadSchema
from .model import Doodad
from .interface import DoodadInterface
from .. import BASE_ROUTE


def make_doodad(
    id: int = 123, name: str = "Test doodad", purpose: str = "Test purpose"
) -> Doodad:
    return Doodad(doodad_id=id, name=name, purpose=purpose)


class TestDoodadResource:
    @patch.object(
        DoodadService,
        "get_all",
        lambda: [
            make_doodad(123, name="Test Doodad 1"),
            make_doodad(456, name="Test Doodad 2"),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(
                f"/api/{BASE_ROUTE}/doodad", follow_redirects=True
            ).get_json()
            expected = (
                DoodadSchema(many=True)
                .dump(
                    [
                        make_doodad(123, name="Test Doodad 1"),
                        make_doodad(456, name="Test Doodad 2"),
                    ]
                )
                
            )
            for r in results:
                assert r in expected

    @patch.object(
        DoodadService, "create", lambda create_request: Doodad(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test doodad", purpose="Test purpose")
            result = client.post(f"/api/{BASE_ROUTE}/doodad/", json=payload).get_json()
            expected = (
                DoodadSchema()
                .dump(Doodad(name=payload["name"], purpose=payload["purpose"]))
                
            )
            assert result == expected


def fake_update(doodad: Doodad, changes: DoodadInterface) -> Doodad:
    # To fake an update, just return a new object
    updated_Doodad = Doodad(
        doodad_id=doodad.doodad_id, name=changes["name"], purpose=changes["purpose"]
    )
    return updated_Doodad


class TestDoodadIdResource:
    @patch.object(DoodadService, "get_by_id", lambda id: make_doodad(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/doodad/123").get_json()
            expected = Doodad(doodad_id=123)
            assert result["doodadId"] == expected.doodad_id

    @patch.object(DoodadService, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/doodad/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object(DoodadService, "get_by_id", lambda id: make_doodad(id=id))
    @patch.object(DoodadService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result = client.put(
                f"/api/{BASE_ROUTE}/doodad/123",
                json={"name": "New Doodad", "purpose": "New purpose"},
            ).get_json()
            expected = (
                DoodadSchema()
                .dump(Doodad(doodad_id=123, name="New Doodad", purpose="New purpose"))
                
            )
            assert result == expected
