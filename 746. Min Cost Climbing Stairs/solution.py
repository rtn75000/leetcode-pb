"""voir ma sol dans se pb pour une super intro a dp : https://leetcode.com/problems/climbing-stairs/ """

"""#first sol  # recursion (top-down)  #TLE(time limit exceded) #TC O(2^n) # SC O(n)   n==len(cost)

app:

cost = [10,15,20]  
                       __________
                  ___ | Final step
             ___ | 20   i=len(cost)=3
        ___ | 15  i=2
       | 10  i=1
        i=0

la recusion sera la suivante : on se trouve sur la marche i=0 on a le choix entre monter a la marche i=1 (1 step) ou i=2 (2 steps), donc f(i=0) va etre egale au prix de la marche actuelle cost[i=0] , 
puis on doit choisir entre faire un step ou 2 donc on doit faire un appel recursive sur i+1 cad 1 et i+2 cad 2  et puisqu'on veut payer le moins possible alors on prendra le min entre si on decide de faire 
maintenant un step et si on decide de faire maintenant 2 step donc cad min(f(1),f(2)) ,il ya donc deux appel recursive le premier est f(1) et le second f(2) comme f(1) est la premier recursion alors d'abord
f(1) va a son tour faire ses appele recursive et seulement apres que f(1) est remonter de ses apppels recursives (ca va ns donner le cout minimal en partant de i=1) alors il va y'avoir la recursion f(2)
qui elle va faire ses appels recursive (et en remontant de ses appels alors elle va retourne le minimal si on part de i=2) et donc f(0) a la fin, une fois que f(1) et f(2) sont remonter,  il va choisir 
le min ente f(1) et f(2) cad le min entre faire 1 step ou 2 step .
ccl f(i) = cost[i]+min(f(i+1),f(i+2))  # c'est seulement en remontant qu'on aura le resultat de f(i+1) et f(i+2)  , f(i+1) et la premier recursion donc seulement apres que f(i+1) a fini f(i+2) commence. 


l'arbre de recursion va donc etre le suivant :
                                      0
                                    /   \
                                   1     2
                                  / \   / \
                                 2   3 3   4
                                / \
                               3   4
                               
l'ordre de la recursion va etre comme ca : 

f(0): cost[0]+min(f(1),f(2)) donc en remontant ca donne 10+min(15,20)==25

    f(1): cost[1]+min(f(2),f(3)) donc en remontant ca donne 15+min(20,0)==15
    
        f(2):  cost[2]+min(f(3),f(4))  donc en remontant ca donne 20+min(0,0)==20
        
            f(3): 
                return 0 car 3 >= len(cost)==4  # base case remontage de la recursion
            f(4):
                return 0 car 3 >= len(cost)==4  # base case remontage de la recursion
        
        f(3): 
            return 0 car 3 >= len(cost)==4  # base case remontage de la recursion
                
    f(2):  cost[2]+min(f(3),f(4))  donc en remontant ca donne 20+min(0,0)==20
        
        f(3): 
            return 0 car 3 >= len(cost)==4  # base case remontage de la recursion
        f(4):
            return 0 car 3 >= len(cost)==4  # base case remontage de la recursion
    
    
    
remarque algo : comme on a vu que f(i) nous donne le minimum cost en commenceant par i , dans n'autre exercice on peut commencer soit par i=0 soit par i=1 donc il faut qu'on fasse 2 recursion f(0) et f(1) et que a la fin 
on return la recursion avec le plus petit cout donc on va simplement faire : return min(f(0),f(1)) cad on fait la recursion de f(1) et f(2) et on return la minimal. 


analyse du TC est SC : 

TC : 

f(i) coute en soit O(1) et fait deux appel rec : f(i+1) et f(i+2) , ici on commence par i=0 pour finir a i=n et on fait i+1 ou i+2 donc ca revient au meme que commencer a i=n et finir a i=0 en
fesant i-1 ou i-2 donc on a la relation de recurrence : T(n) = T(n-1) + T(n-2) + c puisque T(n-1)~T(n-2) donc on peut ecrire T(n) = 2T(n-1) + c on a donc TC=O(2^n)  (voir mes fiche)

SC :

O(n) car on fait +1 a chaque fois (ca revient a faire -1 en partant de i=n) donc la hauteur max de l'arbre de recursion est n donc le stack va etre max de taille n (voir mes fiche)
 """ 


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        size_cost = len(cost)  # rappel : cost O(1)!
        
        def rec (i):
            if i >= size_cost :   # cad si l'escalier i est le dernier escalier ou apres le dernier alors on return 0 , pas d'appel recursive car fin de la recursion dans ce cas 
                return 0
            return cost[i] + min(rec(i + 1), rec(i + 2))  
        
        return min(rec(0), rec(1))  #voir remarque en haut , on fait un appel rec en partant de la premiere marche et un en partant de la deuxieme. 
    
