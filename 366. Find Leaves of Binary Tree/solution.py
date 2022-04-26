"""
#not my sol #DFS #TC O(n) car passe une fois sur tout les nodes #SC O(height)  car la recursion utilise O(height) dans le stack du fct call.

remarque consigne : la consigne dit "as if you were doing this" cad on ne le fait pas vraiment il ne faut donc pas vraiment effacer les leafs nodes 
il faut juste faire comme si on les a supprimees . 

l'idee est de calculer la hauteur de l'arbre car c'est elle qui determinera le nbr de groupe dans la list ( ex : si h=3 alors output = [[...],[...],[...]] car il y'a 3 niveau si h=3).
la hauteur va etre calculer en remontant de la recursion donc les leafs on une hauteur 1. donc les leafs vont tous avoir la hauteur 1 il vont donc etre placer dans output[height-1] avec height=1
(on fait height-1 car list commence par idx 0). donc a chaque fois qu'on monte on rentre la val dans un autre grpe du output 


pour comprendre le code il faut comprendre quand le code s'execute dans un dfs. 

explication de comment marche un dfs : 

    dfs (node) :

          # le code ici s'execute a chaque appel de recursion 
          dfs(node.left)
          # le code ici s'execute lorsqu'on remonte de la recursion de gauche 
          dfs(node.right)
          # le code ici s'execute lorsqu'on remonte de la recursion de droite 
          

VOIR EXPLICATION GITHUB.  

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        def dfs(node):
            
            if not node:
                return 0
            
            depth = max(dfs(node.left),dfs(node.right))+1  
            # le +1 ce fait en remontant de la recursion de droite et gauche (la recursion commence a remonter quand on arrive au leaf car on dfs(left) et dfs(right) return 0 sans faire 
            # de recursion ) (voir github photo)
            
            # a chaque fois que le depth est sup au nbr de list dans l'output on augment le nbr de list 
            if len(ret)<depth:        
                ret.append([])
                
            ret[depth-1].append(node.val)  # on append a la liste d'indx height-1
            
            return depth  
        
        dfs(root)
        
        return ret
