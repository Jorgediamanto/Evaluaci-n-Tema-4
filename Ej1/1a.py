class Node:
    def __init__(self,value,frequency):
        self.value = value
        self.frequency = frequency
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
                if current.left == None:
                    current.left= Node(value)
                else:
                    self.add(current.left,value)

            else:
                if current.right == None:
                    current.right= Node(value)
                else:
                    self.add(current.right,value)
