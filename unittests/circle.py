from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("Radius should not be negative")

    if type(r) not in[int, float]:
        raise TypeError("Radius must be a float or integer")
    if type(r) is bool:
        raise TypeError("Radius must not be a bool")
    if type(r) is str:
        raise TypeError("Radius must not be a string")
    return pi*(r**2)
