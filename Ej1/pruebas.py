def estandarizar(values):
        f = [0,[]]
        values.sort()
        values.reverse()
        for y in values:
            f[1]+=str(y[1])

        for y in values:
            f[0]+=y[0]
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

    def add(self,x,x1):
        if self.root == None:
            self.root = Node(x1)

        else:
            if len(x1[1])%2==0:
                pass
            else:
                pass

                    

x = [[0.2,"A"],[0.17,"F"],[0.13,1],[0.21,3],[0.05,0],[0.09,"M"],[0.15,"T"]]

x1 = estandarizar(x)
print(x1)
