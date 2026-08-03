"""
Program to find GCD of 2 Positive Numbers 
"""
def gcd(a:int, b:int)->int:
    if a < 0 or b < 0:
        return None
    while b:
        a,b = b, a%b
    return a

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

res = gcd(num1,num2)

print(f"GCD of {num1} and {num2} : {res}")