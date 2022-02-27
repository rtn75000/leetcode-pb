"""#my sol #DFS recursive #TC O(n)  n ==  nums of nodes in tree  #SC O(height) can be O(n)
ma solution utilise le fait que chaque recursion a ses propres variables donc a chaque fois qu'on passe de recursion les variable change et quand on remonte la recursion les variables reviennent comme elles etaient . 
dans un arbre binaire a chaque fois qu'on va a gauche on doit changer le max avec la valeur du pere , et a chaque fois qu'on va a droite on doit changer le min avec la valeur du pere , la valeur de l'enfant doit etre 
entre min et max . 
cette arbre est une super explication de comment se comporte le max et le min:

                                                                                         min=-inf  max=+inf
                                                                                                 20                                                                                
                                                                  /                                                               \ 
                                                          min=-inf max=20                                                   min=20  max=+inf   
                                                                 10                                                               30          
                                                  /                              \                                   /                              \                                            
                                         min=-inf max=10                    min=10 max=20                     min=20 max=30                   min=30 max=+inf   
                                                 5                               15                                25                                35 
                                         /             \                 /               \                   /             \                  /               \         
                                min=-inf max=5     min=5 max=10   min=10 max=15     min=15 max=20     min=20 max=25   min=25 max=30    min=30 max=35     min=35 max=+inf                                        
                                       2                8               12                17                22              27              32                 40
                                                                                                        
                                                                                                            
 comme on peut le voir chaque recursion appele left and right quand on appele left alors le maxi doit etre egale a la valeur du pere mais quand on appele right le maxi reste inchanger par rapport au maxi du pere
 donc pour cela dans le code j'utilise une variable temp qui va garder la valeur du maxi pour que apres l'avoir changer pour la recursion de left on la rechange au maxi d'origine pour la recursion de droite. 
 quand on appele la recursion de gauche le mini n'est pas changer donc on touche pas mais quand on appele la recursion de droite alors le mini est egale a la valeur du pere.                            


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        
        mini = float('-inf')
        maxi = float('inf')
        
        def dfs (root) :
            
            if not root : #si le root est vide on rend true car ca voudrais dire qu'on est arriver jusqu'au leaf sans violation des propriete du BST car si non on aurait deja return False donc on ne serait pas arriver ici
                return True  
            
            nonlocal maxi , mini  # on utilise maxi et mini de la fct exterieur 
            
            temp=maxi  # temp garde le maxi de base pour la recursion cote droit
            
            maxi = root.val # maxi pour enfant de gauche
            
            # verification des propriete du BST
            # obliger de mettre la parenthese car sinon A and B or C ca revient a (A and B) or C et donc bien que root.left est null il va verifier root.left.val>=maxi ce qui va donner une erreur
            # car root.left est null donc n'a pas de val
            if root.left and (root.left.val<=mini or root.left.val>=maxi):   
                return False
    
            left = dfs(root.left)  # si on a pas enfrain les propriete du BST alors on appele dfs 
        
            if not left :  # si dfs return false donc left == False et don on return False ce qui va entrainer que tout les dfs vont return False j'usqu'en haut de la recursion
                return False
            
            maxi = temp  # maxi pour efant de droite
            mini=root.val # mini pour enfant de droite 
            
            if root.right and (root.right.val<=mini or root.right.val>=maxi):
                return False
            
            right = dfs(root.right)
            
            if not right : 
                return False  
            
            return True # on arrive ici si AUCUN dfs n'a rendu False car sinon on va jamais arriver a cette ligne 
        
    
        return dfs(root)
    
    
"""#meme idee mais bcp plus concis tres belle sol #not my sol #DFS recursive #TC SC meme que en haut
super facon d'executer dfs !!!"""

class Solution:
    def isValidBST(self, root):
        
        def dfs(node, low, high):
            if not node:
                return True
            if not low < node.val < high: 
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high) # donc si un appel de dfs est False alors ca rend False donc en remontant ca rendra tjrs false 
        
        return dfs(root, float("-inf"), float("inf"))

    
    
"""meme idee , super belle reponse  #DFS iterative #TC SC meme que en haut
super belle reponse pour dfs iterative"""    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not lower < root.val < upper: 
                return False
            if root.right:
                stack.append((root.right, root.val, upper))
            if root.left:
                stack.append((root.left, lower, root.val))
        return True
    
