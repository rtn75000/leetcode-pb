"""
INTRODUCTION AU BACKTRACKING : 

A backtracking algorithm is a problem-solving algorithm that uses a brute force approach for finding the desired output.

The Brute force approach tries out all the possible solutions and chooses the desired solutions.

The term backtracking suggests that if the current solution is not suitable, then backtrack and try other solutions.  

Dfs recursion is used in this approach. (car la recursion se fait sur la profondeur de l'arbre est pas sur la largeur cad l'arbre de recursion va evoluer sur la profondeur d'abord)

This approach is used to solve problems that have multiple solutions. If you want only one optimal solution, you must go for dynamic programming.


Backtracking Algorithm

```
dfs(x) :

    if x is not a solution
        return false       # backtracking (car si on return alors ca veux dire qu'on arrete les appels recursive et on remonte la recursion)
        
    if x is a new solution  
        add to list of solutions
        
    dfs(expand x)         # appel recursive 
    
```
"""

"""  # backtracking (pattern)  # TC O(n*n!)  # SC O(n)  (voir analyse )
ce code est un super patterne pour le backtracking en generale .

VOIR PHOTO GITHUB SUPER EXPLICATION DE COMMENT MARCHE L'ALGO

TC analyse : (voir arbre de recursion photo)
De base on a dans le decision space n choix puis n-1 puis n-2 etc .. cad pour obtenir un seul resultat on doit faire n recursion.En tout il y'aura n! resultat (car pour n element il existe n! 
permutations possibles) donc comme chaque resultat coute n interaction donc TC egale O(n*n!) . 

SC analyse : 
le stack de la recursion va etre O(n) car comme on a vue que l'hauteur de l'arbre est O(n). de plus on a n! permutation a garder dont chaqu'une est O(n), donc cad O(n*n!). 
donc au final SC egale O(n+n*n!) cad O(n*n!).


"""

class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)  # backtracking algo
        return res
    
    def dfs(self, decisionSpace, path, res):
        if not decisionSpace:                      # si le decision space est vide on ajoute le path au res et on remonte la recursion (cad plus d'appel rec)
            res.append(path)                       # que si on a fini la recursion on ajoute au res le path 
            return                                 # backtracking (le return nous permet de remonter la recursion)
        for i in range(len(decisionSpace)):        # on parcours tout les idx de decision space
            # le decision space va inclure tout le decision space sauf le nombre choisi qui sera rajouter au path
            self.dfs(decisionSpace[:i]+decisionSpace[i+1:], path+[decisionSpace[i]], res)  
          
            
"""
remarque :  self.dfs(decisionSpace[:i]+decisionSpace[i+1:], path+[decisionSpace[i]], res)   le '+' creer a chaque fois une nouvelle liste cad on utilise de la memoire en plus ! le premier 
parametre on a pas le choix mais dans le deuxieme on peut faire path.append(decisionSpace[i]) et donc on va travailler sur la meme liste a chaque fois donc quand on a fini la recursion on 
va devoire faire une copy de path car apres path est modifier, donc on gardee une copie avant les modification . apres que la recursion fait return cad quand on remonte la recursion il faut 
retirer un element de path a chaque fois qu'on remonte une recursion on doit retirer le dernier elements ajouter. 

(meme arbre de recursion que le code precedent donc meme TC et SC)

le code va etre le suivant :
"""

class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)  # backtracking algo
        return res
    
    def dfs(self, decisionSpace, path, res):
        if not decisionSpace:                     
            res.append(path[:])                    # shallow copy de path 
            return                                
        for i in range(len(decisionSpace)):        
            path.append(decisionSpace[i])
            self.dfs(decisionSpace[:i]+decisionSpace[i+1:], path , res)  
            path.pop()  # Cette ligne s'execute en remontant de la recursion cad elle va a chaque fois qu'on remonte une recusrion retirer le dernier element ajoute pour pouvoir tester d'autre 
                        # possibilites . 
