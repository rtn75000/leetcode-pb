""" # array #TC O(n) #SC O(1)
on nous demamnde de rendre le distinct maximum voir exemple 3 de la consigne pour comprendre .
l'idee est d'utiliser 3 variables une qui va contenir le max une le deuxieme max et une le 3eme max"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first=second=third=float('-inf')  
        n=len(nums)
        for i in range (0,n):  
                if nums[i]>first: # si on trouve un nouveau max on change first et on met first dans second et second dans third 
                    third= second 
                    second=first
                    first = nums[i]
                elif nums[i]!=first and nums[i]>second:  # chaque max doit etre distinct de l'autre max d'ou la premier condition
                    third= second 
                    second= nums[i]
                elif nums[i]!=first and nums[i]!=second and nums[i]>third: # chaque max doit etre distinct de l'autre max d'ou la premier et deuxieme condition
                    third=nums[i]
        if third == float('-inf') :   # cad si third n'a pas ete change donc il ya pas de third max on rend donc first max       
            return first
        return third
    
    
"""meme chose en plus court """

class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:   # car on veut des valeurs distincte
                if num > v[0]:   v = [num, v[0], v[1]]
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]
