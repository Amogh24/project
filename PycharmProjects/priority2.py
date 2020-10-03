from inputgui import data
import heap2
import random
priority = []
for a in data:
    if a[0] == 1:
        a[0] = 7500
        priority.append(a)
    elif a[0] == 2:
        a[0] = 6000
        priority.append(a)
    elif a[0] == 3:
        a[0] = 4500
        priority.append(a)
    elif a[0] == 4:
        a[0] = 3000
        priority.append(a)
    elif a[0] == 5:
        a[0] = 1500
        priority.append(a)
for a in priority:
    a[0] = a[0]+random.randint(1, 1000)

heap2.heapify(priority)

for b in priority:
    print(b)

