from geometry.shapes import Square, Circle, Rectangle
from geometry.utils import area_stats


x = Square(1)
y = Circle(4)
z = Circle(3)
w = Square(4)
a = Square(14.34)
b = Rectangle(14, 34)
print("Areas:")
print(x.area())
print(y.area())
print(z.area())
print(w.area())
print(a.area())
print(b.area())
print(area_stats(x, y, z, w, a, b))