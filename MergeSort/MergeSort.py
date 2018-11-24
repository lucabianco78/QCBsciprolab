import random
import time

class MergeSort:
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
    
    def merge(self, first, last, mid):
        """
        given the two sublists of __data__: 
        S1 = data[first:mid+1] and S2 = data[mid+1: last+1],
        that are sorted, returns data[first:last+1] sorted and
        containing all the elements of S1 and S2.
        THIS ASSUMES THAT [first,mid] is always is bigger by at 
        most one element than [mid+1,last]
        """
        tmp = []
        i = first
        j = mid + 1
        while i <= mid and j <= last:
            if(self.__data[i] < self.__data[j]):
                tmp.append(self.__data[i])
                i += 1
            else:
                tmp.append(self.__data[j])
                j += 1
                
            self.__comparisons += 1
        # IMPORTANT NOTE:
        # when merging L1: [e1,...,en] L2:[b1,...,bm]
        # if all elements of L1 are < b1. we need to add them
        # at the end of the tmp for them to be included in the
        # solution!
        while i <= mid:
            tmp.append(self.__data[i])
            i += 1
        #IMPORTANT NOTE:
        # when merging L1: [e1,...,en] L2:[s,b1,...,bm]
        # if all elements of L1 are < b1,...,bm elements of L2,
        # and s > en-1 and s < en: 
        # tmp = [e1,..,en-1,s, en] and the following line will in
        # fact copy n+1 elements of tmp on the original data. 
        # the other places from n+1,... will contain the elements of L2
        # which were already sorted!
        self.__data[first:first+len(tmp)] = tmp
            
        
    def recursiveMergeSort(self, first, last):
        """
        recursively applies recursiveMergeSort to 
        the sublist starting from first and ending in last
        splitting it in two and reconstructing the result by merging
        the two lists partially sorted in this way
        """
        if first < last:
            mid = (first + last)//2 #<- index so mid+1 elements go in the first sublist!!! 

            if self.__verbose:
                print("Sorting {}-{}:\t{}".format(first,
                                                 last,
                                                 self.__data[first:last+1]))
            self.recursiveMergeSort(first, mid)
            if self.__verbose:
                print("\t{}".format(self.__data[first:mid+1]))

            self.recursiveMergeSort(mid +1, last)
            
            if self.__verbose:
                print("\t{}".format(self.__data[mid+1 : last+1]))                        
                print("Merging: {} and {}".format(self.__data[first : mid+1],
                                                  self.__data[mid+1 :last+1]))

            self.merge(first,last,mid)

            self.__operations += 3
        
    def sort(self):
        self.__comparisons = 0
        self.__operations = 0
        if self.__verbose:
            print("Initial list:")
            print(self.__data)
            print("\n")
            
        #to check performance    
        start_t = time.time()
        self.recursiveMergeSort(0,len(self.__data)-1)    
        end_t = time.time()
        
        self.__time = end_t - start_t
        
        if self.__verbose:
            print(self.__data)
            print("\nNumber of comparisons: {}".format(self.__comparisons))
            print("Number of operations: {}".format(self.__operations))
            print("In {:.4f}s".format(self.__time))



if __name__ == "__main__":
    d = [7, 5, 10, -11 ,3, -4, 99]
    mergeSorter = MergeSort(d, verbose = True)
    mergeSorter.sort()
    d = []
    for i in range(0,10000):
        d.append(random.randint(0,1000))
    mergeSorter = MergeSort(d, verbose = False)
    mergeSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(mergeSorter.getComparisons()))
    print("Number of swaps: {}".format(mergeSorter.getOperations()))
    print("In {:.4f}s".format(mergeSorter.getTime()))
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("Sorting test passed? {}".format(test))
    
    d = []
    for i in range(0,100000):
        d.append(random.randint(0,1000))
    mergeSorter = MergeSort(d, verbose = False)
    mergeSorter.sort()
    print("\nNumber of elements: {}".format(len(d)))
    print("Number of comparisons: {}".format(mergeSorter.getComparisons()))
    print("Number of swaps: {}".format(mergeSorter.getOperations()))
    print("In {:.4f}s".format(mergeSorter.getTime()))
    test = True
    for el in range(0,len(d)-1):
        test = test and (d[el]<= d[el+1])
    print("Sorting test passed? {}".format(test))

