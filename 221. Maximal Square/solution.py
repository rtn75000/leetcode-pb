"""
j'ai reussi a coder cette question (apres avoir vu l'idee de la solution) avec toute les solutions dp possibles grace a ces solution : 
https://leetcode.com/problems/longest-common-subsequence/submissions/
https://leetcode.com/problems/unique-paths/   (question qui se resoud comme la precedente)
"""



"""
remarque valable pour les dp problem : il faut toujours d'abord trouver la solution recursive puis la memoization puis la tabulation , sinon c'est tres compliquer de faire 
directement la tabulation. 
"""


"""
IDEE GENERALE pour resoudre cette question :

analysons les differente taille des carres :

    - une case contenant un 0 est un carre de area egale 0 (cad il ya pas de carre)
         -----
         | 0 |
         -----  

    - une case contenant un 1 est un carre de cote egale 1 donc de area egale 1 (=1^2)
         -----
         | 1 |
         -----  
    - le carre suivant est un carre de cote egale 2 donc de area egale 4 (=2^2): 
        ---------
        | 1 | 1 | 
        ---------
        | 1 | 1 |
        ---------
      comme on peut le constater le "1" en haut a gauche (la premiere case) a un caree de cote 1 a sa droite, en bas et a sa diagonale .
      
    - le carre suivant est un carre de cote egale 3 donc de area egale 9 (=3^2) : 
        -------------
        | 1 | 1 | 1 |                  
        -------------
        | 1 | 1 | 1 |        
        -------------
        | 1 | 1 | 1 |
        -------------        
      comme on peut le constater le "1" en haut a gauche a un carre de cote 2 a sa droit en bas et a sa diagonale VOIR EXPLICATION GITHUB SCHEMA 1 .  

    - le carre suivant est un carre de cote egale 4 donc de area egale 16 (=4^2): 
        -----------------
        | 1 | 1 | 1 | 1 |
        -----------------
        | 1 | 1 | 1 | 1 |       
        -----------------
        | 1 | 1 | 1 | 1 |
        -----------------
        | 1 | 1 | 1 | 1 |
        -----------------  
      comme on peut le constater le "1" en haut a gauche a un carre de cote 3 a sa droit en bas et a sa diagonale .  
      
    - analysons le carree suivant :
        -------------
        | 1 | 1 | 0 |
        -------------
        | 1 | 1 | 1 |       
        -------------
        | 1 | 1 | 1 |
        -------------    
      comme on peut le constater le "1" en haut a gauche a a sa droite un carre de cote 1 (et pas de cote 2 car on a un zero)  , un carre de cote 2 en bas et un carre de cote 2 a sa diagonale .
      donc le carre qui peut etre former en partant par la premier case est un carre de cote 2 seulement car il est limiter par le carre de cote 1 (qui se trouve a sa droite).
      donc la taille du carre en partant d'une certaine case (qui egale a 1) est egale a 1 (car la case contenant un 1 de laquelle on demarre est un carre de cote 1) plus le min entre le cote du
      carre qui se trouve a sa droite , le cote du carre qui se trouve en bas et le cote du carre qui se trouve en diagonale. 
      
      autre exemple :
      
        -----------------
        | 1 | 1 | 1 | 1 |
        -----------------
        | 1 | 1 | 0 | 1 |       
        -----------------
        | 1 | 1 | 1 | 1 |
        -----------------
        | 0 | 1 | 1 | 1 |
        -----------------  
        
      comme on peut le constater le "1" en haut a gauche a a sa droite un carre de cote 1 (et pas de cote 2 car on a un zero)  , un carre de cote 2 en bas et un carre de cote 1 a sa diagonale .
      donc le carre qui peut etre former en partant par la premier case est 1 + min(1,2,1) cad 1+1 cad 2 cad un carre de cote 2 donc area 4.
      
      autre exemple :
      
        ---------
        | 1 | 0 |      Comme on peut le constater le "1" en haut a gauche a a sa droite un carre de cote 0, un carre de cote 0 en bas et un carre de cote 1 a sa diagonale .   
        ---------      Donc le carre qui peut etre former en partant par la premier case est 1 + min(0,1,0) cad 1+0 cad 1 cad un carre de cote 1 donc area 1.
        | 0 | 1 |
        ---------
      

chaque case egale a '1' peut etre un "depart" d'un carre (cad la case en haut a gauche du carre), donc on doit appliquer la logique qu'on a vu sur toute les case de la matrice.
donc on va traverser la matrice row par row et appliquer cette logique .

au final il faut qu'on return l'area du plus grand , donc cad il faut qu'on trouve le carre avec le plus grand cote puis faire cote*cote , et comme on a vu que chaque case a un carre qui
commence a partir d'elle donc chaque case est potentiellement le debut du plus grand carre donc il faut update le max (si necessaire) a chaque fois qu'on calcule un nouveau carre. 


(remarque : j'ai au debut hesiter et ne suis pas arriver a trouver la solution car meme si j'ai penser a ca j'ai renoncer car il ya enormement de redondance et donc je suis pas aller 
jusqu'au bout de la reflection , donc il faut pas avoir peur de calculer plein de fois la meme chose dans la recursion car apres on poura utiliser la memoization pour ne pas avoir a calculer de 
nouveau ce qui est deja calculer)


"""


