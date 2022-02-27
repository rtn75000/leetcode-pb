""" # first sol # DFS recursive # TC O(n) # SC O(h) h==height can be O(n) 

pour inverser il faut mettre l'enfant de gauche a la place de l'enfant de droite 

quand on fait un appel recursive de ce type : 
l=fct(root.left)
r=fct(root.right)
l'ordre d'ouverture de la recursion : 

                0  
           /        \  
         1           8
       /   \        /  \
      2     5      9    12
     / \   / \    / \   / \
    3   4 6   7  10 11 13 14

alors l'ordre de fermeture de la recursion :

               15 
           /        \  
         7           14
       /   \        /  \
      3     6      10   13
     / \   / \    / \   / \
    1   2 4   5  8   9 11 12

si on comprend comment l'algo marche alors au final les paires qui vont etre switch sont les suivantes : 

                root                     les paires son switch quand le pere se ferme de la recursion c'est pour ca 
           /           \                 qu'on a cette ordre .   (ex en haut on avait 3 et 6 que quand 7 alors le 3 et 6 ce change)
          l4            r4  
        /   \         /    \
      l3     r3      l7     r7 
     /  \   /  \     / \    / \
    l1  r1 l2  r2   l5  r5 l6  r6 
    
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
    
"""  # second sol # DFS iterative # TC O(n) # SC O(h) h==height can be O(n) 
""" 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left #switch
                stack.extend([node.right, node.left]) 
        return root
    
""" #3rd sol #BFS/level order traversal  # TC O(n) # SC O(h) h==height can be O(n) 
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None  
        queue = [root]
        while queue : 
            node = queue.pop(0)           
            if node : 
                node.left, node.right = node.right, node.left #switch
                queue.extend([node.right, node.left])  
        return root 
