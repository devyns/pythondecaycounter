from random import randint
rolls = 100
count = -1

while count < 30:
    count = count + 1
    number = [randint(1, 6) for p in range(1)]
    list = [randint(1, 6) for p in range(rolls)]
    decay = list.count(1)
    left = rolls - decay
    rolls = rolls - decay

    print(count,"time(s)")
    print(decay, "Decayed")
    print(left, "Left")
    # print(list)
    print()



