"""introduction : 

DFS DANS UN GRAPH : (recursive)
 
notre graph va etre representer a l'aide d'un dictionnaire ou la key va etre un vertex x et la valeur va etre une liste de vertex adjacent (Qui se trouve dans le voisinage immédiat.) a x
ex : 

   1-->3               alors ca donne ca : { 1:[3,4], 3:[] , 4:[5] , 5:[] }
   |
   v
   4-->5
   
from collections import defaultdict

class Graph:

	# Constructor
	def __init__(self):
		# default dictionary the value will be an empty list by default 
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)   # u will be the key 



	# A function used by DFS
	def DFSUtil(self, v, visited):

		# marquer le currnt node en tant que node visiter puis l'imprimer 
		visited.add(v)
		print(v, end=' ')

		# appel recursive de dfs sur tout les voisin
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	# The function to do DFS traversal. 
	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()   # on utilise un set car pour ajouter,retirer ou rechercher un element ca coute O(1) (https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations)

		# Call the recursive helper function to print DFS traversal # on ne peut faire la recursion ici directement car cela va cree un nouveau set a chaque fois 
		self.DFSUtil(v, visited)

( comme on peut le constater DFS est appeler sur chaque voisin du vertex 'pere' )

Time complexity: O(V + E), where V is the number of vertices (all the key in dic) and E is the number of edges (all the values in dic) in the graph.
Space Complexity: O(V), since an extra visited set of size V is required. en plus de cela il ya aussi un fonction call stack qui peut etre O(V) (dans le cas o)

BFS DANS UN GRAPH :  (iterative)

notre graph va etre representer a l'aide d'un dictionnaire ou la key va etre un vertex x et la valeur va etre une liste de vertex adjacent (Qui se trouve dans le voisinage immédiat.) a x
ex : 

   1-->3               alors ca donne ca : { 1:[3,4], 3:[] , 4:[5] , 5:[] }
   |
   v
   4-->5
   
from collections import defaultdict

class Graph:

	# Constructor
	def __init__(self):
		# default dictionary the value will be an empty list by default 
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)   # u will be the key 



	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from  queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it  visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

Time complexity: O(V + E), where V is the number of vertices (all the key in dic) and E is the number of edges (all the values in dic) in the graph.
Space Complexity: O(V) pour visited, queue va aussi etre de taille O(V) au max .



"""

