
class Calculator:
    def add(a:int, b:int) ->int:
        return a + b

    def subtract(a:int, b:int) ->int:
        return a - b

    def multiply(a:int, b:int) ->int:
        return a * b

    def divide(a:int, b:int) ->float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

calc = Calculator()
print(calc.add(10, 5))         
print(calc.subtract(10, 5))    
print(calc.multiply(10, 5))    
print(calc.divide(10, 5))      