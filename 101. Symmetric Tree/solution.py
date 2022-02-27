"""#first sol #recursive dfs #TC O(n)  #SC O(h) h==height of tree can be O(n) in worst case 
on doit verifier que le subtree de gauche soit la symetrie du subtree de droite le root on s'en fou car il a pas de symmetrie.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root :    # si l'arbre est vide : 
            return True 
        return self.isSubtreeSymmetric(root.left,root.right)   #verifier la symmetrie des subtrees
        
    def isSubtreeSymmetric(self,t1 : Optional[TreeNode],t2 : Optional[TreeNode]) -> bool:
        if not t1 and not t2:   # if t1 and t2 equal None
            return True
        if not t1 or not t2:    # if t1 equal None but not t2 or opposite 
            return False
        return t1.val == t2.val and  self.isSubtreeSymmetric(t1.left, t2.right) and self.isSubtreeSymmetric(t1.right, t2.left) 
    
"""#2nd sol #iterative dfs #TC O(n)  #SC O(n)  
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]  #LIFO
        while stack:
            t1, t2 = stack.pop()   # pop nous donne un tuple composer de 2 elements #pop ds stack doit donner le dernier element inserer
            if t1==None and t2==None:
                continue
            if t1==None or t2==None:
                return False
            if t1.val == t2.val:
                stack.append((t1.left, t2.right))
                stack.append((t1.right, t2.left))
            else:  # if t1.val != t2.val : 
                return False
            return True
        
"""#3rd sol #BFS #iterative #TC/SC O(n)"""
class Solution(object):
    def isSymmetric(self, root):
        
        if not root:
            return True
        
        queue = [root.left, root.right]  #FIFO
        
        while len(queue) > 0:
            
            left = queue.pop(0)  # pop ds queue doit donner le premier element inserer
            right = queue.pop(0)
             
            if not left and not right:
                continue
            elif left and right and left.val == right.val:
                # Enqueue children
                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)
            else:
                return False
  
        return True
