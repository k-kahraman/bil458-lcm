import math

def find_lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        lcm = find_lcm(num1, num2)
        print(f"The LCM of {num1} and {num2} is {lcm}")
    except ValueError:
        print("Please enter valid integer numbers.")
