"""j'ai reussi a repondre a cette question avec toute les solutions dp possibles apres avoir fait cette question : 
https://leetcode.com/problems/longest-common-subsequence/submissions/"""


""" # sol1   # ma sol (j'ai reussi a la faire en 5 min !!!)  # dfs(aussi appeler brute force recursion)   # TC O(2^(n+m))   # SC O(n+m)

on commence a la case [0][0] et on a deux choix possibles a chaque fois aller a droite ou aller a gauche. Que si on arrive a destination cad a [m-1][n-1] alors on return 1 
et on remonte la recursion , si on depasse les borders de la grid alors on return 0 pour arrete la recursion .
le calcule se fait en remontant de la recursion ou on additionne les valeurs des choix (il ya deux choix possible a chaque fois comme on a vu,chaque choix nous retourne le nombre de 
chemin que le robot peut prendre pour arriver a destination en partant de la case ou le choix est fait )

VOIR ARBRE DE RECURSION GITHUB

TC analyse :
la hauteur de l'arbre est O(n+m) (voir SC analyse) et l'arbre de recursion est un arbre binaire car a chaque fois on a deux choix possibles donc TC egale O(2^(n+m)).

SC analyse : 
on peut aller a droite ou en bas a chaque fois donc la deepest recursion qu'on peut avoir (car on ne peut aller a gauche ou en haut) c'est si on va a droite jusqu'au bout (cout O(n)) puis 
en bas jusqu'au bout (cout O(m)) (ou en bas jusqu'au bout puis a droite jusqu'au bout ca revient au meme) c'est a dire en tout O(n+m) , donc la hauteur de l'arbre est O(n+m). 

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(row,col) : # nous donne le nombre d'unique path que le robot peut prendre a partir de matrix[row][col] pour arriver a destination
            
            if row>m-1 or col>n-1: # si on sort du grid
                return 0 
            
            if row==m-1 and col==n-1:  # si on arrive a destination
                return 1
            
            return dfs(row+1,col)+dfs(row,col+1)
        
        return dfs(0,0)

"""# sol2 # ma sol  # dp top-down/memoization (recursive)  # TC O(n*m)  # SC  O(n*m) 

utilisation d'un cache pour garder les resultats deja calculer.

TC et SC analyse : 
la fonction recoit deux parametre il existe m possible valeur pour le premier parametre et n possible valeur pour le deuxieme parametre donc en tout il y'a n*m paire de parametres 
possible cad il ya n*m combinaisons . Donc on va avoir un TC egale O(n*m) car on a n*m subproblems et chaque subproblem coute O(1) (car la chaque recursion coute O(1)) . le cache va etre
de taille O(n*m) car on doit cache les n*m subproblems pour ne pas avoir a les recalculer.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {}
        
        def dfs(row,col) : 
            
            #cache lookup
            if (row,col) in cache :       #O(1)
                return cache[(row,col)]
            
            if row>m-1 or col>n-1:
                return 0 
            
            if row==m-1 and col==n-1:
                return 1
            
            res = dfs(row+1,col)+dfs(row,col+1)
            cache[(row,col)]=res    # caching result
            return res 
        
        return dfs(0,0)




"""#sol2 bis #using lru_cache()"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def dfs(row,col) : 
            
            if row>m-1 or col>n-1:
                return 0 
            if row==m-1 and col==n-1:
                return 1
            return dfs(row+1,col)+dfs(row,col+1)
        
        return dfs(0,0)


""" # sol3 # ma sol (resolue en 5 min!!!)  # dp bottom-up/tabulation (iterative) # TC O(n*m) # SC O(n*m) du au tableau 

la fonction recoit deux parametre donc on va utiliser un tableau 2D pour la tabulation , en tout il ya n*m subproblems (car le premier parametre a n valeur possible et le deuxieme
a m valeur possible donc en tout n*m combinaisons/subproblems) donc le tableau sera de cette taille. On commence l'iteration par les plus petit subproblems (base case) , on store l'info et ainsi 
on pourra calculer les larger subproblemes qui dependent des smallest subproblems . 

