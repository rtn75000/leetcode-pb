"""#ma sol! # inorder traversal dfs recursive # TC SC O(n)
si on fait inorder traversal a un BST ca nous donne les valeurs du BST ds l'ordre croissant. comme on nous demande la k-ieme valeur et que inorder nous donnera une liste des valeurs dans l'ordre croissant 
donc on retourne l'index k-1 car list commence par 0 donc la k-ieme valeur se trouve a l'indexe k-1. 
more about inorder : https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorderTraversal(root):
            # cad si root pas None alors il ya un appele recursive cote gauche puis on append a au resultat cote gauche la valeur du node actuelle puis appel de la recursion cote droit . Si root==None alors on 
            # return [] cad il ya pas d'appel recursive c'est dc notre condition d'arret. 
            return  inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []
        
        res= inorderTraversal(root) # la fct nous rend une liste des valeurs dans l'ordre croissant 
        
        return res[k-1]
    
"""iterative inorder dfs voir explication ici : https://leetcode.com/problems/binary-tree-inorder-traversal/"""   
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:    
          def inorderTraversal(root):
                res, stack = [], []
                while stack or root:
                    while root:  # on va a gauche tant qu'on peut en ajoutant les elements au stack
                        stack.append(root)  #ajouter au stack
                        root = root.left
                    node = stack.pop()
                    res.append(node.val) # ajouter au res
                    root = node.right #on va a droite 
                    
                return res  
    
          res= inorderTraversal(root) # la fct nous rend une liste des valeurs dans l'ordre croissant 
        
          return res[k-1]
    
    
    
    
