"""file: QuickSort.py"""

import random
import time

class QuickSort:
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
    
    def swap(self, i,j):
        """swaps elements at positions i and j"""
        tmp = self.__data[i]
        self.__data[i] = self.__data[j]
        self.__data[j] = tmp
    
    def pivot(self, start, end):
        """gets the pivot and swaps elements in [start, end]
        accordingly"""
        p = self.__data[start]
        j = start
       
        for i in range(start + 1, end + 1):
            self.__comparisons += 1
            if( self.__data[i] < p):
                j = j + 1
                self.swap(i, j)
                self.__operations += 1
      
        self.swap(start,j)
        self.__operations += 1

        return j
    
    def recQuickSort(self, start, end):
        """gets the pivot and recursively applies
        itself on the left and right sublists
        """
        if start < end:
            #GET THE PIVOT
            j = self.pivot(start, end)
            
            if self.__verbose:
                print("PIVOT: index:{} val:{}".format(j, self.__data[j]))
                print(self.__data)
                print("Running again on (left): {}".format(self.__data[start:j]))
                print("from start: {} to j-1:{}".format(start,j-1))
            #Run on LEFT SUBLIST
            self.recQuickSort(start, j - 1)

            if self.__verbose:
                print(self.__data)
                print("Running again on (right): {}".format(self.__data[j+1:end]))
                print("from start: {} to j-1:{}".format(j+1,end))
            
            #Run on RIGHT SUBLIST
            self.recQuickSort(j + 1, end)
    
    def sort(self):
        self.__comparisons = 0
        self.__operations = 0
        if self.__verbose:
            print("Initial list:")
            print(self.__data)
            print("\n")
            
        #to check performance    
        start_t = time.time()
        
        self.recQuickSort(0,len(self.__data) - 1)
        
        if self.__verbose:
            print("{} comp: {} swaps:{}".format(self.__data,
                                                self.__comparisons,
                                                self.__operations))
                
        end_t = time.time()
        
        self.__time = end_t - start_t
        
        if self.__verbose:
            print(self.__data)
            print("\nNumber of comparisons: {}".format(self.__comparisons))
            print("Number of swaps: {}".format(self.__operations))
            print("In {:.4f}s".format(self.__time))

if __name__ == "__main__":
    d = [7, 3, 10, -11 ,5, -4, 99, 1]
    qkSorter = QuickSort(d, verbose = True)
    qkSorter.sort()
    d = []

    for i in range(0,10000):
        d.append(random.randint(0,1000))
    qkSorter = QuickSort(d, verbose = False)
    qkSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(qkSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(qkSorter.getOperations()))
    print("In {:.4f}s".format(qkSorter.getTime()))
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("Sorting test passed? {}".format(test))
    
    d = []
    for i in range(0,300000):
        d.append(random.randint(0,1000))
    qkSorter = QuickSort(d, verbose = False)
    qkSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(qkSorter.getComparisons()))
    print("Number of push-ups+place: {}".format(qkSorter.getOperations()))
    print("In {:.4f}s".format(qkSorter.getTime()))
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("Sorting test passed? {}".format(test))
