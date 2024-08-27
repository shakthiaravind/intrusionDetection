import random
import csv

l = []
l1 = []

l2 = []
l3 = []
x = 0

for i in range(1, 2):
    l1 = []
    #l1 += ['#'+ str(i)]

    l3 = []
    l3 += [i]
    
    for j in range(64):
        l1 += [round(random.uniform(100.0, 1000.0), 1)] # -20.0, 15.0

    for k in l1[1:]:
        x += k
    y = round(x / 64, 1)

    x = 0
    #l1 += ['##' + str(y)]
    l += [l1]

    l3 += [y]

    l2 += [l3]

with open('temp_time5.csv', 'a', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(l)

##with open('datatest2.csv', 'a', newline='') as file:
##     writer = csv.writer(file)
##     writer.writerows(l2)
        
