"""
explication de comment calculer le nmbre de structure : 

si on a n nodes de valeurs 1 a n (cad c'est dans l'ordre croissant) alors on peut avoir n roots different pour le binary search tree .
prenons pour exemple n = 5 (cad il ya 5 nodes avec une valeur qui varie de 1 a 5) alors on peut avoir 5 roots differents :

       1                 |            2                  |                3                  |               4               |          5          |
        \                |        /      \               |         /            \            |       /              \        |        /            |
    subTree(2 to 5)      |  subTree(1)  subTree(3 to 5)  |  subTree(1 to 2)  subTree(4 to 5) |  subTree(1 to 3)  subTree(5)  |  subTree(1 to 4)    | 
    
 <=>    

           1               |               2              |                3              |              4               |              5               |
     /          \          |         /          \         |         /            \        |         /          \         |         /         \          |
T.W 0 node   T.W 4 node    |  T.W 1 node    T.W 3 node    |  T.W 2 node     T.W 2 node    |    T.W 3 node    T.W 1 node  |  T.W 4 node     T.W 0 node   |

( T.W == tree with )

chaque root cree donc une structure differente, le nombre de structure qu'un root genere est egale au nombre de structure generer par le subtree de gauche fois le nombre de structure
generer par le subtree de droite (la raison qu'on multiplie est que si j'ai disons 3 structures different a gauche du root et 2 structures differentes a droite alors le nombres
total de structures possible avec ce root est egale a 3*2==6 car chaque stucture de gauche peut aller avec une structure differente de droite (si j'ai [a,b,c] et [d,e] alors je peux
cree 6 groupes de deux lettre different :[ad,ae,bd,be,cd,ce]) )
(chaque root creer forcement des structures differentes car comme on peut le voir dans le schema aucun root a les meme subtree a gauche/a droite qu'un autre root (il ya les meme subtree
mais il ne sont pas placer dans le meme coter donc structure differente)  )

Comme on a peu le constater chaque root creer des structures differentes pour chaque root i on aura le nombre suivant de strucures : 
( number Of structure in left subTree of root i ) * ( number Of structure in right subTree of root i)

donc pour un arbre de n nodes on a n root different donc le nombre de structures total est egale a :
  
  _n_
  \     ( number Of structure in left subTree of root i ) * ( number Of structure in right subTree of root i)
  /__  
  i=1

comme on peut voir dans le deuxieme schema d'en haut :
le nombre de structure dans le subtree a gauche du root i est egale au nombre de structure dans un tree de i-1 nodes.
le nombre de structure dans le subtree a droite du root i est egale au nombre de structure dans un tree de n-(i+1)+1 == n-i nodes (car de i+1 a n il ya n-(i+1)+1 elements).

cad que le nbr total de subtructure d'un arbre de n nodes est egale a  :

            for i in range(1,n+1) :                          # loop de 1 a n inclus (car le root peut etre 1 ou 2 ou .. ou n)
                  res += (numOfStruct(i-1)*numOfStruct(n-i))         # numOfStruct(n) nous donne le nombre de structure pour un arbre de n nodes avec des valeurs qui varient de 1 a n
                  
necessiter de la recursion :               
calculons le nombres de structure pour par exemple n=5 : 
numOfStruct(5) =  numOfStruct(0)*numOfStruct(4) + numOfStruct(1)*numOfStruct(3) + numOfStruct(2)*numOfStruct(2) + numOfStruct(3)*numOfStruct(1) + numOfStruct(4)*numOfStruct(0)
donc pour calculer  numOfStruct(5) il nous faut : numOfStruct(4),numOfStruct(3),numOfStruct(2),numOfStruct(1) et numOfStruct(0) 
et pour calculer numOfStruct(4) il nous faut : numOfStruct(3),numOfStruct(2),numOfStruct(1) et numOfStruct(0)
et pour calculer numOfStruct(3) il nous faut : numOfStruct(2),numOfStruct(1) et numOfStruct(0)   
et ainsi de suite d'ou le caractere recursive de la solution.

pour ne pas fausser le calcule comme on utilise numOfStruct(0) dans les multiplication on va definir que numOfStruct(0) = 1 
prenons pour exemple un BST de taille 1 par exemple alors  numOfStruct(1) = numOfStruct(0)*numOfStruct(0) == 1*1 == 1

donc en remontant de la recursion avec seulement numOfStruct(0) = 1 on peut trouver numOfStruct(n) :
numOfStruct(0) = 1
numOfStruct(1) = numOfStruct(0)*numOfStruct(0) == 1*1 == 1
numOfStruct(2) = numOfStruct(0)*numOfStruct(1) + numOfStruct(1)*numOfStruct(0) == 1*1 + 1*1 == 2
numOfStruct(3) = numOfStruct(0)*numOfStruct(2) + numOfStruct(1)*numOfStruct(1) +  numOfStruct(2)*numOfStruct(0)  == 1*2 + 1*1 + 2*1 == 5
etc...
"""



