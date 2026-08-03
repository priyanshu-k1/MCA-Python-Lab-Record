"""
Program to display Fibonacci sequence up to nth term. 
"""
def fib(n:int)->int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)



num = int(input("Enter the number: "))
print(fib(num))