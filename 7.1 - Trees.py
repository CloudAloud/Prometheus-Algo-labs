__author__ = 'minin'

def parent(index):
    return index / 2

def left(index):
    return index * 2 + 1

def right(index):
    return (index * 2) + 2

def inorderTreeWalk(index):
    if index is not None:
        result = str(inorderTreeWalk(tree[index][2]))
        result += ' ' + str(tree[index][0])
        result += ' ' + str(inorderTreeWalk(tree[index][3]))
        return result
    return ''

# Import input data
#filename = 'input_1000a.txt'
filename = 'data_examples_07/input_10a.txt'

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

#array = [5, 3, 7, 2, 4, 0, 8]
print array

# Build tree
tree = []

for index in range(len(array)):
    if index == 0:
        node = [array[index], None, 'u', 'u']
        tree.append(node)
    elif array[index] == 0:
        exit = False
        n = 0
        while exit == False:
            if tree[n][2] == 'u':
                tree[n][2] = None
                exit = True
            elif tree[n][3] == 'u':
                tree[n][3] = None
                exit = True
            n += 1
    else:
        node = [array[index], 'u', 'u', 'u']
        tree.append(node)
        exit = False
        n = 0
        while exit == False:
            if tree[n][2] == 'u':
                tree[n][2] = len(tree) - 1
                node[1] = n
                exit = True
            elif tree[n][3] == 'u':
                tree[n][3] = len(tree) - 1
                node[1] = n
                exit = True
            n += 1

for n in range(len(tree)):
    if tree[n][2] == 'u':
        tree[n][2] = None
    if tree[n][3] == 'u':
        tree[n][3] = None



print ''
for i in tree:
        print i


# Sort values
line = inorderTreeWalk(0)
aarray = []

word = ''
for character in line[:]:
        if (character == ' ') & (word != ''):
            aarray.append(int(word))
            word = ''
        else:
            word += character
if (character != ' ') & (word != ''):
    aarray.append(int(word))


print '\n', aarray