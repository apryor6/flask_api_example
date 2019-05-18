from mypy_extensions import TypedDict


class WidgetInterface(TypedDict, total=False):
    widget_id: int
    name: str
    purpose: str
