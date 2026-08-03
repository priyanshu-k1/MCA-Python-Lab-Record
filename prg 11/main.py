""" Program to take a Tuple as input and use all its built-in functions. """
import ast

user_input = input("Enter a tuple (e.g. (1, 2, 3, 2, 4)): ")
data = ast.literal_eval(user_input)

print("len():", len(data))
print("max():", max(data))
print("min():", min(data))
print("sum():", sum(data))
print("sorted():", sorted(data))
print("any():", any(data))
print("all():", all(data))
print("tuple():", tuple(data))
print("type():", type(data))

print("count(2):", data.count(2))

first_elem = data[0]
print(f"index({first_elem}):", data.index(first_elem))