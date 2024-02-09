## unittest framework
​

'unittest' is a built-in Python library for writing and running unit tests. Unit tests are a fundamental aspect of software development that help ensure the correctness of individual components (units) of your code. unittest provides a framework for defining and running these tests, making it easier to automate testing and catch issues early in the development process.
​
To use unittest, you'll typically follow these steps:
​
# 1. Import the unittest module: You need to import the unittest module at the beginning of your test file.

```python
import unittest
```
​
# 2. Create test cases: Test cases are classes that inherit from unittest.TestCase. Each test case contains test methods, which are individual tests for specific functionality.
​
```python
class MyTestCase(unittest.TestCase):
```
​
# 3. Write some functions that you want to test
​
# 4. Use assertion methods: unittest provides a variety of assertion methods to check conditions in your test methods. Here are some common assertion methods:
​
### Common Assertion Methods
​
* assertEqual(a, b): Checks if 'a' == 'b'
* assertNotEqualt(a, b): Checks if 'a' != 'b'
* assertTrue(x) : Checks if 'x' == True
* assertFalse(x) :  Checks if 'x' == False
* assertIs(a, b) : Checks if 'a' is 'b'
* assertIsNot(a, b) : Checks if 'a' is not 'b'
* assertIsNone(a) :Checks if 'a' is None
* assertIsNotNone(a) : Checks if 'a' is not None
* assertIn(a, b) : Checks if 'a' is in 'b' 
* assertNotIn(a, b) : Check if 'a' is not in 'b'
* assertRaises(exception, callable, *args, **kwargs): Checks if callable(*args, **kwargs) raises the specified exception.


To run the test : python3 -m unittest -v