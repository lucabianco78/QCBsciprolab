import random
import time
import unittest
import QuickSort # the class with the sorter

"""in file: quicksortTest.py"""



class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        #create a test list:
        x = []
        for i in range(300):    
            x.append(random.randint(-100,100))
        self.sorter = QuickSort.QuickSort(x, verbose = False)
    
        
        
    def test_len(self):
        """tests if the length of sorted and unsorted is the same"""
        l = len(self.sorter.getData())
        self.sorter.sort()
        d = len(self.sorter.getData())
        self.assertTrue(l == d)    
    
    def test_swap(self):
        """swap of swap is identical to beginning"""
        #let's copy data
        dcopy = self.sorter.getData()[:]
        for i in range(40):
            i1 = random.randint(0,len(dcopy) - 1)
            i2 = random.randint(0,len(dcopy) - 1)
            self.sorter.swap(i1,i2)
            self.sorter.swap(i1,i2)
            self.assertTrue(self.sorter.getData() == dcopy)
    
    def test_pivot(self):
        """tests if the pivot works"""
        x = []
        for i in range(300):    
            x.append(random.randint(-100,100))
        self.sorter = QuickSort.QuickSort(x, verbose = False)
        j = self.sorter.pivot(0,len(self.sorter.getData()) -1)
        D = self.sorter.getData()
        for i in range(0,j):
            self.assertTrue(D[i] <= D[j])
        for i in range(j+1, len(D)):
            self.assertTrue(D[j] <= D[i])
            
    def test_sort(self):
        """tests if the sort works"""
        x = []
        for i in range(300):    
            x.append(random.randint(-100,100))
        self.sorter = QuickSort.QuickSort(x, verbose = False)
        
        self.sorter.sort()
        d = self.sorter.getData()
        for el in range(0,len(d) - 2):
            self.assertTrue(d[el] <= d[el+1])
    
    def test_empty(self):
            """sorting of empty list is empty"""
            self.assertEqual(QuickSort.QuickSort([]).getData(),[])

            
if __name__ == "__main__":
    unittest.main()
