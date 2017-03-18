__author__ = 'minin'

filename = 'tmp.txt'
file = open(filename, 'r')

inputArray = []

for line in file:
    n1 = ''
    n2 = ''
    switch = False
    for letter in line:
        if letter == ' ':
            switch = True
        else:
            if switch == False:
                n1 += letter
            else:
                n2 += letter
    #print n1, n2
    inputArray.append((int(n1),int(n2[:-1])))

counterTable = []

for line in inputArray:
    if counterTable.count(line[0] + line[1]) == 0:
        counterTable.append(line[0] + line[1])
    print line, line[0] + line[1]

print counterTable
print len(counterTable)
