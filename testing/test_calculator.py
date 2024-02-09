import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.my_calc = Calculator(8,2)
    
    def test_instance(self):
        self.assertIsInstance(self.my_calc,Calculator)
        
    def test_add(self):
        result = self.my_calc.add()
        self.assertEqual(result,10,'The sum is wrong, check the add function')
        
    def test_substract(self):
        self.assertEqual(self.my_calc.substract(),6,'The substraction is wrong, check the substract function')
        
    def test_multiply(self):       
        self.assertEqual(self.my_calc.multiply(),16,'The multiplication is wrong, check the multiply function')
        
    def test_quotient(self):
        self.assertEqual(self.my_calc.get_quotient(),4,"the division is wrong")
   
    def test_the_whole_calcuator(self):
        self.assertEqual(self.my_calc.add(), 10, "Check the sum")
        self.assertNotEqual(self.my_calc.substract(), 7, "Check the diff")
        self.assertEqual(self.my_calc.multiply(), 16, "Check the product")
        self.assertNotEqual(self.my_calc.get_quotient(), 5, "Check the quotint")    
        
    def test_zero_division_error(self):
        calc = Calculator(7,0)
        with self.assertRaises(ZeroDivisionError) as e:
            result = calc.get_quotient()          
        self.assertEqual(str(e.exception),"you cannot divide by zero !")
    

# run: python3 -m unittest -v    