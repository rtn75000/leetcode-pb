"""#my sol #linked list #TC SC O(1)
idee : 
si on a 4->5->6 et on veux supprimer 5 alors on fait 4->6(1)->6(2) puis 4->6(1)->Null
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val  # on copie dans le node a supprimer la valeur du node qui vient apres le node a supprimer 
        node.next = node.next.next #on saute le node qui vient d'etre copier 
