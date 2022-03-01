"""fibonacci rappel :
F(0)=0 F(1)=1 , F(n)=F(n-2)+F(n-1) pour n>1 
 """

"""#sol1 #recursion #TC O(2^n) #SC(n)

explication du TC : 

h=1     2^0=1                        n
                               /            \
h=2     2^1=2            (n-1)                 (n-2)
                        /     \               /    \
h=3     2^2=4        (n-2)    (n-3)      (n-3)     (n-4)
                    / \        / \       /  \        / \
h=4     2^3=8   (n-3)(n-4) (n-4)(n-5) (n-4)(n-5) (n-5)(n-6)
                                 etc...
h=n-1   2^i       jusqu'a que n-i==1 cad i==n-1  donc dermier etape il ya 2^(n-1) leaf donc cout O(2^n) car chaque recursion coute O(1) et il ya en tout O(nombre de leaf) recursion donc O(2^n)

explication SC :
le SC est du a l'usage du stack , le stack garde les recursion il peut y avoir dans le stack max la hauteur de l'arbre car le stack stock les recursion ouverte il peut avoir au max donc O(n)
"""
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n  #cad rturn 0 ou 1
        return self.fib(n - 1) + self.fib(n - 2)
    
    
"""#sol 2 #recursion Top-Down using Memoization  #TC O(n)  #SC O(n) pour la meme raison qu'en haut
comme on peut le voir dans l'arbre des recursion (voir photo github ou voir sol precedente) on calcule plusieur fois le meme fibonaci donc pour ne pas avoir a calculer plusieur fois on va garder les 
fibonnaci deja calculer.
on va utiliser un dict qui sera comme ca {n:F(n)...} donc pour avoir F(n) on fait dict[n]

explication TC : 
ca va etre ca les recursion :

1                           n
                       /        \    
2                (n-1)           (n-2) (return car deja calculer)
                /    \
3           (n-2)    (n-3) (return car deja calculer) 
           / \  
4     (n-3) (n-4)   
      
      etc...
 
n-1


cad on va avoir un arbre de type  :    /\   il ya en tout n leaf donc O(n)
                                      /\          
                                     /\
                                    /\
""" 

class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.cache:  #si dans le n dans le dic cad on a deja calculer F(n) donc rentre dic[n] cad F(n)
            return self.cache[n]
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]
    
    
"""#sol3 #iterative sol #TC O(n) #SC O(1)"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n  #cad return 0 ou 1
        a, b = 0, 1
        for _ in range(1,n):
            a, b = b, a + b  # a devient b , b devient a+b
        return b
