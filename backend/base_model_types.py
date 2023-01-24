from pydantic import BaseModel


class Ranges(BaseModel):
    screen_diag: tuple[float, float]
    ram: tuple[int, int]
    storage: tuple[int, int]
    mass: tuple[float, float]
    price: tuple[float, float]


class Checkboxes(BaseModel):
    manufacturer: list[str]
    category: list[str]
    screen_res: list[str]
    screen_touch: list[str]
    cpu_vendor: list[str]
    storage_type: list[str]
    os: list[str]


class Filter(BaseModel):
    checkboxes: Checkboxes
    ranges: Ranges
    words: str
