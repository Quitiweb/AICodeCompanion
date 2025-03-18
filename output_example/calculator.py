import sys

class Calculator:
    def calculate(self, num1, num2, operation):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return 'Invalid input: numbers must be int or float'
        if operation == 'SUM':
            return num1 + num2
        elif operation == 'RES':
            return num1 - num2
        elif operation == 'MUL':
            return num1 * num2
        elif operation == 'DIV':
            if num2 == 0:
                return 'You cannot divide by 0'
            return num1 / num2
        else:
            return 'Invalid operation'

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: calculator.py num1 num2 operation")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        operation = sys.argv[3].upper()
    except ValueError:
        print('Please provide valid numbers')
        sys.exit(1)

    calc = Calculator()
    result = calc.calculate(num1, num2, operation)
    print(result)
