__author__ = 'minin'

import sys
from datetime import datetime
import cPickle


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
        self.unvisited = {}
        self.greyzone = {}

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
        tmpfile = open('tmp.txt')
        for line in tmpfile:
            counter += 1
            rib = line.split(' ')
            self.nodes[int(rib[0]) - 1].toList[self.nodes[int(rib[1]) - 1]] = int(rib[2])
            #if counter % 100000 == 0:
            #    print 'importFromFile(): ', counter
        print datetime.now(), 'importFromFile():', counter, 'ribs were built'

    def SPF(self, srcNode):
        #print datetime.now(), 'Start SPF() for node:', srcNode.number
        self.initialize()
        srcNode.bestpath = 0
        srcNode.predecessor = [srcNode]
        self.greyzone[srcNode] = srcNode.bestpath
        self.unvisited.pop(srcNode)
        #TODO make greyzone
        counter = 0
        #print 'Start with srcNode:', srcNode.number, ', Best path:', srcNode.bestpath, ', Visited:', len(
        #   self.visited), ', Unvisited:', len(self.unvisited)

        while self.greyzone:
            counter += 1
            if counter % 10000 == 0:
                print datetime.now(), 'SPF(): counter is', counter
            #print datetime.now(), 'SPF(): unvisited lenght is', len(self.unvisited)
            #print datetime.now(), 'SPF(): greyzone lenght is', len(self.greyzone)

            bestNode = self.extractMin()
            if bestNode:
                for node in bestNode.toList:
                    #if (node.bestpath is not None) & (node.predecessor is not []) & (node is not bestNode):
                    if (node.predecessor is not []) & (node is not bestNode):
                        if node.bestpath > bestNode.bestpath + bestNode.toList[node]:
                            node.bestpath = bestNode.bestpath + bestNode.toList[node]
                            node.predecessor.append(bestNode)
                            self.greyzone[node] = node.bestpath
                            try:
                                self.unvisited.pop(node)
                            except KeyError:
                                pass

                        elif node.bestpath == bestNode.bestpath + bestNode.toList[node]:
                            node.predecessor.append(bestNode)
                    elif node is not bestNode:
                        #node.predecessor = bestNode
                        node.predecessor.append(bestNode)
                        node.bestpath = bestNode.toList[node] + bestNode.bestpath
                        try:
                                self.unvisited.pop(node)
                        except KeyError:
                            pass
            else:
                return 0

            try:
                self.greyzone.pop(bestNode)
            except KeyError:
                pass

            #self.unvisited.pop(bestNode)



        #print datetime.now(), 'End SPF() for node:', srcNode.number

    def extractMin(self):
        start_time = datetime.now()
        minimum = None
        minNode = False
        #for node in self.unvisited:
        for node in self.greyzone:
            if (((node.bestpath >= 0) & (minimum is None)) | (node.bestpath < minimum)) & (node.bestpath is not None):
                minimum = node.bestpath
                minNode = node
        #minimum = min(self.unvisited)
        #print minNode.number, minNode.bestpath
        #print datetime.now(), 'extractMin(): Finished in', datetime.now() - start_time
        return minNode
        #return minimum

    def initialize(self):
        #print datetime.now(), 'initialize(): Initializing...'
        #self.visited = []
        self.unvisited = {}
        #self.unvisited = self.nodes[:]
        for node in self.nodes:
            node.bestpath = sys.maxint
            node.predecessor = []
            self.unvisited[node] = node.bestpath

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
                if node.bestpath is sys.maxint:
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
                    result.append(path)
            else:
                result.append(node)
        return result

    def wave(self, start, finish):
        wave = [finish]
        counter = 0
        lastlen = 0
        while wave:
            node = wave.pop(0)

            if lastlen != len(wave):
                print len(wave), node
            lastlen = len(wave)
            #print 'Start with:', wave


            if node == start:
                counter += 1
            else:
                for predecessor in node.predecessor:
                    #print 'Node:', node, 'Predecessor:', predecessor
                    wave.append(predecessor)

            #print 'Finish with:', wave

        return counter

    def wave2(self, start, finish):
        wave = finish.predecessor
        counter = len(wave)
        while wave.count(start) != len(wave):
            #print 'Wave:', wave
            for node in wave[:]:
                if node != start:
                    counter += len(node.predecessor) - 1
                    wave.pop(wave.index(node))
                    for predecessor in node.predecessor:
                        wave.append(predecessor)
        return wave


    def fasttrace(self, start, finish):
        print 'Start fasttrace() for start =', start.number, 'and finish =', finish.number
        self.SPF(start)
        #return self.walk(finish)
        print 'Cost:', finish.bestpath
        #paths = len(self.wave2(start, finish))
        #print 'Paths:', paths
        paths = self.wave(start, finish)
        print 'Paths:', paths
        node = finish
        while node != start:
            print node.number
            node = node.predecessor[0]

    def trace(self, start, finish):
        print 'Start trace() for start =', start.number, 'and finish =', finish.number
        self.SPF(start)
        #return self.walk(finish)
        print 'Cost:', finish.bestpath
        #paths = len(self.wave2(start, finish))
        #print 'Paths:', paths
        paths = self.wave(start, finish)
        print 'Paths:', paths


class Node:
    def __init__(self):
        self.number = 0
        self.toList = {}
        self.predecessor = []
        self.bestpath = None

def uconvert(graph):
    print datetime.now(), 'Start uconvert()...'
    for node in graph.nodes:
        predecessorList, toList = [], []
        for link in node.toList:
            toList.append(graph.nodes[link - 1])
        for predecessor in node.predecessor:
            predecessorList.append(graph.nodes[predecessor - 1])
        node.toList, node.predecessor = toList, predecessorList
    print datetime.now(), 'uconvert() finished.'

def read(filename):
    print datetime.now(), 'Start read()'
    dumpfile = open(filename, 'r')
    graph = cPickle.load(dumpfile)
    print datetime.now(), 'Read from', filename
    uconvert(graph)
    return graph

prodMode = False
#prodMode = True

if prodMode:
    filename = 'USA-FLA.txt'
    start = 100561
    finish = 1070344
else:
    filename = 'test_09/test'
    start = 0
    finish = 5

#file = open(filename, 'r')
#graph = Graph()
#graph.importFromFile(file)

#graph.SPF(graph.nodes[start])
#graph.showtable()
#graph.trace(graph.nodes[start], graph.nodes[finish])
#graph.fasttrace(graph.nodes[start], graph.nodes[finish])

graph = read(filename + '.dump')

node = graph.nodes[finish]

print node.number, node.bestpath, node.predecessor, node.toList