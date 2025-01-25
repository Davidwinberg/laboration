import random
n = 0
for k in range(1000000):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 < 1:
        n += 1
print(4*(n/10))

