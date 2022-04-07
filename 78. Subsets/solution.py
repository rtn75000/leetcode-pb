"""
INTRODUCTION : 

difference entre PERMUTATION COMBINATION et SUBSET  :

-> PERMUTATION : soit un array de n elements il existe n! permutatiuon, exemple : nums=[1,2,3] alors il existe 3! permutations :  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

-> SUBSETS : soit un array de n elements alors il existe 2^n subset car chaque element peut etre choisi ou non dans le subset , exemple :  nums=[1,2,3] alors il existe 2^3 subsets : 
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]].

-> COMBINATION : la combination est une permutations dont l'ordre n'est pas important cad que AB revient au meme que BA et donc si on a AB on ne veut pas aussi BA .  exemple : 
nums = [1,2,3] alors tout les combination de 2 nombre est : [1,2] , [1,3] et [2,3]  . cas general : quand on choisi r nombre parmit n alors il existe (n!)/(r!(n−r)!) combination , dans 
l'exemple precedent on a choisi deux nombre parmis 3 donc il existe (3!)/(2!(3-2)!) cad 6/(2*1) cad 3 combinations. 

"""

""" # sol 1 # GENERAL BACKTRACKING PATTERN USE #TC et SC O(n*2^n) 

cette soltion n'est pas tres intuitive mais ca utilise le pattern general du backtracking (utiliser dans permutation et combination) donc c'est pour cela que je l'utilise.

VOIR PHOTO EXPLICATIVE GITHUB (photo 1)

l'idee est de selectionner a chaque fois un nombre du decision space qui sera rajouter dans le path , le decision space (cad les choix qu'il nous reste a faire) va etre tout les nombres 
qui viennent apres le nombre selectionner. on fait cela de facon recursive cad on selectionne le premier nombre puis sur ce qui reste on selectionne le premier nombre et ainsi de suite 
puis en remontant de la recursion on va selectionner le 2eme nombre a chaque fois puis le 3eme en remontant de la recursion du 2eme nombre etc...

TC analyses : Il ya en tout O(2^n) subsets comme expliquer dans l'intro , chaque subset et de taille O(n) (cad il est au max n), donc pour un subset il faut O(n) interactions ( Car a chaque
iteration on ajoute 1 nombre au subset donc si il est de taille O(n) il faut O(n) iteration pour le completer. ) et comme il ya en tout O(2^n) subsets ca veut dire que TC egale O(n*2^n).

SC analyses : la hauteur de l'arbre est O(n) (cad stack space O(n)) de plus on garde O(2^n) subset qui sont de taille O(n) donc en tout on a O(n*2^n+n) cad O(n*2^n).


"""

class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, decisionSpace, path, res):
        res.append(path)
        for i in range(len(decisionSpace)):
            self.dfs(decisionSpace[i+1:], path+[decisionSpace[i]], res)
            
""" #sol 1bis #meme sol que 1 mais plus optmal au niveau du space voir permutation I pour comprendre pk c'est plus optimale """           


class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self,  decisionSpace, path, res):
        res.append(path[:])         # on fait une copy de path car apres il sera modifier 
        for i in range(len(decisionSpace)):
            path.append(decisionSpace[i])
            self.dfs(decisionSpace[i+1:], path, res)
            path.pop()              # s'execute en remontant de la recursion
            
"""# sol 2  #backtracking  #TC et SC O(n*2^n)

solution d'ici : https://www.youtube.com/watch?v=REOH22Xwdkk&ab_channel=NeetCode

solution plus intuitive :

on choisi un nombre et a chaque fois on fait 2 possibilites soit on le selectionne soit on le selectionne pas et ainsi de suite avec les autres nombres.

VOIR 2 EME PHOTO GIT HUB SUPER EXPLICATION AVEC ARBRE DE RECURSION .

TC analyse : il existe 2^n subsets pour arriver a chaque subset il faut O(n) iteration (car on doit passer sur les n nombres, qui seront selectionner ou pas ca change pas car de tout les 
facons meme si il sont pas selectionner on fait une iteration sonc en tout pour n'importe qu'elle subset on aura O(n) iteration pour le trouver ) donc en tout on a TC egale a O(n*2^n).
SC analyse : la hauteur de l'arbre est O(n) donc le stack coute SC O(n), de plus ( on peut enlever cette partie du SC car c'est le output mais la pluspart dans ce cas l'on laisser donc 
je l'ecrit qd meme) il ya O(2^n) subset a garder dont la taille max est n cad O(n) donc SC egale O(n) + O(n*2^n) = O(n*2^n)

"""

class Solution:
    
    def subsets(self, nums):
        
            res = []
            self.dfs(nums, 0, [], res)
            return res

    def dfs(self, nums, i, path, res):   # i est l'index du nombre ds nums qu'on selectionne ou pas 
        
            if i >= len(nums):
                    res.append(path[:])
                    return

            # decision to include nums[i]
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)  #recursion on path with nums[i]

            # decision NOT to include nums[i]
            path.pop()   # we pop nums[i]
            self.dfs(nums, i + 1, path, res)   #recursion on path without nums[i]



