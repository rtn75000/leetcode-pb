"""il ya une solution avec heap mais je pense qu'ici l'interviewer veut qu'on utilise la solution de divide and conquer car elle est plus efficace donc on va pas voir la solution avec la heap
(la heap solution a le meme time complexity que la deuxieme sol mais a O(M*K) extra space)
"""

""" #first sol  #merge #TC O(k^2 * M) avec M la taille max des linked-list , k c'est le nombre de linked-list  #SC O(1) (ici merge n'a pas besoin d'utiliser d'extra space car on est pas 
avec un array mais avec une linked-list voir le code pour comprendre)

c'est la premier solution qui vient a l'esprit on fusione  2 linked-list (ce qui coute O(len(l1)+len(l2)) car on passe simplement une fois sur chaque linked list a l'aide d'un pointeur pour chaque linked-list et
on compare les valeurs pointer si val(p1)<val(p2) alors met val(p1) dans le resultat et on fait p1+=1 si c'est l'inverse alors on avance p2 ) puis le resultat on le fusionne avec la linked-list d'apres, ex si on 
a [[1,4,5],[1,3,4],[2,6],[7,10,8]] alors on fusionne
[1,4,5],[1,3,4] ce qui donne [1,1,3,4,4,5] puis ensuite on fusionne cette linked-list avec [2,6] ce qui donne [1,1,2,3,4,4,5,6] puis on fusione ca avec [7,10,8] ce qui donne [1,1,2,3,4,4,5,6,7,8,10]. mais cette 
solution sera couteuse car  soit M la taille max de chaque linked list alors cad donne :
M+M pour la fusion de la premier et la deuxieme linked-list .
2M+M pour fusion resultat et 3eme linked-lis
3M+M pour fusion resultat et 4eme linked-lis
...
(K-1)M + M = K*M pour la fusion du resultat et de la K-eme linked-list
Ce qui donne au total 2M+3M+4M+...+K*M  == (2+3+4+...+k)*M == O(k^2 * M)  (car 1+2+3+4+...+k = k(k+1)/2 = O(k^2))

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
     
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)     # cur va etre le pointeur qui bouge , l1/l2 c'est le node qu'on regarde maintenant ds l1/l2
        while l1 != None and l2 != None:   #si on a fini une des list on arrete
            if l1.val <= l2.val:        
                cur.next = l1        
                cur = cur.next      #on fait avancer cur
                l1 = l1.next    #
            else:
                cur.next = l2
                cur = cur.next       #on fait avancer cur
                l2 = l2.next
        
        #on append la list qu'on a pas fini
        if l1 != None: cur.next = l1   
        if l2 != None: cur.next = l2
        return dummy.next    # retour du resultat (on return la tete bien entendu)
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)    
        if k == 0: return None  #si il ya 0 linked list
        if k == 1: return lists[0]   #si il ya 1 linked list c'est elle la reponse car elle est deja trier
        
        curList = lists[0]    #curList va etre le resultat qu'on obtient a chaque fois
        for i in range(1, k):
            curList = self.mergeTwoLists(curList, lists[i])
        return curList
    
    
"""#not my sol #divide and conquer #merge #TC O(KlogK*M) avec M la taille max des linked-list , k c'est le nombre de linked-list  #SC O(1)
l'idee est la suivante ,au lieu de merge a chaque fois le resultat on merge 2 par 2 puis on merge les resultat 2 par 2 et ainsi de suite . prenons pour ex 6 linked-list:

     1e linked-list        2e linked-list       3e linked-list         4e linked-list          5e linked-list         1e linked-list
           \                       /                    \                      /                       \                    /
            \                     /                      \                    /                         \                  /      
              merge them O(2*M)                             merge them O(2*M)                             merge them O(2*M)
                     \                                              /                                              /
                      \                                            /                                              /  
                       \                                          /                                              /
                        ------ merge them O(2M+2M) == O(4M) ------                                              /
                                             \                                                                 /     
                                              \                                                               /                                          
                                               \                                                             /                     
                                                \                                                           /        
                                                 \                                                         /
                                                  --------------merge them O(4M+2M) == O(6M)---------------
     
     
  pour comprendre le TC on va faire un example d'arbre du merge, prenons ici 16 L-L au depart  : 
  
   L-L            L-L           L-L         L-L         L-L         L-L         L-L         L-L         L-L         L-L           L-L         L-L       L-L         L-L           L-L         L-L 
      \         /                 \         /             \         /             \         /             \         /               \         /           \         /               \         / 
       \       /                   \       /               \       /               \       /               \       /                 \       /             \       /                 \       /   
         O(2M)                       O(2M)                   O(2M)                   O(2M)                   O(2M)                     O(2M)                 O(2M)                     O(2M)   
            \                           /                      \                       /                        \                        /                      \                        /    
             \                         /                        \                     /                          \                      /                        \                      / 
              ----------O(4M)----------                           -------O(4M)-------                              --------O(4M)-------                            --------O(4M)-------             
                           \                                               /                                                  \                                              /           
                            \                                             /                                                    \                                            /                 
                             \                                           /                                                      \                                          /                 
                              \                                         /                                                        \                                        /
                               \                                       /                                                          \                                      /
                                ----------------O(8M)------------------                                                            ----------------O(8M)-----------------     
                                                   \                                                                                                 /                            
                                                    \                                                                                               /                             
                                                     \                                                                                             /                              
                                                      \                                                                                           /                               
                                                       \                                                                                         /                               
                                                        -----------------------------------------O(16M)------------------------------------------            
     
