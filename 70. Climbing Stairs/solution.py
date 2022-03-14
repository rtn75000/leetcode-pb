"""introduction au dynamic programming  :

on utilise le dynamic programming quand 2 conditions sont remplis : 
- overlapping subproblem cad les subproblemes se repete il est facile de voir si les subproblemes se repete en dessinant un arbre de recursion. 
- optimal substructure cad que la solution optimal peut se construire a l'aide des solutions optimales des subproblemes .

donc en deux mots il faut que le pb peut etre resolue de facon recursive et que les subproblemes se repete . 

il ya deux sortes de dynamic programming :

- memoization (Top-down approach cad il commence par tout le pb est le divise en plus petite partie a chaque fois (de n a 1 )) : recursive with cache , on utilise un cache (dic ou lis par exemple) 
pour garder les resultat deja calculer pour ne pas avoir a les recalculer par la suite . 

- tabulation (Bottom-up approach cad il commence par le cas le plus simple pour finir ensuite sur le cas general (de 1 (base state) a n)) :  iterative avec tableau (le tableau peut etre 1D,2D... depends du nombre de 
parametre de la fonction. dans certain cas il nous suffit d'utiliser 2 variables qui stock les 2 resultat des 2 precedente fonction pour calculer le resultat de la fction du dessus ) , le tableau garde les resultats deja
calculer. 

tabulation est plus rapide que memoization car il n'est pas recursive .
"""

"""
SOLUTIONS INTRODUCTION :

comme on peut le constater ce pb est recursive car a chaque escalier on choisi un et/ou deux step donc cette decision doit se faire a chaque fois de facon recursive jusqu'a qu'on atteigne le dernier escalier. 
on va dc commencer par n et finir a 0 a chaque recursion on aura 2 recursion une pour n-1 (1 escalier) et une pour n-2 (deux escalier) . ca va nous donner l'arbre de recursion suivant 

                                                              F(n)
                                               /                                \ 
                                           F(n-1)                             F(n-2)
                                        /           \                   /                  \
                                    F(n-2)         F(n-3)            F(n-3)              F(n-4)
                                   /    \         /     \            /    \              /     \           
                               F(n-3) F(n-4)  F(n-4)  F(n-5)     F(n-4)  F(n-5)      F(n-5)  F(n-6) 
                                     .               .                 .                    .
                                     .               .                 .                    .           
                                     .               .                 .                    .
                                     .               .                 .                    .                                                                                                       
                              F(cdt arret)     F(cdt arret)       F(cdt arret)        F(cdt arret)
                              
dans notre cas comme n est sup egale a 1 alors le base case va etre n==1 et aussi n==2 car si on fait que condition d'arret a  n==1 alors F(2) il appelera recursivement F(1) et F(0)
(cad n==0 or n>=1 , on peut faire F(0) return 0 mais pour des raison de logique vaut mieux que F(2) soit lui une condition d'arret comme ca il ya pas d'appel recursive quand n==2,
le dernier appel recursive va se faire quand n==3 il appelera F(2) et F(1) ) 
F(1) => si il ua un esclier il ya que une option donc return 1 .
F(2) => si il ya 2 escalier il ya 2 options 1+1 ou 2 donc return 2. 
                                    
donc si on prend par exemple n=6 ca donne ca : 

                                                       F(6)
                                               /                  \ 
                                            F(5)                  F(4)
                                        /        \             /        \
                                    F(4)         F(3)        F(3)       F(2)
                                   /    \      /     \      /    \                        
                                 F(3)  F(2)  F(2)   F(1)  F(2)   F(1)       
                                 / \   
                             F(2)  F(1) 
                             
comme on peut le voir il ya plusieurs fois le meme calcul qui est fait (pour plus d'explication voir photo github dans mes solutions.) donc on doit utiliser dp pour optimiser la solution .
sans DP la solution coute O(2^n) (car la relation de recurrence revient a T(n)=2T(n-1)+c donc d'apres le master theorem for decreasing function(voir mes fiches) a=2 b=1 f(n)=O(c*n^0) donc TC = O(n^0*2^(n/1)) = O(2^n).
on peut aussi arriver a ce resultat en analysant l'abre de recursion comme chaque recursion cout c donc on a c+2c+4c+8c+...+(2^k)c+...+ (2^n-1)c cad c*(1+2+4+8+...+(2^n-1)) = O(c*((2^n)-1)) = O(2^n) (voir mes fiches 
tout y est expliquer je fait aussi les fiches dans github)

dp solutions :

I) Memoizations 

on va faire une recursion normale sauf que on utlisera un dictionnaire qui va garder les recursion deja calculer .
pour comprendre le TC prenons pour exemple n==6 , la recursion avec memoization va donner ca : (la recursion est de la sorte F(n) appel F(n-1) et F(n-2) donc ce qui va etre ouvert en premier ca va etre F(n-1) qui 
lui va appeler f(n-2) et f(n-3) et ainsi de suite voir github ordre d'ouverture de la recursion )

                                            recursion :              cost per level : 
                                         
                                               F(6)                        C
                                             /     \ 
                                          F(5)     F(4)                   2*C
                                        /    \          
                                    F(4)     F(3)                         2*C
                                   /    \                           
                                 F(3)  F(2)                               2*C
                                 / \   
                             F(2)  F(1)                                   2*C

donc on voit que le cout total est egal a O(height*2*C) cad O(n*2*C) cad O(n)   [rappel C est une constante] [la taille de l'arbre est egale a n car a chaque fois on reduit de 1 donc il y'aura en tout n level]

le space complexity est O(n) car on doit garder F(1) F(2) F(3)....F(n) dans un dict . (il ya aussi O(n) pour la recursion comme il peut avoir au max n recursion ouverte en meme temps (le max de recursions ouverte
en meme temps est donner par la hauteur de l'arbre) donc le stack de la recursion esst de taille O(n) au max)

II) Tabulation : 

on va resoudre de facon iterative en commancant par le base case est en remontant vers le cas generale . voir la 3eme solution pour comprendre. 

"""


