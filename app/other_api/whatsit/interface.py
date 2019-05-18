from mypy_extensions import TypedDict


class WhatsitInterface(TypedDict, total=False):
    whatsit_id: int
    name: str
    purpose: str
