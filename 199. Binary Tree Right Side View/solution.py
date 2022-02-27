"""
INTRODUCTION BFS/Level order traversal  :

For each node, first the node is visited and then it’s child nodes are put in a FIFO queue. 

def printLevelOrder(root):

	if not root :
		return

	# queue for level order traversal
	queue = collections.deque()

	# Enqueue Root 
	queue.append(root)

	while queue :

		# Print front of queue and remove it from queue
		print(queue[0].val)
		node = queue.popleft()

		# Enqueue left child if not None
		if node.left :
			queue.append(node.left)

		# Enqueue right child if not None
		if node.right :
			queue.append(node.right)

en faite la queue va etre comme ca a chaque iteration : 
queue = [root] puis :
queue = [root.left,root.right] puis :
queue = [root.right, root.left.left, root.left.right]
queue = [root.left.left, root.left.right, root.right.left, root.right.right]
queue = [root.left.right, root.right.left, root.right.right, root.left.left.left, root.left.left.right]
queue = [root.right.left, root.right.right, root.left.left.left, root.left.left.right , root.left.right.left, root.left.right.right]
etc...
cad on pop un membre qui se trouve en tete puis on rajoute ses 2 enfants en fin de la queue de cette maniere on va pop dans l'ordre du bfs cad on va pop en commencant par tout en en haut de l'arbre  de gauche a droite 
par exemple si on a ca :    1     alors la queue va etre la suivante: queue=[1]
                          /   \                                       queue=[2,3]  
                         2     3                                      queue=[3,4,5]                                                
                        / \   / \                                     queue=[4,5,6,7]                  
                       4   5 6   7                                    queue=[5,6,7]     (ici juste on pop on rajoute pas car les enfant sont null)                                                                                                                                                 queue=[6,7]     (ici juste on pop on rajoute pas car les enfant sont null)
                                                                      queue=[7]     (ici juste on pop on rajoute pas car les enfant sont null)                                  
                                                                      queue=[]     (ici juste on pop on rajoute pas car les enfant sont null)                                  
                                                                                                        
 et donc si on print a chaque fois la tete de la queue a chaque iteration ca nous donnera au finale 1 2 3 4 5 6 7 cad le level order traversal.                                                                                                       

TC / SC O(n)
"""

"""#my sol #bfs #TC SC O(n) car bfs
dans cette exercice il faut simplement append a output le node le plus a droite de chaque niveau.
l'idee est de faire bfs en ajoutant a chaque element son level et comme bfs met dans la queue niveau par niveau donc des qu'on popleft de la queue et on a un niveau different que l'element precedent ca veut dire
que l'element precedent est le dernier du niveau precedent donc on doit le rajouter a l'output .
par exemple si on a         1     alors la queue va introduire les element dans l'ordre suivant 1 2 3 4 6 on a donc les element par niveau : niv0 niv1 niv1 niv2 niv2
                          /   \                                          
                         2     3                                                                       
                        /     /                                                     
                       4     6 
(pour comprendre comment bfs et sa queue marche voir l'introduction)

remarque : on peut pas allez juste a droite car si on a ca  1 alors le output=[1,3,5] et si on aller que a droite ca donne [1,3]
                                                           / \             
                                                          2   3          
                                                           \
                                                            5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []

        if not root :
            return output 
         
        # queue for level order traversal
        queue = collections.deque([[root,0]]) #il faut mettre une double parenthese car si on met qu'une alors ca veut dire un stack avec 2 elements root et level alors qu'on veut un stack avec un element [root,level] 
        
       
        while queue :
    
            cur = queue.popleft() # cur == [treenode,level]
         
            # Enqueue left child if not None and the level of child is level of parent + 1
            if cur[0].left :  
                queue.append([cur[0].left,cur[1]+1])

            # Enqueue right child if not None and the level of child is level of parent + 1
            if cur[0].right :
                queue.append([cur[0].right,cur[1]+1])
                
            #on ajoute cur[0].val si le prochain element dans le queue a un level different car ca veut dire que cur[0] est le dernier node du level 
            if queue and cur[1] != queue[0][1] :
                output.append(cur[0].val)
            elif not queue:             # si il ya plus d'element dans queue alors cur[0] est le dernier node de l'arbre donc il faut le rajouter car c'est lui qui est le plus a droite au dernier niveau
                output.append(cur[0].val)
              
                
        return output
    
"""ya une sol dfs mais qui a mon gout est bcp moins intuitive : https://leetcode.com/problems/binary-tree-right-side-view/discuss/1051930/Python-simple-dfs-explained """
        
        
