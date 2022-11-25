x=[1.0, ['3', 'A', 'F', 'T', '1', 'M']]
xx=x
x1 = []
x2 = []
y1=len(x[1])/2
a=0
for y in x[1]:
    x1+=y
    a+=1
    if a==y1:
        break

xx[1].reverse()

a=0

for y in xx[1]:
    x2+=y
    a+=1
    if a==y1:
        break
x2.reverse()

print(x1)
print(x2)


