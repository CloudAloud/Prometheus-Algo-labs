__author__ = 'minin'

#filename = 'test_06.txt'
filename = 'input_06.txt'
file = open(filename, 'r')

inputArray = []
hashArray = []


def hash(key, len):
    return key % len

def hashInsert(array, key):
    array[hash(element, x)].append(element)

def hashSearch(array, key):
    if array[hash(key, x)]:
        for element in array[hash(key, x)]:
            if element == key:
                return element
            else:
                return False
    else:
        return False

for i in file:
    inputArray.append(int(i[:-1]))
    hashArray.append([])

x = len(inputArray)/3
#x = 1000


for element in inputArray:
    hashInsert(hashArray, element)

counter = 0
for s in range(-1000, 1000):
    #print s
    for element in inputArray:
        y = s - element
        if (hashSearch(hashArray, y) != False) & (element != y):
            print element, y
            counter += 1

print counter
