# Foobar

Foobar is a Python library for dealing with ome geometric tasks.

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
import geometry import Circle, Square, Rectangle, area_stats

#construct a square with side length 4:
square = Square(4)

# Shapes can also have non-integer side lenghts:
rectangle = Rectangle(6.5, 3)

# Construct a Circle
circle = Cirlce(3.2)

# Print the area of the circle:
print(circle.area())

# Print a summary of the areas of all three shapes:
print(area_stats(square, rectangle, circle))
```

## License

[MIT](https://choosealicense.com/licenses/mit/)