chaque niveau nous coute K*M  (avec K le nbr de linked-list et M la taille de chaque Linked-list) car comme on peut le constater au premier niveau on va passer une fois sur tout les membres
de tout les linked list donc K*M meme chose pour le niveau 2 ,3 ,4  etc..
comme on peut le voir la hauteur max est logK car au debut on fait K/2 merge puis K/4 puis K/8 puis K/16 etc donc on a en tout logK niveau , or comme chaque niveau coute O(K*M) donc en tout
ca nous coute O(logK*K*M )
(pour comprendre cela ya une video de neetcode : https://www.youtube.com/watch?v=q5a5OiGbT6Q&ab_channel=NeetCode )
     
dans le shema precedent on avait un nombre paire qui se diviser en deux a chaque fois jusqu'au dernier niveau mais il se peut qu'on ai qqch comme ca :
    L-L            L-L           L-L         L-L         L-L         L-L         
      \         /                 \         /             \         /            
       \       /                   \       /               \       /                 
         O(2M)                       O(2M)                   O(2M)                   
            \                           /                     /
             \                         /                     /
              ----------O(4M)----------                     /                
                           \                               /                          
                            \                             /                               
                             \                           /                        
                              ----------O(6M)------------
                              
ou qqch comme ca :                               
    L-L            L-L           L-L         L-L         L-L                  
      \         /                 \         /            /         
       \       /                   \       /            /                  
         O(2M)                       O(2M)             /                     
            \                           /             /        
             \                         /             /       
              ----------O(4M)----------             /                    
                           \                       /                                 
                            \                     /                                      
                             \                   /          
                                ------O(5M)------
                             
si on regarde bien on fait merge(idxpaire,idxpaire+1) mais si
sol d'ici : https://leetcode.com/problems/merge-k-sorted-lists/discuss/1447503/Python-2-solutions-Clean-and-Concise
     
     """

class Solution:
    
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:   #merge deux linked liste, facile a comprendre
        dummyHead = curHead = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                curHead.next = l1
                curHead = curHead.next
                l1 = l1.next
            else:
                curHead.next = l2
                curHead = curHead.next
                l2 = l2.next
                
        if l1 != None: curHead.next = l1
        if l2 != None: curHead.next = l2
        return dummyHead.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0: return None
        step = 1
        while step < k:
            for i in range(0, k-step, step + step):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+step])
            step += step 
        return lists[0]
    
    
    
""" (besoin de reecrire cette explication pas tres claire...)
explication de cette partie : 
        step = 1
        while step < k:
            for i in range(0, k-step, step + step):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+step])
            step += step 
            
on doit appeler le merge de la facon suivante :           
Step = 1, on saute une place a chaque fois; on va de 0 a K-1 pour la dernier liste
    lists[0] = mergeTwoLists(lists[0], lists[1]).
    lists[2] = mergeTwoLists(lists[2], lists[3]).
    ...
    lists[K-2] = mergeTwoLists(lists[K-2], lists[K-1])
Step = 2, on saute 3 place a chaque fois ;  on va de 0 a K-2 comme on peut voir que le denier merge est mergeTwoLists(lists[K-4], lists[K-2])  
    lists[0] = mergeTwoLists(lists[0], lists[2]).
    lists[4] = mergeTwoLists(lists[4], lists[6]).
    ...
    lists[K-4] =  mergeTwoLists(lists[K-4], lists[K-2])            
Step = 3, on saute 7 place; on va de 0 a K-3
    lists[0] = mergeTwoLists(lists[0], lists[2]).
    lists[8] = mergeTwoLists(lists[4], lists[6]).
    ...
    lists[K-8] = mergeTwoLists(lists[K-8], lists[K-4])            
Step = 4, on saute 15 place 
    lists[0] = mergeTwoLists(lists[0], lists[2]).
    lists[8] = mergeTwoLists(lists[4], lists[6]).
    ...
    lists[K-16] = mergeTwoLists(lists[K-16], lists[K-8])    
etc ...    

par ex si on 9 linked list on doit faire ca : 

    L-L          L-L            L-L         L-L         L-L         L-L         L-L         L-L         L-L           9 L-L
      \         /                 \         /             \         /             \         /           / 
       \       /                   \       /               \       /               \       /           /    
         O(2M)                       O(2M)                   O(2M)                   O(2M)            /               5 L-L    
            \                           /                      \                       /             /                                                          
             \                         /                        \                     /             /                                                     
              ----------O(4M)----------                           -------O(4M)-------              /                  3 L-L                                          
                           \                                               /                      /                                                                                
                            \                                             /                      /                                                                                   
                             \                                           /                      /                                                                                               
                              \                                         /                      /                                                                       
                               \                                       /                      /                                                                    
                                ----------------O(8M)------------------                      /                        2 L-L                 
                                                   \                                        /                                                                                 
                                                    \                                      /                                                                                    
                                                     \                                    /                                                                          
                                                      \                                  /                                                                               
                                                       \                                /                                                                                       
                                                         ------------O(9M)-------------                               1 L-L

on remarque que a chaque fois qu'a chaque etape qu'on a nombre impaire de L-L la dernier linked list n'est pas merge avec une autre .

            
            """
    
