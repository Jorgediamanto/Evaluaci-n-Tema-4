x=[1.0, ['3', 'A', 'F', 'T', '1', 'M']]
x3 = [[0.2,"A"],[0.17,"F"],[0.13,"1"],[0.21,"3"],[0.05,"0"],[0.09,"M"],[0.15,"T"]]
xx=x
x1 = [[],0]
x2 = [[],0]

y1=len(x[1])/2
a=0
for y in x[1]:
    x1[0]+=y
    a+=1
    if a==y1:
        break

xx[1].reverse()

a=0

for y in xx[1]:
    x2[0]+=y
    a+=1
    if a==y1:
        break
x2[0].reverse()

for y in x1[0]:
    for yy in x3:
        if y == yy[1]:
            x1[1]=round(x1[1]+yy[0],2)


for y in x2[0]:
    for yy in x3:
        if y == yy[1]:
            x2[1]=round(x2[1]+yy[0],2)         

print(x1)
print(x2)


