import timeit
import math
import random
from minmaxlist import minmax_contains, minmax_remove, minmax_add

# Within range of N values, try to randomly
# insert or remove value, for a number of trials.
def trialmm(n, extent):
    mm = []
    for t in range(n):
        i = random.randint(0,extent)
        if minmax_contains(mm, i):
            minmax_remove(mm, i)
        else:
            minmax_add(mm, i)

def trial(n, extent):
    mylist = []
    for t in range(n):
        i = random.randint(0,extent)
        if i in mylist:
            mylist.remove(i)
        else:
            mylist.append(i)


def runTrial(option):
    size = 100
    n = 8
    print ("Table for:", option)
    print ('N\t1E2\t1E3\t1E4\t1E5\t1E6')
    for p in range(6):
        extent = 100
        line = str(n) + '\t'
        for e in range(5):
            cmd = option + '(' + str(n) + "," + str(extent) + ')'
            tm = timeit.timeit(cmd, number=10000, setup="from __main__ import " + option)
            line += '%.2f' % tm
            line += '\t'
            extent *= 10
        print (line)
        n *= 2

if __name__ == '__main__':
    runTrial("trial")
    runTrial("trialmm")
    