""" #sol1 #my code(not my idea) #dfs(recursion brute force) # TC O(m*n*3^(m+n))  # SC O(n+m)

on applique ce qui est decrit dans l'intro de facon recursive ... 
voir code il est tres comprehensible ...


TC analyse :   (n==num of row  et  m==num of col)

pour la hauteur de l'arbre voir SC analyse , a chaque recursion on fait 3 appele recursive donc ca veut dire qu'on a un recursion tree 3-ary, donc TC egale a O(3^(m+n)) pour chaque dfs.
Comme on fait n*m fois le dfs (car on fait dfs en partant de toute les cases) donc ca veut dire que au total TC est egale a O(m*n*3^(m+n))

SC analyse : 

la recursion se deplace dans la matrice soit vers la droite, soit vers le bas , soit en diagonale donc ca veut dire qu'on peut pas revenir en arriere, donc le deepest recurions qu'on peut avoir 
est si on va a droite jusqu'au bout (cout O(m)) puis on descend jusqu'au bout (cout O(n)) ou si on descend jusqu'au bout (cout O(n)) puis on va a droite jusqu'au bout (cout O(m)). 
exemple si on a la matrice suivante : 
        -----------------                                            -----------------           -----------------                 
        |   |   |   |   |                                            | 1 |   |   |   |           | 1 | 2 | 3 | 4 |                         
        -----------------                                            -----------------           -----------------                    
        |   |   |   |   |     alors la deepest recursion est soit    | 2 |   |   |   |   soit    |   |   |   | 5 |   cad en tout n+m ou n+m deplacement/appel recursive.                 
        -----------------                                            -----------------           -----------------                             
        |   |   |   |   |                                            | 3 | 4 | 5 | 6 |           |   |   |   | 6 |                              
        -----------------                                            -----------------           -----------------                             
donc la hauteur de l'arbre de recursion va etre O(n+m) donc la taille de la stack recursion va etre O(n+m)

"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        numOfRow = len(matrix) 
        numOfCol = len(matrix[0]) 
        res = 0  # va conserver le coter le plus grand
        
        #dfs retourne la taille du cote du carre qui demarre a la case matrix[row][col]
        def dfs(row,col) :
            
            if row > numOfRow -1 or col > numOfCol - 1 or matrix[row][col] == '0' :  # si on sort des limite de la matrice ou si la case est egale a 0
                return 0 
            
            # si on arrive a cette ligne de code ca veut dire que la case est egale 1
            # on fait la recursion sur le carre qui demarre de la case a droite , le carre qui demarre de la case en bas et le carre qui demarre de la case a diagonale
            right = dfs(row,col+1)
            down = dfs(row+1,col)
            diag = dfs(row+1,col+1)
            
            # la taille du carre qui demarre a la case matrix[row][col] est egale a :
            # 1 + min(carre qui demarre de la case a droite, carre qui demarre de la case en bas, carre qui demarre de la case a diagonale)
            return 1+min(right,down,diag)
        
        # il faut faire la recursion en partant de chaque case qui egale 1 , car comme expliquer dans l'intro , chaque case qui egale 1 est un nouveau depart de carre.
        # l'iteration se fait row par row (on aurait peu faire col par col (et dans ce cas faire for col ... for row :) ca change pas car on veut juste traverser la matrice 
        # et dans les deux cas ca marche)
        for row in range (numOfRow):
            for col in range(numOfCol):
                if matrix[row][col] == '1':   
                    res=max(res,dfs(row,col))  # res va garder la plus grande valeur retourner par les dfs cad il va etre la taille du plus grand cote des carre de la matrice.
                    
        return res**2   #on fait au res^2 car res est la taille du cote et nous on veut l'area
            
"""  # sol2   # my solution(apres avoir vu l'idee de la sol1)   # dp top-down/memoization (recursive)   # TC O(m*n)   # SC O(m*n)

