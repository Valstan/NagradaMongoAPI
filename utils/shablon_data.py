from dataclasses import dataclass


@dataclass
class GetField:
    collection: str = "error"
    table: str = "error"
    field: str = "error"
