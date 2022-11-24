class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Huffman:
    def __init__(self):
        self.root = None

    def add(self,current,value):
        if self.root == None:
            self.root = Node(value)

        else:
            if value < current.value:
                if current.left == None