"""
#not my sol # sol 1 # dfs #top-down/memoization #dp #TC sans memoization O(3^n) voir photo git hub (c'est le meme algo comme celui du catalan number )  et avec memoization TC = O(n^2)
#SC O(n) car la recursion a une profondeur O(n) (car n appel n-1 puis n-1 appel n-2 etc...)
(remarque : on parle de dfs car la recursion ce fait dans la profondeur et pas dans la largeur )

pour comprendre l'algo lire l'intro.

VOIR ARBRE DE RECURSION SCHEMA 1 GITHUB , EXPLIQUATION NECESSITER DE LA MEMOIZATION AINSI QUE LE TC ET SC de la memoization.
"""

class Solution:
    def numTrees(self, n: int) -> int:
        
        @lru_cache           #memoization
        def numOfStruct(n):
            
            if n<1 :          # si c'est 0 c'est le base case , on retourn 1 car par defaut quand le subtree est vide on va dire qu'il ya une structure pour ne pas fausser le calcule (voir intro)
                return 1
            
            res=0  #pas besoin d'etre definie en dehors de la fct parcqu'on veut que chaque recursion est sont propre res
            for i in range(1,n+1) :                              # loop de 1 a n inclus (car le root peut etre 1 ou 2 ou .. ou n)
                  res += (numOfStruct(i-1)*numOfStruct(n-i))     # numOfStruct(n) nous donne le nombre de structure pour un arbre de n nodes avec des valeurs qui varient de 1 a n
                    
            return res  #retourne le resultat de numOfStruct(n) cad le nombre de structure pour un arbre de taille n
        
        return numOfStruct(n)
            
        
