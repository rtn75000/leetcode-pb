"""  #not my sol  #dfs recursive #binary tree #TC O(n)  #SC O(h) h==height of tree can be O(n) in worst case . 

pour calculer le diametre il faut additionner la hauteur (la hauteur c'est la plus longue distance du node au leaf) de droite et de gauche de chaque node, explication : dans le BT suivant:
              
                 3
               /   \
              5     7
            /   \      
           6     2     
          / \     \
        10   9     1
              \     \ 
               4     8
               
-si on prend le node 3 alors la hauteur de gauche est 4 et la hauteur de droite est 1 donc ici le diametre est 4+1==5 (8-1-2-5-3-7 ou 4-9-6-5-3-7)
-si on prend le node 5 alors la hauteur de gauche est 3 et la hauteur de droite est 3 donc ici le diametre est 6 (4-9-6-5-2-1-8)
-si on prend le node 10 ou 4 ou 8 ou 7 le diametre sera 0 
-si on prend le node 9 ou 1 le diametre sera 1 
-si on prend le node 2 le diametre sera 2 
le diametre de l'arbre va etre le plus grand diametre trouver donc ici le diametre va etre 6

          
donc pour calculer le diametre de chaque node il nous faut la hauteur de gauche et de droite, ensuite il faut comparer avec les diametres trouver jusqu'a present et garder le diametre max . 
pour touver la hauteur il faut tout simplement faire un appel recursive en remontant de la recursion on gardera la hauteur la pus grande entre le cote gauche et cote droit . 

app : c'est compliquer a ecrire mais il faut comprendre qu'il ya deux recursion chaque recursion ne calcul rien tant qu'on est pas arriver au leaf c'est en remontant que tout les calcules se font .

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0     
        
        def longest_path(node):
            
            if not node:    #cndition d'arret de la recursion
                return 0
            
            nonlocal diameter   #fait reference a une variable non local permet d'utiliser une variable exterieur ds la fonction
            
            # recherhe de la hauteur de gauche et de droite 
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # le diametre est le diametre max entre le diametre actuelle cad left_path + right_path et le diametre max trouver auparavant 
            diameter = max(diameter, left_path + right_path)

            # la hauteur d'un node c'est la plus grande distance entre lui et les leaf donc c'est le max entre le cote gauche et le cote droit 
            return max(left_path, right_path) + 1    # +1 car left_path et right_path son la hauteur jusqu'au enfant donc pour inclur la distance au pere on rajoute 1

        longest_path(root)
        return diameter
    
    
    """on ne verra pas de solution iterative elle est plus compliquer"""
