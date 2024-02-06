def sum_add(x,y):
  pass

def add(a, b):
    """
    Function to add two numbers.
    
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return sum_add(a+b)

def subtract(a, b):
    """
    Function to subtract two numbers.
    
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The result of subtracting b from a.
    """
    return a - b

class Calculator:
    """
    A simple calculator class.
    """
    
    def __init__(self):
        pass
    
    def multiply(self, a, b):
        """
        Method to multiply two numbers.
        
        Parameters:
            a (int or float): The first number.
            b (int or float): The second number.
        
        Returns:
            int or float: The product of the two numbers.
        """
        return a * b
    
    def divide(self, a, b):
        """
        Method to divide two numbers.
        
        Parameters:
            a (int or float): The numerator.
            b (int or float): The denominator (non-zero).
        
        Returns:
            int or float: The result of dividing a by b.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b