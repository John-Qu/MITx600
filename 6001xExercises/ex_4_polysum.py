


def polysum(n, s):
    """sum the area and square of the perimeter
    of the regular polygon
    n: int, sides of the regular polygon.
    s: float, length of each side.
    return summary, float rounded to 4 decimal place."""

    import math

    area = 0.25*n*s**2/math.tan(math.pi/n)
    peri = s*n
    summary = area + peri**2
    return round(summary, 4)


print(polysum(5, 2.2))