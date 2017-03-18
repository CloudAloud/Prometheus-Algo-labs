__author__ = 'minin'

import sys

#X = sys.argv[1]
#Y = sys.argv[2]
#X = "1234"
#Y = "5678"
X = "1685287499328328297814655639278583667919355849391453456921116729"
Y = "7114192848577754587969744626558571536728983167954552999895348492"

def split(number):
    first = number[:len(number)/2]
    second = number[len(number)/2:]
    return first, second

def normalize(number):
    if len(number)%2 == 0:
        return number
#    elif len(number) == 1:
#        return number
    else:
        number = "0" + number
        return number

def normalize2(x, y):
    #print "normalize2: start with x=" + x + " and y=" + y
    if len(x) > len(y):
        #print "normalize2: x(" + x + ") > y(" + y + ")"
        while len(x) != len(y):
            y = "0" + y
    elif len(x) < len(y):
        #print "normalize2: x(" + x + ") < y(" + y + ")"
        while len(x) != len(y):
            x = "0" + x
    #print "normalize2: x="+ x + ",y=" + y

    power = 0
    while 2 ** power < len(x):
        power = power + 1
    #print "normalize2: power=" + str(power)

    while len(x) != 2 ** power:
        x = "0" + x
        y = "0" + y

    #print "normalize2: end with x=" + x + " and y=" + y
    return x, y

def multiply(x, y):
    #print "multiply: start with x=" + x + " and y=" + y
    if (len(x) == 1) & (len(y) == 1):
        #print "multiply: x="+ x + ",y=" + y + " return " + str(int(x) * int(y))
        return str(int(x) * int(y))
    else:
        #print "multiply: calling normalize2(" + x + ", " + y + ")"
        x , y = normalize2(x, y)
        #y = normalize2(x, y)[1]
        #print "multiply: after normalizatoin x="+ x + ",y=" + y
        a = split(x)[0]
        b = split(x)[1]
        c = split(y)[0]
        d = split(y)[1]
        #print "multiply: a="+ a + ",b=" + b + ",c=" + c + ",d=" + d
        #print "multiply: calculating ac"
        ac = multiply(a, c)
        #print "multiply: calculating bd"
        bd = multiply(b, d)
        #print "multiply: calculating ad_plus_bc"
        ad_plus_bc = str(int(multiply(str(int(a) + int(b)), str(int(c) + int(d)))) - int(ac) - int(bd))
        if int(ad_plus_bc) == 12:
            print ad_plus_bc
        #print "multiply: ac="+ ac + ",bd=" + bd + ",ad_plus_bc=" + ad_plus_bc
        #print "multiply: 10**len(x)=" + str(10 ** len(x))
        #print "multiply: 10**len(x)/2=" + str(10 ** (len(x) / 2))
        #power = 10 ** len(x)
        #print "multiply: power=" + str(power)
        acc = ac
        for i in range(len(x)):
            acc = acc + "0"
        #print "multiply: acc=" + acc
        #power = 10 ** len(x) / 2
        ad_plus_bcc = ad_plus_bc
        for i in range(len(x) / 2):
            ad_plus_bcc = ad_plus_bcc + "0"
        #print "multiply: ad_plus_bcc=" + ad_plus_bcc
        #print "multiply: ac="+ ac + ",bd=" + bd + ",ad_plus_bc=" + ad_plus_bc + ",acc=" + acc + ",ad_plus_bcc=" + ad_plus_bcc
        return str(int(acc) + int(ad_plus_bcc) + int(bd))

    #print str(a) + " " + str(b) + " " + str(c) + " " + str(d)



print multiply(X, Y)