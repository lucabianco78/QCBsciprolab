import random
import time
import unittest
import MergeSort # the class with the sorter

"""in file: mergesortTest.py"""



class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        #create a test list:
        x = []
        for i in range(300):    
            x.append(random.randint(-100,100))
        self.sorter = MergeSort.MergeSort(x, verbose = False)
                          
    def test_A(self):
        """sort([10,20,30],[15,25,35]) == [10,15,20,25,30,35]"""
        mySorter = MergeSort.MergeSort([10,20,30,15,25,35], verbose = False)
        mySorter.sort()
        self.assertEqual(mySorter.getData(), [10, 15, 20, 25, 30, 35])
            
    def test_B(self):
        """merge must not affect the size of the list"""
        dcopy = self.sorter.getData()[:]
        self.sorter.sort()
        self.assertTrue(len(dcopy) == len(self.sorter.getData()))
        
    def test_C(self):
        """merging only changes start to end indexes"""
        #let's copy data
        d = [7, 9, 11, 23, 35, 8, 11, 22, 37, 81]
        self.sorter = MergeSort.MergeSort(d, verbose = False)
        dcopy = [7, 9, 11, 23, 35, 8, 11, 22, 37, 81]
        self.sorter.merge(0,4,2)
        for i in range(5,len(self.sorter.getData())):
            self.assertTrue(self.sorter.getData()[i] == dcopy[i])

    def test_D(self):
        """sort of single element is the same element"""
        #let's copy data
        d = [1]
        mysorter = MergeSort.MergeSort(d, verbose = False)
        mysorter.sort()
        self.assertEqual(mysorter.getData(), [1])

    def test_sort(self):
        """tests if the sort works"""
        x = []
        for i in range(300):    
            x.append(random.randint(-100,100))
        self.sorter = MergeSort.MergeSort(x, verbose = False)
        self.sorter.sort()
        d = self.sorter.getData()

        for el in range(0,len(d) - 2):
            self.assertTrue(d[el] <= d[el+1])
    
    def test_empty(self):
            """sorting of empty list is empty"""
            sorter = MergeSort.MergeSort([])
            sorter.sort()
            self.assertEqual(sorter.getData(),[])

            
if __name__ == "__main__":
    unittest.main()
