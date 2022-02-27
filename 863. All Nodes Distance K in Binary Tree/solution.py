"""# point sur bfs graph et binary tree #DFS recursive #BFS iterative #TC SC O(V+E)

comme on ne peut retourner en arriere dans un BT (et donc on ne pourra pas par exemple trouver la distance entre 5 et 1 dans l'ex 1 de lennoncer ) alors on va transformer l'arbre en un graph .

TRANSFORMER UN ARBRE BINAIRE EN GRAPH: (super idee tjrs valabe)
un graph comme on a deja vue peut etre representer par un dictionnaire ou la key est un vertex et la valeur est une liste des vertex voisin . 
si on remarque bien un node d'un arbre binaire peut avoir au max 3 voisins : son pere et ses 2 enfants . donc pour transformer un arbre binaire en un graph il faut traverser l'arbre et ajouter au dictionnaire tout
les voisin du current node cad le peur si il existe et les enfants si ils existes . pour cela on utilisera un dfs sur un arbre binaire:
app de la construction du graph a l'aide de dfs (recursive) : 
doit l'arbre binaire suivant    3      alors si on applique le dfs de la construction du graph de notre algo ca donne ca :
                              /   \                                                                   
                             5     1                                                                       
                            / \                                                                         
                           6   2                                                                          
  graph=collections.defaultdict(list)   
  
  dfs (3,None):   # le dfs recoit un TreeNode et le parent de celui ci 
  
      #no father 
      graph[3].append(5)    donc graph={3:[5]}   # taking care of left child
      dfs(5,3):
      
            graph[5].append(3)   donc graph={3:[5], 5:[3]}   #taking care of parent 
            graph[5].append(6)   donc graph={3:[5], 5:[3,6]}   #taking care of left child
            dfs(6,5):
            
                    graph[6].append(5)   donc graph={3:[5], 5:[3,6], 6:[5]}   #taking care of parent 
                    #no child  
                    
            graph[5].append(2)    donc graph={3:[5], 5:[3,6,2], 6:[5]}   #taking care of right child
            dfs(2,5):
            
                    graph[2].append(5)   donc graph={3:[5], 5:[3,6,2], 6:[5], 2:[5]}   #taking care of parent 
                    #no child  
                    
      graph[3].append(1)     donc graph={3:[5,1], 5:[3,6,2], 6:[5], 2:[5]} # taking care of right child 
      dfs(1,3):
            
            graph[1].append(3)  donc graph={3:[5,1], 5:[3,6,2], 6:[5], 2:[5], 1:[3]} # taking care of parent
            #no child
            
            
            
maintenant qu'on a vu comment construire un graph a partir d'un BT il nous reste plus qu'a faire un bfs en partant du node target. on fait un bfs car c'est mieux qu'un dfs vu que le bfs traverse niveau par niveau 
donc des que le niveau du bfs atteint k on a plus qu'a rendre tout les valeurs des nodes de ce niveau et on a fini, alors que si on fait un dfs on devra dans tout les cas traverser tout l'arbre (car on doit descendre jusqu'au leaf puis remonter et ainsi de suite j'usqu'a qu'on trouve tout les nodes au niveau k).
ATTENTION : on fait un bfs sur un graph et pas sur un tree donc on doit ici utiliser un set visited pour ne pas repasser plusieur fois sur le meme node 

rappel BFS :

I)Level order traversal/BFS d'un BT  :

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
 
 TC SC O(n), n num of nodes 
 
II) BFS ds un graph :

on va utiliser en plus de cela une list/set(car les valeur sont unique , l'avantage est que le search est O(1)) pour savoir quel node a deja ete visiter pour ne pas refaire bfs sur des nodes qu'on leur a deja fait .
a chaque fois qu'un node va etre ajouter a la queue du bfs il sera considerer visiter .


def BFS(root):

	if not root :
		return
    
    # to keep track of visited node
    visited = set()   
        
	# queue for BFS
	queue = collections.deque()

	# Enqueue Root  # root est l'element de depart qu'on choisi ce n'est pas comme dans un binary tree ou le root il y'en a qu'un
	queue.append(root)
    
    # mark the element as visited
    visited.add(root)
    
	while queue :

		# Print front of queue and remove it from queue
		print(queue[0].val)
		node = queue.popleft() # Retire le premier

		# Enqueue all non-visited adjacent vertex of node (dequeued vertex) and mark it as visited 
		for adj in self.graph[node]:
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                    
TC SC O(V+E)                                
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = collections.defaultdict(list) #cad tout les val sont [] par default
    
        def dfs(node, parent_node):
            if not node :
                return
            if parent_node:
                graph[node].append(parent_node) #graph[node] c'est la valeur de la key node comme cette valeur est une liste alors pour ajouter un nouvelle element on utilise append
            if node.left:
                graph[node].append(node.left)
                dfs(node.left, node)
            if node.right:
                graph[node].append(node.right)
                dfs(node.right, node)
                
        dfs(root, None) # construction du graph 
        
        # BFS to retrieve the nodes with given distance
        
        # Starting from the target node
        queue = collections.deque([(target, 0)])
        
        # keep the records, since the graph is all connected
        visited = set()
        
        # mark target as visited
        visited.add(target)
        
        # results
        ans = []
        
        while queue:
            
            node, distance = queue.popleft()  #retire le premier
            
            # we've reached the desired distance/radius
            if k == distance:
                ans.append(node.val)
            
            # we haven't reached the desired distance, keep going
            elif distance < k:
                for adj in graph[node]:
                    if adj not in visited: 
                        queue.append((adj, distance+1))
                        visited.add(node)
            
            # il ne va pas y avoir ds queue des elemnts avec distance > k car si distance == k alors on append pas (adj, distance+1) a la queue que si distance<k alors on append . donc la distance max des
            # elements ds la queue va etre l, et donc des qu'on a fini de pop tout les elements avec la distance k la queue va etre vide est donc on va forcement quitter le while . 
             
        
        return ans   
    
"""BONUS SUPER IMPORTANT : super resumer de dfs iterative ds graph et binary tree

