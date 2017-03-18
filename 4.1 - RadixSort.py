__author__ = 'minin'

def RadixSort(array):

    # Run CountingSort for each index
    for i in range(len(array[0])):
        index = len(array[0]) - i - 1
        array = CountingSort(array, index)


    return array

def CountingSort(array, position):

    # Initialize variables
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    countArray = []
    shadowArray = []
    positionArray = []
    arrayAlphabet = []
    sortedArray = []

    # Fill in sortedArray
    for i in range(len(array)):
        sortedArray.append('')


    # Fill in arrayAlphabet array with letters from alphabet
    for letter in alphabet:
        arrayAlphabet.append(letter)

    # Fill in shadowArray with the position letters
    for item in array:
        shadowArray.append(item[position])

    # Count how many times letter appears in shadowArray
    for j in alphabet:
        countArray.append(shadowArray.count(j))

    # Make an array with positions of each letter in the alphabet
    counter = 0
    for i in range(len(countArray)):
        positionArray.append(counter + countArray[i])
        counter += countArray[i]


    for i in range(len(array)):
        position = len(array) - i - 1
        #print positionArray[arrayAlphabet.index(shadowArray[position])]
        sortedArray[positionArray[arrayAlphabet.index(shadowArray[position])] - 1] = array[position]
        positionArray[arrayAlphabet.index(shadowArray[position])] -= 1

    # Print out results
    '''print shadowArray
    print countArray
    print positionArray
    print arrayAlphabet
    print sortedArray'''

    return sortedArray

def FindMinMax(array):

    if len(array) % 2 == 0:
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



    return 0

# Initialize array
filename = 'anagrams.txt'
file = open(filename, 'r')
unsortedArray = []

for line in file:
    unsortedArray.append(line[:3])

# Sort input array

sortedArray = RadixSort(unsortedArray)

# Calculate letters usage
megaString = []
shadowAlphabet = []

for line in sortedArray:
    for letter in line:
        megaString.append(letter)


for letter in 'abcdefghijklmnopqrstuvwxyz':
    shadowAlphabet.append(megaString.count(letter))

# Find out the most used letter
theMostOftenLetter = 'abcdefghijklmnopqrstuvwxyz'[FindMinMax(shadowAlphabet)[1]]

# Recover and show password
password = sortedArray[0] + theMostOftenLetter + sortedArray[len(sortedArray) - 1]

print password

print CountingSort(unsortedArray, 2)[0]
print CountingSort(CountingSort(unsortedArray, 2), 1)[0]