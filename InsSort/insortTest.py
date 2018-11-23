import random
import time
import unittest
import InsSort # the class with the sorter

"""in file: insortTest.py"""



class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        #create a test list:
        x = []
        for i in range(300):    
            x.append(random.randint(-100,100))
        self.sorter = InsSort.InsertionSort(x, verbose = False)
                          
    def test_len(self):
        """tests if the length of sorted and unsorted is the same"""
        l = len(self.sorter.getData())
        self.sorter.sort()
        d = len(self.sorter.getData())
        self.assertTrue(l == d)
                
    def test_sort(self):
        """tests if the sort works"""
        self.sorter.sort()
        d = self.sorter.getData()
        for el in range(0,len(d) - 2):
            self.assertTrue(d[el] <= d[el+1])
    
    def test_empty(self):
            """sorting of empty list is empty"""
            self.assertEqual(InsSort.InsertionSort([]).getData(),[])

            
if __name__ == "__main__":
    unittest.main()