ITERATIVE DFS DANS UN BINARY TREE VS GRAPH : 

Le dfs iterative lui utilise une stack est pas une queue comme le bfs.

-ITERATIVE DFS IN BT : 

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:     
       
        if not root :
            return []
        
        #stack for dfs
        stack = [root]
        
        #resultat
        output = []
        
        while stack:
            root = stack.pop()  #pop ca veut dire on enleve le dernier element
            if root:
                output.append(root.val)
                if root.right :  # ATTENTION on met d'abord le cote droit 
                    stack.append(root.right)
                if root.left :   
                    stack.append(root.left)
        
        return output      # nous rend tout les element dans l'ordre preorder
            

 app :        1              le stack va etre le suivant : 
           /    \            stack = [1]  pop et append au res donc res=[1], ajout enfant droite puis gauche au stack
          2      3           stack = [3,2] pop (enleve 2 car pop retire le dernier element) et append au res donc res=[1,2], ajout enfant droite puis gauche au stack
        /  \      \          stack = [3,5,4] pop (enleve 4 car pop retire le dernier element) et append au res donc res=[1,2,4], comme 4 n'a pas d'enfant donc rien est ajouter au stack
       4    5      6         stack = [3,5] pop (enleve 5 car pop retire le dernier element) et append au res donc res=[1,2,4,5], comme 5 n'a pas d'enfant donc rien est ajouter au stack
                             stack = [3] pop (enleve 3 ) et append au res donc res=[1,2,4,5,3], 3 a un seul enfant a droite qui sera rajouter au stack
                             stack = [6] pop (enleve 6 ) et append au res donc res=[1,2,4,5,3], comme 6 n'a pas d'enfant donc rien est ajouter au stack
                             stack == [] donc le while est fini donc on return res et on a fini . 
 
           
 -ITERATIVE DFS IN GRAPH : 
 pour ne pas faire dfs sur un node deja visiter il faut utiliser une list/set pour tracker les nodes deja visites et ne pas refaire dfs sur eux. 
 remarque tre importante dans un graph le dfs n'est pas obliger d'etre de gauche a droite comme dans un arbre car il ya pas gauche ou droite dans un arbre donc il faut huste suivre a a chaque fois le meme sens ou
 de gauche a droite ou de droite a gauche , ex si on a :
            4--9
           /
         1 -- 3   7--8    alors dfs peut etre  1 2 5 6 7 8 3 4 9 ou 1 4 9 3 2 6 7 8 5 ca depend dans quelle sens on va a chaque fois. mais ce qui est important c'est que au final on va a chaque fois dans la profondeur
           \     /        et pas dans la largeur .
            2 --6
             \
              5
    
    def DFS(self,s):            # prints all vertices in DFS manner from a given source.
                                
        visited = set()  #que si les valeurs sont unique sinon utiliser list
 
        # Create a stack for DFS
        stack = []
 
        # Push the current source node.
        stack.append(s)
        
        # mark source as visited
        visited.add(s)
        
        #resultat
        output = []
 
        while stack :
        
            # Pop a vertex from stack and add  it to result
            
            node = stack.pop()  #retire le dernier
            
            output.append(node)
 
            # push to stack all non-visited adjacent vertex of node (dequeued vertex) and mark it as visited
            for adj in (self.graph[node]):    
                if adj not in visited :
                    stack.append(adj)
                    visited.add(adj)
 
 app :
            4--9           dfs(s==1) :
           /               stack = [1] on pop et append au res donc res=[1] puis on rajoute tout les voisin de 1 au stack                                             
         1 -- 3   7--8     stack = [2,3,4]  on pop (enleve 4) et append au res donc res=[1,4] puis on rajoute tout les voisin de 4 au stack                  
           \     /         stack = [2,3,9]  on pop (enleve 9) et append au res donc res=[1,4,9] puis on rajoute tout les voisin de 9 au stack, pas de voisin donc rien est ajouter                                         
            2 --6          stack = [2,3]  on pop (enleve 3) et append au res donc res=[1,4,9,3] puis on rajoute tout les voisin de 3 au stack, pas de voisin donc rien est ajouter                                 
             \ /           stack = [2]  on pop (enleve 2) et append au res donc res=[1,4,9,3,2] puis on rajoute tout les voisin de 2 au stack                                             
              5            stack = [5,6]  on pop (enleve 6) et append au res donc res=[1,4,9,3,2,6] puis on rajoute tout les voisin de 6 au stack 
                           stack = [5,7]  on pop (enleve 7) et append au res donc res=[1,4,9,3,2,6,7] puis on rajoute tout les voisin de 7 au stack
                           stack = [5,8]  on pop (enleve 8) et append au res donc res=[1,4,9,3,2,6,7,8] puis on rajoute tout les voisin de 8 au stack, pas de voisin donc rien est ajouter   
                           stack = [5]  on pop (enleve 5) et append au res donc res=[1,4,9,3,2,6,7,8,5] puis on rajoute tout les voisin de 5 au stack, pas de voisin non visiter donc rien est ajouter   
                           stack==[] donc fin while , on return res cad res=[1,4,9,3,2,6,7,8,5] qui nous donne un dfs du graph
                           
"""
                           
              
              
