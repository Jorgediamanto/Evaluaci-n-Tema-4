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
        self.value = value[0]
        self.frequency = value[1]
        self.right = None
        self.left = None

    


class Huffman:
    def __init__(self):
        self.root = None

    def hacer_arbol(self,x,x3):
        print(x)
        if self.root == None:
            self.root = Node(x)

        else:
            if len(x[0])%2==0 and len(x[0])!=1:


                
                xx=x
                x1 = [[],0]
                x2 = [[],0]
                y1=len(x[0])/2
                a=0
                for y in x[0]:
                    x1[0]+=y
                    a+=1
                    if a==y1:
                        break

                for y in x1[0]:
                    for yy in x3:
                        if y == yy[1]:
                            x1[1]=round(x1[1]+yy[0],2)
                
                print(x1)

                xx[0].reverse()

                a=0

                for y in xx[0]:
                    x2[0]+=y
                    a+=1
                    if a==y1:
                        break
                x2[0].reverse()

                for y in x2[0]:
                    for yy in x3:
                        if y == yy[1]:
                            x2[1]=round(x2[1]+yy[0],2) 

                print(x2)


                self.root.left = Huffman()
                self.root.left.hacer_arbol(x1,x3) 
                self.root.left.hacer_arbol(x1,x3)   
                self.root.right = Node(x2)
            elif len(x[0])%2!=0 and len(x[0])!=1:
                print("hola")
                pass

                    

x3 = [[0.2,"A"],[0.17,"F"],[0.13,"1"],[0.21,"3"],[0.09,"M"],[0.15,"T"]]

x = estandarizar(x3)
x.reverse()

print(x)
a = Huffman()
a.hacer_arbol(x,x3)
a.hacer_arbol(x,x3)
#print(a.root.left.value)
