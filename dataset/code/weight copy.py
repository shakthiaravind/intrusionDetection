import csv
import copy
import math
import statistics

l1 = []     #contains position (x,y) of all the 64 sensors -> [[x0, y0], [x1, y1], ... ]

with open('graphdataset.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        l = []      #(xi, yi) 0<= i < 63 -> [xi, yi]
        x = float(row[0])
        y = float(row[1])

        l = [x,y]
        l1 += [l]

#print(l1)
                
l2 = []     #distance of si from sj 0<= i, j < 63 -> [[d0, d1, d2, ... , d63], [

for i in l1:
    d1 = []
    for j in l1:
        d = round(((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5, 2)

        d1 += [d]

    l2 += [d1]

#print(l2)

l3 = copy.deepcopy(l2)

#==========================================================

min2 = [] 
min3 = []       #6 nearest sensor of each sensor -> [[dist1, sensor number1], [dist2, sensor number2], ... [dist6, sensor number6],

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

#============================================================

ll = []
ll1 = []
t = []
ll2 = []
ll3 = [] #weight matrix

for a in range(10):
    ll = []
    ll1 = []
    t = []
    ll2 = []
    ll3 = [] #weight matrix
    
    t = []
    file_name = 'temp_time'+ str(a)+ '.csv'
    file_name1 ='laplacianMat_time'+ str(a)+ '.csv'
    #file_name2 = 'weightMat_time'+ str(a)+ '.csv'

    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for j in row:
                t += [float(j)]
    print(t)

    #print(t)

    sums = 0 #####
    for i in range(64):
        ll = []
        ll2 = []
        k = 0
        s = [min3[i][1], min3[i][3], min3[i][5], min3[i][7], min3[i][9], min3[i][11]] #nearest sensor number
        #print(s)
        for j in range(64):
            if j in s:
                jj = j
                ll += [min3[i][k]]
                #print(ll)
                
                if t[i] != t[jj] : #####
                    sums = ((t[i] - t[jj]) ** 2) / ( 2 * statistics.variance(t))
                    #print(t[i], t[j], sums)
                if i != j:
                    ll2 += [round(math.exp(-    (( (min3[i][k] ** 2) / (2 * statistics.variance([i, jj])) ) + sums)), 2) ] ######
                    #print(round(math.exp(-    (( (min3[i][k] ** 2) / (2 * statistics.variance([i, jj])) ) + sums)), 2) )
                k += 2
                #print(k)
            else:
                ll += [0]
                ll2 += [0]

        ll1 += [ll]
        ll3 += [ll2]

##    with open(file_name2, 'a', newline='') as file:
##        writer = csv.writer(file)
##        writer.writerows(ll3)
        
    #print(ll1)
    #print(ll3)
    ll4 = []
    ll5 = [] #diagonal matrix

    for i in range(64):
        weight = 0
        ll4 = []
        for j in range(64):
            weight += ll3[i][j]

        for k in range(64):
            if i == k:
                ll4 += [round(weight, 2)]
            else:
                ll4 += [0]

        ll5 += [ll4] 

    #print(ll5)
    ll6 = [] #laplacian matrix
    for i in range(64):
        ll7 = []
        for j in range(64):
            ll7 += [ll5[i][j] - ll3[i][j]]

        ll6 += [ll7]

    #print(ll6)
    with open(file_name1, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(ll6)
                

    
        