"""
# sol 2 #not my sol #dp #bottom-up(iterative)/Tabulation #TC O(n^2) voir analyse #SC O(n) pour le tableau utiliser 


comme on a peu le voir pour calculer numOfstruct() a l'aide de la recursion on fait par exemple pour n=5 :
numOfStruct(5) =  numOfStruct(0)*numOfStruct(4) + numOfStruct(1)*numOfStruct(3) + numOfStruct(2)*numOfStruct(2) + numOfStruct(3)*numOfStruct(1) + numOfStruct(4)*numOfStruct(0)
numOfStruct(4) =  numOfStruct(0)*numOfStruct(3) + numOfStruct(1)*numOfStruct(2) + numOfStruct(2)*numOfStruct(1) + numOfStruct(3)*numOfStruct(0)
numOfStruct(3) =  numOfStruct(0)*numOfStruct(2) + numOfStruct(1)*numOfStruct(1) + numOfStruct(2)*numOfStruct(0) 
numOfStruct(2) =  numOfStruct(0)*numOfStruct(1) + numOfStruct(1)*numOfStruct(0) 
numOfStruct(1) =  numOfStruct(0)*numOfStruct(0) 
numOfStruct(0) =  1
puis on remonte de numOfStruct(0) pour calculer numOfStruct(5)

donc avec un tableau qui va garder les resultat on peut directement faire pour calculer par exemple n=4 :

numOfStruct(0) =  1                                                                                        <=> dp[0] = 1 
numOfStruct(1) =  numOfStruct(0)*numOfStruct(0) == 1*1 == 1                                                <=> dp[1] = dp[0]*dp[0] == 1*1 == 1
numOfStruct(2) =  numOfStruct(0)*numOfStruct(1) + numOfStruct(1)*numOfStruct(0) == 1*1 + 1*1 == 2          <=> dp[2] = dp[0]*dp[1] + dp[1]*dp[0] == 1*1 + 1*1 == 2   
numOfStruct(3) =  NOS(0)*NOS(2) + NOS(1)*NOS(1) + NOS(2)*NOS(0) == 1*2+1*1+2*1 == 5                        <=> dp[3] = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0] == 1*2+1*1+2*1 == 5
numOfStruct(4) =  NOS(0)*NOS(3) + NOS(1)*NOS(2) + NOS(2)*NOS(1) + NOS(3)*NOS(0) == 1*5+1*2+2*1+5*1 == 14   <=> dp[4] = dp[0]*dp[3] + dp[1]*dp[2] + dp[2]*dp[1] + dp[3]*dp[0] = 1*5+1*2+2*1+5*1 = 14

Analyse TC :

    on a une double boucle : 
                              ""  for j in range(1,n+1):            
                                            for i in range(1,j+1):  ""  
                                            
    analisons les iterations :
    j=1 :  i=1 to 1(inclus)                  donc 1 iteration
    j=2 :  i=1 to 2(inclus)                  donc 2 iterations
    j=3 :  i=1 to 3(inclus)                  donc 3 iterations
    j=4 :  i=1 to 4(inclus)                  donc 4 iterations
    j=5 :  i=1 to 5(inclus)                  donc 5 iterations
    ...
    j=n :  i=1 to n(inclus)                  donc n iterations
 
    donc il ya au total 1+2+3+4+5+...+n iterations cad (n(n+1))/2 cad O(n^2) iteration chaque iteration coute O(1) donc TC = O(n^2)*O(1) = O(n^2)    
  

remarque : on ne pourra pas optimiser l'espace en utilisant des variables comme on a vu dans certaine solution car ici pour calculer dp[n] on a besoin de dp[n-1],dp[n-2],...,dp[0] 
           donc on ne peut pas utiliser un nombre fini de variable. 
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)   # dp[i] = numOfStruct(i) cad nous donne le nombre de structure differente si n=i  #on fait n+1 car on commence a 0 et on fini a n donc il nous faut n+1 cases ds le tab
        dp[0] = 1  
        for j in range(1,n+1):           # j c'est le nombre de nodes dans notre arbre  # de 1 a n inclus 
            for i in range(1,j+1):         # i c'est le root # de 1 a j inclus (j est le nbr de node ds notre arbre)    # comme dans la recursion
                dp[j]+=(dp[i-1]*dp[j-i])
        return dp[n]

""" #sol 3 #math #nbr catalan #TC O(n) # SC O(1)
le nombre de structure d'un tel BST de n nodes est egale au n-ieme nombre catalan :

le nombre catalan est defini par la formule suivante : 

         C(n+1) = ((4n+2)/(n+2)) * C(n)     , C(0)=1
        
donc par exemple C(3)  == ((4*3+2)/(3+2)) * C(2) == ((4*3+2)/(3+2)) * (((4*2+2)/(2+2)) * C(1))  == ((4*3+2)/(3+2)) * (((4*2+2)/(2+2)) * (((4*1+2)/(1+2)) * C(0))) == 2,8*2,5*2*1 = 14 
"""
class Solution:
    def numTrees(self, n: int) -> int:
        res = 1
        for i in range(n) : 
            res *= ((4*i+2) / (i+2))
        return int(res)  #pour rendre un nombre entier 
    
    
    
