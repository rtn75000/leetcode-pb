"""#pas ma sol #built-in sort #O(nlogn) #O(n)    n == len (trips)
l'idee est de mettre ds une meme list (depart,nbr de passager qu'on fait monter) et (fin , -nbr de passager qu'on fait descendre) , ensuite on trie cette liste dans l'ordre croissant donc ca va etre trier
en fonction de quand les passagers montent ou descendent . 
On passe a travers la list tout simplement en ajoutant a la capaciter le nbr de passager a faire monter ou en enlevant le nbr de passager qui desend si a un moment on depasse la capacite alors on ne peut prendre
toute les personnes. 

sol d'ici : https://leetcode.com/problems/car-pooling/discuss/319088/Simple-Python-solution"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for numOfPassengers, start, end in trips:   #O(n)
            lst.append((start, numOfPassengers))
            lst.append((end, -numOfPassengers))
        lst.sort()  #O(nlogn)
        numOfPassengersInCar = 0
        for element in lst:   #O(2n)==O(n)
            numOfPassengersInCar += element[1]    
            if numOfPassengersInCar > capacity:
                return False
        return True
    
    
"""meme idee qu'en haut en utilisant un min heap  #TC O(nlogn) #SC O(n)"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []   
        for numOfPassengers, start, end in trips: #O(n)
            heapq.heappush(heap, (start, numOfPassengers))      # le heap sera trier par rapport au premier membre du tuples cad par rapport a start/end   #O(logn)
            heapq.heappush(heap, (end, -numOfPassengers)) 
        while heap: # voir remarque an bas 
            capacity -= heapq.heappop(heap)[1]     #le pop nous donne le plus petit start/end cad le plus proche arret ou on fait monter ou descendre des passagers . 
            if capacity < 0:
                return False
        return True 
    
"""remarque : mon analyse du  TC du 'while heap' :
si on analyse le 'while heap' coute   log(n)+log(n-1)+log(n-2)+...+log(1) == log (n*n-1*n-1*...*1)  == log (n!) ( <  n*log n == logn+...+logn  )
                                      |                                  |                                                      |            |
                                      ------------------------------------                                                      --------------
                                                    n fois                                                                          n fois
moi j'aurai donc dis que TC du pgrm est O(nlogn + log (n!)) mais ds le codes que j'ai vu ya ecrit O(nlogn) peut etre parceque  O(nlogn + log (n!)) < O(nlogn + nlogn) < O(2*nlogn)==O(nlogn)
"""
