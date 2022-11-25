def estandarizar(values):
        f = [0,[]]
        values.sort()
        values.reverse()
        for y in values:
            f[1]+=str(y[1])

        for y in values:
            f[0]=round(f[0]+y[0],2)
        return f


class Node:
    def __init__(self,value):
        self.value = value[1]
        self.frequency = value[0]
        self.right = None
        self.left = None

    


class Huffman:
    def __init__(self):
        self.root = None

    def add(self,x,x3,current):
        if self.root == None:
            self.root = Node(x)

        else:
            if len(x[1])%2==0 and len(x[1])!=1:


                if current.left==None:
                    xx=x
                    x1 = [[],0]
                    y1=len(x[1])/2
                    a=0
                    for y in x[1]:
                        x1[0]+=y
                        a+=1
                        if a==y1:
                            break

                    for y in x1[0]:
                        for yy in x3:
                            if y == yy[1]:
                                x1[1]=round(x1[1]+yy[0],2)
                    
                    print(x1)


                    current.left = Node()

                if current.right==None:
                    xx=x
                    current.right = Node()
            else:
                pass

                    

x3 = [[0.2,"A"],[0.17,"F"],[0.13,"1"],[0.21,"3"],[0.09,"M"],[0.15,"T"]]

x = estandarizar(x3)
print(x)
