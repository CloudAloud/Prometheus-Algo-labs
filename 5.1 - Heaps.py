__author__ = 'minin'

# Initialize variables
filename = 'input_16_10000.txt'
#filename = 'data_examples_05/input_01_10.txt'
file = open(filename, 'r')
inputArray = []
hlow = []
hhigh = []


def parent(index):
    return index / 2

def left(index):
    return index * 2 + 1

def right(index):
    return (index * 2) + 2

def maxHeapify(array, index):
    #global array
    l = left(index)
    r = right(index)

    if l < len(array):
        if array[l] > array[index]:
            largest = l
        else:
            largest = index
    else:
        largest = index

    if r < len(array):
        if array[r] > array[largest]:
            largest = r
    #elif parent(largest) != largest:
        #return maxHeapify(array, parent(largest))

    if largest != index:
        tmp = array[index]
        array[index] = array[largest]
        array[largest] = tmp

        return maxHeapify(array, largest)
    else:
        return array
    pass

def minHeapify(array, index):
    #global array
    l = left(index)
    r = right(index)

    if l < len(array):
        if array[l] < array[index]:
            smallest = l
        else:
            smallest = index
    else:
        smallest = index

    if r < len(array):
        if array[r] < array[smallest]:
            smallest = r




    if smallest != index:
        tmp = array[index]
        array[index] = array[smallest]
        array[smallest] = tmp

        return minHeapify(array, smallest)
    else:
        return array
    pass

def buildMaxHeap(array):
    for i in range(len(array)/2-1,-1,-1):
        array = maxHeapify(array,i)
    return array

def buildMinHeap(array):
    for i in range(len(array)/2-1,-1,-1):
        array = minHeapify(array,i)
    return array

def findMinMax(iArray):

    array = iArray[:]
    if len(array) == 1:
        return 0, 0

    elif len(array) % 2 == 0:
        array.append(array[len(array) - 1])

    if array[0] < array[1]:
            min = 0
            max = 1
    else:
        min = 1
        max = 0

    for i in range(2,len(array) - 2, 2):
        if array[i] <= array[i + 1]:
            if array[i] < array[min]:
                min = i
            if array[i + 1] > array[max]:
                max = i + 1
        else:
            if array[i] > array[max]:
                max = i
            if array[i + 1] < array[min]:
                min = i + 1

    return min, max

def insertMaxTmp(array, element):
    array.append(element)
    return maxHeapify(array, len(array) - 1)

def insertMax(array, element):
    array.append(element)
    return buildMinHeap(array)
    #return maxHeapify(array, len(array) - 1)

def insertMin(array, element):
    array.append(element)
    return buildMaxHeap(array)
    #return minHeapify(array, len(array) - 1)


for line in file:
    inputArray.append(int(line))


# Insert element into a heap
counter = 1
for element in inputArray[1:]:
    #print 'Start: ', H_high, H_low
    # Place element in array
    if len(hlow) == 0:
        hhigh.append(element)
    #elif element < findMinMax(H_low)[1]:
    elif element < hlow[0]:
        hlow = insertMin(hlow, element)
    else:
        hhigh = insertMax(hhigh, element)

    # Check if arrays are equal or near that
    if (len(hlow)-len(hhigh) > 1) | (len(hhigh)-len(hlow) > 1):
        #print 'Enter diff with', hhigh, hlow
        if len(hlow) > len(hhigh):
            #print 'pop max', findMinMax(H_low)[1]
            #insertMax(H_high, H_low.pop(findMinMax(H_low)[1]))
            #H_high = insertMax(H_high, H_low.pop(0))
            hhigh = insertMax(hhigh, hlow[0])
            hlow[0] = hlow.pop()
            maxHeapify(hlow, 0)
            #print 'popped: ', H_high, H_low
            #buildMaxHeap(H_low)
        else:
            #print 'Pop from H_high:', findMinMax(H_high)[0], ' = ', H_high[findMinMax(H_high)[0]]
            #insertMin(H_low, H_high.pop(findMinMax(H_high)[0]))
            #print 'Pop from H_high:', H_high[0], H_high
            #H_low = insertMin(H_low, H_high.pop(0))
            hlow = insertMin(hlow, hhigh[0])
            hhigh[0] = hhigh.pop()
            minHeapify(hhigh, 0)
            #print 'popped: ', H_high, H_low
            #buildMinHeap(H_high)
    '''
    if len(hhigh) > len(hlow):
        print 'Medians:', hhigh[0]
        pass
    elif len(hhigh) < len(hlow):
        print 'Medians:', hlow[0]
        pass
    else:
        print 'Medians:', hlow[0], hhigh[0]
        pass
    '''
    if counter == 2015:
        print hlow[:5]
        print hhigh[:5]

    counter += 1
    #print 'H_low:', hlow
    #print 'H_high:', hhigh, '\n'




print 'Finish: ', hlow, hhigh



#a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
#a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#a = buildMaxHeap(a)
#a = buildMinHeap(a)
