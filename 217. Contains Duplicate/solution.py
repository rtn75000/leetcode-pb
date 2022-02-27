"""#my sol #built-in sort #TC O(nlogn) #SC O(1) in python
on trie est si nums[i]=nums[i+1] cad on a un duplicate et donc on return true"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # len(nums)-1 car len(nums)-1 n'est pas inclu donc le dernier i va etre l'index de l'avant dernier car on fait i+1 dans le if donc pour ne pas depasser le dernier idx on veut 
        # que i soit max l'avant dernier pour que i+1 soit au max le dernier.
        for i in range (len(nums)-1) : 
            if nums[i]==nums[i+1]:
                return True
        return False
"""#my sol #hastable # TC O(n)  # SC O(n)
on a un dict qui va counter le nbr d'apparition de chaque lettre si une lettre apparait plus de deux fois on rend True"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = collections.defaultdict(int) 
        for val in nums : 
            if d[val]==1 : 
                return True   # cad si on a deja rencontre val alors d[val] sera egale a 1 donc return True 
            d[val]+=1     
        return False
