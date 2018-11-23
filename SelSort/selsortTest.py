import random
import time
import unittest
import SelSort # the class with the sorter

"""in file: selsortTest.py"""



class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        #create a test list:
        x = []
        for i in range(300):    
            x.append(random.randint(-100,100))
        self.sorter = SelSort.SelectionSort(x, verbose = False)
                          
    def test_swap1(self):
        """swap of swap is identical to beginning"""
        #let's copy data
        dcopy = self.sorter.getData()[:]
        for i in range(40):
            i1 = random.randint(0,len(dcopy) - 1)
            i2 = random.randint(0,len(dcopy) - 1)
            self.sorter.swap(i1,i2)
            self.sorter.swap(i1,i2)
            self.assertTrue(self.sorter.getData() == dcopy)
    def test_swap2(self):
        """length of swapped data does not change"""
        
        l = len(self.sorter.getData())
        for i in range(40):
            i1 = random.randint(0,l - 1)
            i2 = random.randint(0,l - 1)
            self.sorter.swap(i1,i2)
            self.assertTrue(len(self.sorter.getData()) == l)
        
    def test_swap3(self):
        """swapping only changes i and j indexes (if i!=j)"""
        #let's copy data
        dcopy = self.sorter.getData()[:]
        for i in range(40):
            #let's copy data
            dcopy = self.sorter.getData()[:]
            i1 = random.randint(0,len(dcopy) - 1)
            i2 = random.randint(0,len(dcopy) - 1)
            if i1 != i2:
                self.sorter.swap(i1,i2)
                for ind in range(0,len(dcopy)):
                    if ind != i1 and ind != i2:
                        self.assertTrue(dcopy[ind] == self.sorter.getData()[ind])
    
    def test_argmin(self):
        """
        tests if j=argmin(i) then j <= data[i:]
        """
        l = len(self.sorter.getData())
        for i in range(40):
            ind = random.randint(0,l - 1)
            minP = self.sorter.argmin(ind)
            for j in self.sorter.getData()[ind:]:
                self.assertTrue(self.sorter.getData()[minP] <= j)
                
    def test_sort(self):
        """tests if the sort works"""
        self.sorter.sort()
        d = self.sorter.getData()
        for el in range(0,len(d) - 2):
            self.assertTrue(d[el] <= d[el+1])
    
    def test_empty(self):
            """sorting of empty list is empty"""
            self.assertEqual(SelSort.SelectionSort([]).getData(),[])

            
if __name__ == "__main__":
    unittest.main()