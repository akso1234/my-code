import random
A = set(random.sample(list(range(1, 21)), 5))
B = set(random.sample(list(range(1, 21)), 5))

print("A:", A)
print("B:", B)

print()
print("A | B =", A | B)
print("A & B =", A & B)
print("A - B =", A - B)
print("A ^ B =", A ^ B)
