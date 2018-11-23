"""file: InsSort.py"""

import random
import time

class InsertionSort:
    def __init__(self,data, verbose = True):
        self.__data = data
        self.__comparisons = 0
        self.__operations = 0
        self.__verbose = verbose
        self.__time = 0
        
    def getData(self):
        return self.__data
    
    def getTime(self):
        return self.__time
    
    def getComparisons(self):
        return self.__comparisons
    
    def getOperations(self):
        return self.__operations
    
    
    
    def sort(self):
        self.__comparisons = 0
        self.__operations = 0
        if self.__verbose:
            print("Initial list:")
            print(self.__data)
            print("\n")
            
        #to check performance    
        start_t = time.time()
        for i in range(1, len(self.__data)):
            temp = self.__data[i]
            j = i
            while j > 0 and self.__data[j-1] > temp:
                self.__data[j] = self.__data[j - 1]
                self.__operations += 1
                self.__comparisons += 1
                j = j - 1
                
            self.__data[j] = temp
            self.__operations += 1
            if(j > 0):
                self.__comparisons += 1
            if self.__verbose:
                print("It. {}: {} comp: {} push+place:{}".format(i,
                                                           self.__data,
                                                           self.__comparisons,
                                                           self.__operations
                                                          ))
                
        end_t = time.time()
        
        self.__time = end_t - start_t
        
        if self.__verbose:
            print(self.__data)
            print("\nNumber of comparisons: {}".format(self.__comparisons))
            print("Number of push-ups+place: {}".format(self.__operations))
            print("In {:.4f}s".format(self.__time))

if __name__ == "__main__":
    d = [7, 5, 10, -11 ,3, -4, 99, 1]
    insSorter = InsertionSort(d, verbose = True)
    insSorter.sort()
    d = []
    for i in range(0,10000):
        d.append(random.randint(0,1000))
    insSorter = InsertionSort(d, verbose = False)
    insSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(insSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(insSorter.getOperations()))
    print("In {:.4f}s".format(insSorter.getTime()))
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("Sorting test passed? {}".format(test))
    
    d = []
    for i in range(0,20000):
        d.append(random.randint(0,1000))
    insSorter = InsertionSort(d, verbose = False)
    insSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(insSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(insSorter.getOperations()))
    print("In {:.4f}s".format(insSorter.getTime()))
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("Sorting test passed? {}".format(test))