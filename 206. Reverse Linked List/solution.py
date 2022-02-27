"""iterative solution : #O(n) TC   #O(1) SC

introduction : dans python si on fait object1= object2 les 2 objets seront situer a la meme adresse cad c'est juste une etiquette qu'on donne a une adresse et si on modifie un des object cela modifiera l'autre 
automatiquement :

n1=ListNode(1)
n2=n1
si on fait print(n1) ou print(n2) ca nous donnera la meme adresse , si on modifie n1 par exemple 
n1.val = 2
alors si on fait print(n2.val) ca va donner 2! 

l'idee est simple:

-initialisation :
    prev=None
    curr=head  

       1  ->  2  ->  3  ->  4 
       ^      
    head,curr    
         
       
-while loop : 

1er iterartion :

  nxt=current.next 

       1  ->  2  ->  3  ->  4 
       ^      ^      
   head,curr nxt
       
  curr.next=prev, ca veut dire que current/head (les 2 car comme dans l'intro on a dit qu'ils ont la meme adresse) ne pointe plus sur 2 mais sur None 
   
   None <- 1  -X->  2  ->  3  ->  4 
           ^        ^      
       head,curr   nxt
  
   prev=curr : 

       None <- 1        2  ->  3  ->  4 
               ^        ^      
       head,curr,prev  nxt

   curr=nxt :
   
       None <- 1          2  ->  3  ->  4 
               ^          ^      
           head,prev  curr,nxt
        
        
2eme iteration: 

  nxt=current.next : 

       None <- 1          2  ->  3  ->  4 
               ^          ^      ^
           head,prev     curr   nxt
        
       
  curr.next=prev :
   
       None <-  1 <------ 2  -X->  3  ->  4 
                ^         ^        ^
            head,prev   curr     nxt
       
  prev=curr :

       None <-  1 <------  2  -X->  3  ->  4 
                ^          ^        ^
              head     curr,prev   nxt
 
   curr=nxt :
   
       None <-  1 <------  2  -X->  3  ->  4 
                ^          ^        ^
               head      prev     curr,nxt
        
        
etc...  (donc on fais reverse a chaque fois sur 2 nodes seulements)

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr :
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev # on retourne prev et pas curr car curr sera egale a None a la fin 
    
    
"""recursive solution : #O(n) TC  #O(n) SC:because recursion will call itself n times that cost O(1) each"""
class Solution:
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
