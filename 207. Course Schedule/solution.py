"""
introduction : 
TOPOLOGICAL SORT (appeler aussi topological order):
 - un topological sort d'un directed graph (graph orienter cad les edges ont un sens) est un ordre des vertex (sommets) tel que pour tout directed edge u->v alors u apparaitera avant v dans cette ordre de vertex. 
 - un topological sort existe seulement si il ya pas de cycle dans le graph car si il y'en a un on ne pourra pas respecter la definition du topological sort car si on a par exemple u->v->u cad un cycle alors
   si on regarde u->v ca veut dire que u doit etre avant v dans l'ordre mais si on regarde v->u alors v doit etre avant u dans l'ordre donc c'est contradictoire on ne peut etablir un ordre topologique. 
 - il peut avoir plusieur topological sort pour un meme graph , ex si on a 1->2->4  alors le topological order peut etre 1234 ou 1324 .
                                                                           |     ^
                                                                           v     |
                                                                           3 -----
 - il ya plusieurs possibilitees d'algo pour faire un topological sort, une des facon et d'utiliser un dfs . ( Dans cette exercice on va utiliser un patern (tavnite) ressemblant mais pour l'algo au complet voir 
   la partie 2 de ce pb : https://leetcode.com/problems/course-schedule-ii/  )

 
DFS dans graph : 

remarque : dans un graph quand on fait dfs on le fait que une fois sur chaque node c'est pour cela qu'on utilise tjrs une list pour savoir si un node a etait visiter ou non (dans un arbre on a pas besoin car
le dfs ne peut retomber sur le meme node).

dfs(v) dans un directed graph nous permet d'atteindre tout les descendants d'un node v cad tout les vertex qui on un path entre le vertex v et eux . 
(si on veut faire le dfs de tout le graph il faut faire dfs sur tout les node non visited car faire un dfs que sur un node va appeler recursivement dfs que sur les nodes qui on un path avec ce node mais pas sur les
autres node donc on doit refaire dfs sur les angles qu'on a pas atteinds avec le dfs precedent c'est por cela qu'on va refaire dfs que sur les non visited )

code DFS pour un node : 

	# A function used by DFS
	def DFSUtil(v, visited):

		# Mark the current node as visited and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices adjacent to this vertex
		for neighbour in self.graph[v]:  
			if neighbour not in visited:  # que les non visited car si on fait dfs sur des visited on va reimprimer des nodes deja visiter 
				self.DFSUtil(neighbour, visited)

	# The function to do DFS traversal. It uses # recursive DFSUtil()
	def DFS(v):

		# Create a set to store visited vertices
		visited = set()  #on utilise un set car chaque node a une valeur unique et le set nous permet de faire search en O(1)

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)



code DFS pour passer sur tout le graph : 

comme dit precedement il faut faire dfs plusieur fois tant que on a pas visiter tout les nodes car un dfs ne traverse pas forcement tout le graph il traverse que ses descendant . 

    #meme chose qu'en haut
	def DFSUtil(self, v, visited):
		# Mark the current node as visited and print it
		visited.add(v)
		print(v,end=" ")

		# recur for all the vertices adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)
	

	def DFS(self):
		# create a set to store visited vertices
		visited = set()
		# call the recursive helper function to print DFS traversal starting from all non visited vertices one by one
		for vertex in self.graph:
			if vertex not in visited:
				self.DFSUtil(vertex, visited)
 
le TC  de ces 2 code est O(V+E)  et le SC et O(V) car on utilise un set pour savoir qui est visited ou non ce set et donc de la taille des vertex.
analyse du TC : dfs visite chaque node au mois une fois donc forcement que ca coute O(V) en plus de cela pour chaque node on verifie tout ses voisin donc O(E) donc en tout on a O(V+E)

EXPLICATION DE NOTRE ALGO DE CE PB :

explication de l'ennoncer : on donne une liste de paires de cours prerequisites = [[a1,b1],..,[ai,bi],...] chaque paires [ai,bi] signifie que le cours bi doit etre pris avant ai. l'exo est de s'avoir si 
prerequesites nous donne un pgrm impossible a faire comme par exemple [[1,0],[0,1]] car pour faire 1 il faut faire 0 mais pour faire 0 il faut 1 ce qui est impossible. donc si il y'a une boucle cela va etre impossible
de faire tout les cours .

l'idee est donc de transformer prerequisites en un directed graph et de detecter s'il ya un cycle ou non . 
pour transformer prerequisites en un directed graph on va simplement creer un edge ai->bi dans notre directed graph pour chaque paires [ai,bi]. pour representer un directed grap on peut utiliser un dictionnaire  
qui aura en tant que key les vertex et en tant que valeur une liste de vertex qui sont voisin au vertex key. 
ex :  1->2->4  alors graph = {1:[2,3] , 2:[4] , 3:[4] , 4:[]}
      |     ^
      v     |
      3 -----
dans ceette exo comme les nodes sont des numeros et on a tout les num de 0 a numsCourses-1 cad que on a un 
      
pour detecter un cycle dans le graph on va faire DFS en partant de chaque vertex non visiter (car si il on deja etait visiter ca voudrait dire qu'on a deja fait un dfs sur eux donc pas besoin de refaire) . on fait un dfs 
car un dfs nous donnera tout les vertex qu'on peut atteindre en partant d'un certain vertex v donc si on lance un dfs d'un vertex v dfs va etre appeler recursivement sur tout les descendants de v donc si on retombe 
sur le meme vertex v dans les appel recursive du dfs ca voudrait dire qu'il existe un path v->...->v cad un cycle . Notre algorithme va utiliser 3 states pour chaque vertex  : 0 veut dire que le vertex n'a pas etait
visiter (cad on a pas fait de dfs sur ce vertex), 1 veut dire que ce vertex a deja fini sont dfs (cad on a fini tout les recursions dfs de ses descendants ), -1 veut dire que le dfs est en cours (cad on est encore dans
la recursion de dfs). Si lors du dfs on rencontre un state==0 alors comme maintenant on va lui faire dfs on change le state en state=-1 , si on rencontre un state == 1 ca veut dire que on a deja fait dfs a ce node 
donc ca sert a rien de refaire on peut directement return sans continuer a appeler dfs sur les descendant de ce node, i on rencontre un state==-1 ca voudrait dire que le dfs retombe sur un node qui a lui meme appeler se 
dfs donc on a un cycle . a la fin du dfs en remontant de la recursion on change le state (0) en 1 car quand on remonte de la recursion ca veut dire qu'on a fini de visiter les descendant et donc on a fini le dfs du
vertex qui a fini la recursion (puisqu'il remonte de cette derniere ). 

dans cette algo on va utiliser deux array un pour la representation du graph et un pour les states des vertex. 

"""
"""#first sol # not my sol #dfs recursive  #topological sort #TC O(V+E) car utilise dfs #SC O(V+E) pour la construction du graph (et encore O(V) pour la list state)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
            
            # build Adjacency list from Edges list
            adjList  = defaultdict(set)
            for crs, pre in prerequisites: #chaque element de prerequesites est une list de deux element le cours et son cours prerequis
                adjList[crs].add(pre)   # on aura donc un dictio qui represente un graph car la valeurs de la vertex key represente les voisin ds le graph de ce vertex
            
    
            # Each vertex can have 3 different states:
            # state 0   : vertex is not visited. It's a default state.
            # state -1  : vertex qui a son dfs en cours, cad on a pas fini de faire dfs sur ses descendants. 
            # state 1   : vertex qui a fini son dfs
            state = [0] * numCourses   # au debut tout les vertex ne sont pas visiter 
    
    
    
    
            def dfs(v):
                #if state[v] == 1:
                    # dans ce cas ca veut dire qu'on a deja fini de faire precedement le dfs de ce vertex donc pas besoin de refaire , on return false ( cad que il ya pas de cycle jusqu'a present ) 
                    # et donc ca veut dire  qu'on ne rappele pas le dfs recursivement pour ses descendant)           
                #    return False
                if state[v] == -1:
                    # ca veut dire que on est en cours du dfs de ce vertex donc comme on retombe sur lui pdt son propre dfs ca veut dire qu'il ya un cycle. 
                    return True 
    
                # on arrive ici si le state du node est ni -1 ni 1 il sera donc 0 ,donc maintenant on marque se node comme etant en cours de son dfs cad -1
                state[v] = -1

            
               # cette boucle est tres importante a comprendre : 
               # on appele recursivement dfs sur tout les voisin de v qui eux meme vont ensuite appeler dfs sur leur voisin et ainsi de suite jusqu'a ce qu'il y'ai plus de voisin. 
               # si il ya plus de voisin alors on ne va pas rentrer dans le for car adjList == [] dans ce cas, et on va donc continuer le code : state[v] = 1  cad v est marquer comme node qui a fini sont dfs
               # puis on return false , donc quand il ya pas de voisin il ya pas d'appel recursive du dfs le dfs retournera false donc si il ya pas de voisin c'est une condition d'arret. 
               # une autre condition d'arret est si un cycle est detecter alors dfs ne s'appel plus recursivement il rend true .
               # apres avoir eu un condition d'arret dfs rend True si c'est un cycle et False si il ya pas de voisin , donc comme dfs est appeler dans la boucle for alors if dfs(i) avec i un node qui enclanche 
               # une condition d'arret alors dfs va rendre true ou false si il rend true du a un cycle alors le dfs qui a appeler dfs i va rendre true ce qui va faire que aussi la dfs d'en haut sera true est ainsi de
               # de suite . mais si on a aucun cercle alors dfs(i) va tjrs etre false donc aucun dfs va etre True donc if dfs(i) dans le for va tjrs etre false donc tout les dfs vont finir le for sans rendre qqch
               # il vont continuer les lignes apres for qui sont state[v]=1 et return False cad il vont tous rendre False et donc en remontant la condition if dfs(i) va tjrs etre false. 
               # app : 0->1->2  pas de cycle
               #
               #                    False : donc if dfs(1)== if False donc rentre pas ds if , on continue car for se termine , donc suite de dfs(0): state[0]=1 et return False cad dfs(0) return False
               #                   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
               # dfs(0) :          |                                                                                                                                                                                   |   
               # state [0] =-1     |                              False: donc if dfs(2)==if False donc rentre pas ds if ,on continue car for terminer donc suite dfs(1): state[1]=1 et return False, donc dfs(1) return False 
               # for i in [1]:     v                                  -------------------------------------------------------------------------------------------------------                  
               #   if dfs(i) cad dfs(1) -->  dfs(1) : state[1]=-1     |                                                                                                     |
               #                                     for i in [2]:    v                                                                                                     |   
               #                                        if dfs(i) cad dfs(2) --> dfs (2) : state [2]=-1                                                                     |                                                 
               #                                                                           for i in [] : #pas de voisin donc pas d'appel de dfs car rentre pas ds for       |
               #                                                                           state[2]=1                                                                       |     
               #                                                                           return False ---------------------------------------------------------------------
               #               
               # app : 0->1->0  avc cycle
               #                                 True : donc if dfs(1)== if True donc rentre ds if donc dfs(0) return True  cad il ya un cycle 
               #                   -----------------------------------------------------------------------------------------------------------
               #                   |                                                                                                         |   
               # state [0] =-1     |                             True : donc if dfs(0)==if True donc rentre ds if et donc dfs(1) va return True 
               # for i in [1]:     v                                  -------------------------------------------------------------------------------------------------------                  
               #   if dfs(i) cad dfs(1) -->  dfs(1) : state[1]=-1     |                                                                                                     |
               #                                     for i in [0]:    v                                                                                                     |   
               #                                        if dfs(i) cad dfs(0) --> dfs (0) : state [0]==-1   donc dfs(0) return True  -----------------------------------------
               #                                                                           
               #  remarque : ca change pas cbm de voisin il ya car apartir du moment ou un voisin return true alors on rentre dans la condition du for et donc on return True on continue pasle for ni les lignes d'apres
               #             donc mem si tous les voisin sont false sauf un qui est true alors le dfs va rendre true et va remonter en haut ce qui va faire que meme celui d'en haut va rentrer ds la condition if du
               # for ce qui va faire qu'il va return True et ainsi de suite jusqu'a que la fct va rendre true jusqu'en haut du retoure de la recursion .
                for i in adjList[v]:  
                    if state[i] != 1 : # on appele recursivement dfs sur tout les voisins de v qu'on leur a pas deja fini leur dfs car si on leur a deja fini leur dfs pas besoin de leur refaire encore une fois dfs 
                        if dfs(i) :    #dfs est True si il ya un cycle
                            return True  
    
                state[v] = 1      # cette ligne se fait apres qu'on remonte de la recursion seulement si tout les dfs des voisin etait False car sinon on aurait return True avant et donc cette ligne ne s'execute pas 
                                  # car la fct a deja return cad elle a fini avant de lire cette ligne
                return False      
            
            
            
            
            # ces lignes sont de la fct exterieur et non dfs voir indentation 
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if state[v] != 1 : #cad que les node qu'on leur a pas deja fait dfs car ca sert a rien de refaire 
                    if dfs(v):  # si on a un cycle quand on fait dfs(v) alors dfs(v) sera True donc l'algo va return false (il va donc forcement quitter le for car il se termine)
                        return False

            return True  #si on est arriver ici ca veut dire qu'on a pas detecter de cycle donc notre algo return true .
        
        
