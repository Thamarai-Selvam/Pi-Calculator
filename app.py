import math
import random as r

inside = total = 0
while True:
    x = r.random()
    y = r.random()
    dist = math.sqrt(x*x+y*y)
    if dist < 1:
        inside += 1
    total += 1
    pi = 4.0 * inside / total
    print(pi)
        

