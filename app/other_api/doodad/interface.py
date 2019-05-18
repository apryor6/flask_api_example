from mypy_extensions import TypedDict


class DoodadInterface(TypedDict, total=False):
    doodad_id: int
    name: str
    purpose: str
