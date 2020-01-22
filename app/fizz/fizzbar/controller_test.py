from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import FizzbarService
from .schema import FizzbarSchema
from .model import Fizzbar
from .interface import FizzbarInterface
from .. import BASE_ROUTE


def make_fizzbar(
    id: int = 123, name: str = "Test fizzbar", purpose: str = "Test purpose"
) -> Fizzbar:
    return Fizzbar(fizzbar_id=id, name=name, purpose=purpose)


class TestFizzbarResource:
    @patch.object(
        FizzbarService,
        "get_all",
        lambda: [
            make_fizzbar(123, name="Test Fizzbar 1"),
            make_fizzbar(456, name="Test Fizzbar 2"),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(
                f"/api/{BASE_ROUTE}/fizzbar", follow_redirects=True
            ).get_json()
            expected = (
                FizzbarSchema(many=True)
                .dump(
                    [
                        make_fizzbar(123, name="Test Fizzbar 1"),
                        make_fizzbar(456, name="Test Fizzbar 2"),
                    ]
                )
                
            )
            for r in results:
                assert r in expected

    @patch.object(
        FizzbarService, "create", lambda create_request: Fizzbar(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test fizzbar", purpose="Test purpose")
            result = client.post(f"/api/{BASE_ROUTE}/fizzbar/", json=payload).get_json()
            expected = (
                FizzbarSchema()
                .dump(Fizzbar(name=payload["name"], purpose=payload["purpose"]))
                
            )
            assert result == expected


def fake_update(fizzbar: Fizzbar, changes: FizzbarInterface) -> Fizzbar:
    # To fake an update, just return a new object
    updated_Fizzbar = Fizzbar(
        fizzbar_id=fizzbar.fizzbar_id, name=changes["name"], purpose=changes["purpose"]
    )
    return updated_Fizzbar


class TestFizzbarIdResource:
    @patch.object(FizzbarService, "get_by_id", lambda id: make_fizzbar(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/fizzbar/123").get_json()
            expected = Fizzbar(fizzbar_id=123)
            assert result["fizzbarId"] == expected.fizzbar_id

    @patch.object(FizzbarService, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/fizzbar/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object(FizzbarService, "get_by_id", lambda id: make_fizzbar(id=id))
    @patch.object(FizzbarService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result = client.put(
                f"/api/{BASE_ROUTE}/fizzbar/123",
                json={"name": "New Fizzbar", "purpose": "New purpose"},
            ).get_json()
            expected = (
                FizzbarSchema()
                .dump(
                    Fizzbar(fizzbar_id=123, name="New Fizzbar", purpose="New purpose")
                )
                
            )
            assert result == expected
