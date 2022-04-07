""" # backtracking #TC et SC O(n*n!)  comme dans permutations I car si il ya pas de doublons dans notre cas, alors on a le meme arbre de recursion que permutaion I  (si il ya des doublons 
alors on aura des appels recursive en moins )
voir d'abord permutations I : https://leetcode.com/problems/permutations/
A chaque for loop on a un decision space et un path , chaque iteration du meme for choisi un autre nbr qui va etre pris du decision space est mit dans le path 
ex si on a decisionSpace == [1,1,2] alors for va de 0 a 2 :
i=0 : cad on va prendre decisionSpace[0] et le mettre dans le path : decisionSpace == [1,2]  ,  path + [1] 
i=1 : cad on va prendre decisionSpace[1] et le mettre dans le path : decisionSpace == [1,2]  ,  path + [1] 
i=2 : cad on va prendre decisionSpace[2] et le mettre dans le path : decisionSpace == [1,1]  ,  path + [2] 
comme on peut le constater la recursion de i=0 et i=1 va nous donner la meme chose car on a le meme decision space et le meme path donc apres avoir fait la recursion de i=0 si on fait celle 
de i=1 on va recevoir exactement la meme permutation a la fin , or comme on veut 'unique permutations' donc on ne veut pas refaire la meme chose , d'ou la condition dans le code que si 
decisionSpace[i]==decisionSpace[i-1] cad que si le nombre qu'on selectionne egale au nombre precedement selectionner alors ne pas faire de recursion continuer le for loop (remarque:
on est obliger de sort() les elements pour que les duplicates soit les un apres les autres et donc pouvoir verifier si decisionSpace[i]==decisionSpace[i-1] ) .

"""

class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()  # sort afin de garder les doublons les un a coter des autres. 
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #cette condition marche parceque on a fait un sorting au par avant donc si il ya un duplicate ils se trouvent a la suite l'un de l'autre  
                continue # cad continue dans le for sans faire les autres lignes 
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)  # voir explication dans permutation I  
             
