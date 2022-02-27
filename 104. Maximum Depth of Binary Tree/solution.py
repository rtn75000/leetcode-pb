"""#ma solution #dfs recursive  #TC O(n) #SC O(height) height can be O(n)"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi = 0    
        def dfs (root,height) : 
          #maxi est exterieur a la fonction , comme ce n'est pas une variable local il n'est pas propre a chaque appel de recursion donc quand on remonte les recursion il reste inchanger il revient pas a son etat precedent
            nonlocal maxi    
            if not root : 
                maxi=max(maxi,height)
                return  # permet d'arreter la recursion quand on arrive au leaf
            dfs(root.left,height+1)
            dfs(root.right,height+1)
        dfs(root,0)  #modifie maxi 
        return maxi 
    
"""meme idee #pas ma sol mais plus concis

app :         1               
           /     \            
          2       3           
                 /             
                6
                
dfs (1) :
     left=dfs(2):
     
         left=dfs(null): 
            
                return 0
                
         rigth=dfs(null):
           
                return 0 
                
         return max(left,right) + 1 cad 0+1 cad 1
         
     rigth=dfs(3):
     
         left=dfs(6):
     
             left=dfs(null): 

                    return 0

             rigth=dfs(null):

                    return 0 

             return max(left,right) + 1 cad 0+1 cad 1
             
         rigth=dfs(null):
         
                    return 0
                    
         return max(left,right) + 1 cad 1+1 cad 2
         
     return max(left,right) + 1 cad 2+1 cad 3

"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    
    
"""#my sol!!! #iterative #BFS #TC SC O(n)
comme bfs va niveau par niveau le dernier element dans le stack va etre du dernier niveau forcement donc quand on sort du while res va avoir distance du dernier element qui correspond a la hauteur de l'arbre.  
app :         1               
           /     \            
          2       3           
                 / \           
                6   7
                
on introduit dans le stack (node,distance)           

queue= [(1,1)] , popleft (enleve 1) puis ajout de ses enfants dans la queue en augmentant la distance de 1
queue= [(2,2),(3,2)], , popleft (enleve 2) puis ajout de ses enfants dans la queue en augmentant la distance de 1, comme 2 n'a pas d'enfant donc on ajoute rien.
queue= [(3,2)], popleft (enleve 3) puis ajout de ses enfants dans la queue en augmentant la distance de 1
queue= [(6,3),(7,3)], popleft (enleve 6) puis ajout de ses enfants dans la queue en augmentant la distance de 1, comme 6 n'a pas d'enfant donc on ajoute rien.
queue= [(7,3)], popleft (enleve 7) puis ajout de ses enfants dans la queue en augmentant la distance de 1, comme 7 n'a pas d'enfant donc on ajoute rien.
queue=[] donc while est fini la derniere distance rencontrer est 3 donc height==3

"""

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root :
            return 0  
        
        #queue pour le BFS
        queue = collections.deque([(root,1)])  # le root est considerer dans notre exo comme height 1
                
        while queue :   
            
            node,distance = queue.popleft() # on retire a chaque fois au debut
            
            if node.left : 
                queue.append((node.left,distance+1)) #on append a la fin
            if node.right : 
                queue.append((node.right,distance+1)) #on append a la fin
            
        
        return distance   # python reconnait les variables des nested while ! (meme si distance est dans while il reconnait la variable meme en dehors du while)
                          # python reconnait les variables de tout les nested loop(while for) on condition (if, else)!!!!!
            
