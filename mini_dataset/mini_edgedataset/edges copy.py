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

##print(l)
##print('\n\n', l1)

l2 = []

for i in l1:
    d1 = []
    for j in l1:
        d = round(((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5, 2)

        d1 += [d]

    l2 += [d1]

#print(l2)
l3 = copy.deepcopy(l2)
min2 = []
min3 = []

for i in l3:
    min2 = []
    for j in range(7):
        min1 = min(i)
        k = i.index(min1) ##
        min2 += [min1, k]

        #i.remove(min1)
        i[k] = 9999

    min2.remove(0.0)
    min2.pop(0) ##
    min3 += [min2]

#print(min3)
##print('\n\n')


z = []
y = []
for i in range(64):
    for j in range(64):
        z += [0]
    y += [z]

##ll1 = ll * 64
    
print(y)
##print('\n\n')

#print(min3[1][1])
a = 0

for i in range(64):
    k = 0
    s = {min3[i][1], min3[i][3], min3[i][5], min3[i][7], min3[i][9], min3[i][11]}
    print(s)
    for j in range(64):
        if j in s:
             y[i][j] = min3[i][k]
             k += 2
        else:
            y[i][j] = 0
        #a += 1

#print(z)
#print([ min3[0][1], min3[0][3], min3[0][5], min3[0][7], min3[0][9], min3[0][11]])
        

##with open('edges.csv', 'a', newline='') as file:
##    writer = csv.writer(file)
##    writer.writerows(ll1)


            
        
        
    




        
        
        
