#!/usr/bin/python3

def add(x, y):
    """Add function"""
    if type(x) not in [int, float]:
        raise TypeError("x must be a real number")
    return x + y

def subtract(x, y):
    """Subtract function"""
    if type(x) not in [int, float]:
        raise TypeError("x must be a real number")
    return x - y

def mult(x, y):
    """Multiplication function"""
    if type(x) not in [int, float]:
        raise TypeError("x must be a real number")
    return x * y

def divide(x, y):
    """Divide function"""
    if type(x) not in [int, float]:
        raise TypeError("x must be a real number")
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return x / y
