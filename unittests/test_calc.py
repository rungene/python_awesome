import calc
import unittest

class TestCalc(unittest.TestCase):
    def test_positive(self):
        #Test funs when x, y >= 0
        self.assertAlmostEqual(calc.add(1,1),2)
        self.assertAlmostEqual(calc.subtract(1,1),0)
        self.assertAlmostEqual(calc.mult(1,1),1)
        self.assertAlmostEqual(calc.divide(1,1),1)

    def test_negative_x(self):
        #Test funs when x is -ve, y >= 0
        self.assertAlmostEqual(calc.add(-1,1),0)
        self.assertAlmostEqual(calc.subtract(-1,1),-2)
        self.assertAlmostEqual(calc.mult(-1,1),-1)
        self.assertAlmostEqual(calc.divide(-1,1),-1)
    
    def test_negative_y(self):
        #Test funs when x>0, y< 0
        self.assertAlmostEqual(calc.add(1,-1),0)
        self.assertAlmostEqual(calc.subtract(1,-1),2)
        self.assertAlmostEqual(calc.mult(1,-1),-1)
        self.assertAlmostEqual(calc.divide(1,-1),-1)
    
    def test_negative_both(self):
        #Test funs when x, y < 0
        self.assertAlmostEqual(calc.add(-1,-1),-2)
        self.assertAlmostEqual(calc.subtract(-1,-1),0)
        self.assertAlmostEqual(calc.mult(-1,-1),1)
        self.assertAlmostEqual(calc.divide(-1,-1),1)

    def test_types_add(self):
        #Make sure type errors are raise when necessary
        self.assertRaises(TypeError, calc.add, 3+5j, 1)
        self.assertRaises(TypeError, calc.add, True, 1)
        self.assertRaises(TypeError, calc.add, "radius",1)
    def test_types_subtract(self):
        #Make sure type errors are raise when necessary
        self.assertRaises(TypeError, calc.subtract, 3+5j, 1)
        self.assertRaises(TypeError, calc.subtract, True, 1)
        self.assertRaises(TypeError, calc.subtract, "radius",1)
    
    def test_types_mult(self):
        #Make sure type errors are raise when necessary
        self.assertRaises(TypeError, calc.mult, 3+5j, 1)
        self.assertRaises(TypeError, calc.mult, True, 1)
        self.assertRaises(TypeError, calc.mult, "radius",1)
    
    def test_types_divide(self):
        #Make sure type errors are raise when necessary
        self.assertRaises(TypeError, calc.divide, 3+5j, 1)
        self.assertRaises(TypeError, calc.divide, True, 1)
        self.assertRaises(TypeError, calc.divide, "radius",1)
    
    def test_ZeroDivisonError_divide(self):
        self.assertRaises(ZeroDivisionError, calc.divide,1,0)
