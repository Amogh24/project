from inputgui import data
import heap2
import random

for a in data:
    if a[0] == 1:
        a[0] = 7500 + random.randint(1, 1000)

    elif a[0] == 2:
        a[0] = 6000 + random.randint(1, 1000)

    elif a[0] == 3:
        a[0] = 4500 + random.randint(1, 1000)

    elif a[0] == 4:
        a[0] = 3000 + random.randint(1, 1000)

    elif a[0] == 5:
        a[0] = 1500 + random.randint(1, 1000)



heap2.heapify(data)

for b in data:
    print(b)

