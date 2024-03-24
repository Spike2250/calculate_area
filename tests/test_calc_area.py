from math import pi
from calc_area.calculations import (
    triangle,
    circle,
    rectangle,
    square,
    sphere,
)


def test_triangle_calc_area():
    assert triangle.calc_area(3, 4, 5) == 6
    assert round(triangle.calc_area(3, 3, 3), ndigits=2) == 3.9


def test_triangle_is_exist():
    assert triangle.is_exist(1, 2, 3) is False
    assert triangle.is_exist(3, 4, 5) is True
    assert triangle.is_exist(5, 5, 5) is True
    assert triangle.is_exist(4, 5, 12) is False
    assert triangle.is_exist(2, 6, 8) is False
    assert triangle.is_exist(2, 6, 7) is True


def test_triangle_is_right():
    assert triangle.is_right(3, 4, 5) is True
    assert triangle.is_right(5, 12, 13) is True
    assert triangle.is_right(3, 3, 3) is False
    assert triangle.is_right(6, 7, 8) is False


def test_circle_calc_area():
    assert circle.calc_area(1) == pi
    assert circle.calc_area(2) == 4 * pi
    assert circle.calc_area(3) == 9 * pi


def test_sphere_calc_area():
    assert sphere.calc_area(1) == 4 * pi
    assert sphere.calc_area(2) == 16 * pi
    assert sphere.calc_area(3) == 36 * pi


def test_rectangle_calc_area():
    assert rectangle.calc_area(2, 4) == 8
    assert rectangle.calc_area(1, 1) == 1


def test_square_calc_area():
    assert square.calc_area(3) == 9
    assert square.calc_area(2) == 4
    assert square.calc_area(1) == 1
