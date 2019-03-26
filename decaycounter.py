from random import *
rolls = 100
count = 0
left = 1

while left > 0 and count < 30 :
    count = count + 1
    list = [randint(1, 6) for p in range(rolls)]
    decay = list.count(1)
    left = rolls - decay
    rolls = rolls - decay

    print(count,"time(s)")
    print(decay, "Decayed")
    print(left, "Left")
    print()



