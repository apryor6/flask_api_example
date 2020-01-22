from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import WhatsitService
from .schema import WhatsitSchema
from .model import Whatsit
from .interface import WhatsitInterface
from .. import BASE_ROUTE


def make_whatsit(
    id: int = 123, name: str = "Test whatsit", purpose: str = "Test purpose"
) -> Whatsit:
    return Whatsit(whatsit_id=id, name=name, purpose=purpose)


class TestWhatsitResource:
    @patch.object(
        WhatsitService,
        "get_all",
        lambda: [
            make_whatsit(123, name="Test Whatsit 1"),
            make_whatsit(456, name="Test Whatsit 2"),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(
                f"/api/{BASE_ROUTE}/whatsit", follow_redirects=True
            ).get_json()
            expected = (
                WhatsitSchema(many=True)
                .dump(
                    [
                        make_whatsit(123, name="Test Whatsit 1"),
                        make_whatsit(456, name="Test Whatsit 2"),
                    ]
                )
                
            )
            for r in results:
                assert r in expected

    @patch.object(
        WhatsitService, "create", lambda create_request: Whatsit(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test whatsit", purpose="Test purpose")
            result = client.post(f"/api/{BASE_ROUTE}/whatsit/", json=payload).get_json()
            expected = (
                WhatsitSchema()
                .dump(Whatsit(name=payload["name"], purpose=payload["purpose"]))
                
            )
            assert result == expected


def fake_update(whatsit: Whatsit, changes: WhatsitInterface) -> Whatsit:
    # To fake an update, just return a new object
    updated_Whatsit = Whatsit(
        whatsit_id=whatsit.whatsit_id, name=changes["name"], purpose=changes["purpose"]
    )
    return updated_Whatsit


class TestWhatsitIdResource:
    @patch.object(WhatsitService, "get_by_id", lambda id: make_whatsit(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/whatsit/123").get_json()
            expected = Whatsit(whatsit_id=123)
            assert result["whatsitId"] == expected.whatsit_id

    @patch.object(WhatsitService, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/whatsit/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object(WhatsitService, "get_by_id", lambda id: make_whatsit(id=id))
    @patch.object(WhatsitService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result = client.put(
                f"/api/{BASE_ROUTE}/whatsit/123",
                json={"name": "New Whatsit", "purpose": "New purpose"},
            ).get_json()
            expected = (
                WhatsitSchema()
                .dump(
                    Whatsit(whatsit_id=123, name="New Whatsit", purpose="New purpose")
                )
                
            )
            assert result == expected
