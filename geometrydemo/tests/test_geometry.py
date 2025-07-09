import pytest
from geometry.shapes import Square, Circle, Rectangle
from geometry.utils import area_stats

def test_square_area_zero_and_positive():
    # Arrange: choose side lengths
    x = Square(0)
    y = Square(14)
    z = Square(3.4)
    # Act: compute areas
    x_area = x.area()
    y_area = y.area()
    z_area = z.area()
    # Assert: use pytest.approx to compare with expected
    assert x_area == 0
    assert y_area == 196
    assert z_area == pytest.approx(11.56)

def test_stats_keys_and_values():
    # Arrange: create several shapes
    x = Square(1)
    y = Circle(4)
    z = Circle(3)
    w = Square(4)
    # Act: call area_stats
    ans = area_stats(x, y, z, w)
    # Assert: stats is dict, has correct keys, and values are numbers
    assert type(ans) == dict
    assert list(ans.keys()) == ["n", "total", "mean", "min", "max"]
    assert all(isinstance(x, int) or isinstance(x, float) for x in ans.values())

def test_stats_raises_without_shapes():
    # Assert that calling area_stats() raises ValueError
    with pytest.raises(ValueError):
        area_stats()

def test_rectangle():
    # Arrange: choose side lengths
    x = Rectangle(0, 6)
    y = Rectangle(4, 2)
    z = Rectangle(1.5, 1.8)
    # Act: compute areas
    x_area = x.area()
    y_area = y.area()
    z_area = z.area()
    # Assert: use pytest.approx to compare with expected
    assert x_area == 0
    assert y_area == 8
    assert z_area == pytest.approx(2.7)