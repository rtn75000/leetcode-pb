"""1er solution: #iterative #TC: O(n)  #SC: O(1)
l'idee est simple si j'ai prev->a->b->b.next il faut que: prev->b->a->b.next .Comme le head n'a pas de prev alors on rajoute un dummyNode avant 

le code (modifier) : https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        
        # ajout du dummy qui pointe sur head
        cur = dummy = ListNode(0,head) 
        
# si on a une linked list vide cad head==Node alors la 1er condition de la boucle est false : cur.next cad dummy.next est egal a None (cad false) donc on rentre pas dans le while et donc on retourne directement dummy.next
# qui est none . si on a une linked list avec que un node alors la 2eme consition de la boucle est false : cur.next.next cad  dummy.next.next egale a head.next egal a None (cad false) donc on rentre pas dans le while et
# donc on retourne directement dummy.next cad le head
       
        while cur.next and cur.next.next:  # cette condition verifie qu'il ya un 3 nodes : cur->cur.next->cur.next.next soit prev->a->b (->b.next qui peut etre None)
            first = cur.next                
            sec = cur.next.next
            cur.next = sec          # cad:  cur.next =cur.next.next  soit cur -> cur.next.next  (cad prev->b)
            first.next = sec.next   # cad:  cur.next.next = cur.next.next.next   soit  cur.next -> cur.next.next.next  (cad a->b.next)
            sec.next = first        # cad:  cur.next.next.next = cur.next  soit cur.next.next->cur.next  (cad b->a )
            #on a donc au finale prev->b->a->b.next
            
            cur = cur.next.next     # on fait avancer le cur de deux position a chaque fois car on s'occupe de deux node a chaque iteration (cad cur=b.next)
        return dummy.next      # on retourne le head de la linked list  
"""2eme solution #recursive  #TC:O(n)  #SC:O(n) car ouvre n/2 recursion qui coute O(1)
le code: https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode
l'idee ici c'est que on s'occupe de 2 node a chaque fois :  a->b->c->d->e 
                                                            ^     ^     ^                  
                                                           rec   rec   rec      
                                                           
                                     se coter se lit de bas en haut :                      
1er recursion:  b->a->c->d->e   |   return b
                ^               |
2eme recursion: b->a->d->c->e   |   return d 
                      ^         |
3eme recursion: b->a->d->c->e   |   return e
                            ^
donc swapPairs(a)  retourne b qui est le head de la nouvelle linked list           
""" 

class Solution(object):
    def swapPairs(self, node):
        
        #si node==None ou il ya que un node cad node.next==None alors return node
        if not node or not node.next: 
            return node  
        
        # la prochaine recursion doit se faire sur 2 node apres cad recursion(node1)->node2->recursion(node3)->node4->recursion(node5)->...
        new_start = node.next.next  #cad c 
        
        #swap: a=b et b=a   cad a.val=b.val,a.next=b.next et b.val=a.val,b.next=a.next  donc maintenant b->a->c
        node, node.next = node.next, node  
        
        #recursion
        node.next.next = self.swapPairs(new_start)
        
        return node # la derniere recursion va rendre le head 
    
    
