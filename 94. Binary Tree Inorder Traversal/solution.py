""" #iterative inorder dfs #TC SC O(n)
rappel : inorder c'est LNR ( left node right) donc si on a ca :  

              1               
           /     \            
          2       3            alors le inorder traversal ca donne ca 4 2 5 1 6 3 7 
        /  \     /  \           
       4    5   6    7
      
en fait ca marche de la facon suivante on fait LNR a chaque fois fonc quand on va L on refait LNR et ainsi de suite quand on fini left on remonte de la recursion et on fait N cad on imprime puis R  qui a nouveau un appel
recursive de LNR sur le node de droite et ainsi de suite . 

notre algo marche de la facon suivante il va tout a gauche en entrant les elenment dans le stack puis des qu'il ya plus de gauche il pop un element du stack le rajoute au res et puis il va a droite de cette element. 
puis il recommence va tout a gauche pop un element puis va a droite et ainse de suite . 
app :    
              1               stack = [1,2,4] ,on a append tout les element de gauche, puis pop (enleve 4) puis append a res : res = [4] puis root = 4.right cad null
           /     \            stack= [1,2] comme root est nul donc il ya pas la possibilite d'aller a gauche, pop(enleve 2)  puis append a res : res = [4,2] puis root=2.rigth cad root=5
          2       3           stack=[1,5] on a append root puis ya plus de possibilite d'aller a gauche donc pop(enleve 5)  puis append a res : res = [4,2,5] puis root=5.rigth cad null
        /  \     /  \         stack = [1] pas de gauche donc pop (enleve 1)  puis append a res : res = [4,2,5,1] puis root=1.right cad root=3
       4    5   6    7        stack=[3,6] on a append root et ses element de gauche, puis pop (enleve 6) puis append a res : res = [4,2,5,1,6] puis root=6.right cad root=null
                              stack = [3] root null donc pas de gauche donc pop (enleve 3)  puis append a res : res = [4,2,5,1,6,3] puis root=3.right cad root=7
                              stack=[7] on a append root  puis pop (enleve 7) puis append a res : res = [4,2,5,1,6,3,7] puis root=7.right cad root=null
                              comme root == null et stack == [] alors on a fini le while donc return res cad [4,2,5,1,6,3,7]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iteratively       
    def inorderTraversal(self, root):
        res, stack = [], []
        while stack or root:
            while root:  # on va a gauche tant qu'on peut en ajoutant les elements au stack
                stack.append(root)  #ajouter au stack
                root = root.left
            node = stack.pop()
            res.append(node.val) # ajouter au res
            root = node.right #on va a droite 

        return res
  

    
"""recursive inorder"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def inorderTraversal(self,root):
         return  self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        
"""       

il ya un patern qui permet d'avoir quasiment le meme code pour inorder preorder et post order il utilise un flag ds le stack qui permet de determiner si le node a ete visiter cad si on a deja fait rentrer ses 2 enfant
dans le stack si oui alors on l'append au res si non on roujoute c'est enfant au stack et on le rerajoute mais cette fois ci avec le flag True cad qu'il est visited

"""

"""
In preorder, the order should be root -> left -> right But when we use stack, we append in reverse order: right -> left -> root

 
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:  
                    res.append(node.val)
                else:  # preorder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res
"""

"""
In inorder, the order should be left -> root -> right But when we use stack, we append in reverse order: right -> root -> left


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res

"""

"""
In postorder, the order should be left -> right -> root But when we use stack, we append in reverse order: root -> right -> left

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res
    """


