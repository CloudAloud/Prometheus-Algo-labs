__author__ = 'minin'


class Node:
    def __init__(self, key='u', parent='u', left='u', right='u'):
        self.key, self.parent, self.left, self.right = key, parent, left, right

    def show(self):
        #print self.value, self.parent, self.left, self.right
        print '\nSelf:\t', self, '\nValue:\t', self.key, \
            '\nParent:\t', self.parent, '\nLeft:\t', self.left, '\nRight:\t', self.right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insertNext(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            newNode.parent = None
        else:
            if self.root.left == 'u':
                self.root.left = newNode
                newNode.parent = self.root
            elif self.root.right == 'u':
                self.root.right = newNode
                newNode.parent = self.root
            else:
                pass  # Continue it!!!!!!!!!!!!!!!!!!!!!!

    def importArray(self, array):

        print 'Start with:\t\t\t', array
        # Build table with relations
        preTree = []
        for index in range(len(array)):
            if index == 0:
                node = [array[index], None, 'u', 'u']
                preTree.append(node)
            elif array[index] == 0:
                exit = False
                n = 0
                while exit == False:
                    if preTree[n][2] == 'u':
                        preTree[n][2] = None
                        exit = True
                    elif preTree[n][3] == 'u':
                        preTree[n][3] = None
                        exit = True
                    n += 1
            else:
                node = [array[index], 'u', 'u', 'u']
                preTree.append(node)
                exit = False
                n = 0
                while exit == False:
                    if preTree[n][2] == 'u':
                        preTree[n][2] = len(preTree) - 1
                        node[1] = n
                        exit = True
                    elif preTree[n][3] == 'u':
                        preTree[n][3] = len(preTree) - 1
                        node[1] = n
                        exit = True
                    n += 1

        # Change undefined children to None
        for n in range(len(preTree)):
            if preTree[n][2] == 'u':
                preTree[n][2] = None
            if preTree[n][3] == 'u':
                preTree[n][3] = None


        # Create nodes
        result = []
        for i in range(len(preTree)):
            result.append(Node(preTree[i][0]))

        # Build tree from nodes
        for index in range(len(result)):
            try:
                result[index].parent = result[preTree[index][1]]
            except TypeError:
                result[index].parent = None
            try:
                result[index].left = result[preTree[index][2]]
            except TypeError:
                result[index].left = None
            try:
                result[index].right = result[preTree[index][3]]
            except TypeError:
                result[index].right = None

        self.root = result[0]

        array = self.inorderTreeWalk(self.root)
        array.sort()
        print 'Imported:\t\t\t', self.inorderTreeWalk(self.root)
        self.inorderTreeInsert(self.root, array)
        print 'Balanced:\t\t\t', self.inorderTreeWalk(self.root)
        print 'Root:\t\t\t\t', self.root.key

    def inorderTreeInsert(self, root, array):
        if root:
            self.inorderTreeInsert(root.left, array)
            #print 'old', root.key, array
            root.key = array.pop(0)
            #print 'new', root.key, array
            self.inorderTreeInsert(root.right, array)

    def inorderTreeWalk(self, root):
        if root:
            result = []
            for i in self.inorderTreeWalk(root.left):
                result.append(i)
            result.append(root.key)
            for i in self.inorderTreeWalk(root.right):
                result.append(i)
            return result
        else:
            return []

    def leafWalk(self, root):
        if root:
            result = []
            for i in self.leafWalk(root.left):
                result.append(i)
            if root.left is None and root.right is None:
                result.append(root)
            for i in self.leafWalk(root.right):
                result.append(i)
            return result
        else:
            return []

    def findSum(self, value, root):
        pathlist = []
        for leaf in self.leafWalk(self.root):
            start = leaf
            path = []
            while leaf:
                path.append(leaf.key)
                leaf = leaf.parent
            print 'Path for leaf', start.key, ':\t', path
            pathlist.append(path)
        print 'Pathlist:\t\t\t', pathlist

        for path in pathlist:
            print path, find(value, path)

def find(value, path):
    #print '>>> Start search', value, 'in', path
    result, nextPath = [], []
    if path:
        while len(path) > 0:
            if path[0] > value:
                path.pop(0)
            elif path[0] == value:
                result.append(path.pop(0))
            else:
                nextPath.append(path.pop(0))

        #print '--- searching', value,  'with result', result, 'and nextPath', nextPath

        if nextPath:

            for i in range(len(nextPath)):
                #answer = []
                for k in find(value-nextPath[i], nextPath[i+1:]):
                    answer = []
                    answer.append(nextPath[i])
                    try:
                        for l in k:
                            answer.append(l)
                    except TypeError:
                        answer.append(k)
                    counter = 0
                    for j in answer:
                        counter += j
                    if counter == value:
                            result.append(answer)


        #print '<<< Stop search', value, 'in', path, 'with', result
        return result
    else:
        return []


filename = 'data_examples_07/input_10a.txt'
#filename = 'data_examples_07/input_10b.txt'
#filename = 'input_1000a.txt'

file = open(filename, 'r')

array = []
for line in file:
    word = ''
    for character in line[:]:
        if character == ' ':
            array.append(int(word))
            word = ''
        else:
            word += character

tree = Tree()

#array = [5, 3, 7, 2, 4, 0, 8]
#array = [1, 4, 6, 10, 0, 0, 0, 7, 0, 8, 0, 0, 2, 5, 0, 0, 3, 9, 0]

tree.importArray(array)
tree.findSum(9, tree.root)

#a = [3, 4, 2, 5, 1]
#a = [3, 2, 1, 4, 5]
#a = [3, 4, 2, 5, 1, 6, 7, 8, 9]
#print find(9,array)