""" #first sol #not my sol  #DFS recursive in graph  #TC O(M×N) where M is the number of rows and N is the number of columns. voir explication # SC O(n*m). voir explication
rappel : DFS et BFS dans un graph pour eviter de revenir sur le meme node garde tout les nodes visiter dans une set .
Dans cette exo on va utiliser la meme idee on va faire dfs ou bfs que sur les 1 cad on va considerer comme vertex que les 1, des qu'on a visiter un 1 on le change en 0 pour ne pas le visiter a nouveau .
un vertex cad un 1 sera considerer voisin si il se trouve a droite ou a gauche ou en haut on en bas d'un autre 1. 
on va simplement traverser tout la matrice et si on rencontre un 1 alors on lance sur lui un dfs . lors du dfs tout voisin (cad un 1 adjacent) sera changer en 0 pour le marquer comme visiter donc a la fin du dfs 
tout les 1 adjacent vont etre changer en 0 , si par la suite on rencontrera un autre 1 alors il va a son tours lancer un dfs . donc le nombre de fois qu'on lance un dfs constitue le nombre d'iles. 
ex :

1 0 0 0 1        le premier dfs en partant de matrix[0][0] donne ca :   0 0 0 0 0   le deuxieme dfs en partant de matrix[3][0] donne ca : 0 0 0 0 0  le 3 eme dfs en partant de matrix[3][3] donne ca : 0 0 0 0 0 
1 1 1 1 1                                                               0 0 0 0 0                                                         0 0 0 0 0                                                     0 0 0 0 0       
0 0 0 0 0                                                               0 0 0 0 0                                                         0 0 0 0 0                                                     0 0 0 0 0   
1 1 0 0 1                                                               1 1 0 0 1                                                         0 0 0 0 1                                                     0 0 0 0 0 
on a en tout 3 depart de dfs donc on a 3 ile 

le code d'ici : https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution

TC explication : on passe sur tout les membres de la matrix , il ya en tout n*m elements donc il ya O(m*n) iteration chaque iteration peut appeler un dfs. annalisons le cout de dfs : 

-si notre matrix est comme un echequier : 
0 1 0 1 0 1
1 0 1 0 1 0 
0 1 0 1 0 1
1 0 1 0 1 0
alors on va avoir en tout O((m*n)/2) dfs car chaque un appel un dfs, mais chaque dfs coute au max O(1) car aucun 1 a un voisin egale a 1.

-si notre matrix est comme ca : 
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
alors on aura 1 appele de dfs qui coute O(m*n) esuite tout va etre echanger en 0 donc pas d'autre dfs 

ccl le dfs peut avoir en tout max O(n*m) iteration (qui peuvent etre fait en une fois on en plusieur fois). conc en tout on va avoir O(m*n) iteration pour passr un fois sur la matrix et O(m*n) iteration pour tout les dfs 
donc on a O(2*m*n)=O(m*n)

SC : il va avoir utilisation de la stack lors d'appel recursive du dfs au max on aura O(m*n) appel recursive . ce cas la va etre si notre matrix et de la forme : 
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
chaque element apelle dfs sur sont voisin , un element visiter n'est pas revisiter donc en tout il peut avoir un dfs pour chaque element donc on aura en tout O(n*m) appel recursive de dfs en une fois. 
"""

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int: 
        
        if not grid:
            return 0

        count = 0        # comptera le nbr de separated dfs
        for row in range(len(grid)):   # row
            for col in range(len(grid[0])):  #column
                if grid[row][col] == '1':  # que si la case est egale a 1 alors elle active un dfs 
                    self.dfs(grid, row, col)      #remarque: bien que la fct dfs est declarer apres comme c'est une fct de la classe alors elle peut etre declarer apres.
                    count += 1   # a la fin d'un dfs on a une ile en plus 
        return count

    def dfs(self, grid, row, col):
        
        # les 4 premieres condition verifie si on est sortie des limites de la matrix , la 5e condition verifie si la case est egale a 1 .
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] != '1': 
            return             
        
        grid[row][col] = '0'   # on change le node visiter en 0 
        
        # on fait dfs sur les voisin de gauche droite en haut et en bas 
        self.dfs(grid, row+1, col) 
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)
        
        
"""#2nd sol #BFS iterative #TC O(M×N) where M is the number of rows and N is the number of columns # SC O(n*m) 

le code est bien expliquer. voir le code 

TC SC explication : meme explication que la premier sol .

"""

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:         
        
        if not grid :
            return 0

        count = 0        # comptera le nbr de separated dfs
        for row in range(len(grid)):   # row
            for col in range(len(grid[0])):  #column
                if grid[row][col] == '1':  # que si la case est egale a 1 alors elle active un bfs 
                    self.bfs(grid, row, col)      #remarque: bien que la fct bfs est declarer apres comme c'est une fct de la classe alors elle peut etre declarer apres.
                    count += 1   # a la fin d'un bfs on a une ile en plus 
        return count

    def bfs(self, grid, row, col):
        
        queue = collections.deque()
        queue.append((row, col))   # ajouter la cas actuelle ds la queue 
        grid[row][col] = '0'    # mark as visited
        
        while queue:
            
            directions = [(0,1), (0,-1), (-1,0), (1,0)]  # droite, gauche , bas , haut 
            r, c = queue.popleft()   # pop le premier entre dans le queue FIFO , cad maintenant on va verifier les voisin de la case matrix[r][c]
            for dr , dc  in directions:     #chaque element dans direction est composer d'un tuple contenant 2 element 1 pour l'ajout de direction sur les row et un ajout de direction sur les columns
                nr, nc = r + dr, c + dc     # la nouvelle direction des row/column nr/nc est egale a l'ancienne direction r/c plus l'ajout de direction de row/column             
                if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and grid[nr][nc] == '1':  # on verifie que nc et nr sont bien ds les limites de la matrix et que la case contient un 1 
                    queue.append((nr, nc))  # si toute les condition sont respecter alors on doit ajouter le voisin a la queue 
                    grid[nr][nc] = '0'      # une fois que le voisin est ajouter on peut le marquer comme visited (on s'occupera de lui plus tard quand on va pop de la queue)
 
