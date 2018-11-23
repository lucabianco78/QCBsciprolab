"""In file: performance_test.py"""
import sys
sys.path.append('InsSort')
import InsSort
sys.path.append('SelSort')
import SelSort
import random

def getNrandom(n):
    res = []
    for i in range(n):
        res.append(random.randint(-10000,10000))
    return res

def testSorters(myList, verbose = False):
    #copy because the sorter will actually change the list!
    myList1 = myList[:] 
    selSorter = SelSort.SelectionSort(myList, verbose = False)
    insSorter = InsSort.InsertionSort(myList1, verbose = False)
    if verbose:
        print("TestList:\n{}".format(myList))
        print("TestList1:\n{}".format(myList1))
    selSorter.sort()
    insSorter.sort()
    if verbose:
        print("Outputs:")
        print(myList)
        print(myList1)
    print("Test with {} elements".format(len(myList)))
    print("Insertion sort:")
    print("Number of comparisons: {}".format(insSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(insSorter.getOperations()))
    print("In {:.4f}s".format(insSorter.getTime()))
    print("Selection sort:")
    print("Number of comparisons: {}".format(selSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(selSorter.getOperations()))
    print("In {:.4f}s".format(selSorter.getTime()))    

testList = getNrandom(10)
testSorters(testList, verbose = True)
print("#############")
testList = getNrandom(1000)
testSorters(testList, verbose = False)
print("#############")
testList = getNrandom(10000)
testSorters(testList, verbose = False)
print("#############")
testList = getNrandom(20000)
testSorters(testList, verbose = False)
print("#############")
testList = list(range(1000))
testSorters(testList, verbose = False)
print("#############")
testList = list(range(5000))
testList.sort(reverse = True)
testSorters(testList, verbose = False)
a = list(range(1000))
b = list(range(1000,2000))
b.sort(reverse = True)
testList = a + b
testSorters(testList, verbose = False)
