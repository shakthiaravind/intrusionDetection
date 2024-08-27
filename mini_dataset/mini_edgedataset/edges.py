import csv
import copy

l1 = []

with open('graphdataset2.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        l = []
        x = float(row[0])
        y = float(row[1])

        l = [x,y]
        l1 += [l]

l2 = []

for i in l1:
    d1 = []
    for j in l1:
        d = round(((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5, 2)

        d1 += [d]

    l2 += [d1]

l3 = copy.deepcopy(l2)
min2 = []
min3 = []

for i in l3:
    min2 = []
    for j in range(7):
        min1 = min(i)
        k = i.index(min1) 
        min2 += [min1, k]

        i[k] = 9999

    min2.remove(0.0)
    min2.pop(0) 
    min3 += [min2]

#print(min3)

ll = []
ll1 = []

for i in range(64):
    ll = []
    k = 0
    s = [min3[i][1], min3[i][3], min3[i][5], min3[i][7], min3[i][9], min3[i][11]]
    for j in range(64):
        if j in s:
            ll += [min3[i][k]]
            k += 2
        else:
            ll += [0]

    ll1 += [ll]

#print(ll1)
        
with open('edges.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(ll1)
