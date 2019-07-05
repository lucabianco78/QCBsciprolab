"""
NAME:
SURNAME:
Matricola: 

ReversibleQueue.py
"""

from MyQueue import MyQueue

class ReversibleQueue(MyQueue):

        
    
    def printContent(self):
        """prints all the elements in the queue reporting the minimum and maximum value of the queue 
        using only standard queue operations. The queue must be unaffected by the method"""

    
    def reverseK(self, K):
        """reverses the first K elements of the queue"""

        
        

if __name__ == "__main__":
    Q = ReversibleQueue()
    data = [ 72, 11, 2, 13, 87, 27, 44, 3, 1, -10, 4]
    for el in data:
        Q.enqueue(el)
    print("First in queue: {}".format(Q.top()))
    Q.printContent()

    print("Empty? {}".format(Q.isEmpty()))
    print("First in queue: {}".format(Q.top()))


    Q2 = ReversibleQueue()
    dataStr = ["APPLE", "BLUEBERRY", "PINEAPPLE"]
    for el in dataStr:
        Q2.enqueue(el)

    Q.reverseK(0)
    print("\nQ now (rev(0) unchanged):")
    Q.printContent()
    Q.reverseK(-5)
    print("\nQ now (rev(-5) unchanged):")
    Q.printContent()
    Q.reverseK(5)
    print("\nQ now (first 5 rev):")
    Q.printContent()
        
    print("\nQ2:")
    Q2.printContent()
    Q2.reverseK(0)
    print("\nQ2 now (rev(0) unchanged):")
    Q2.printContent()
    print("\nQ2 now (rev(rev(2))unchanged):")
    Q2.reverseK(2)
    Q2.reverseK(2)
    Q2.printContent()
    Q2.reverseK(10)
    print("\nQ2 now (rev(10):")
    Q2.printContent()
