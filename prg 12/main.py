"""Program to take a Set as input and use all its built-in functions."""
import ast

user_input = input("Enter a set (e.g. {1, 2, 3, 4, 5}): ")
data = ast.literal_eval(user_input)

print("len():", len(data))
print("max():", max(data))
print("min():", min(data))
print("sum():", sum(data))
print("sorted():", sorted(data))
print("any():", any(data))
print("all():", all(data))
print("type():", type(data))

s1 = data.copy()
print("copy():", s1)

s1.add(100)
print("after add(100):", s1)

s1.remove(100)
print("after remove(100):", s1)

s1.discard(999)
print("after discard(999):", s1)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("union():", a.union(b))
print("intersection():", a.intersection(b))
print("difference():", a.difference(b))
print("symmetric_difference():", a.symmetric_difference(b))

print("isdisjoint():", a.isdisjoint({10, 20}))
print("issubset():", {1, 2}.issubset(a))
print("issuperset():", a.issuperset({1, 2}))

