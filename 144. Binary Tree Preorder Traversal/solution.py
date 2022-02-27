""" #iterative dfs on binary tree #TC SC O(n)
rappel : preorder c'est NLR (node left right) donc si on a ca :  

              1               
           /     \            
          2       3            alors le preorder traversal ca donne ca 1 2 4 5 3 6 7
        /  \     /  \           
       4    5   6    7


app :         1              le stack va etre le suivant : 
           /    \            stack = [1]  pop et append au res donc res=[1], ajout enfant droite puis gauche au stack
          2      3           stack = [3,2] pop (enleve 2 car pop retire le dernier element) et append au res donc res=[1,2], ajout enfant droite puis gauche au stack
        /  \      \          stack = [3,5,4] pop (enleve 4 car pop retire le dernier element) et append au res donc res=[1,2,4], comme 4 n'a pas d'enfant donc rien est ajouter au stack
       4    5      6         stack = [3,5] pop (enleve 5 car pop retire le dernier element) et append au res donc res=[1,2,4,5], comme 5 n'a pas d'enfant donc rien est ajouter au stack
                             stack = [3] pop (enleve 3 ) et append au res donc res=[1,2,4,5,3], 3 a un seul enfant a droite qui sera rajouter au stack
                             stack = [6] pop (enleve 6 ) et append au res donc res=[1,2,4,5,3], comme 6 n'a pas d'enfant donc rien est ajouter au stack
                             stack == [] donc le while est fini donc on return res et on a fini . 
                             
In recursive preorder, the order should be root -> left -> right , but when we use stack for iterative preorder the order should be : root (pop) -> right (append) -> left (append)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:     
       
        if not root :
            return []
        
        stack = [root]
        output = []
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right :
                    stack.append(root.right)
                if root.left :
                    stack.append(root.left)
        
        return output
    
"""recursive preorder"""
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []
