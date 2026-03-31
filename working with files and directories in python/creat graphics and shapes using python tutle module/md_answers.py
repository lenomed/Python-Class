from md import multiply, divide

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

def multiple_Quocient(num1, num2):
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        product = multiply(num1, num2)
        quotient = divide(num1, num2)
        
        print(f"The product of {num1} and {num2} is: {product}")
        print(f"The quotient of {num1} and {num2} is: {quotient}")
    except ValueError as e:
        print(e)

multiple_Quocient(num1, num2)