"""#1bis solution #recursion avec built-in cache pour eviter de calculer les fct deja calculer #TC et SC meme que memoization donc voir explication TC et SC ds sol 2   # TC SC O(n)"""    

from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        size_cost = len(cost)  # rappel : cost O(1)!
        
        @lru_cache  #va garder les fonctions deja calculer automatiquement dans le caches 
        def rec (i):
            if i >= size_cost :   # cad si l'escalier i est le dernier escalier ou apres le dernier alors on return 0 , pas d'appel recursive car fin de la recursion dans ce cas 
                return 0
            return cost[i] + min(rec(i + 1), rec(i + 2))  
        
        return min(rec(0), rec(1))  #voir remarque en haut , on fait un appel rec en partant de la premiere marche et un en partant de la deuxieme. 
    
"""#sol 2 #DP #memoization (top down)  #TC et SC  O(n)

comme on peut le voir dans l'arbre de recursion on calcul plusieur fois la meme recursion donc on va utiliser un cache (ici un dic) pour garder les recursion deja calculer. 

app:

cost = [10,15,20]  
                       __________
                  ___ | Final step
             ___ | 20   i=len(cost)=3
        ___ | 15  i=2
       | 10  i=1
        i=0

l'arbre de recursion va donc etre le suivant sans cache :

                                      0
                                    /   \
                                   1     2
                                  / \   / \
                                 2   3 3   4
                                / \
                               3   4
                               
l'arbre de recursion avec cache  :

                                      0
                                    /  \
                                   1    2
                                  / \   
                                 2   3 
                                / \
                               3   4
                               
                               
TC et SC :  
  
dans ce pb (comme dans fibonnaci ou climbing stairs) a l'aide du cache on va passer d'un arbre comme ca     /     \     a un arbre comme ca  /\   donc on va avoir un TC de O(n) (voir explication ds 70. Climbing Stairs)
                                                                                                           : : : : :                        /\     
                                                                                                          /  \   /  \                      /\       
                                                                                                         : : : : : : :                    /\           
                                                                                                         /\  /\ /\  /\                   /\            
                                                                                                                            
et un SC de O(n) car la hauteur de l'arbre va etre O(n) . (car a chaque fois on reduit de 1 la recursion , voir explication ds 70. Climbing Stair)

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        size_cost = len(cost)  # rappel : cost O(1)!
        memo = {}
        
        def rec (i):
            
            # condition d'arret
            if i >= size_cost :   # cad si l'escalier i est le dernier escalier ou apres le dernier alors on return 0 , pas d'appel recursive car fin de la recursion dans ce cas 
                return 0
            
            #si pas condition d'arret alors verifier si recursion deja calculer si non faire la recursion et mettre le resultat ds le dic
            if i in memo :  #si la fonction rec(i) a deja etait calculer return le resultat calculer
                return memo[i]         
            # on arrive ici si res(i) n'a pas etait calculer
            memo [i] = cost[i] + min(rec(i + 1), rec(i + 2)) 
            return  memo[i]
        
        return min(rec(0), rec(1))  #voir remarque en haut , on fait un appel rec en partant de la premiere marche et un en partant de la deuxieme. 
    
    
"""#sol 3 #DP #Tabulation(bottom up,iterative)  #TC et SC O(n) voir code 

video explicative : https://www.youtube.com/watch?v=Mji1qxFkONA&ab_channel=TimothyHChang

il faut trouver un moyen de rendre la fonction iterative , ici la logique utiliser est que a partir de i>=2 le prix minimal pour arriver a i est egale au prix de i + min (min cost for i-1 stairs,min cost for i-2 stairs):

app:

cost = [10,15,20,25]  
                            __________
                       ___ | Final step
                  ___ | 25     i=4=len(cost)
             ___ | 20  i=3
        ___ | 15  i=2
         10  i=1
        i=0

initialisation:
    tab=[10,15,0,0] # comme on peut directement commencer soit a i=0 soit a i=1 alors le cout minimal pour arriver a i=0 ou a i=1 est forcement d'y arriver directement sans passer par une autre marche
                    # donc tab[0] qui est le cout minimal pour arriver a i=0 est egale a cost[0] cad 10 
                    # donc tab[1] qui est le cout minimal pour arriver a i=1 est egale a cost[1] cad 15
                    # seulement quand i>=2 il faudra prendre en compte un chemin precedent car on ne peut pas y arriver directement 

