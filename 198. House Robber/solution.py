
"""#sol 1 #mon idee #dfs #dp #Top-down/memoization   # TC O(n) voir 2eme schema github # SC O(n) car le stack de recursion coute O(n) puis garder les valeurs calculees coute O(n) 
j'ai fait une super video ou j'explique pq le greedy ne marche pas et j'ai expliquer comment marche la recursion : https://youtu.be/Y8WCs1wrv1s 
VOIR AUSSI GIT HUB SCHEMA 1 ET 2 : ARBRE DE RECURSION et PQ IL FAUT MEMOIZATION
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache
        
        def dfs(idx):
            
            if idx >= len(nums):  # car si on depasse alors ca a aucune valeur donc on return 0
                return 0
        
            return nums[idx] + max(dfs(idx+2), dfs(idx+3)) # la valeur de la maison i plus le max entre le chemin qui passe par la maison i+2 et le chemin qui passe par la maison i+3 
            
        return max(dfs(0),dfs(1))  # on doit faire le dfs des 2 premieres maison 

"""#sol1 bis # memoization sans lru_cache # same TC and SC 
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {} 
        
        def dfs(idx):
            
            if idx in memo :
                return memo[idx]
            
            if idx >= len(nums):
                return 0
            res = nums[idx] + max(dfs(idx+2), dfs(idx+3)) 
            memo[idx] = res 
            return res           
        return max(dfs(0),dfs(1))

""" #sol2 #dp #bottom-up(iterative)/Tabulation #TC O(n) #SC O(n) car on utilise un tableau de taille n

remarque super importante (10 may 2022) : 
Le dynamic programming bottom-up aussi appeler tabulation est l'utilisation d'un tableau qui permet de garder les resultat precedement calculer , et le code doit etre iterative. 
Il ne doit pas forcement etre l'inverse de la recursion, les deux condition indispensable c'est : 1) l'utilisation d'un tableau qui garde les calcules , 2) le code doit etre iterative.
Every DP solution has a table that we populate starting with the base case or the simplest of cases for which we already know the answer. 

dans notre cas on peut facilement passer de la solution top-down a bottom-up :
dans le top-down on a vu que le calcule se fait en remontant de la recursion, c'est a dire le calcule ce fait du derniere index vers le premier index .
le calcule est le suivant dfs(i)= nums[i]+max(dfs(idx+2),dfs(idx+3)) , dfs(idx) qui nous donnera donc le meilleur chemin de i a la fin .
donc ici aussi on va calculer en partant du dernier index vers le premier et on va garder le resultat dans le tableau: la case dp[i] nous donnera le meilleur chemin de 
i a la fin. le dernier index est len(nums)-1 il utilise (len(nums)-1)+2 et (len(nums)-1)+3 donc il faudra ajouter au tableau 3 indexes en plus qui vont etre egale a 0, car ils
sont en dehors de la taille de nums donc il ont pas de valeur. 
a la fin on retourne le max entre dp[0] et dp[1] car comme on a vu dp[i] nous donne le meilleur chemin de i a la fin , donc on doit comparer entre le chemin qui part de la premiere
maison et le chemin qui part de la deuxieme maison.
(en conclusion on fait le remontage de la recursion top-down a l'aide du tableau de dp)

app :  nums=[2,1,1,3,4,1,1]

dp[9]=0
dp[8]=0
dp[7]=0
dp[6]=nums[6]+max(dp[8],dp[9])     
dp[5]=nums[5]+max(dp[7],dp[8])     
dp[4]=nums[4]+max(dp[6],dp[7])    
dp[3]=nums[3]+max(dp[5],dp[6])    
dp[2]=nums[2]+max(dp[4],dp[5])    
dp[1]=nums[1]+max(dp[3],dp[4])     
dp[0]=nums[0]+max(dp[2],dp[3])     

le tableau ca donne ca : 

              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   0    |   0   |   0   |    1   |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------                                                
                                                                     ^                 ^        ^
                                                                   dp[6]             dp[8]    dp[9]

              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   0    |   0   |    1   |   1    |    0    |   0    |   0  |
              ---------------------------------------------------------------------------------------                          
                                                             ^                 ^        ^
                                                           dp[5]             dp[7]    dp[8]
                                                                  
              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   0    |   5   |   1   |   1    |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------
                                                    ^                ^        ^
                                                  dp[4]            dp[6]    dp[7]       
   
              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   4    |   5   |   1   |   1    |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------                                                
                                           ^                 ^      ^
                                         dp[3]             dp[5]  dp[6]

              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   6    |   4    |   5   |   1   |   1    |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------                          
                                  ^                 ^        ^
                                dp[2]             dp[4]    dp[5] 

              ---------------------------------------------------------------------------------------
     dp :     |   0   |   6   |   6    |   4    |   5   |   1   |   1    |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------                          
                          ^                ^        ^
                        dp[1]            dp[3]    dp[4] 

              ---------------------------------------------------------------------------------------
     dp :     |   8   |   6   |   6    |   4    |   5   |   1   |   1    |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------                          
                  ^               ^        ^
                dp[0]           dp[2]    dp[3]
                
return max(dp[0],dp[1])   ==>  8 

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
          
        dp = [0]*(len(nums)+3)   # cad le dernier index va etre len(nums)+2 (car comme a 0)
        
        for i in range (len(nums)-1,-1,-1) :
            
            dp[i] = nums[i]+max(dp[i+2],dp[i+3])
            
        return max(dp[0],dp[1])
    
"""  # sol3 #iterative #same as bottom-up approach #TC O(n) #SC O(1)

