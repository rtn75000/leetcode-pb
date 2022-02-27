"""#ma solution !!! #64ms (99,98%)   #DFS recursive #TC O(n) #SC O(height) for recursion call

-choix du path :

    soit un arbre de ce type la : 

                A
              /   \
             B     C
            / \   / \  
           D  E   F  G              

    si on choisi FCG alors on ne peut plus rajouter autre chose car par ex FCGA n'est pas un path entre 2 node mais si on choisi GC on peut rajouter autre chose tel que GCAB qui est un passe entre B et G.
 
-comprendre les differentes possibilites  :

     Dans chaque subproblem de type :    A      on a 6  possibilites :
                                        / \ 
                                       B   C
    - si A+B+C > A+B et A+B+C> A+C et A+B+C> A  et A+B+C> B et A+B+C> C ca veut dire que A+B+C est le max path . on ne peut rien ajouter a A+B+C comme expliquer en haut dans path.
    - si A+B > A+B+C et A+B > A+C et A+B > A et A+B > B et A+B > C ca veut dire que A+B est le max path . on pourra choisir de rajouter a AB ou non.
    - si A+C > A+B+C et A+C > A+B et A+C > A et  A+C > B et  A+C > B ca veut dire que A+C est le max path . on pourra choisir de rajouter a AC ou non.
    - si A > A+B+C et A > A+B et A > A+C et A > B et A > C  ca veut dire que A est le max path . on pourra choisir de rajouter a A ou non.
    - si B > A+B+C et B > A+B et B > A+C et B > A et B > B ca veut dire que B est le max path . donc ici on choisi que B on ne pourra ensuite rajouter qqch car il ya pas de continuite vu qu'on va sauter A. 
    - si C > A+B+C et C > A+B et C > A+C et C > A et C > B ca veut dire que C est le max path . donc ici on choisi que C on ne pourra ensuite rajouter qqch car il ya pas de continuite vu qu'on va sauter A. 
    
    donc si A+B+C ou C ou B est max path on ne peux rien ajouter mais si A+B ou A+C ou A est max path alors on peux choisir de rajouter ou non . donc pour cela on va a chaque fois rendre 2 resultat un 
    resultat sur lequelle on peut rajouter et un sur le quelle on ne peut pas rajouter :
    return [max(A+B, A+C, A),max(A+B, A+C, A+B+C , A, B, C)]
    
   remarque : un leaf va rendre [leaf.val,leaf.val] car lui aussi ou il vaut mieu lui en rajouter ou il vaut mieu ne pas lui en rajouter 

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root) : 
            if not root.left and not root.right : # si root est un leaf
                return [root.val,root.val]   # [valeur qu'on peut en rajouter  , valeur qu'on ne peut en rajouter ] 
            if root.left and not root.right :  #si enfant que a gauche
                left = dfs(root.left)
                return [max( root.val+left[0], root.val), max(root.val, root.val+left[0], left[1])]
            if root.right and not root.left :  #si enfant que a droite 
                right = dfs(root.right)
                return [max( root.val+right[0], root.val), max(root.val, root.val+right[0], right[1])]
            left = dfs(root.left)
            right = dfs(root.right)    
            return [  max( root.val+left[0], root.val+right[0] ,root.val )  ,   max(  root.val+right[0], root.val+left[0], root.val+left[0]+right[0], root.val, left[1], right[1]  )  ]
        
        res=dfs(root)  
        return max(res[0],res[1]) # on rend le max entre la valeur finale qu'on peut modifier et la valeur final qu'on ne peut modifier 
            
            
