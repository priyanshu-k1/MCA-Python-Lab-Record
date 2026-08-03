"""
Program to take a Dictionary as input and use all its built-in functions.
"""
import ast

user_input = input("Enter a dictionary (e.g. {'a': 1, 'b': 2, 'c': 3}): ")
data = ast.literal_eval(user_input)

print("len():", len(data))
print("str():", str(data))
print("type():", type(data))
print("sorted():", sorted(data))
print("any():", any(data))

d = data.copy()
print("copy():", d)

print("get('a'):", d.get('a'))
print("get('z', 0):", d.get('z', 0))

print("keys():", list(d.keys()))
print("values():", list(d.values()))
print("items():", list(d.items()))


d.update({'e': 5, 'f': 6})
print("after update({'e': 5, 'f': 6}):", d)

popped_val = d.pop('a', None)
print("pop('a'):", popped_val, "| after pop:", d)

d.clear()
print("after clear():", d)