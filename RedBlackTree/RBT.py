class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = "BLACK"
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert(self, key):
        z = Node(key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "RED"
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)
        self.root.color = "BLACK"

    def preorder(self,filename):
        with open(filename, 'w') as f:
            self._preorder(self.root,f)

    def _preorder(self, x, f):
        if x != self.nil:
            f.write(f'{x.key} {x.color}\n')
            self._preorder(x.left,f)
            self._preorder(x.right,f)


# Example usage
input_file = open("./input.txt", "r")
if not input_file:
    print("File doesn't exist.")
else:
    numOfKeys = int(input_file.readline().strip())
    if numOfKeys < 1:
        print("The number of keys is less than 1")
        exit(0)
    arr = []
    i = 0
    while i < numOfKeys:
        key = input_file.readline().strip()
        if not key:
            break
        arr.append(int(key))
        i += 1

    if numOfKeys > i:
        print("The number of keys is not correct")
        print("The output file will sort the total amount of Keys.\n")
        numOfKeys = i

input_file.close()


tree = RedBlackTree()
for i in range(len(arr)):
    tree.insert(arr[i])
output_file = open("./output.txt", "w")
tree.preorder('output.txt')



    