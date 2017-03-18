__author__ = 'minin'


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.sccList = []
        self.currentScc = 0

    def importFromFile(self, file):
        list = []
        connections = []
        digitsList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for line in file:
            number = ''
            pair = []

            for digit in line:
                if digitsList.count(digit) == 1:
                    number = number + digit
                elif number != '':
                    list.append(int(number))
                    pair.append(int(number))
                    number = ''
                else:
                    number = ''

            connections.append(pair)

        list.sort()

        for i in range(list.pop()):
            node = Node()
            self.nodes.append(node)
            self.nodes[i].number = i + 1

        for pair in connections:
            graph.nodes[pair[0] - 1].toList.append(graph.nodes[pair[1] - 1])
            graph.nodes[pair[1] - 1].fromList.append(graph.nodes[pair[0] - 1])

    def DFS(self):
        for node in self.nodes:
            node.color = 'White'
            node.predecessor = None

        time = 0
        for node in self.nodes:
            if node.color == 'White':
                time = self.DFS_visit(node, time)

    def DFS_visit(self, node, time):
        time += 1
        node.opening_time = time
        node.color = 'Grey'
        for next in node.toList:
            if next.color == 'White':
                next.predecessor = node
                time = self.DFS_visit(next, time)
        node.color = 'Black'
        time += 1
        node.closing_time = time
        return time

    def reverse_DFS(self):
        list, nodelist = [], []
        for node in self.nodes:
            node.color = 'White'
            node.predecessor = None
            list.append((node, node.closing_time))

        for node in sorted(list, key=lambda nodde: nodde[1], reverse=True):
            nodelist.append(node[0])

        for node in nodelist:
            if node.color == 'White':
                self.sccList.append([])
                self.reverse_DFS_visit(node)
                self.currentScc += 1

    def reverse_DFS_visit(self, node):
        node.color = 'Grey'
        self.sccList[self.currentScc].append(node)
        for next in node.fromList:
            if next.color == 'White':
                next.predecessor = node
                self.reverse_DFS_visit(next)
        node.color = 'Black'

    def printSCC(self):
        self.importFromFile(file)
        self.DFS()
        self.reverse_DFS()

        sccList = []
        for scc in self.sccList:
            sccList.append(len(scc))
        sccList.sort()
        sccList.reverse()
        print sccList





class Node:
    def __init__(self):
        self.color = 'White'
        self.number = 0
        self.toList = []
        self.fromList = []
        self.predecessor = None
        self.opening_time = None
        self.closing_ime = None


filename = 'test_08/test_08_1.txt'
filename = 'test_08/test_08_4.txt'
file = open(filename, 'r')

graph = Graph()

graph.printSCC()
'''
print '\n Number \t',
for n in range(10):
    print '\t\t', graph.nodes[n].number,
print '\n Color \t\t',
for n in range(10):
    print '\t', graph.nodes[n].color,
print '\n Opening time',
for n in range(10):
    print '\t\t', graph.nodes[n].opening_time,
print '\n Closing time',
for n in range(10):
    print '\t\t', graph.nodes[n].closing_time,
    '''