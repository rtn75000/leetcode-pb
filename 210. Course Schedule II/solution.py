"""voir ma sol de course schedule 1 super important : https://leetcode.com/problems/course-schedule/submissions/
ce pb est le meme que 1 mais on nous demande de nous rendre en plus si il ya pas de loop l'ordre des cours qui doit etre pris . en faite ca revient tout simplement a retourner le topological order car le topological
order est un ordre ou u apparait avant v si u->v donc ici aussi on veut que un cours u soit avant un cours v si u depend de v . il existe plusieur possibilite dans le topological order donc c'est pour cela qu'il ya 
plusieur reponse possible (voir explication dans le lien precedent). """
"""#first sol #not my sol #dfs recursive #Topological sort # TC/ SC O (V+E)  #same code as course schedule 1 with few changement (3 lignes de codes) #voit TC et SC explication ds course schedule 1  """

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
 
            # build Adjacency list from Edges list
            adjList  = defaultdict(set)
            for crs, pre in prerequisites: #chaque element de prerequesites est une list de deux element le cours et son cours prerequis
                adjList[crs].add(pre)   # on aura donc un dictio qui represente un graph car la valeurs de la vertex key represente les voisin ds le graph de ce vertex
            
    
            # Each vertex can have 3 different states:
            # state 0   : vertex is not visited. It's a default state.
            # state -1  : vertex qui a son dfs en cours, cad on a pas fini de faire dfs sur ses descendants. 
            # state 1   : vertex qui a fini son dfs
            state = [0] * numCourses   # au debut tout les vertex ne sont pas visiter 
            stack = []  # le stack va contenir l'ordre topologique 
    
    
    
            def dfs(v,stack):
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
                        if dfs(i,stack) :    #dfs est True si il ya un cycle
                            return True  
    
                state[v] = 1      # cette ligne se fait apres qu'on remonte de la recursion seulement si tout les dfs des voisin etait False car sinon on aurait return True avant et donc cette ligne ne s'execute pas 
                                  # car la fct a deja return cad elle a fini avant de lire cette ligne
                stack.append(v)  #on append au stack en remontant de la recursion donc les premier dans le stack vont etre ce de la fin de la recursion cad les cours que les autres depende d'eux 
                return False      
            
            
            
            
            # ces lignes sont de la fct exterieur et non dfs voir indentation 
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if state[v] != 1 : #cad que les node qu'on leur a pas deja fait dfs car ca sert a rien de refaire 
                    if dfs(v,stack):  # si on a un cycle quand on fait dfs(v) alors dfs(v) sera True donc l'algo va return une empty list car il ya pas de reponse possible 
                        return []

            return stack  #si on est arriver ici ca veut dire qu'on a pas detecter de cycle donc notre algo return l'ordre topologique
        
        
"""#solution 2 #not my sol #  topological sort a l'aide de khan algoritme  #BFS iterative #easy
"""



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
 				                 
            return self.topoBFS(numCourses, prerequisites) 
            
    def topoBFS(self, numNodes, prerequisites):
        
            # build Adjacency list from Edges list
            adjList  = defaultdict(set)
            for crs, pre in prerequisites: # chaque element de prerequesites est une list de deux element le cours et son cours prerequis
                adjList[pre].add(crs)   # on aura donc un dictio qui represente un graph car la valeurs de la vertex key represente les voisin ds le graph de ce vertex : pre->crs #inverse d'en haut
    
            # 1. A list stores No. of incoming edges of each vertex
            inDegrees = [0] * numNodes
            for crs, pre in prerequisites: #chaque element de prerequesites est une list de deux element le cours et son cours prerequis
                # crs and pre form a directed edge pre->crs cad il ya un incoming egdes dans pre
                inDegrees[crs] += 1
     
            # 2. a queue of all vertices with no incoming edge at least one such node must exist in a non-empty acyclic graph.
            # vertices in this queue have the same order as the eventual topological sort.
            queue = deque()
            for v in range(numNodes):
                if inDegrees[v] == 0:  #cad il ya pas de incoming edge ds v donc il ya pas de prerequis pour v
                    queue.append(v)
    
            # initialize count of visited vertices
            count = 0
            # an empty list that will contain the final topological order
            topoOrder = []
    
            while queue:
                # pop a vertex from front of queue.
                # depending on the order that vertices are removed from queue,  a different solution is created
                v = queue.popleft()
                # append it to topoOrder
                topoOrder.append(v)
    
                # increase count by 1
                count += 1
    
                # for each descendant of current vertex, reduce its in-degree by 1 car le descendant aura maintenant un incomming edges en moins
                for neighboor in adjList[v]:
                    inDegrees[neighboor] -= 1
                    # if in-degree becomes 0, add it to queue
                    if inDegrees[neighboor] == 0:
                        queue.append(neighboor)
    
            if count != numNodes: # si on a pas tout les vertex dans topoOrder ca veut dire qu'il ya un cycle ( y'a un vertex qui aura le inDegree > 0 donc rentrera pas dans topoOrder ) est donc on return []
                return []  # graph has at least one cycle 
            else:
                return topoOrder
    
        
       



