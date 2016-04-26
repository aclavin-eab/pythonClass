#Author Andrew Clavin
"""
Write a class that represents a rational number
(i.e., a number that can be represented as a fraction).
The constructor for your class should take as parameters
a numerator and denominator. In addition,
implement the following methods for your class:
• arithmetic: __add__, __sub__, __mul__, __truediv__
• comparison: __lt__, __eq__, __le__
• __str__
When you are done, you should be able to perform calculations
like the following:
a = Rational(3, 2) # 3/2
b = Rational(1, 3) # 1/3
sum = a + b
print(sum)
print(a < b)
"""

class Rational
    """Rational Number Class"""
    __init__(self, numerator, denomenator):
        self.numerator = numerator
        self.denomenator = denomenator
        self.value = "" + numerator + "/" + denomenator
        self.digit = numerator / denomenator

    def __add__(self, summand):
        numerator = (self.numerator * summand.denomenator) + (summand.numerator * self.denomenator)
        denomenator = (self.denomenator * summand.denomenator)
        return "" + numerator + "/" + denomenator

    def __sub__(self, term):
        numerator = (self.numerator * summand.denomenator) - (summand.numerator * self.denomenator)
        denomenator = (self.denomenator * summand.denomenator)
        return "" + numerator + "/" + denomenator

    def __mul__(self, term):
        numerator = (self.numerator * summand.numerator
        denomenator = (self.denomenator * summand.denomenator)
        return "" + numerator + "/" + denomenator

    def __truediv__(self, term):
        numerator = (self.numerator * summand.denomenator
        denomenator = (self.denomenator * summand.numerator)
        return "" + numerator + "/" + denomenator

    def __lt__(self, other):
        if (self.numerator * other.denomenator) < (other.numerator * self.denomenator):
                     return true
        else:
                     return false
    def __eq__(self, other):
        if (self.numerator * other.denomenator) == (other.numerator * self.denomenator):
                     return true
        else:
                     return false
    def __le__(self, other):
        if (self.numerator * other.denomenator) <= (other.numerator * self.denomenator):
                     return true
        else:
                     return false
