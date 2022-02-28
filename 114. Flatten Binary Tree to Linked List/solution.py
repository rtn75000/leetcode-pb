"""#1er sol #ma solution #dfs recursive #TC moi je pense que c'etait O(n) parceque meme avec la boucle je pense que on passe max 2 fois sur chaque nodes mais la plupart des commentaires considere cela O(n^2) 
donc c'est pas un bon TC (voir ici les commentaires : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36987/Straightforward-Java-Solution) #SC O(n) pour la recursion

mon idee est la suivante : 
soit un arbre  1   alors pour obtenir   1   on fait les etapes suivante : soit root==node1 alors :
              / \                        \
             2   3                        2
                                           \
                                            3
temp=root.right cad temp==node3            

root.right=root.left cad root.right == node 2 donc on a  :   1
                                                            / \                    
                                                           2   2
root.left = None donc on a :    1
                                 \                    
                                  2      
                                  
puis maintenant on fait : 
while root.right :
        root=root.right 
cad tant que on peut aller a droite on va a droite on fait ca car on peur avoir un arbre comme ca      1   est donc ds ce cas on va avoir ca avant le while : 1    est donc pour faire pointer node 4 sur l'ancien left 
                                                                                                      / \                                                      \  
                                                                                                     2   3                                                      2         
                                                                                                    /                                                            \
                                                                                                   4                                                              4
comme root==node1 alors il faut faire right jusqu'a qu'on arrive a node 4 c'est pour ca on fait le while.  
donc a la fin du while root == node 2.

root.right = temp cad node2.right == node 3 donc on a  1
                                                        \                    
                                                         2
                                                          \
                                                           3 

on va faire cela de facon recursive en traversant tout l'arbre voir github pour une photo explicative :
https://github.com/rtn75000/leetcode-pb/blob/main/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List/photo%20explication%20de%20la%20sollution%201%20.md

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs (root) :

            if not root : 
                return 
            
            dfs(root.left)
            dfs(root.right)
            
            if root.left : 
                temp = root.right
                root.right=root.left
                root.left=None
                while root.right :
                    root=root.right 
                root.right=temp
                      
        dfs(root)

      
    
    
"""sol 2  #dfs recursive #TC O(n) #SC O(height)  worst case O(n)

cette solution est un peu dure a comprendre mais elle nous permet de bien s'exercer dans le dfs . 
 
app: 
 
 commancont par un arbre simple : 
 
     1       root == node 1 donc si on fait dfs(root.left) comme node 2 est un leaf il return lui meme cad node 2 donc dfs(node1.left)==node 2 . meme chose pour dfs(root.right) comme node 3
    / \      est un leaf il return lui meme cad node 3 donc dfs(node1.right)==node 3 . maintenant on veut flatten l'arbre donc comme root a un element a gauche on doit le mettre a droite .
   2   3     on va donc faire que le resultat du dfs(root.left) qui nous donne node 2 pointe a droite (car on veut les elemens que a droite) sur root.right cad sur node 3 donc dfs(root.left).right = root.right
             cad node2.right==node3 donc on obtient   1   donc maintenant on veut root.right cad node2 (bien entendue que quand on parle d'un node on parle aussi de tout ce qu'il pointe dessus) soit a droite de 
                                                     / \                                                                                                                                                                     
                                                    2   3                                                                                                                                                                     
                                                     \                                                                                                                                                                       
                                                      3                                                                                                                                                                      
            root (cad node1)  donc root.right=root.left cad node1.right==node2 donc on obtient   1    maintenant il faut donc supprimer le coter gauche donc root.left=None on obtient donc  1    
                                                                                                / \                                                                                           \
                                                                                               2   2                                                                                           2
                                                                                                \   \                                                                                           \
                                                                                                 3   3                                                                                           3
                                                                                                                                                                                                                            
  maintenant dison on a un arbre comme celui ci  : 
  
          4
         / \                                                                                                                                                                                                                 
        1   5
       / \   \
      2   3   6

