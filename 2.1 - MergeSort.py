__author__ = 'minin'

import unittest

counter = 0

class MyTests(unittest.TestCase):

    def setUp(self):
        pass

#doubleSort function
    def test_doubleSort_1(self):
        self.assertEqual(doubleSort([1, 2, 3, 4, 5], [3, 5, 2, 1, 4]), ([1, 2, 3, 4, 5], [3, 5, 2, 1, 4]))

    def test_doubleSort_2(self):
        self.assertEqual(doubleSort([1, 2, 3, 4, 5], [2, 5, 3, 1, 4]), ([1, 2, 3, 4, 5], [2, 5, 3, 1, 4]))

    def test_doubleSort_3(self):
        self.assertEqual(doubleSort([3, 5, 2, 1, 4], [2, 5, 3, 1, 4]), ([1, 2, 3, 4, 5], [1, 3, 2, 4, 5]))

    def test_doubleSort_4(self):
        self.assertEqual(doubleSort([2, 5, 3, 1, 4], [3, 5, 2, 1, 4]), ([1, 2, 3, 4, 5], [1, 3, 2, 4, 5]))

    def test_doubleSort_5(self):
        self.assertEqual(doubleSort([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))

    def test_doubleSort_6(self):
        self.assertEqual(doubleSort([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))

#merge function
    def test_merge_1(self):
        self.assertEqual(merge([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_merge_2(self):
        self.assertEqual(merge([4, 5, 1, 2, 3]), [1, 2, 3, 4, 5])

    def test_merge_3(self):
        self.assertEqual(merge([4, 5, 1, 3]), [1, 3, 4, 5])

    def test_merge_4(self):
        self.assertEqual(merge([1, 3, 5, 7, 9, 0, 2, 4, 6, 8]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_5(self):
        self.assertEqual(merge([1, 9, 3, 4, 5]), [1, 3, 4, 5, 9])

#    def test_merge_6(self):
#        self.assertEqual(merge([1, 3, 5, 4, 5]), [1, 3, 4, 5, 9])

#mergeSort function
    def test_mergeSort_1(self):
        self.assertEqual(mergeSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_mergeSort_2(self):
        self.assertEqual(mergeSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_mergeSort_3(self):
        self.assertEqual(mergeSort([2, 4, 3, 5, 1]), [1, 2, 3, 4, 5])
#calc function
    def test_calc_1(self):
        self.assertEqual(calc(1, 1), 0)

    def test_calc_2(self):
        self.assertEqual(calc(2, 2), 0)

    def test_calc_3(self):
        self.assertEqual(calc(4, 236), 10)

    def test_calc_4(self):
        self.assertEqual(calc(236, 4), 10)

    def test_calc_5(self):
        self.assertEqual(calc(236, 236), 0)




def readFromFile(filename):
    numbers = '1234567890'
    dictionary = {}
    file = open(filename, 'r')

    for line in file:
        numbersList = []
        number = ''

        for value in line:
            if numbers.count(value) == 1:
                number += value
            else:
                if number != '':
                    numbersList.append(int(number))
                    number = ''
        userID = numbersList[0]
        preferences = numbersList[1:]

        dictionary[userID] = preferences

    file.close()
    return dictionary


def doubleSort(first, second):
    a, b = first[:], second[:]
    for j in range(1, len(first)):
        keya, keyb = a[j], b[j]
        i = j - 1
        #print "j = {0}, i = {1}, keya = {2}, keyb = {3}".format(j, i, keya, keyb)
        while (i >= 0) & (a[i] > keya):
            a[i + 1] = a[i]
            b[i + 1] = b[i]
            i -= 1
        a[i + 1] = keya
        b[i + 1] = keyb
    return a, b


def merge(a):
    result = a[:]
    l = a[:len(a) / 2]
    r = a[len(a) / 2:]
    l.append('x')
    r.append('x')
    i, j, = 0, 0
    global counter

    for k in range(len(result)):
        if (l[i] != 'x') & ((l[i] <= r[j]) | (r[j] == 'x')):
            result[k] = l[i]
            i += 1
        elif r[j] != 'x':
            result[k] = r[j]
            j += 1
            if l[i] != 'x':
                counter += len(l) - i - 1
    #print counter, result, l, r
    return result

def merge_back(a):
    l = a[:len(a) / 2]
    r = a[len(a) / 2:]
    result = []
    l.append('x')
    r.append('x')
    i, j, = 0, 0
    global counter
    while (l[i] != 'x') | (r[j] != 'x'):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
            if l[i] != 'x':
                counter += 1
    print counter, l, r
    return result


def mergeSort(a):
    #if type(a) == int:
    #print 'mergeSort: ' + str(type(a))  + " len: " + str(len(a)) + " len/2: " + str(len(a) / 2)
    if len(a) == 1:
        #print 'return ' + str(a)
        return a
    else:
        #print a[:len(a) / 2] + a[len(a) / 2:]
        #print merge(mergeSort(a[:len(a) / 2]) + mergeSort(a[len(a) / 2:]))
        return merge(mergeSort(a[:len(a) / 2]) + mergeSort(a[len(a) / 2:]))


def calc(user1, user2):
    global counter
    #print 'user {0}: {1}'.format(user1, database[user1])
    #print 'user {0}: {1}'.format(user2, database[user2])
    #print database[236]
    counter = 0
    mergeSort(doubleSort(database[user1], database[user2])[1])
    return counter

#database = readFromFile('input_1000_5.txt')
database = readFromFile('input_1000_100.txt')


#print database[1], database[2], database[3], database[4], database[236]
print calc(618,1)
print calc(1,618)
print calc(951,178)
print calc(178,951)

#unittest.main()
