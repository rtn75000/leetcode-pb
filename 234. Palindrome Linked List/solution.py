"""on veut O(n) TC et O(1) SC (avec recursion on ne peut avoir O(1) car stack call)
#iterative # O(n) TC  # O(1) SC #one pass
le code d'ici :https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).
visualisation : https://leetcode.com/problems/palindrome-linked-list/discuss/1137027/JS-Python-Java-C%2B%2B-or-Easy-Floyd's-%2B-Reversal-Solution-w-Explanation

important : 
voir ma solution ici probleme tres ressamblant : https://leetcode.com/problems/reorder-list/ 

ici aussi il ya 3 etape : 
-trouver le milieu (a l'aide de 2 pointeur un rapide et un lent 
-a partir du milieux faire reverse 
-comparer les 2 moitiers
ex: 1->2->2->1 apres la 2eme etape ca va nous donner :    1->2->2<-1     
                                                          ^        ^
                                                         head     prev 
donc on compare head avec prev puis on fait avancer les 2 :     1->2->2<-1     et on compare 
                                                                   ^  ^
                                                                 head prev                                           
comme prev n'a pas ou aller alors c'est fini est ca rend true                 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # compare the first and second half nodes
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
