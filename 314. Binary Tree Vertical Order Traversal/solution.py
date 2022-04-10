""" #BFS   # TC O(n) car bfs (on traverse chaque node une fois) , n c'est le nbr de node dans le tree #SC O(n) car on utilise un hash table qui va conserver tout les valeurs des nodes. 

ennoncer : il faut rendre les column de gauche a droite et chaque column contient les valeur de haut en bas (voir ex 2 pour comprendre)

( voir introduction bfs : "All Nodes Distance K in Binary Tree"  )

le root de l'arbre correspond a la column 0 puis qd  on va a gauche alors on reduit de 1 si on va a droite on augmente de 1. (voir photo git)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root :
            return []
        
        # dictionnaire dont les key correspondent a la column et les valeurs correspondent au nodes apartenent a cette column  (voir github photo)
        dic = defaultdict(list)
        
        # queue for level order traversal (bfs)
        queue = collections.deque()

        val = min_column = max_column = 0
        
        # Enqueue Root 
        queue.append((root,val))
        
        while queue :

            # val correspond a la column du node           
            root,val = queue.popleft()
            
            dic[val].append(root.val)
            
            min_column = min(min_column, val)  # on a besoin des ces valeurs pour traverser les column de gauche a droite a la fin
            max_column = max(max_column, val)           

            # Enqueue left child if not None
            if root.left :
                queue.append((root.left,val-1))

            # Enqueue right child if not None
            if root.right :
                queue.append((root.right,val+1))
                
        return [dic[key] for key in range(min_column, max_column + 1)]
    
    
    
