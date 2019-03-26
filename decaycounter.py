from random import *
from prettytable import PrettyTable

rolls = 100
count = 0
left = 1

table = PrettyTable()

table.field_names = ["Throw", "Particles Decayed", "Particles Left"]
table.add_row([0, 0, 100,])

while left > 0 and count < 30 :
    count = count + 1
    list = [randint(1, 6) for p in range(rolls)]
    decay = list.count(1)
    left = rolls - decay
    rolls = rolls - decay

    # print(count,"time(s)")
    # print(decay, "Decayed")
    # print(left, "Left")
    # print()
    table.add_row([count, decay, left,])

table.align["Throw"] = "l"
table.align["Particles Decayed"] = "l"
table.align["Particles Left"] = "l"
print(table)