Quand on fait un bottom-up il faut essayer de faire l'inverse de la recursion dfs top-down, car ca permet de faire la 'traduction' de facon intuitive car le calcule de la recursion se fait 
en remontant c'est donc cette partie qu'il faut 'traduire' en bottom-up :
La recursion top-down descend la recursion jusqu'au base case et puis la elle arrete les appel recursive et c'est en remontant qu'elle fait les calcules , donc au finale le calcule se fait
en partant du base case et en remontant vers le cas generale. Ici le base case c'est quand on sort du grid (row>m-1 or col>n-1) dans ce cas la valeur sera 0 ou qd on arrive a destination
(row==m-1 and col==n-1) dans ce cas la valeur sera 1, et le cas generale c'est quand on ce trouve au debut du grid.
Donc dans le bottom-up on va commencer par le cas "le plus" de base c'est le cas ou row>m-1 and col>n-1 (j'ai pas choisi le cas row==m-1 and col==n-1 car il est plus dedans dans le tableau
alors que row>m-1 and col>n-1 c'est quand row==m and col==n donc c'est encore plus a l'extremite), puisque le tableau dp est de la forme suivante : 

                                       0   1   2         m              
                                      -------------     -----                  
                                   0  |   |   |   | ... |   |                       
                                      -------------     -----                                
                                   1  |   |   |   | ... |   |               
                                      -------------     -----             
                                        .   .   .    .    .                                                                           
                                        .   .   .    .    .                                
                                      -------------     -----                                                     
                                   n  |   |   |   | ... | X |                                   
                                      -------------     -----       
                                      
C'est pour cela qu'on va commencer l'iteration de notre tableau par la case en bas a droite (ou il ya le X) qui est la case qui est le cas 'le plus' base case , le cas ou row>m-1 and col>n-1
(cad row==m and col==n).  
On doit parcourir tout les case du tableau car chaque case represente un autre subproblems.

On utilisera un tableau 2D (car 2 parametres) de la facon suivante : les column du tableau represente les colonnes de la matices il auront donc une valeur de 0 a m (inclu , m represente 
le cas ou col>m-1) et les row represente les row de la matices il auront donc une valeur de 0 a n (inclu , n represente le cas ou row>n-1) 

prenons pour exemple : m=2, n=3  alors on aura le tableau suivant :

     0   1   2   3
    -----------------
 0  |   |   |   |   |
    -----------------
 1  |   | X |   |   |
    -----------------
 2  |   |   |   |   |
    -----------------
   
Chaque cellule represente un subproblem , par exemple la cellule avec le X represente dfs(1,1) .

Comme dans la recursion dfs on a vue que dfs(row,col) nous donne le nombre d'unique path que le robot peut prendre a partir de matrix[row][col] pour arriver a destination, de meme dans
le bottom-up : tab[row][col] nous rend le nombre d'unique path que le robot peut prendre a partir de matrix[row][col] pour arriver a destination.

Dans la recursion, si on est pas dans les base case alors on va faire  dfs(row+1,col)+dfs(row,col+1) , donc de meme dans bottom-up dans ce cas (ou ce n'est pas les bases case)
tab[row][col] est egale a tab[row+1][col]+tab[row][col+1] .

Donc comme on a vu, pour calculer tab[row][col] il va nous falloir : tab[row+1][col]+tab[row][col+1] cad pour calculer n'importe qu'elle cellule il nous faudra 
la cellule d'en bas et de droite donc il nous faudra parcourir soit row par row (de droite a gauche car le point de depart et (en bas) a droite) soit col par col (de bas en haut car le
point de depart et en bas (a droite)), dans les deux cas ca repondra a nos besoin (dans cette exercice). nous on va choisir de parcourir col par col.
il nous faut des valeur de depart qui n'ont pas besoin d'etre calculer avec des valeurs precedente (ce sont les bases cases), pour qu'on puisse ensuite utiliser c'est valeur de depart 
pour calculer le reste ( Dans tout les dp tabulation ca marche comme ca il nous faut des valeur de depart pour 'lancer' le calcule ) ce sont les bases case .
les base case vont etre calculer en premier ce qui va nous permettre de calculer le reste , c'est pour cela qu'on commence l'iteration au "plus" base case possible comme on a vue en haut.


app :
m=2, n=3

      0   1   2   3
    -----------------
 0  | 0 | 0 | 0 | 0 |
    -----------------
 1  | 0 | 0 | 0 | 0 |
    -----------------
 2  | 0 | 0 | 0 | 0 |
    -----------------
    
premiere iteration : 

     0   1   2   3
   -----------------
 0 | 0 | 0 | 0 | 0 | 
   -----------------
 1 | 0 | 0 | 0 | 0 |         la case avec le X va etre la premiere iteration a calculer puisque row>m-1 and col>n-1 :  tab[2][3] = 0
   -----------------  
 2 | 0 | 0 | 0 | X | 
   -----------------
     
