"""INTRODUCTION : 

difference entre PERMUTATION COMBINATION et SUBSET  :

-> SUBSETS : soit un array de n elements alors il existe 2^n subset car chaque element peut etre choisi ou non dans le subset , exemple :  nums=[1,2,3] alors il existe 2^3 subsets : 
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]].

-> PERMUTATION : soit un array de n elements il existe n! permutatiuon, exemple : nums=[1,2,3] alors il existe 3! permutations :  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

-> COMBINATION : la combination est une permutations dont l'ordre n'est pas important cad que AB revient au meme que BA et donc si on a AB on ne veut pas aussi BA .  exemple : 
nums = [1,2,3] alors tout les combination de 2 nombre est : [1,2] , [1,3] et [2,3]  . cas general : quand on choisi r nombre parmit n alors il existe (n!)/(r!(n−r)!) combination , dans 
l'exemple precedent on a choisi deux nombre parmis 3 donc il existe (3!)/(2!(3-2)!) cad 6/(2*1) cad 3 combinations. 


"""

""" # sol1 #backtracking #TC O( k * (n!)/(k!(n−k)!) )  #SC O( k * (n!)/(k!(n−k)!) )

VOIR PHOTO GITHUB SUPER EXPLICATION AVEC ARBRE DE RECURSION . 

TC analyse : chaque combinaison est de taille k donc il nous faut k iteration pour trouver une combinaison comme il existe (n!)/(k!(n−k)!) combination alors ca veut dire que TC egale 
             O( k * (n!)/(k!(n−k)!) )

SC analyse : la hauteur de l'arbre est O(k) donc le stack est O(k) en SC , de plus on a (n!)/(k!(n−k)!) combination de taille k donc il faut O( k * (n!)/(k!(n−k)!) ) pour les stocker
             donc SC est egale a O( k * (n!)/(k!(n−k)!) ) + O(k) cad O( k * (n!)/(k!(n−k)!) )
"""

class Solution:
    def combine(self, n, k):
        res = []
        self.dfs(list(range(1, n+1)), k, [], res)
        return res
    
    def dfs(self, decisionSpace, k, path, res):
        if len(path) == k:
            res.append(path)
            return 
        for i in range(len(decisionSpace)):
            self.dfs(decisionSpace[i+1:], k, path+[decisionSpace[i]], res)
            
            
            
""" # sol1 bis #backtracking #TC SC meme chose que sol1
 
un peu plus econome au niveau du SC car n'utilise pas ' path+[decisionSpace[i]] ' dans la recursion


"""

class Solution:
    def combine(self, n, k):
        res = []
        self.dfs(list(range(1, n+1)), k, [], res)
        return res
    
    def dfs(self, decisionSpace, k, path, res):
        if len(path) == k:
            res.append(path[:])
            return 
        for i in range(len(decisionSpace)):
            path.append(decisionSpace[i])
            self.dfs(decisionSpace[i+1:], k, path, res)
            path.pop()
