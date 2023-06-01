class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'Red'

class redBlackTree():
    def __init__(self):
        self.isNull = Node(0)
        self.isNull.color = 'Black'
        self.isNull.left = None
        self.isNull.right = None
        self.root = self.isNull

    def min(self, node):
        while node.left != self.isNull:
            node = node.left
        return node

    def rotateL(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.isNull:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotateR(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.isNull:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def transplant(self, toRemove, toReplace):
        if toRemove.parent == None:
            self.root = toReplace
        elif toRemove == toRemove.parent.left:
            toRemove.parent.left = toReplace
        else:
            toRemove.parent.right = toReplace
        toReplace.parent = toRemove.parent

    def rebalanceDelete(self, x):
        while x != self.root and x.color == 'Black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'Red':
                    w.color = 'Black'
                    x.parent.color = 'Red'
                    self.rotateL(x.parent)
                    w = x.parent.right

                if w.left.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.parent
                else:
                    if w.right.color == 'Black':
                        w.left.color = 'Black'
                        w.color = 'Red'
                        self.rotateR(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = 'Black'
                    w.right.color = 'Black'
                    self.rotateL(x.parent)
                    x = self.root
            #same as above with right and left swapped
            else:
                w = x.parent.left
                if w.color == 'Red':
                    w.color = 'Black'
                    x.parent.color = 'Red'
                    self.rotateR(x.parent)
                    w = x.parent.left

                if w.right.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.parent
                else:
                    if w.left.color == 'Black':
                        w.right.color = 'Black'
                        w.color = 'Red'
                        self.rotateL(s)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = 'Black'
                    w.left.color = 'Black'
                    self.rotateR(x.parent)
                    x = self.root
        x.color = 'Black'

    def deleteNode(self, key):
        node = self.root
        tbd = self.isNull
        while node != self.isNull:
            if node.data == key:
                tbd = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if tbd == self.isNull:
            print("Key not Found")
            return

        oColor = tbd.color
        if tbd.left == self.isNull:
            x = tbd.right
            self.transplant(tbd, x)
        elif tbd.right == self.isNull:
            x = tbd.left
            self.transplant(tbd,x)
        else:
            y = self.min(tbd.right)
            oColor = y.color
            x = y.right
            if y.parent == tbd:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = tbd.right
                y.right.parent = y

            self.transplant(tbd, y)
            y.left = tbd.left
            y.left.parent = y
            y.color = oColor
        if oColor == 'Black':
            self.rebalanceDelete(x)

    def rebalanceInsert(self, newNode):
        p = newNode.parent
        gp = p.parent
        while p.color == 'Red':
            if p == gp.left:
                z = gp.right
                if z.color == 'Red':
                    z.color = 'Black'
                    p.color = 'Black'
                    gp.color = 'Red'
                    newNode = gp
                else:
                    if newNode == p.right:
                        newNode = p
                        self.rotateL(newNode)
                    p.color = 'Black'
                    gp.color = 'Red'
                    self.rotateR(gp)
            else:
                z = gp.left

                if z.color == 'Red':
                    z.color = 'Black'
                    p.color = 'Black'
                    gp.color = 'Red'
                    newNode = gp
                else:
                    if newNode == p.left:
                        newNode = p
                        self.rotateL(newNode)
                    p.color = 'Black'
                    gp.color = 'Red'
                    self.rotateL(gp)
            if newNode == self.root:
                break
        self.root.color = 'Black'

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.isNull
        node.right = self.isNull
        node.color = 'Red'

        if self.root == None:
            self.root = node
            self.root.color = 'Black'
            return

        leaf = None
        current = self.root

        while current != self.isNull:
            leaf = current            
            if node.data > current.data:
                current = current.right
            else:
                current = current.left


        node.parent = leaf
        if node.parent == None:
            self.root = node
            node.color = 'Black'
            return
        elif node.data > node.parent.data:
            node.parent.right = node
        else:
            node.parent.left = node

        self.rebalanceInsert(node)

    def getRoot(self):
        print(str(self.root.data))

    def print_in_order(self, node):
        if node.left != self.isNull:
            self.print_in_order(node.left)
        print(str(node.data))
        if node.right != self.isNull:
            self.print_in_order(node.right)

bst = redBlackTree()

bst.insert(1)
bst.insert(1)
bst.insert(5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
bst.print_in_order(bst.root)
bst.deleteNode(6)
bst.deleteNode(1)
bst.deleteNode(8)
bst.deleteNode(1)
bst.deleteNode(5)
bst.deleteNode(3)

bst.getRoot()
