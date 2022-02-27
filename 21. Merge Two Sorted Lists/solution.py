"""# iterative # TC O(len(l1)+len(l2))  #SC O(1)  
code d'ici : https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place)."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0) # le plus simple c'est de cree un nouveau head et de merge les elements a ce head
        while l1 and l2:  # tant que il ya pas une linked list qui se vide 
            if l1.val < l2.val:
                cur.next = l1  # ici curr pointe sur l1 
                l1 = l1.next   
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next  # on fait avancer curr
        cur.next = l1 or l2 # a la fin du while on peut avoir une linked list qui est pas encore vide donc on append tout la list a notre linked list (a or b cad ca prend la valeur de a si pas null ou b si a est null)
        return dummy.next # on retourne sans le head qu'on a rajouter 
    
    
"""#recursive  # TC O(len(l1)+len(l2))  #SC O(len(l1)+len(l2)) 
code d'ici : https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
la recursion : 
list1[0]+merge(list1[1:],list2)  if list1[0]<list2[0]
list2[0]+merge(list1,list2[1:])  otherwise
"""
    
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:   
        if not l1 or not l2:  #  if either of l1 or l2 is null, there is no merge to perform, so we simply return the non-null list.
            return l1 or l2
        #we determine which of l1 and l2 has a smaller head, and recursively set the next value for that head to the next merge result.
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
