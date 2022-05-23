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
        
        def dfs(row,col) : 
            
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
possible cad il ya n*m combinaisons . Donc on va avoir un TC egale O(n*m) car on a n*m subproblems et chaque subproblem coute O(1) (car la chaque recursion coute O(1)) . le cache va etre de taille O(n*m) car on doit cache les n*m subproblems pour ne pas avoir a les recalculer.
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

le bottom-up veut juste dire qu'on utilise un tableau , on peut commencer le calcule par le debut ou la fin ca change rien , mais moi je prefere ici commencer par la fin (dans certain cas 
c'est plus intuitive de commencer par le debut) car si on regarde comment la recursion top-down marche (c'est comme ca tout le temps) : elle descend la recursion jusqu'au 
base case et puis la elle arrete les appel recursive et c'est en remontant qu'elle fait les calcules , donc au finale le calcule se fait en partant du base case (ici le base case 
c'est quand on sort du grid ou qd on arrive a destination) et en remontant vers le cas generale (ici le cas le plus generale c'est quand on ce trouve au debut du grid).
Donc dans le bottom-up on va commencer par le cas "le plus" de base c'est le cas ou on se trouve a la case tab[m-1][n-1] et donc la valeur est 1 (comme dans la recursion)
(de plus on va rajouter une row et une column de 0 qui represente le cas ou on sort du grid) et on va remonter vers le cas generale.
A chaque fois qu'on fait un dp tabulation on initialise le tableau avec les valeurs des base case , donc ici on initialise tout le tableau en 0 et la case tab[m-1][n-1] aura une valeur 1.
puis on commence l'iteration a la case qui vient apres cad a la case qui est au dessus de tab[m-1][n-1].

On doit parcourir tout les case du tableau car chaque case represente un autre subproblems.

prenons pour exemple : m=3, n=4 :

   -----------------
   |   |   |   |   |
   -----------------
   |   |   |   |   |
   -----------------
   |   |   |   |   |
   -----------------
   
On a vue dans la recursion qu'on fait un double appel recursif dfs(row+1,col)+dfs(row,col+1) , de plus le calcule se fait en remontant donc dfs(row,col) va etre egale a la valeur retourner par
dfs(row+1,col) plus la valeur retourner par dfs(row,col+1) donc dans notre tableau ca veut dire que la valeur de la case tab[row][col] va etre egale a tab[row+1][col] + tab[row][col+1] 
cad la case d'en bas plus la case a droite 

exemple :

initialisation : 
   -----------------
   | 0 | 0 | 0 | 0 | 0
   -----------------
   | 0 | 0 | 0 | 0 | 0        
   -----------------  
   | 0 | 0 | 0 | 1 | 0
   -----------------
     0   0   0   0   0 

premiere iteration : 

   -----------------
   | 0 | 0 | 0 | 0 | 0
   -----------------
   | 0 | 0 | 0 | X | 0        la case avec le X va etre la premiere iteration a calculer : tab[1][3] = tab[2][3] + tab[1][4] == 1+0 =1
   -----------------  
   | 0 | 0 | 0 | 1 | 0
   -----------------
     0   0   0   0   0 

l'iteration remonte colonne par colonne donc le prochaine element calculer est : 

   -----------------
   | 0 | 0 | 0 | X | 0
   -----------------
   | 0 | 0 | 0 | 1 | 0        
   -----------------  
   | 0 | 0 | 0 | 1 | 0
   -----------------
     0   0   0   0   0 

puis :

   -----------------
   | 0 | 0 | 0 | 1 | 0
   -----------------
   | 0 | 0 | 0 | 1 | 0        
   -----------------  
   | 0 | 0 | X | 1 | 0
   -----------------
     0   0   0   0   0 

etc ...

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range (n+1)] for _ in range (m+1)]   # tableau avec une column et une row en plus (tout les case vont etre egale a 0)
        
        dp[m-1][n-1]=1    # base case : si on est a la destination alors la valeur est 1
        
        # l'iteration ce fait en remontant les column (d'ou l'ordre des boucle d'abord col ensuite row)
        for col in range (n-1,-1,-1):  
            for row in range (m-1,-1,-1):
                
                # on saute le base case dp[m-1][n-1] pour ne pas le modifier 
                if row == m-1 and col==n-1: 
                    continue
                    
                dp[row][col] = dp[row+1][col]+dp[row][col+1]
       
        return dp[0][0] 
    
"""#bonus #sol4 #dp tabulation with less memory utilisation #TC O(n*m) #SC O(m)

Comme on a peu le constater chaque case pour etre calculer a besoin de la case a droite et la case en bas donc on a besoin au finale en meme temps que de 2 colonnes :

par exemple pour cette exemple :

   -----------------
   | 0 | 0 | 0 | 0 | 0
   -----------------
   | 0 | 0 | 0 | 0 | 0        
   -----------------  
   | 0 | 0 | 0 | 1 | 0
   -----------------
     0   0   0   0   0 

                                                                                                                                            
                        -----                                                     ---------                                                                          
                        | Y | 0                                                   | T | Y |                                                                           
                        -----                                                     ---------                                                          
il suffit d'avoir :     | X | 0     pour caluler X,Y . puis il suffit d'avoir :   | S | X |    pour calculer R,S,T.     etc ...           
                        -----                                                     ---------                                                            
                        | 1 | 0                                                   | R | 1 |                                                                              
                        -----                                                     ---------                                                       
                          0   0                                                     0   0                                                          
                          

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #two column of m row
        previous = [0]*(m+1)
        current = [0]*(m+1)
        
        #base case of destination
        current[m-1]=1
        
        # iteration on all the subproblem
        # but store result in only two column
        for col in range (n-1,-1,-1):
            for row in range (m-1,-1,-1):
                
                if row == m-1 and col==n-1:  #if subproblem is the base cass of destination don't change it, cotinue to next subproblem
                    continue
                    
                # previous[row] ca represente la case a droite 
                # current[row+1] ca represente la case en bas 
                current[row] = previous[row]+current[row+1]
                
            # The current column becomes the previous one, and vice versa.
            # on s'en fou des valeur du nouveau current car ils vont etre modifier donc meme si elles valent maintenant previous (apres le swap) ca nous derenge pas car
            # on ne l'est regarde pas 
            previous, current = current, previous
            
        return previous[0]  
    
    
    
