__author__ = 'minin'

from datetime import datetime

print datetime.now()

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



    def importFromFile(self, file):
        print datetime.now(), 'importFromFile(): Start on file', filename
        vertexNumber = 0
        counter = 0
        tmpfile = open('tmp.txt', mode='w')
        tmpfile.flush()
        for line in file:
            if counter != 0:
                tmpfile.write(line)
                counter += 1
            else:
                print datetime.now(), 'importFromFile(): Creating nodes...'
                pair = line.split(' ')
                for i in range(int(pair[0])):
                    node = Node()
                    self.nodes.append(node)
                    self.nodes[i].number = i + 1
                counter += 1
                print datetime.now(), 'importFromFile():', len(self.nodes), 'Nodes were created'

        counter = 0

        print datetime.now(), 'importFromFile(): Building ribs...'
        tmpfile = open('c:\Users\minin\\tmp\\tmp.txt')
        for line in tmpfile:
            counter += 1
            rib = line.split(' ')
            self.nodes[int(rib[0]) - 1].toList[self.nodes[int(rib[1]) - 1]] = int(rib[2])
            #if counter % 100000 == 0:
            #    print 'importFromFile(): ', counter
        print datetime.now(), 'importFromFile():', counter, 'ribs were built'

    def OLDimportFromFile(self, file):
        print 'importFromFile(): Start on file "', filename
        vertexNumber = 0
        counter = 0
        print 'importFromFile(): Start to parse all lines'
        for line in file:
            pair = line.split(' ')
            for i in range(len(pair)):
                pair[i] = int(pair[i])

            if vertexNumber != 0:
                self.nodes[self.nodes.index(self.nodes[pair[0] - 1])].toList[self.nodes[pair[1] - 1]] = pair[2]
                counter += 1
            else:
                vertexNumber = pair[0]
                ribNumber = pair[1]
                print 'importFromFile(): Start on file "', filename, '" with', vertexNumber, 'nodes and', ribNumber, 'ribs'
                print 'importFromFile(): Create nodes'
                for i in range(vertexNumber):
                    node = Node()
                    self.nodes.append(node)
                    self.nodes[i].number = i + 1
                print 'importFromFile():', len(self.nodes) ,'Nodes were created'

            if counter % 1000 == 0:
                print 'importFromFile(): ', counter


        print 'importFromFile(): Finished'

        #list.sort()

        '''for i in range(vertexNumber):
            node = Node()
            self.nodes.append(node)
            self.nodes[i].number = i + 1'''

        '''for pair in connections:
            #print pair
            fromNode = self.nodes[pair[0] - 1]
            toNode = self.nodes[pair[1] - 1]
            cost = pair[2]

            self.nodes[self.nodes.index(fromNode)].toList[toNode] = cost'''

        '''ribs = 0
        for node in self.nodes:
            ribs += len(node.toList)

        if (vertexNumber == len(self.nodes)) & (ribNumber == ribs):
            pass
            #print 'Check is OK'
        else:
            print 'Start on file "', filename, '" with', vertexNumber, 'nodes and', ribNumber, 'ribs, but ', self, 'have', len(
                self.nodes), 'nodes and', ribs, 'ribs'
        '''

        print 'importFromFile(): End on file "', filename

    def SPF(self, srcNode):
        print datetime.now(), 'Start SPF() for node:', srcNode.number
        self.initialize()
        srcNode.bestpath = 0
        srcNode.predecessor = [srcNode]
        counter = 0
        #print 'Start with srcNode:', srcNode.number, ', Best path:', srcNode.bestpath, ', Visited:', len(
        #   self.visited), ', Unvisited:', len(self.unvisited)

        while self.unvisited:
            print datetime.now(), 'SPF(): unvisited lenght is', len(self.unvisited)

            pretendent = self.extractMin()
            if pretendent:
                bestNode = pretendent
            else:
                return 0
            #print 'Best node is', bestNode.number, ', visited:', len(self.visited), ', unvisited:', len(self.unvisited)
            self.visited.append(self.unvisited.pop(self.unvisited.index(bestNode)))

            for node in bestNode.toList:
                if (node.bestpath is not None) & (node.predecessor is not []) & (node is not bestNode):
                    if node.bestpath > bestNode.bestpath + bestNode.toList[node]:
                        node.bestpath = bestNode.bestpath + bestNode.toList[node]
                        node.predecessor.append(bestNode)
                    elif node.bestpath == bestNode.bestpath + bestNode.toList[node]:
                        node.predecessor.append(bestNode)
                elif node is not bestNode:
                    #node.predecessor = bestNode
                    node.predecessor.append(bestNode)
                    node.bestpath = bestNode.toList[node] + bestNode.bestpath
        print datetime.now(), 'End SPF() for node:', srcNode.number

    def extractMin(self):
        start_time = datetime.now()
        #print datetime.now(), 'extractMin(): Starting'
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
        print datetime.now(), 'extractMin(): Finished in', datetime.now() - start_time
        return minNode

    def initialize(self):
        self.visited = []
        self.unvisited = self.nodes[:]
        for node in self.nodes:
            node.bestpath = None
            node.predecessor = []

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

    def walk(self, finish):
        result = []
        for node in finish.predecessor:
            if node.predecessor[0] != node:
                for path in self.walk(node):
                    #path.append(node)
                    result.append(path)
                    pass
            else:
                #return [node]
                result.append(node)
        return result

    def trace(self, start, finish):
        print 'Start trace() for start:', start.number, 'and finish:', finish.number
        self.SPF(start)
        #return self.walk(finish)
        print 'Paths:', len(self.walk(finish))
        print 'Cost:', finish.bestpath



class Node:
    def __init__(self):
        self.number = 0
        self.toList = {}
        self.predecessor = []
        self.bestpath = None




#filename = 'test_09/input_8_10.txt'
#filename = 'test_09/test'
#filename = 'USA-FLA.txt'
filename = 'c:\\Users\\minin\\tmp\\USA-FLA.txt'
file = open(filename, 'r')

graph = Graph()
#graph.importFromFile(file)
#graph.SPF(graph.nodes[0])
#graph.showtable()
#graph.trace(graph.nodes[100561], graph.nodes[1070344])




'''graph.SPF(graph.nodes[0])
start = graph.nodes[0]
finish = graph.nodes[-2]
current = finish

print '\n', finish.number,
while current != start:
    print current.number, current.predecessor[0].number
    for i in current.predecessor:
        print i.number
    current = current.predecessor[0]'''