"""#1er sol # regular recursion #TLE(time limit exceeded) #TC O(2^n) #SC O(n)  pour la recursion comme il peut avoir au max n recursion ouverte en meme temps (le max de recursions ouverte
en meme temps est donner par la hauteur de l'arbre) donc le stack de la recursion est de taille O(n) au max)
voir explication en haut .

app n==4 :

CS(4) :  #equal 3+2==5                                        4
    CS(3):  #equal 2+1==3                                   /   \
        CS(2):                                             3     2
            return 2                                      / \
        CS(1):                                           2   1
            return 1
    CS(2):  
        return 2 
        
le last return egale a 5 donc la reponse est 5 possibilites 
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    
"""#1bis # regular recursion using special decorator #not TLE  #utilise un dic pour cache les resultat donc TC et SC comme la 2nd sol cad O(n) voir explication la bas"""

from functools import lru_cache

class Solution:
    
    @lru_cache   #  lru_cache decorator will automatically cache the computed result, so climbStairs(x) will not be calculated more than once.  
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
"""#2nd sol #DP #memoization (recursive) #TC et SC O(n) voir explication dans solution introduction.

app: n==5 

CS(5):  #equal 5+3==8 , caching CS(4): add {5:8} (cad {n:possibilities})  [7th return,last return]                      F(5)                   
    CS(4): #equal 3+2==5 , caching CS(4): add {4:5} (cad {n:possibilities})  [5th return]                              /    \          
        CS(3): # equal 2+1==3 , caching CS(3): add {3:3} (cad {n:possibilities})  [4th return]                     F(4)   F(3)                        
            CS(2):                                                                                               /    \                           
                return 2  [first return]                                                                        F(3)  F(2)                                
            CS(1):                                                                                              / \   
                return 1  [2nd return]                                                                      F(2)  F(1)      
        CS(2):
            return 2  [3rd return]
    CS(3): # result already in cache so return 3  [6th return]
    
last return is 8 so result is 8    
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo ={1:1, 2:2} #initialisation du dic avec les conditions d'arret  
    
        def climb(n):
            if n in memo: # if the recurssion was already done before , then the result is in the dictio  #search in dic cost O(1)
                return memo[n]
            else:         # if the recursion was not already done store the recursion result in the dictio and return it 
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]
        
        return climb(n)
    
"""#3nd sol #DP # Tabulation (iterative) #TC et SC O(n)
comme on peut le voir dans l'arbre de la solution precedent (de bas en haut)  F(3)=F(2)+F(1) , F(4)=F(3)+F(2) , ... cad F(n)=F(n-1)+F(n-2) donc on doit calculer d'abord F(n-1) et F(n-2) et ensuite on aura la valeur de 
F(n).

app : n==6 

res=[0,1,2]

1er iteration de for :
res[3]=res[2]+res[1] cad res=[0,1,2,3] 

2e iteration de for :
res[4]=res[3]+res[2] cad res=[0,1,2,3,5] 

3e iteration de for:
res[5]=res[4]+res[3] cad res=[0,1,2,3,5,8] 

4e iteration de for:
res[6]=res[5]+res[4] cad res=[0,1,2,3,5,8,12] 

return res[n] cad res[6] cad 12 
"""
class Solution :
    def climbStairs(self, n: int) -> int:    
        if n==1 or n==2 :
            return n
        res = [0 for i in range(n+1)]   # creation d'un tableau de taille n (rappel : n+1 n'est pas inclus dans range) pour garder les precedents resultats au debut tout les cases sont egale a 0 # SC TC O(n)
        res[1], res[2] = 1, 2           # initialisation des cas de bases 
        for i in range(3, n+1):         # on commence par 3 (car on a deja 1 et 2) puis on monte vers le cas general n
            res[i] = res[i-1] + res[i-2]   
        return res[n]
    
"""#4th sol #using logic #TC O(n) # SC O(1) 
comme on peut le voir dans la solution precedente pour calculer F(n) il nous faut juste F(n-1) et F(n-2) cad on a besoin de garder seulement le resultat des deux valeurs precedentes

app : n==6 

 one_step_before = 2 
 two_steps_before = 1      
 
 1st iteration :
   actual_step = 2 + 1 == 3
   two_steps_before = 2                  
   one_step_before = 3 

2nd iteration :
   actual_step = 2 + 3 == 5
   two_steps_before = 3                 
   one_step_before = 5 
   
 etc ..  
"""

class Solution :
    def climbStairs(self, n: int) -> int:   
        if n==1 or n==2 :
            return n
        
        one_step_before = 2 
        two_steps_before = 1 
        actual_step = 0

        for _ in range(3,n+1):
            actual_step = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = actual_step
        
        return actual_step
