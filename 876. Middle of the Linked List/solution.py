""" #two pointers #TC O(n) #SC O(1)
on utilise un pointeur lent cad qui se deplace que de 1 a chaque fois et un pointeur rapide qui se deplace de 2 a chaque fois. 
pour comprendre il faut voir un exemple si la taille de liste est paire et un si la taille est impaire. 
exemple de cas impaire :
For example, head = [1, 2, 3, 4, 5].
step 0: [1, 2, 3, 4, 5]
         ^
        s,f 
step 1: [1, 2, 3, 4, 5]
            ^  ^
            s  f 
step 2: [1, 2, 3, 4, 5]     f.next==None donc on a fini s==3 est le milieu
               ^     ^
               s     f 
               
exemple de cas paire :
For example, head = [1, 2, 3, 4].
step 0: [1, 2, 3, 4]
         ^
        s,f 
step 1: [1, 2, 3, 4]      
            ^  ^
            s  f     
step 2: [1, 2, 3, 4]Null    f==None donc fini    s==3 est le milieu  
               ^     ^
               s     f     
               
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        slow = fast = head
        # cette condition est importante : - 'fast.next' est la ds le cas ou la taille est impaire car ds ce cas le dernier fast va etre le dernier node est node.next == None
        #                                  - 'fast' est la dans le cas ou la taille est paire car dans ce cas le dernier fast va etre None 
        while fast and fast.next:  
            slow = slow.next
            fast = fast.next.next
        return slow
