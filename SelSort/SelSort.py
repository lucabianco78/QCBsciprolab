"""file: SelSort.py"""

import random
import time

class SelectionSort:
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
    
    def getOperations(self):
        return self.__operations
    
    def getComparisons(self):
        return self.__comparisons
    
    def swap(self, i, j):
        """
        swaps elements i and j in data.
        """
        if(i != j): #no point in swapping if i==j
            tmp = self.__data[i]
            self.__data[i] = self.__data[j]
            self.__data[j] = tmp
        
    def argmin(self, i):
        """
        returns the index of the smallest element of
        self.__data[i:]
        """
        mpos = i
        N = len(self.__data)
        minV = self.__data[mpos]
        for j in range(i + 1,N): # from i+1 to N. U[i+1:]
            if(self.__data[j] < minV):
                mpos = j
                minV = self.__data[j]
            #just for checking
            self.__comparisons += 1
        
        return mpos
    
    def sort(self):
        self.__comparisons = 0
        self.__operations = 1
        if self.__verbose:
            print("Initial list:")
            print(self.__data)
            print("\n")
            
        #to check performance    
        start_t = time.time()
        for i in range(len(self.__data) - 1):
                j = self.argmin(i)
                self.swap(i,j) 
                self.__operations += 1
                if self.__verbose:
                    print("It. {}. data[{}]<->data[{}] {}<->{}".format(i,
                                                                       i,
                                                                       j,
                                                                       self.__data[i],
                                                                       self.__data[j]))
                    print(self.__data)    
        end_t = time.time()
        
        self.__time = end_t - start_t
        
        if self.__verbose:
            print(self.__data)
            print("\nNumber of comparisons: {}".format(self.__comparisons))
            print("Number of swaps: {}".format(self.__operations))
            print("In {:.4f}s".format(self.__time))



if __name__ == "__main__":
    d = [7, 5, 10, -11 ,3, -4, 99, 1]
    selSorter = SelectionSort(d, verbose = True)
    selSorter.sort()
    d = []
    for i in range(0,10000):
        d.append(random.randint(0,1000))
    selSorter = SelectionSort(d, verbose = False)
    selSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(selSorter.getComparisons()))
    print("Number of swaps: {}".format(selSorter.getOperations()))
    print("In {:.4f}s".format(selSorter.getTime()))
    test = True
    for el in range(1,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("Sorting test passed? {}".format(test))
    
    d = []
    for i in range(0,20000):
        d.append(random.randint(0,1000))
    selSorter = SelectionSort(d, verbose = False)
    selSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(selSorter.getComparisons()))
    print("Number of swaps: {}".format(selSorter.getOperations()))
    print("In {:.4f}s".format(selSorter.getTime()))
    test = True
    for el in range(1,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("Sorting test passed? {}".format(test))
    
