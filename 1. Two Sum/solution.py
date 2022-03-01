"""#ma sol #hashTable #TC SC O (n)
l'idee est de passer a travers nums et a chaque nombre current se poser la question si il exite un nombre b tel que target-current == b . on utilisera un hashtable pour que le search coute O(1) pour trouver
un nombre qui egale a target-current (si on utilise pas de hashtable le search coute n a chaque fois car on doit pour chaque nbr repasser sur tout l'array pour trouver un nombre b tel que target-current == b ,
donc en tout coute O(n^2) ).
on utilisera un hashmap qui a pour key les nombres et pour valeur l'index du nbr dans nums. 

app :  nums = [3,2,3] target=6

premier for :
    dictio = {3:0, 2:1 3:2}

deuxieme for :
    -idx = 0 
        puisqu'il existe un nombre dans le dictio tel qu'il est egale a target-nums[0] cad 6-3==3 et en plus de cela sont idx dans num est different (idx==2) alors on retourne les idx de ces deux nombre 
        return [0,2]


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictio = {} #SC O(n)
        for idx,nbr in enumerate(nums):  #TC O(n)
            dictio[nbr]=idx
        for idx in range(len(nums)):
            if target-nums[idx] in dictio and dictio[target-nums[idx]] != idx : #il faut que l'index du nbr trouver dans le dictio soit differente du nmbre actuel car on ne peut utiliser le meme element deux fois 
                return [idx,dictio[target-nums[idx]]]
