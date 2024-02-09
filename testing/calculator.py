class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
    
    def substract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def get_quotient(self):
        if self.b == 0:
            raise ZeroDivisionError('you cannot divide by zero !')
        return self.a/self.b