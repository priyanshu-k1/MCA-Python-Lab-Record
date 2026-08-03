def gcd(a:int, b:int)->int:
    while b:
        a,b = b, a%b
    return a

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

res = gcd(num1,num2)

print(f"GCD of {num1} and {num2} : {res}")