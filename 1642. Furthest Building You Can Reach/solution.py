""" # pas ma sol  #min-heap/PQ  #TC O(nlogL) #SC O(L)    #n==len(heights)  #L=ladders cad nbr d'echelles 

solution d'ici  : https://leetcode.com/problems/furthest-building-you-can-reach/discuss/918515/JavaC%2B%2BPython-Priority-Queue
TC/SC d'ici : https://leetcode.com/problems/furthest-building-you-can-reach/discuss/1177210/Easy-Solution-w-Clear-Explanation-and-Comments-or-Priority-Queue-and-Multiset

l'idee est de garder dans une heap les hauteur qu'on doit utiliser une echelle ou des bricks et a chaque fois que la taille de cette heap est superieur au nombre de ladders ca veut dire qu'on doit forcement utiliser des
bricks donc on va utiliser des bricks pour la plus petite hauteur comme ca on conserve un max de brick car on utilise les ladders pour les plus grande hauteur . si on a pas assez de bricks alors ca veut dire qu'on ne 
peut plus avancer .


app : heights=[4,12,2,7,18,20,25] bricks=11 ladders=2
-i=0 : d=heights[i + 1] - heights[i]  cad d=12-4=8>0 donc pour passer de i a i+1 il faut utiliser une echelle ou des briques , on va donc faire rentrer cette distance dans le min heap : heap=[8]
-i=1 : d=heights[i + 1]-heights[i]  cad d=2-12=-10<0 donc pour passer de i a i+1 il ne faut pas ni d'echelle ni des briques , donc on s'avance 
-i=2:  d=heights[i + 1]-heights[i]  cad d=7-2=5>0 donc pour passer de i a i+1 il faut utiliser une echelle ou des briques , on va donc faire rentrer cette distance dans le min heap : heap=[8,5]
-i=3:  d=18-7=11>0 donc pour passer de i a i+1 il faut utiliser echelle/briques , on va donc faire rentrer d dans le min heap : heap=[8,5,11] mais comme len(heap)>ladders (nbr d'echelle) cad 
que forcement dans c'est 3 distances il faudra utiliser des briques pour l'une d'entre elle donc comme on veut conserver les echelles pour les grandes distance on va utiliser les briques pour la
plus petite distance donc on va faire heapq.heppop(heap) ce qui nous donne 5 donc maintenant il nous reste bricks-=5 cad 6 briques .
-i=4:  d=20-18=2>0 donc pour passer de i a i+1 il faut utiliser echelle/briques , on va donc faire rentrer d dans le min heap : heap=[8,11,2] mais comme len(heap)>ladders (nbr d'echelle) cad
qu'on doit utiliser des briques pour l'une des distances , on va dc prendre la plus petite distance donc heapq.heppop(heap) ce qui nous donne 2  donc maintenant il nous reste bricks-=2 cad 4
briques.
-i=5:  d=25-20=5>0 donc pour passer de i a i+1 il faut utiliser echelle/briques , on va donc faire rentrer d dans le min heap : heap=[8,11,5] mais comme len(heap)>ladders (nbr d'echelle) cad
qu'on doit utiliser des briques pour l'une des distances , on va dc prendre la plus petite distance donc heapq.heppop(heap) ce qui nous donne 5  donc maintenant il nous reste bricks-=5 cad -1 briques donc briques<0 
donc ca veut dire qu'on a pas assez de briques pour passer de i a i+1 donc on return i qui sera le dernier building qu'on peut atteindre. 


"""

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # SC O(L) avec L le nbr d'echelle car au max le heap sera de la taille du nbr d'echelle voir la suite pour comprendre. 
        for i in range(len(heights) - 1): # a chaque iteration on avance d'immeuble  #TC O(n)
            d = heights[i + 1] - heights[i]  
            if d > 0: # si la distance entre deux immeuble est possitif ca veut dire que l'immeuble apres i est plus grand et dc qu'il faut utiliser ou des briques ou une echelles pour avancer.  
                heapq.heappush(heap, d)    # on rentre la distance dans la min heap   #TC O(log L)  avec L le nbr d'echelle car au max le heap sera de la taille du nbr d'echelle. 
                
            # si la taille de la heap est superieur a ladders ca veut dire qu'on doit forcement utiliser des briques donc on va faire sortir la plus petite distance pour la remplir de briques.
            if len(heap) > ladders:      
                bricks -= heapq.heappop(heap)   #le pop nous rend la plus petite hauteurs comme ca on utilise le moins de briques possibles.   
                #TC O(log L) ,L nbr d'echelle car au max le heap sera de la taille du nbr d'echelle.
                
            if bricks < 0:   # si on a pas assez de brique on ne peut pas avancer donc on sort du for .
                return i
            
        return len(heights) - 1  # cad on a reussi a aller jusqu'au bout. 
