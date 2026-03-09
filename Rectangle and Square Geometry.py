from dataclasses import dataclass
from math import sqrt

@dataclass
class Rectangle:
    width: int
    height: int

    # --- Geometry ---
    @property
    def area(self) -> int:
        return self.width * self.height

    @property
    def perimeter(self) -> int:
        return 2 * (self.width + self.height)

    @property
    def diagonal(self) -> float:
        return sqrt(self.width ** 2 + self.height ** 2)

    # --- ASCII Picture ---
    def picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return (("*" * self.width) + "\n") * self.height

    # --- Containment ---
    def amount_inside(self, other: "Rectangle") -> int:
        return self.area // other.area

    # --- String Representation ---
    def __str__(self):
        return f"Rectangle({self.width}×{self.height})"


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    @property
    def side(self) -> int:
        return self.width

    @side.setter
    def side(self, value: int):
        self.width = value
        self.height = value

    # Override width/height to maintain square constraint
    @property
    def width(self) -> int:
        return super().width

    @width.setter
    def width(self, value: int):
        self._width = value
        self._height = value

    @property
    def height(self) -> int:
        return super().height

    @height.setter
    def height(self, value: int):
        self._width = value
        self._height = value

    def __str__(self):
        return f"Square({self.side})"
