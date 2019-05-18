from mypy_extensions import TypedDict


class FizzbazInterface(TypedDict, total=False):
    fizzbaz_id: int
    name: str
    purpose: str
