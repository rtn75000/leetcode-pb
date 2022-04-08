""" #sol 1 #backtracking #TC SC O(n*2^n) comme dans subset I (car au pire il ya pas de duplicate cad on devra passer sur tout les possibiliter)

VOIR SUBSET I POUR COMPRENDRE. 

Comme dans subset I jusque ici on a ajouter un sort() et une condition pour ne pas ajouter dans le path un nbr deja ajouter. """

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, decisionSpace , path, res):
        res.append(path)
        for i in range(len(decisionSpace)):
            if i > 0 and decisionSpace[i] == decisionSpace[i-1]: #on veut pas selectionner un numero deja selectionner 
                continue
            self.dfs(decisionSpace[i+1:], path+[decisionSpace[i]], res)
        
""" #sol 1 bis #backtracking #TC SC O(n*2^n)

meme chose que sol 1 juste un peut plus optimal au niveau du SC car on utilise pas path+[decisionSpace[i]] qui fait une copie de l'array a chaque fois mais on utilise le meme path auquel
on ajoute et enleve .
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self,  decisionSpace, path, res):
        res.append(path[:])         # on fait une copy de path car apres il sera modifier 
        for i in range(len(decisionSpace)):
            if i > 0 and decisionSpace[i] == decisionSpace[i-1]: #on veut pas selectionner un numero deja selectionner 
                continue
            path.append(decisionSpace[i])
            self.dfs(decisionSpace[i+1:], path, res)
            path.pop()              # s'execute en remontant de la recursion


