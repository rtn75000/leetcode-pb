"""# ma solution #linked list #two pointers #TC O(n+m) (car on passe que deux fois sur chaque linked list ) #SC O(1)
l'idee est de calculer la taille des deux linked listes . dans le cas ou une linked list est plus grande que l'autre on doit sauter les premiers nodes de la grande linked list pour avoir deux liste de memes tailles
afin de pouvoir passer a l'aide de deux pointeurs sur les linked list pour les comparer si un pointeur egale l'autre alors on a trouver le debut de la partie en commun . 
VOIR PHOTO GIT HUB EXPLICATION . 
remarque = un node egale a un autre si il a la meme adresse on regarde pas ca valeur ou sur celui le next car on compare deux objets et donc leur adresse est comparer (cette remarque 
est la dans le cas ou on a par ex deux linked list 1->2->3 , 1->2->3 qui ne sont pas relier donc si on comparer les valeurs et les next on penserais quelles sont relier mais en veriter le '==' compare 
les objets si ils sont identiques cad si c'est le meme objets dans la memoire )
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # find size of each linked list ---------- 
        
        sizeA = sizeB = 0 
        ptrA = headA
        ptrB = headB 
        
        while ptrA :
            sizeA +=1
            ptrA = ptrA.next 
            
        while ptrB :
            sizeB +=1
            ptrB = ptrB.next 
        
        # ----------------------------------------
        
        # put both pointers at the same level in the linked list ------------
        
        numOfNodeToSkip = abs(sizeA-sizeB)
        
        # remettre pointeur au debut 
        ptrA = headA 
        ptrB = headB 
        
        # on avance le pointeur de la plus grande linked list pour qu'il lui reste a parcourir le meme nbr de nodes que la plus petite linked list
        if sizeA > sizeB : 
            while numOfNodeToSkip :
                numOfNodeToSkip -=1     # comme on avance on doit retirer un node a skipper  
                ptrA = ptrA.next 
        else :
            while numOfNodeToSkip :
                numOfNodeToSkip -=1
                ptrB = ptrB.next 
        
        # ----------------------------------------------------------------
        
        # les pointeurs sont au meme niveau (cad il leur reste a parcourir le meme nbr de nodes)
        # il reste plus qu'a les comparer , des qu'ils sont egaux on retourne le node -----------------------------------------------------

        while ptrA :  # on peut aussi mettre ptrB ca change pas car maintenant on parcours meme nbr de nodes sur les deux liste 
            if ptrA == ptrB :
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
            
        #------------------------------------------------------------------------------------------------------------------------------
               
        # si on est arriver ici ca veut dire que il ya pas de partie en commun donc on retourne null
        return None        
        
        
        
        
        
        
        
        
        
        
        
        
