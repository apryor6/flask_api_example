from .service import QueryService


def test_execute():
    result = QueryService.execute("a complicated query")

    assert result == "Success"