le bottom-up precedent marche de la facon suivante  :
prenons pour exemple que nums est de taille 7 : nums=[2,1,1,3,4,1,1] donc dp va faire les calcules suivants :
dp[9]=0
dp[8]=0
dp[7]=0
dp[6]=nums[6]+max(dp[8],dp[9])    pour calculer dp[6] on utilise dp[8] et dp[9]  
dp[5]=nums[5]+max(dp[7],dp[8])    pour calculer dp[5] on utilise dp[7] et dp[8]    on a donc fait un 'shift left' de 1 par rapport a en haut  
dp[4]=nums[4]+max(dp[6],dp[7])    pour calculer dp[4] on utilise dp[6] et dp[7]    "                                                       "
dp[3]=nums[3]+max(dp[5],dp[6])    pour calculer dp[3] on utilise dp[5] et dp[6]    "                                                       "
dp[2]=nums[2]+max(dp[4],dp[5])    pour calculer dp[2] on utilise dp[4] et dp[5]    "                                                       "
dp[1]=nums[1]+max(dp[3],dp[4])    pour calculer dp[1] on utilise dp[3] et dp[4]    "                                                       "
dp[0]=nums[0]+max(dp[2],dp[3])    pour calculer dp[0] on utilise dp[2] et dp[3]    "                                                       "

si on regarde le tableau ca donne ca : 

              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   0    |   0   |   0   |    1   |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------                                                
                                                                     ^                 ^        ^
                                                                   dp[6]             dp[8]    dp[9]

              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   0    |   0   |    1   |   1    |    0    |   0    |   0  |
              ---------------------------------------------------------------------------------------                          
                                                             ^                 ^        ^
                                                           dp[5]             dp[7]    dp[8]
                                                                  
              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   0    |   5   |   1   |   1    |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------
                                                    ^                ^        ^
                                                  dp[4]            dp[6]    dp[7]       
   
              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   4    |   5   |   1   |   1    |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------                                                
                                           ^                 ^      ^
                                         dp[3]             dp[5]  dp[6]

              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   6    |   4    |   5   |   1   |   1    |    0    |   0    |   0   |
              ---------------------------------------------------------------------------------------                          
                                  ^                 ^        ^
                                dp[2]             dp[4]    dp[5]
                                                                  
     etc ...                                                               
                                                                   
  donc pour faire le  shift il nous faut 4 valeurs cur qui correspond a dp[i] , one_after correspond a dp[i+1] , two_after correspond a dp[i+2] et three_after correspond a dp[i+3]
  le shift ce fait ainsi :
              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   0    |   0   |   0   |   0    |    1    |   0    |   0   |
              ---------------------------------------------------------------------------------------
                                                                    ^         ^        ^        ^
                                                                   cur   one_after  two_after  three_after  
              ---------------------------------------------------------------------------------------
     dp :     |   0   |   0   |   0    |   0    |   0   |    0   |   1    |    0    |   0    |   0  |
              ---------------------------------------------------------------------------------------           
                                                             ^       ^         ^         ^
                                                            cur   one_after  two_after  three_after 
                                                            
             ( comme on peut voir  three_after = two_after puis two_after = one_after puis one_after = cur puis cur=0 car c'est avant le calcule )  
     etc...      
     
     ccl : ils suffit d'utiliser que 4 valeurs. 
              
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
               
        cur = one_after = two_after = three_after = 0
        
        for i in range (len(nums)-1,-1,-1) :
            
            cur = nums[i] + max(two_after , three_after)
            three_after = two_after 
            two_after = one_after
            one_after = cur
            cur = 0 
            
        return max(one_after , two_after)
    
    
"""remarque de fin : tout les reponses sont baser sur la meme idee que d'une maison i on peut aller a la maison i+2 ou i+3. """
    
