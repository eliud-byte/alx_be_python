import unittest
from simple_calculator import  SimpleCalculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 10.6), 10.6)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertRaises(TypeError, self.calc.add, "hello", 5)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-8, -4), -4)
        self.assertEqual(self.calc.subtract(-8, 4), -12)
        self.assertEqual(self.calc.subtract(8, -4), 12)
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        self.assertRaises(TypeError, self.calc.subtract, 2, "one")
    
    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(9, 6), 54)
        self.assertEqual(self.calc.multiply(-4, -6), 24)
        self.assertEqual(self.calc.multiply(-1, 6), -6)
        self.assertEqual(self.calc.multiply(9, -5), -45)
        self.assertEqual(self.calc.multiply(0, -6), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        #self.assertRaises(TypeError, self.calc.multiply, "hundred", 5)
    
    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(0, 0), None)
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(0, 3), 0)
        self.assertEqual(self.calc.divide(0, -3), 0)
        self.assertEqual(self.calc.divide(-6, 5), -1.2)
        self.assertEqual(self.calc.divide(7, -2), -3.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333333333)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333333)
        self.assertRaises(TypeError, self.calc.divide, "hello", 5)

    

    

if __name__ == "__main__":
    unittest.main()