import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(),'HELLO')
        
    def test_isupper(self):
        self.assertTrue('NIZAR'.isupper())
        self.assertFalse('python'.isupper())
        
    def test_python_in_a_list(self):
        list_of_languages = ['C#','php','Java','Python']
        self.assertIn('Python',list_of_languages)
        self.assertNotIn('Matlab',list_of_languages)
        
    def test_regex(self):
        pattern = r'^[A-Z][a-z]+'
        test_string = 'Hello'
        self.assertRegex(test_string,pattern)

# run: python3 -m unittest -v