using cache for already calculated cell . 

TC analyse : 

Dfs recoit 2 parametres le premier parametre row peux avoir n valeurs differentes , le deuxieme parametre col peut avoir m valeur differente. Donc en tout il ya n*m combinaison
possibles des parametres donc cad il y'a en tout n*m subproblem different , cad dans le recursive tree on va avoir au max n*m nodes donc TC du dfs egale O(n*m).
Bien que on fait dfs en partant de chaque celle on va caluler en tout dans tout les dfs que une fois chaque case car on aura la reponse dans le cache des case deja calculer donc
en tout on va avoir O(m*n) iterations. 


SC analyse :
 
il ya en tout n*m cellules donc on doit garder au max n*m resultat donc SC = O(n*m) du a la taille du cache (il ya aussi la recursion stack masi dans ce cas elle est neglieable).
Autre facon de trouver le SC (ca marche tjrs) : dfs recoit 2 parametres le premier parametre row peux avoir n valeurs differentes , le deuxieme parametre col peut avoir m valeur differente. 
Donc en tout il ya n*m combinaison possible des parametres donc cad il y'a en tout n*m subproblem different donc le cache sera de taille O(n*m) 

"""          

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        numOfRow = len(matrix) 
        numOfCol = len(matrix[0]) 
        res = 0 
        cache ={}
        
        def dfs(row,col) :
            
            # cache lookup : 
            if (row,matrix) in cache : 
                return cache[(row,matrix)]
            
            if row > numOfRow -1 or col > numOfCol - 1 or matrix[row][col] == '0' :
                return 0 
            
            right = dfs(row,col+1)
            down = dfs(row+1,col)
            diag = dfs(row+1,col+1)
            
            val = 1 + min(right,down,diag)              
            cache[(row,matrix)] = val      # caching the result
            return val
        
        for row in range (numOfRow):
            for col in range(numOfCol):
                if matrix[row][col] == '1':
                    res=max(res,dfs(row,col))
                    
        return res**2
            

""" #sol2 bis  #dp top-down/memoization (recursive) with lru_cache #TC and SC same as above
""" 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        numOfRow = len(matrix) 
        numOfCol = len(matrix[0]) 
        res = 0 
        
        @lru_cache(None)
        def dfs(row,col) :
            
            if row > numOfRow -1 or col > numOfCol - 1 or matrix[row][col] == '0' :
                return 0 
            
            right = dfs(row,col+1)
            down = dfs(row+1,col)
            diag = dfs(row+1,col+1)
        
            return 1 + min(right,down,diag)
        
        
        for row in range (numOfRow):
            for col in range(numOfCol):
                if matrix[row][col] == '1':
                    res=max(res,dfs(row,col))
        return res**2
   
    
""" # sol3 # my solution(apres avoir vu l'idee de la sol1) #dp bottom-up/tabulation(iterative) #TC O(n*m) #SC O(n*m) du au tableau

