
"""
#heap 

Time: O(N) for init, O(logN) for other functions
Space: O(N)

l'idee est de garder un heap qui contiendra toute les places disponible au debut les place dispo sont de 1 a n inclus , on va donc creer un array [1,...,n] , cette array est forcement un min heap
ce qui nous conviens parfaitement car on aura pas besoin de faire heapify (coute O(n)) dans l'initialisation. l'ennoncer demande de prendre a chaque fois le unreserved seat avec le nbr le plus 
petit donc ca revient a prendre le top du heap car c'est un min heap donc dans la fct reserve on fait tout simplement pop sur le heap . la fonction unreserve elle doit remettre un nbr dans le
heap donc on utilise push pour que ce nbr soit remit en conservant les proprietes de la min heap.  

"""
class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))  #TC O(n) #SC O(n)

    def reserve(self) -> int:
        return heapq.heappop(self.heap) #TC O(logn)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)  #TC O(logn)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
