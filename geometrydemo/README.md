# Geometry

Geometry is a Python library for dealing with some geometric tasks.

## Installation

Clone the repository: 

```bash
git clone https://github.com/dnieal/lab-4-pkg.git
cd lab-4-pkg.git
```

Use pip to create an editable installation

```bash
pip install -e .
```

## Usage

```python
from geometry.shapes import Circle, Square, Rectangle
from geometry.util import area_stats

# Construct a square with side length 4:
square = Square(4)

# Shapes can also have non-integer side lenghts:
rectangle = Rectangle(6.5, 3)

# Construct a Circle with radius 3.2
circle = Cirlce(3.2)

# Print the area of the circle:
print(circle.area())

# Print a summary of the areas of all three shapes:
print(area_stats(square, rectangle, circle))
```

## License

[MIT](https://choosealicense.com/licenses/mit/)