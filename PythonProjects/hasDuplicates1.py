import time
import timeit

def has_duplicates1(list):
    dups = False
    
    for i in range(len(list)):
        for j in range(len(list)):
            if((i != j) and (list[i] == list[j])):
                dups = True
    return dups

def has_duplicates2(list):
    dups = True
    if(len(list) == len(set(list))):
        dups = False
    
    return dups

def test1(size, trials):
    testList = list(range(size))

    start = time.time()
    
    for i in range(1, trials):
        has_duplicates1(testList)

    end = time.time()

    avgTime = (end-start)/trials

    return avgTime
        

def test2(size, trials):
    testList = list(range(size))
    #for i in range(0, size-1):
        #testList.append(i)
    
    #time1 = timeit.timeit(has_duplicates2(testList), number = trials)

    #time2 = timeit(has_duplicates2(testList), number = trials)

    t1 = timeit.Timer("has_duplicates2({})".format(testList), "from __main__ import has_duplicates2")
    time1 = t1.timeit(number = trials)


    avgTime = time1/trials

    return avgTime

print(test1(100, 100))
print(test2(100, 100))


def has_duplicates3(list):
    testList = []
    dups = False
    
    for i in range(len(list)):
            if(list[i] in testList):
                dups = True
            else:
                testList.append(list[i])
    return dups

def has_duplicates4(list):
    testSet = {}
    dups = False
    
    for i in range(len(list)):
            length1 = len(testSet)
            testSet.add(list[i])
            length2 = len(testSet)
            if length1 == length2: 
                dups = True

    return dups

