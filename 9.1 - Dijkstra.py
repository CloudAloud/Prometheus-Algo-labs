__author__ = 'minin'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Graph:
    def __init__(self):
        self.nodes = []
        self.sccList = []
        self.currentScc = 0

    def importFromFile(self, file):
        list = []
        connections = []
        digitsList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        vertexNumber = 0
        ribNumber = 0
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

            if vertexNumber == 0:
                vertexNumber = pair[0]
                ribNumber = pair[1]
                #print 'Start on file "', filename, '" with', vertexNumber, 'nodes and', ribNumber, 'ribs'
            else:
                connections.append(pair)

        list.sort()

        for i in range(vertexNumber):
            node = Node()
            self.nodes.append(node)
            self.nodes[i].number = i + 1

        for pair in connections:
            #print pair
            fromNode = self.nodes[pair[0] - 1]
            toNode = self.nodes[pair[1] - 1]
            cost = pair[2]

            #self.nodes[pair[0] - 1].toList.append((self.nodes[pair[1] - 1], pair[2]))
            #self.nodes[pair[1] - 1].fromList.append((self.nodes[pair[0] - 1], pair[2]))

            self.nodes[self.nodes.index(fromNode)].toList[toNode] = cost

        ribs = 0
        for node in self.nodes:
            ribs += len(node.toList)

        if (vertexNumber == len(self.nodes)) & (ribNumber == ribs):
            pass
            #print 'Check is OK'
        else:
            print 'Start on file "', filename, '" with', vertexNumber, 'nodes and', ribNumber, 'ribs, but ', self, 'have', len(
                self.nodes), 'nodes and', ribs, 'ribs'

    def SPF(self, srcNode):
        self.initialize()
        srcNode.bestpath = 0
        srcNode.predecessor = True

        #print 'Start with srcNode:', srcNode.number, ', Best path:', srcNode.bestpath, ', Visited:', len(
        #   self.visited), ', Unvisited:', len(self.unvisited)

        while self.unvisited:
            pretendent = self.extractMin()
            if pretendent:
                bestNode = pretendent
            else:
                return 0

            #print 'Best node is', bestNode.number, ', visited:', len(self.visited), ', unvisited:', len(self.unvisited)
            self.visited.append(self.unvisited.pop(self.unvisited.index(bestNode)))

            for node in bestNode.toList:
                if (node.bestpath is not None) & (node.predecessor is not None) & (node is not bestNode):
                    if node.bestpath > bestNode.bestpath + bestNode.toList[node]:
                        node.bestpath = bestNode.bestpath + bestNode.toList[node]
                        node.predecessor = bestNode
                elif node is not bestNode:
                    node.predecessor = bestNode
                    #node.bestpath = bestNode.toList[node] + bestNode.bestpath
                    node.bestpath = bestNode.toList[node] + bestNode.bestpath
                    #print 'Cycle: node is', node.number, ', best path is', node.bestpath, ', visited:', len(
                    #self.visited), ', unvisited:', len(self.unvisited)

    def extractMin(self):
        minimum = None
        minNode = False
        #print self.unvisited
        for node in self.unvisited:
            #print node.number, node.bestpath
            #if (node.bestpath > 0) & (node.bestpath < minimum):
            if (((node.bestpath >= 0) & (minimum is None)) | (node.bestpath < minimum)) & (node.bestpath is not None):
                minimum = node.bestpath
                minNode = node
                #print 'set node to', node.number, 'and set minimum to', minimum

        #print 'Extract: min node is', minNode.number, ', best path is', minNode.bestpath
        return minNode


    def initialize(self):
        self.visited = []
        self.unvisited = self.nodes[:]
        for node in self.nodes:
            node.bestpath = None
            node.predecessor = None

    def showtable(self):
        print bcolors.WARNING, '\t',
        for node in graph.nodes:
            print '\t', node.number,

        for node in graph.nodes:

            if node.number < 10:
                tab = '\t'
            else:
                tab = ''

            print '\n', node.number, bcolors.OKBLUE, tab,

            #print '\n', node.number,
            graph.SPF(node)
            for node in graph.nodes:
                if node.bestpath is None:
                    result = '-'
                else:
                    result = node.bestpath

                print '\t', result,


            print bcolors.WARNING,
        print bcolors.ENDC


class Node:
    def __init__(self):
        self.number = 0
        self.toList = {}
        self.predecessor = None
        self.bestpath = None
        self.paths = 1



#filename = 'test_09/input_8_10.txt'
filename = 'test_09/test'
#filename = 'test_09/input_4_1000.txt'
file = open(filename, 'r')

graph = Graph()
graph.importFromFile(file)
graph.showtable()


graph.SPF(graph.nodes[0])
start = graph.nodes[0]
finish = graph.nodes[-2]
current = finish

print '\n', finish.number,
while current != start:
    print current.predecessor.number,
    current = current.predecessor
