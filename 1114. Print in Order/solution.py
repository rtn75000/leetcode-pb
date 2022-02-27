"""super article qui detaille tout sur la concurrency en general de python :
https://leetcode.com/problems/print-in-order/discuss/335939/5-Python-threading-solutions-(Barrier-Lock-Event-Semaphore-Condition)-with-explanation

more documentation: https://docs.python.org/3/library/threading.html"""

# one of the solution given is : Start with two locked locks. First thread unlocks the first lock that the second thread is waiting on. Second thread unlocks the second lock that the third thread is waiting on. 

from threading import Lock

class Foo:
    def __init__(self):
        self.locks = (Lock(),Lock())   # When declared, a lock is in unlocked state. 
        self.locks[0].acquire()        # acquire() lock the lock 
        self.locks[1].acquire()
        
     
    def first(self, printFirst):
        printFirst()
        self.locks[0].release()  # open the lock
          
    def second(self, printSecond):     
        with self.locks[0]:            #  equivalent a :  self.locks[0].acquire()
            printSecond()              #                  printSecond()
            self.locks[1].release()    #                  self.locks[1].release()
                                       #                  self.locks[0].release()
    def third(self, printThird):
        with self.locks[1]:
            printThird()