alors on fait :
dfs(node4) :
                                                           return node 3 
    leftTail=dfs(node1): <-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                                                                        |
         leftTail=dfs(node2): <---                                                                                                                                                                      |
                                 |                                                                                                                                                                      |
              return node2 -------                                                                                                                                                                      |                    
                                                                                                                                                                                                        |  
         rightTail=dfs(node3): <---                                                                                                                                                                     |                    
                                  |                                                                                                                                                                     |      
              return node3 --------                                                                                                                                                                     |            
                                                                                                                                                                                                        |                
         if root.left : #comme node1.left est pas Null donc il faut flatten :                                                                                                                           |        
                                                                                        1                                                                                                               |        
            leftTail.right = root.right     \                                            \                                                                                                              |    
            root.right = root.left           | => ca donne ce qu'on a vu en haut cad      2                                                                                                             |
            root.left=None                  /                                              \                                                                                                            |
                                                                                            3                                                                                                           |
         #maintenant ce qui est important c'est de retourner la fin de cette arbre cad node3 car si en remontant on veut append a la fin de cette arbre le cote droit il nous faut le node3 donc on     |
         #return rightTail (qui est le tail du cote droit cad le leaf du cote droit ) or leftTail (cad si ya pas de rightTail voir exemple apres alors on rend leftTail)                                |
         #comme ici on a rightTail alors ca va return rightTail cad 3                                                                                                                                   |
                                                                                                                                                                                                        |    
         return rigthTail or leftTail cad return rightTail car rightTail pas null donc return node3 -----------------------------------------------------------------------------------------------------
         
         remarque : l'arbre va etre comme ca  4
                                             / \        
                                            1   5
                                             \   \
                                              2   6
                                               \
                                                3           
    
    rightTail=dfs(node5): <------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                                                                        |
         leftTail=dfs(None): <---                                                                                                                                                                       |
                                |                                                                                                                                                                       |
              return None -------                                                                                                                                                                       |                    
                                                                                                                                                                                                        |  
         rightTail=dfs(node6):  <--                                                                                                                                                                     |          
                                  |                                                                                                                                                                     |      
              return node6 --------                                                                                                                                                                     |            
                                                                                                                                                                                                        |                
         if root.left : #comme node5.left est Null donc la condition est false on fait pas le if car il ya rien a flatten                                                                               |              
                   ...                                                                                                                                                                                  |    
                                                                                                                                                                                                        |
         return rigthTail or leftTail cad return rightTail car rightTail pas null donc return node6 -----------------------------------------------------------------------------------------------------
         
         remarque : l'arbre va etre comme ca  4
                                             / \        
                                            1   5
                                             \   \
                                              2   6                                                                 
                                               \                                                     4       
                                                3                                                     \  
                                                                                                       1        
    if root.left : #comme node4.left est pas Null donc il faut flatten :                                \                                                                                                    
                                                                                                         2                                                                                       
        leftTail.right = root.right  cad node3.right==node5           \                                   \                                                     
        root.right = root.left    cad node4.right==node1               | => ca donne cette arbre           3                                                                                         
        root.left=None                                                /                                     \                                     
                                                                                                             5
                                                                                                              \
                                                                                                               6
                                                                                                               
    return rigthTail or leftTail cad return rightTail car rightTail pas null donc return node6 (on rend rightTail pour un futur append)         
    
    
remarque : raison pour la quelle on fait   return rigthTail or leftTail et pas seulement return rightTail : 

prenons par exemple l'arbre suivant    1 
                                      /
                                     2
                                    /
                                   3 

si on fait l'algo avec seulement return rightTail ca donne ca : 

dfs(node1) : 
        
        leftTail=dfs(node2) :             <----------------------------------------------------------------------------------------------------------- 
                                                                                                                                                     |             
                leftTail=dfs(node3): <--                                                                                                             |             
                                       |                                                                                                             |                         
                        return node3 ---                                                                                                             |             
                                                                                                                                                     |                 
                rightTail=dfs(None): <--                                                                                                             | 
                                       |                                                                                                             |                               
                        return None  ---                                                                                                             |   
                                                                                                                                                     |                   
                if root.left :  # comme node2.left est pas null donc on rentre ds le if :                                                            |               
                                                                                                                                         1           |                                   
                    leftTail.right = root.right   cad node3.right==node2.right cad node3.right==None    \                               /            |                       
                    root.right = root.left    cad node2.right==node3                                     |=> on obtient donc           2             |                   
                    root.left=None                                                                      /                               \            |                       
                                                                                                                                         3           |                   
                                                                                                                                                     |
                si il y'avait que return rigthTail alors on aurait return None  ----------------------------------------------------------------------
                
        rightTail=dfs(None): <--                                                                                                              
                               |                                                                                                                                            
                return None  --- 
                
        if root.left :  # comme node1.left est pas null donc on rentre ds le if :                                                                  
                                                                                                                                                                 
                leftTail.right = root.right   , leftTail==None donc il a pas de right donc erreur !!!                                                


si on fait l'algo avec return rightTail or leftTail ca donne ca : 

dfs(node1) : 
                                               node3
        leftTail=dfs(node2) :             <----------------------------------------------------------------------------------------------------------- 
                                                                                                                                                     |             
                leftTail=dfs(node3): <--                                                                                                             |             
                                       |                                                                                                             |                         
                        return node3 ---                                                                                                             |             
                                                                                                                                                     |                 
                rightTail=dfs(None): <--                                                                                                             | 
                                       |                                                                                                             |                               
                        return None  ---                                                                                                             |   
                                                                                                                                                     |                   
                if root.left :  # comme node2.left est pas null donc on rentre ds le if :                                                            |               
                                                                                                                                         1           |                                   
                    leftTail.right = root.right   cad node3.right==node2.right cad node3.right==None    \                               /            |                       
                    root.right = root.left    cad node2.right==node3                                     |=> on obtient donc           2             |                   
                    root.left=None                                                                      /                               \            |                       
                                                                                                                                         3           |                   
                                                                                                                                                     |
                return rigthTail or leftTail   donc comme rightTail==None donc return leftTail cad node3 ---------------------------------------------
                
        rightTail=dfs(None): <--                                                                                                              
                               |                                                                                                                                            
                return None  --- 
                
        if root.left :  # comme node1.left est pas null donc on rentre ds le if :    
                                                                                                                           1
                leftTail.right = root.right    cad node3.right==node1.right cad node3.right==None    \                      \
                root.right = root.left    cad node1.right==node1.left cad node1.right==node2          |=> on obtient donc    2 
                root.left=None                                                                       /                        \
                                                                                                                               3
        return rigthTail or leftTail   donc comme rightTail==None donc return leftTail cad node3 

"""


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs (root) :

            if not root :  # dans le cas on on a que left ou que right alors en dfs right ou dfs left donne None respectivement
                return None 
            
            if not root.left and not root.right : # si root est un leaf
                return root 
            
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            
            if root.left : 
                leftTail.right = root.right
                root.right = root.left
                root.left=None
                
            return rightTail or leftTail
                      
        dfs(root)
