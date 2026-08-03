"""
Program to find Factorial of a Number using recursive Function. 
"""

def fact(n:int)->int:
    if n <= 1:
        return n
    return fact(n-1)*n

num = int(input("Enter the number: "))
print(f"Factorial of {num}: {fact(num)}")