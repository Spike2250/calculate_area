
def calc_area(a, b, c):
    sides = sorted([a, b, c])

    if not is_exist(*sides):
        return '[yellow]There is no triangle with these sides!!![/yellow]'

    if is_right(*sides):
        return sides[0] * sides[1] / 2

    half_per = sum([a, b, c]) / 2
    return (half_per * (half_per - a) * (half_per - b) * (half_per - c)) ** 0.5


# проверка треугольника на существование
def is_exist(a, b, c):
    if a + b > c:
        return True
    return False


# проверка треугольника на прямоугольность
def is_right(a, b, c):
    if c ** 2 == a ** 2 + b ** 2:
        return True
    return False
