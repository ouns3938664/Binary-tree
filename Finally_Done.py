class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    print2DTree(root)
                else:
                    self.left.insert(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = Node(data)
                    print2DTree(root)
                else:
                    self.right.insert(data)


def print2DTree(root, space=0, LEVEL_SPACE=5):
    if (root == None):
        return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    # print() # neighbor space
    for i in range(LEVEL_SPACE, space):
        print(end=" ")
    print("|" + str(root.data) + "|<")
    print2DTree(root.left, space)


def lastNodeDel(root, myLastNode):
    myQueue = []
    myQueue.append(root)
    while (len(myQueue)):
        temp = myQueue.pop(0)
        if temp is myLastNode:
            temp = None
            return
        if temp.right:
            if temp.right is myLastNode:
                temp.right = None
                return
            else:
                myQueue.append(temp.right)
        if temp.left:
            if temp.left is myLastNode:
                temp.left = None
                return
            else:
                myQueue.append(temp.left)


def delNode(root, delTarget):
    if root == None:
        return None
    if root.left is None and root.right is None:
        if root.data == delTarget:
            temp = root.right
            root = None
            return temp
    delTarget_node = None
    myQueue = []
    myQueue.append(root)
    temp = None
    while (len(myQueue)):
        temp = myQueue.pop(0)
        if temp.data == delTarget:
            delTarget_node = temp
        if temp.left:
            myQueue.append(temp.left)
        if temp.right:
            myQueue.append(temp.right)
    if delTarget_node:
        lastNodeVal = temp.data
        lastNodeDel(root, temp)
        delTarget_node.data = lastNodeVal
    return root


def build(arr, lower, upper):
    size = upper - lower + 1
    if size <= 0:
        return None
    middle = size // 2 + lower

    subtree_root = Node(arr[middle])
    subtree_root.left = build(arr, lower, middle - 1)
    subtree_root.right = build(arr, middle + 1, upper)
    return subtree_root


def myBalance(new_root):

    def printBalanceTree(new_root, space=0, LEVEL_SPACE=5):
        if (new_root == None):
            return
        space += LEVEL_SPACE
        printBalanceTree(new_root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space):
            print(end=" ")
        print("|" + str(new_root.data) + "|<")
        printBalanceTree(new_root.left, space)

    myIntTree = [eval(i) for i in myListTree]
    myIntTree.sort()
    new_root = build(myIntTree, 0, len(myIntTree)-1)
    printBalanceTree(new_root)
    return new_root


def myDel(root):
    delTarget = int(input('Del Node: '))
    root = delNode(root, delTarget)
    delLoc = myListTree.index(str(delTarget))
    myListTree.pop(delLoc)
    print2DTree(root)
    myAdd()


def myAdd():
    while (1):
        myNode = input(
            'Add Node (Type D for Delete mode Or B to Show Balance): ')
        if myNode.isdigit():
            myListTree.append(str(myNode))
            root.insert(int(myNode))
        elif myNode is 'D':
            myDel(root)
            break
        elif myNode is 'B':
            myBalance(root)
            break
        else:
            print('Only INT!')


myListTree = []
while (1):
    myRoot = input('Add Root:')
    if myRoot.isdigit():
        root = Node(int(myRoot))
        rootDel = (input('Press R to delete root or Press any to skip: '))
        while rootDel is 'R':
            root = delNode(root, int(myRoot))
            myRoot = input('Add Root:')
            root = Node(int(myRoot))
            rootDel = (input('Press R to delete root or Press any to skip: '))
        break
    else:
        print('Only INT!')
myListTree.append(str(myRoot))
print2DTree(root)
while (1):
    myAdd()
    new_root = None
