""" je ne m'attarde pas sur ce pb queleque petite explication :
cette solution utilise un max heap on prend a chaque fois les 2 max et on retire de chacun 1 . """
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
            heap = [-a,-b,-c]
            heapq.heapify(heap)   # O(n)  (n taille du heap)
            score =0
            # cette loop est O(2*10^5) car a chaque fois on choisi 2 nombre on enleve 1 et on les remet dans le heap , or le nmb est max 10^5 donc on peut le faire O(2*10^5) si a=b=c=10^5 
            while len(heap) >= 2:      # when remaining length >=2 
                p1 = heapq.heappop(heap) # O(logn)                 
                p2 = heapq.heappop(heap) # O(logn)
                if p1+1 !=0:
                    heapq.heappush(heap,p1+1) # O(logn)
                if p2+1 != 0:
                    heapq.heappush(heap,p2+1) # O(logn)
                score += 1
            return score

        
"""il ya une solution mathematique O(1) : https://leetcode.com/problems/maximum-score-from-removing-stones/discuss/1053645/Python3-math """
