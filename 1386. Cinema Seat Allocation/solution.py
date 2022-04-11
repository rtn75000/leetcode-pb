"""
#logic #hashtable #mon raisonnement(pas mon code) #TC : O(M)  #SC: O(M) ,   M is the size of the reserved seats.
(c'est que de la logique pas de technique speciale)
les exemples explique bien la logique.
"""
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 2*n  # tout les possibilites sont 2*n car on peut faire asseoir max deux famille dans une rangee .
        ht = defaultdict(set)
        for row, seat in reservedSeats:
            ht[row].add(seat)      #  dict key are row and dict value are reserved seat number in this row
        for row in ht:
            cnt = 0
            if 2 not in ht[row] and 3 not in ht[row] and 4 not in ht[row] and 5 not in ht[row]:
                cnt +=1
            if 6 not in ht[row] and 7 not in ht[row] and 8 not in ht[row] and 9 not in ht[row]:
                cnt += 1
            if 4 not in ht[row] and 5 not in ht[row] and 6 not in ht[row] and 7 not in ht[row] and cnt == 0: # cnt == 0 si on a rien ajoute avt 
                cnt += 1
            res += (cnt-2)
        return res