la fonction recoit deux parametre donc on va utiliser un tableau 2D pour la tabulation , en tout il ya n*m subproblems (car le premier parametre a n valeur possible et le deuxieme
a m valeur possible donc en tout n*m combinaisons/subproblems) donc le tableau sera de cette taille. On commence l'iteration par les plus petit subproblems (base case) , on store l'info et ainsi 
on pourra calculer les larger subproblemes qui dependent des smallest subproblems . 

le bottom-up veut juste dire qu'on utilise un tableau , on peut commencer le calcule par le debut ou la fin ca change rien , mais moi je prefere ici commencer par la fin (dans certain cas 
c'est plus intuitive de commencer par le debut) car si on regarde comment la recursion top-down marche (c'est comme ca tout le temps) : elle descend la recursion jusqu'au 
base case et puis la elle arrete les appel recursive et c'est en remontant qu'elle fait les calcules , donc au finale le calcule se fait en partant du base case (ici le base case 
c'est quand on sort du grid ou qd on arrive a une case avec un 0) et en remontant vers le cas generale (ici le cas le plus generale c'est quand on ce trouve au debut du grid).
Donc dans le bottom-up on va commencer par le cas "le plus" de base c'est le cas ou on se trouve a la case matrix[m-1][n-1] car il ya pas de case dans la matrix  ni a droite ni en bas
ni a la diagonale de cette case (car c'est la case en bas a droite).
On va rajouter une row et une column de 0 qui represente le cas ou on sort du grid , de plus tout le tableau du dp va etre initialiser avec des 0 car au debut on a decouvert aucun carre.

On doit parcourir tout les case du tableau car chaque case represente un autre subproblems. on va parcourir row par row (on peut aussi col par col ca change pas)

prenons pour exemple la matrice suivante : (m=3, n=4)

   -----------------
   | 1 | 0 | 1 | 0 |
   -----------------
   | 1 | 1 | 1 | 1 |
   -----------------
   | 0 | 1 | 1 | 0 |
   -----------------
   
On a vu dans la recursion que dfs(row,col) = 1 + min(dfs(row,col+1), dfs(row+1,col), dfs(row+1,col+1)) , cad que dfs(row,col) utilise la valeur qui lui sera retourne par la case de 
droite , la case de gauche et la case en diagonal, donc dans notre tableau ca revient a dire que la valeur de la case tab[row][col] va etre egale a :
1 + min(tab[row][col+1], tab[row+1][col], tab[row+1][col+1] ) 


app :

    initialisation : 
       -----------------
       | 0 | 0 | 0 | 0 | 0
       -----------------
       | 0 | 0 | 0 | 0 | 0        
       -----------------  
       | 0 | 0 | 0 | 0 | 0
       -----------------
         0   0   0   0   0 

    premiere iteration : 

       -----------------
       | 0 | 0 | 0 | 0 | 0
       -----------------
       | 0 | 0 | 0 | 0 | 0        la case avec le X va etre la premiere iteration a calculer , comme matrix[1][3] == '0' alors on fait rien cad la case reste egale a 0
       -----------------  
       | 0 | 0 | 0 | X | 0
       -----------------
         0   0   0   0   0 

    l'iteration parcours row par row donc le prochaine element calculer est : 

       -----------------
       | 0 | 0 | 0 | 0 | 0
       -----------------
       | 0 | 0 | 0 | 0 | 0        comme matrix[2][3] == '1' alors tab[2][3] va etre egale a 1 + min(tab[2][4],tab[3][3],tab[3][4]) cad 1 + min(0,0,0) cad 1 
       -----------------  
       | 0 | 0 | X | 0 | 0
       -----------------
         0   0   0   0   0 

    puis :

       -----------------
       | 0 | 0 | 0 | 0 | 0
       -----------------
       | 0 | 0 | 0 | 0 | 0        
       -----------------  
       | 0 | 0 | 1 | 0 | 0
       -----------------
         0   0   0   0   0 

    etc ...

    au finale ca donne : 

    matrix :                             tableau dp :

       -----------------                 -----------------                                  
       | 1 | 0 | 1 | 0 |                 | 1 | 0 | 1 | 0 | 0               
       -----------------                 -----------------                               
       | 1 | 1 | 1 | 1 |                 | 1 | 2 | 1 | 1 | 0            cad le max va etre 2 donc la valeur retourner va etre 2*2 cad 4                    
       -----------------                 -----------------                              
       | 0 | 1 | 1 | 0 |                 | 0 | 1 | 1 | 0 | 0                                          
       -----------------                 -----------------
                                           0   0   0   0   0  


""" 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        numOfRow = len(matrix) 
        numOfCol = len(matrix[0]) 
        res = 0 
        dp = [[0 for _ in range(numOfCol+1)] for _ in range(numOfRow+1)]
        for row in range (numOfRow-1,-1,-1):   
            for col in range(numOfCol-1,-1,-1):
                if matrix[row][col] == '1':
                    dp[row][col] = 1 + min (dp[row][col+1],dp[row+1][col],dp[row+1][col+1])
                    res = max(res,dp[row][col])
        return res**2
    
# remarque: on peut inverser le for expliquer ... 

""" 
# sol4 # my solution(apres avoir vu l'idee de la sol1) #dp bottom-up/tabulation(iterative) with space optimization #TC O(n*m) # SC(m)

Comme on a peu le constater chaque case pour etre calculer a besoin de la case a droite la case en bas et la case en diagonale donc on a besoin au finale en meme temps que de 2 row (ou que
2 colonnes ca revient au meme) :

par exemple pour l'exemple precedent a la place de garder le tableau suivant :

   -----------------
   | 0 | 0 | 0 | 0 | 0
   -----------------
   | 0 | 0 | 0 | 0 | 0        
   -----------------  
   | 0 | 0 | 0 | 0 | 0
   -----------------
     0   0   0   0   0 
     
il suffit d'avoir :   | Z | W | Y | X | 0     pour calculer X,Y,W,Z  , et il suffit d'avoir  | U | T | S | R | 0   pour calculer R,S,T,U  etc.....
                      -----------------                                                      -----------------      
                        0   0   0   0   0                                                    | Z | W | Y | X | 0                         

(on aurait peu faire la meme chose avec les colonnes)
""" 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        numOfRow = len(matrix) 
        numOfCol = len(matrix[0]) 
        res = 0 
        
        # les deux ranges qu'on a besoin : 
        previous = [0]*(numOfCol+1)
        current = [0]*(numOfCol+1)
        
        for row in range (numOfRow-1,-1,-1):
            for col in range(numOfCol-1,-1,-1):
                
                if matrix[row][col] == '1':
                    # current[col+1] c'est la case a droite , previous[col] c'est la case en bas, previous[col+1] c'est la case en diagonale 
                    current[col] = 1 + min (current[col+1],previous[col],previous[col+1])   
                    res = max(res,current[col])
                    
                # Attention : ici il faut update current avec 0 si matrix[row][col] == '0' car dans la solution precedente par defaut tout les case etait egale a 0
                # mais ici comme on fait un swap et que current devient previous donc current a les case differente de 0.
                else : 
                    current[col] = 0 
                    
            # on swap pour que previous devient current et que current devient previous 
            previous,current=current,previous
            
        return res**2

