__author__ = 'minin'


import sys

filename = 'input__10000.txt'
#filename = 'data_examples_03/input__1000.txt'

def Partition(array, pStart, rFinish):

    # Second task
    '''
    tmp = array[pStart]
    array[pStart] = array[rFinish]
    array[rFinish] = tmp
    '''
    # Third task
    ''''''
    first = array[pStart]
    second = array[(rFinish+pStart)/2]
    third = array[rFinish]
    if ((first > second) & (first > third)):
        if second > third:
            tmp = array[(rFinish+pStart)/2]
            array[(rFinish+pStart)/2] = array[rFinish]
        else:
            tmp = array[rFinish]
    elif ((second > first) & (second > third)):
        if first > third:
            tmp = array[pStart]
            array[pStart] = array[rFinish]
        else:
            tmp = array[rFinish]
    elif ((third > first) & (third > second)):
        if first > second:
            tmp = array[pStart]
            array[pStart] = array[rFinish]
        else:
            tmp = array[(rFinish+pStart)/2]
            array[(rFinish+pStart)/2] = array[rFinish]
    elif first == second:
        tmp = array[pStart]
        array[pStart] = array[rFinish]

    array[rFinish] = tmp

    xPivot = array[rFinish]
    iEndOfLPart = pStart - 1
    for jStartOfUnsorted in range(pStart, rFinish):
        if array[jStartOfUnsorted] <= xPivot:
            iEndOfLPart += 1
            tmp = int(array[jStartOfUnsorted])
            array[jStartOfUnsorted] = int(array[iEndOfLPart])
            array[iEndOfLPart] = int(tmp)

    tmp = int(array[rFinish])
    array[rFinish] = int(array[iEndOfLPart+1])
    array[iEndOfLPart+1] = int(tmp)

    counter = rFinish - pStart
    #print counter
    return iEndOfLPart+1, counter

def QuickSort(array, p, r, counter = 0):
    if p < r:
        tmp = Partition(array, p, r)
        q = tmp[0]
        counter += tmp[1]
        counter += QuickSort(array, p, q - 1)
        counter += QuickSort(array, q + 1, r)
    return counter


file = open(filename, 'r')
unsortedArray = []
for line in file:
    unsortedArray.append(int(line))

finish = unsortedArray.pop(0)


# The fisrt task
#print unsortedArray
#print QuickSort(unsortedArray, 0, finish - 1)

# The second task
#print unsortedArray
print QuickSort(unsortedArray, 0, finish - 1)