boucle:

    premier iteration i=2:
        pour arriver a i=2 soit on passe de i=0 a i=2 (2 steps) soit on passe de i=1 a i=2 (1 step) donc le cout minimal pour arriver a i=2 est le cout de i=2 plus min(tab[2-1],tab[2-2]) : 
        donc tab[2]=cost[2]+min(tab[1],tab[0]) == 20+min(15,10) == 20+10 == 30 (tab[i] est egale au minimal cost pour arriver a l'escalier i)  donc tab=[10,15,30,0]

    deuxieme iteration i=3:
        pour arriver a i=3 soit on passe de i=1 a i=3 (2 steps) soit on passe de i=2 a i=3 (1 step) donc le cout minimal pour arriver a i=3 est le cout de i=3 plus min(tab[3-1],tab[3-2]) : 
        donc tab[3]=cost[3]+min(tab[2],tab[1]) == 25+min(30,15) == 25+15 == 40 (tab[i] est egale au minimal cost pour arriver a l'escalier i)  donc tab=[10,15,30,40]

fin boucle.

le dernier escalier ( ici i=4 ) n'a pas de prix donc on ne peut pas faire tab[idx_last_stair] = cost[idx_last_stair] + min(tab[idx_last_stair-1],tab[idx_last_stair-1]) ( ici cost[4]+min(tab[3],tab[2]) ) car  
cost[idx_last_stair] n'existe pas, donc on termine la boucle a i=idx_last_stair-1 (ici i=4-1 donc derniere iteration i=3) donc a la fin de l'iteration on aura dans tab le cost minimal pour arriver a tout les escalier 
entre 0 et idx_last_stair-1 inclus. donc pour arriver a l'escalier i=idx_last_stair on a le choix de passer par i=idx_last_stair-1 ou par i=idx_last_stair-2 cad le cout minimal pour arriver a
l'escalier i=idx_last_stair est egale a min entre tab[-1] (dernier valeur du tableau qui correspond au cout minimal pour arriver a i=idx_last_stair-1 ) et tab[-2] (avant derniere valeur du tableau qui correspond
au cout minimal pour arriver a i=idx_last_stair-2 ).
donc minimal_cost_idx_last_stair = min (tab[-1],tab[-2]) donc dans notre cas minimal_cost_idx_last_stair=min(40,30) == 30  donc return 30

"""    

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        size = len(cost)  #num of stair including final stair
        tab=[0]*size  #SC O(n)
        tab[0]=cost[0]
        tab[1]=cost[1]
        for i in range (2,size) :  #rappel : size n'est pas inclu      #TC O(n)
            tab[i]=cost[i]+min(tab[i-1],tab[i-2])
        return min(tab[-1],tab[-2])
    
    
"""#4th sol #using logic with dp tabulation #TC O(n) # SC O(1) voir code 

comme on peut le constater on a besoin que deux de valeur pour calculer f(i) : f(i-1) et f(i-2) donc on va garder que deux valeurs precedente a i, qui vont etre remplacer a chaque fois pour le i suivant.

app :

cost = [10,15,20,25]  
                            __________
                       ___ | Final step
                  ___ | 25     i=4=len(cost)
             ___ | 20  i=3
        ___ | 15  i=2
         10  i=1
        i=0

initialisation:
    prev1=10
    prev2=15
    
loop :
    first iteration i=2:
        tmp = cost[2]+min(prev1,prev2) == 20+min(10,15) == 30
        prev1 = prev2 == 15
        prev2 = tmp == 30
    second iteration i=3 : 
        tmp = cost[3]+min(prev1,prev2) == 25+min(15,30) == 40
        prev1 = prev2 == 30
        prev2 = tmp == 40
#fin loop voir sol precedente pour comprendre pq

return min(prev1,prev2) cad min(30,40) donc return 30   
 """

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        size = len(cost)  #num of stair including final stair
        
        prev1=cost[0]  #prev1 va representer 2 idx avant i
        prev2=cost[1]  #prev2 va representer 1 idx avant i 
        
        for i in range (2,size) :          #rappel : size n'est pas inclu     #TC O(n)
            
            tmp=cost[i]+min(prev1,prev2)      
            prev1=prev2    #on fait avancer prev1 , prev1 va devenir le cout minimal pour atteindre i-1
            prev2=tmp      #on fait avancer prev2 , prev2 va devenir le cout minimal pour atteindre i  
            #donc au prochain i prev1 va representer deux idx avant le nouveau i et prev 2 va representer 1 idx avant le nouveau i
            
        return min(prev1,prev2) # comme dans la sol precedente la derniere marche n'a pas de cost[i] donc en sortant de l'iteration on va prendre le min entre la marche qui precede
                                # la dernier marche et l'avant avant dernier marche 
         
