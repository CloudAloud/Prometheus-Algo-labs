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

    def importArray(self, array, parent=None):
        if array[0] == 0:
            array.pop(0)
            return None
        else:
            # Create a new node with a parent
            node = Node(array.pop(0), parent)

            # Make it root for tree if root doesn't exist yet
            if not self.root:
                self.root = node

            # Build tree by adding new nodes and connect them to the root
            node.left = self.importArray(array, node)
            node.right = self.importArray(array, node)

            return node

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
        result = []
        for leaf in self.leafWalk(self.root):
            next = leaf
            path = []
            while next:
                path.append(next.key)
                next = next.parent
            #print 'Path for leaf', leaf.key, ':\t', path
            for i in self.find(value, leaf):
                i.reverse()
                if result.count(i) == 0:
                    result.append(i)
        return result



    def find(self, value, node):
        result = []
        # Make path list
        while node is not None:
            #print "Look for", value, "in node:", node.key
            preresult = []
            path = self.calc(value, node)
            if path:
                for i in path:
                    preresult.append(i)
                result.append(preresult)
            node = node.parent

        return result

    def calc(self, value, node):
        result = []
        if node.key == value:
            result.append(node.key)
        elif (node.key < value) and (node is not self.root):
            #print "Call calc for value", value-node.key, " in node", node.parent.key
            prepath = self.calc(value-node.key, node.parent)
            if prepath:
                result.append(node.key)
                for i in prepath:
                    result.append(i)
        return result

def findBack(value, path):
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
                for k in find(value - nextPath[i], nextPath[i + 1:]):
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

v = 1940
#filename = 'data_examples_07/input_100e.txt'
filename = 'input_1000a.txt'

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
array.append(int(word))

tree = Tree()

tree.importArray(array)

array = tree.inorderTreeWalk(tree.root)
array.sort()

tree.inorderTreeInsert(tree.root, array)
#print tree.root.key
#for leaf in tree.leafWalk(tree.root):
#    print leaf.key
for i in tree.findSum(v, tree.root):
    print i