l'iteration remonte colonne par colonne donc les prochain elements calculer sont : 

    0   1   2   3
   -----------------
 0 | 0 | 0 | 0 | Y |          la case avec le X , puisque col>n-1 :  tab[1][3] = 0
   -----------------
 1 | 0 | 0 | 0 | X |          la case avec le Y , puisque col>n-1 :  tab[0][3] = 0
   -----------------  
 2 | 0 | 0 | Z | 0 |          la case avec le Z , puisque row>m-1 :  tab[2][2] = 0
   -----------------
                                
puis :

      0   1   2   3
    -----------------
 0  | 0 | 0 | 0 | 0 |        la case avec le X , puisque row==m-1 and col==n-1 :  tab[1][2] = 0
    -----------------
 1  | 0 | 0 | X | 0 |
    -----------------
 2  | 0 | 0 | 0 | 0 |
    -----------------

puis :

      0   1   2   3
    -----------------
 0  | 0 | 0 | X | 0 |        la case avec le X , puisque ce n'est pas un base case alors :  tab[0][2] = tab[0+1][2]+tab[0][2+1] = 1+0 = 1
    -----------------
 1  | 0 | 0 | 1 | 0 |
    -----------------
 2  | 0 | 0 | 0 | 0 |
    -----------------

etc ...

a la fin ca donne : 

      0   1   2   3
    -----------------
 0  | 3 | 2 | 1 | 0 |        
    -----------------
 1  | 1 | 1 | 1 | 0 |
    -----------------
 2  | 0 | 0 | 0 | 0 |
    -----------------
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range (n+1)] for _ in range (m+1)]   # tableau avec une column et une row en plus (tout les case vont etre egale a 0)
        
        dp[m-1][n-1]=1    # base case : si on est a la destination alors la valeur est 1
        
        # l'iteration ce fait en remontant les column (d'ou l'ordre des boucle d'abord col ensuite row)
        for col in range (n-1,-1,-1):  
            for row in range (m-1,-1,-1):
                
                if row>m-1 or col>n-1: 
                     dp[row][col] = 0 
                        
                elif row==m-1 and col==n-1:
                     dp[row][col] = 1
                        
                else:   
                    dp[row][col] = dp[row+1][col]+dp[row][col+1]
       
        return dp[0][0]   #car comme on remonte col par col en commencent par le cote droit alors le resultat va se trouver apres avoir tout remonter cad en haut cote gauche

"""#bonus #sol4 #dp tabulation with less memory utilisation #TC O(n*m) #SC O(m)

Comme on a peu le constater chaque case pour etre calculer a besoin de la case a droite et la case en bas donc on a besoin au finale en meme temps que de 2 colonnes (ou que deux row mais
ici comme on a fait l'iteration col par col alors pour que ca soit la meme chose on va prendre deux col (si on fait l'iteration row par row alors on prends 2 row) ):

par exemple pour cette exemple :

      0   1   2   3
    -----------------
 0  | 0 | 0 | 0 | 0 |
    -----------------
 1  | 0 | 0 | 0 | 0 |
    -----------------
 2  | 0 | 0 | 0 | 0 |
    -----------------
    

donc :  (remarque : les 0 et 1 dans les tableau suivant sont les bases case il n'utilise donc pas de valeur precedente pour etre calculer)

                          2   3                                                        1   2                                                        
                        --------                                                     --------                                                                        
                     0  | X | 0 |                                                 0  | S | X |                                                                            
                        ---------                                                    ---------                                                        
il suffit d'avoir :  1  | 1 | 0 |   pour caluler X  . puis il suffit d'avoir :    1  | R | 1 |   pour calculer R,S.     etc..   
                        ---------                                                    ---------                                                       
                     2  | 0 | 0 |                                                 2  | 0 | 0 |                                                                                 
                        ---------                                                    ---------                        

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #two column of m row
        previous = [0]*(m+1)
        current = [0]*(m+1)
        
        # iteration on all the subproblem
        # but store result in only two column
        for col in range (n-1,-1,-1):
            for row in range (m-1,-1,-1):
                
                if row>m-1 or col>n-1: 
                     current[row] = 0   # current est une colonne donc les index sont les row
                        
                elif row==m-1 and col==n-1:
                     current[row] = 1
                        
                else:   
                    # previous[row] ca represente la case a droite 
                    # current[row+1] ca represente la case en bas 
                    current[row] = current[row+1]+previous[row]
                
            # The current column becomes the previous one, and vice versa.
            # il faut que current devient previous car si on fait que previous = current alors quand on va modifier previous ca modifie current 
            # car current est un array donc quand on fait previous = current ,previous pointe su la meme adresse que current, ca ne va pas etre juste une copie.
            # donc comme on a initialiser previous et current comme 2 array diff alors quand on fait le swap elle reste deux array diff 
            previous, current = current, previous
            
        return previous[0]  
    
   
