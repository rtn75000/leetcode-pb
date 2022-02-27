"""la mediane est la middle value d'une list ordonner si la liste est de taille impaire , si la list est de taille paire alors c'est la moyenne des deux valeurs du milieu, ex : [1,2,4,8,20] la mediane est 4,
[1,4,6,14,32,69] la mediane est (6+14)/2==10"""

"""# not my sol  # max heap  # min heap   # TC O(1) for __init__() and findMedian()  ;  O(logn) for addNum()  # SC O(n) (for __init__)

on utilise une maxHeap qui conservera la moitier des nbr , les nombres les plus petit , donc maxHeapPop nous donnera le plus grand nbr parmis les plus petit . 
on utilise une minHeap qui conservera la moitier des nbr , les nombres les plus grand , donc minHeapPop nous donnera le plus petit nbr parmis les plus grands . 
Si le nombre d'element ajouter est paire alors les 2 heaps auront le memes nombres d'element ( la mediane sera la moyenne de maxheappop+minheappop ). Si le nbr d'element ajouter est
impaire alors le max heap qui contient les plus petit nbrs aura un nbr en plus (il contiendra donc la mediane, maxheappop nous donnera la mediane ) . 

l'algo fonction de la facon suivante : 
-quand on ajoute un nouvelle element a l'aide de la fct addNum(num), tout d'abord ce nombre sera ajouter dans le maxheap le max heap va ensuite donner son plus grand nombre au min heap. si le 
min heap contient plus de nbr que le max heap alors il va donner son plus petit nbr au max heap, de cette facon il y'aura toujours un nbr en plus dans le max heap si le nbr d'element 
ajouter au total est impaire.   
-quand on veut connaitre la mediane des elements ajouter a l'aide la fct findMedian() alors si  maxHeap.size > minHeap.size cad que le nbr total d'element est impaire et donc la mediane se
trouve dans le max heap donc on va faire return top of the maxHeap, ce qui donne le plus grand nombre parmis les plus petit. si maxHeap.size == minHeap.size cad que le nbr total d'element est 
paire donc la mediane est egale a  (maxHeap.top() + minHeap.top()) / 2 

solution et super explication d'ici : https://leetcode.com/problems/find-median-from-data-stream/discuss/1330646/C%2B%2BJavaPython-MinHeap-MaxHeap-Solution-Picture-explain-Clean-and-Concise"""
class MedianFinder:
    
    def __init__(self):   # O(1)
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        
        # comme heappush est pour minheap ds python donc on fait -num pour que ca revient au meme qu'un max heap
        heappush(self.maxHeap, -num)   # O(logn)
        
        # on fait -heappop(self.maxHeap) car on a fait -num ds le push de maxheap , or dans min heap on veut faire push num donc on fait -heappop(self.maxHeap) ce qui revient a -(-num) cad num
        heappush(self.minHeap, -heappop(self.maxHeap))   # O(2*logn)==O(logn)
        
    
        if len(self.minHeap) > len(self.maxHeap):
            # faie passer le min de minheap a maxheap
            heappush(self.maxHeap, -heappop(self.minHeap))  # on fait -heappop(self.minHeap) car heappush c'est pour minheap    # O(2*logn)==O(logn)

    def findMedian(self) -> float:     # O(1)
        if len(self.maxHeap) > len(self.minHeap):  # si nbr total d'element impaire 
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2 # si nbr total d'element paire 
    
"""Follow up: (voir ennoncer)
1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?

We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle value to get our median.

Time and space complexity would be O(100) = O(1).

2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

As 99% is between 0-100. So can keep a counter for less_than_hundred and greater_than_hundred.
As we know soluiton will be definately in 0-100 we don't need to know those number which are >100 or <0, only count of them will be enough."""
