from input import data
import heap
import random
priority = []
for a in data:
    if a[0] == 1:
        b = [7500, a[2], a[3]]
        priority.append(b)
    elif a[0] == 2:
        b = [6000, a[2], a[3]]
        priority.append(b)
    elif a[0] == 3:
        b = [4500, a[2], a[3]]
        priority.append(b)
    elif a[0] == 4:
        b = [3000, a[2], a[3]]
        priority.append(b)
    elif a[0] == 5:
        b = [1500, a[2], a[3]]
        priority.append(b)
for b in priority:
    b[0] = b[0]+random.randint(1, 1000)

heap.heapify(priority)

for b in priority:
    print(b)

