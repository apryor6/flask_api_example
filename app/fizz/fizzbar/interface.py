from mypy_extensions import TypedDict


class FizzbarInterface(TypedDict, total=False):
    fizzbar_id: int
    name: str
    purpose: str
