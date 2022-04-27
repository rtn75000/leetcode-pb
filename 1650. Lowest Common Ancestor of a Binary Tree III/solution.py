"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""



""" # sol 1 #TC O(height) #SC O(height)
comme on a un pointeur sur le pere donc on peut remonter depuis un certain node jusqu'au root donc on va trouver le path d'un des nodes p,q puis on remonte le path de l'autre node tant que on trouve pas un node du path qu'on remonte qui se trouve dans le path deja trouver . 
remarque : j'avais une approche tres ressemblente de trouver les deux path de p et q puis de comparer les paths , le probleme c'est qu'en utilisant un set ca garde pas l'ordre (You cannot have order in sets, there is no way to tell how Python orders it) donc on ne peut pas les comparer pour trouver le premier qui correspond (car pas dans l'ordre ). j'ai finalement rouver une solution qui combine le set (pour avoir search en O(1)) et list pour conserver l'ordre d'un path au moins
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node': 
        path = set()
        while p:
            path.add(p)
            p = p.parent 
        # on remonte le path de q tant que on ne trouve pas un node en commun avec le path de p
        while q not in path: # cost O(1) car on utilise un set (search dans set c'est O(1))
            q = q.parent 
        return q
    
"""#my sol #sol 1 bis #TC/SC O(height)"""    

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node': 
        pathP = set()
        pathQ = list()
        while p:
            pathP.add(p)
            p = p.parent 
        while q:
            pathQ.append(q)
            q = q.parent 
        for element in pathQ :   #pathQ est une list donc garde l'ordre du path 
            if element in pathP : #pathP est un set donc O(1)
                return element 

"""(il existe une solution en SC O(1) : 
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1)
A comprendre ... """

