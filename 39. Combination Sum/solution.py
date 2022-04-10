""" #sol 1 # backtracking # TC O(n^(t/m)) voir analyse   # SC O(t/m) for function call stack , output not taken into consideration
pour comprendre le backtracking voir ma resolution des problemes suivant : 
- Permutation 
- Combination

VOIR PHOTO GITHUB EXPLICATION AVEC ARBRE DE RECURSION

si on prend pour exemple [2,3,6,7] enfaite il faut essayer 2,...,2 avec 3,....,3 avec 6,....,6 avec 7,......,7 ou chacun peut etre present 0 fois ou plus. 

TC analyse : 

Comme on a deja pu le constater le dfs backtracking creer un arbre de recursion n-ary tree (cad chaque node a de 0 a n enfant) (n == len(candidates) ) (le nbr d'enfant est en fct de la boucle for
du node pere) le nombre de node que contient un n-ary tree est donner par la formule suivante : n^treeHeight .
Dans notre cas la taille de l'arbre est egale a t/m ou t est la target et m est la valeur minimal parmis candidates (explication : l'appel de recusion se fait tant qu'on a pas depasser target
donc le max de recursion se fait quand on ajoute a chaque fois le plus petit candidates cad en tout on va rajouter t/m (si par exemple target egale 6 est min=2 alors on va faire au max 6/2 
appel rec au max cad 3 appel rec) ) . 
Donc l'arbre de recursion a n^(t/m) nodes , chaques node est un appel de recursion , or chaque appel coute O(1) donc le TC egale a O(n^(t/m))*O(1) cad TC = O(n^(t/m)).

SC analyse :
 
la taille du fct call stack est egale a la hauteur de l'arbre comme on a vue dans TC analyse la hautur de l'arbre est O(t/m) ou t est la target et m est la valeur minimal parmis candidates . 
on va pas prendre en compte la taille du output (bien qu'on la pris en compte dans les autres backtracking mais cela n'est pas necessaire car le output n'est normalement pas pris en 
consideration dans le SC ) . donc SC egale O(t/m) .

"""

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, decisionSpace, target, path, res):
        if target < 0:    # cad notre combination/path a une sum superieur a path donc ca sert a rien de continuer cette combination/path donc on refait pas d'appel rec , on remonte la recursion.
            return 
        if target == 0:   # cad qu'on a trouver une combination/path qui a pour sum target 
            res.append(path)
            return 
        for i in range(len(decisionSpace)):
            # le decision space inclu le nombre qui vient d'etre selectionner dans le path car il peut etre selectionner plusieur fois 
            # ( C'est pour ca que on fait decisionSpace[i:] et pas decisionSpace[i+1:] )
            self.dfs(decisionSpace[i:], target-decisionSpace[i], path+[decisionSpace[i]], res)
            
            
            
            
""" #sol 1 bis # backtracking #TC et SC meme que sol 1 # juste un peu plus econome sur le SC (car on utilise le meme path a chaque fois et pas une copie)
"""    

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, decisionSpace, target, path, res):
        if target < 0:    
            return 
        if target == 0:   
            res.append(path[:])  #copy de path pour ne pas que les modif d'apres s'applique sur ce path
            return 
        for i in range(len(decisionSpace)):
            path.append(decisionSpace[i])
            self.dfs(decisionSpace[i:], target-decisionSpace[i], path, res)         
            path.pop()
            
