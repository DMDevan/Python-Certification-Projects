class Rectangle():
    def __init__(self, width, height):
        # Store dimensions internally
        self._width = width
        self._height = height

    # ----- Geometry Methods -----

    def get_area(self):
        # Area = width × height
        return self._width * self._height
    
    def get_perimeter(self):
        # Perimeter = 2 × (width + height)
        return 2 * (self._width + self._height)

    def get_diagonal(self):
        # Diagonal from Pythagorean theorem
        return (self._width ** 2 + self._height ** 2) ** 0.5

    # ----- ASCII Picture -----

    def get_picture(self):
        # Reject shapes that are too large to print
        if self._width > 50 or self._height > 50:
            return "Too big for picture."

        # Build picture row by row
        picture = ""
        for row in range(self._height):
            for column in range(self._width):
                picture += "*"
            picture += "\n"
        return picture

    # ----- Containment Calculation -----

    def get_amount_inside(self, shape: "Rectangle"):
        # Ensure argument is a Rectangle or subclass (Square)
        if not isinstance(shape, Rectangle):
            raise TypeError("Argument must be a Rectangle or Square.")
        
        # Number of times the smaller shape fits inside this one
        return self.get_area() // shape.get_area()

    # ----- Assignment-Required Setters -----

    def set_width(self, value):
        # Update width with validation
        if value < 1:
            raise ValueError("Width cannot be less than one.")
        self._width = value

    def set_height(self, value):
        # Update height with validation
        if value < 1:
            raise ValueError("Height cannot be less than one.")
        self._height = value

    # ----- String Representation -----

    def __str__(self):
        # Required output format
        return f"Rectangle(width={self._width}, height={self._height})"


class Square(Rectangle):
    def __init__(self, side):
        # A square is a rectangle with equal sides
        self._width = side
        self._height = side

    # ----- Side Property -----

    @property
    def side(self):
        # Side is equivalent to width/height
        return self._width

    @side.setter
    def side(self, value):
        # Update both dimensions to maintain square shape
        if value < 1:
            raise ValueError("Side cannot be less than one.")
        self._width = value
        self._height = value

    # ----- Override Width Property -----

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        # Changing width also changes height
        if value < 1:
            raise ValueError("Width cannot be less than one.")
        self._width = value
        self._height = value

    # ----- Override Height Property -----

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        # Changing height also changes width
        if value < 1:
            raise ValueError("Height cannot be less than one.")
        self._width = value
        self._height = value

    # ----- Assignment-Required Methods -----

    def set_side(self, value):
        # Assignment API for updating side
        self.side = value

    def set_width(self, value):
        # Maintain square constraint
        self.width = value

    def set_height(self, value):
        # Maintain square constraint
        self.height = value

    # ----- String Representation -----

    def __str__(self):
        # Required output format
        return f"Square(side={self._width})"
