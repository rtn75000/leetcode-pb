"""il faut juste trouver un pique dc la solution va etre de chercher le milieu a chaque fois tant que celui ci n'est pas un peak , un peak est obtenue si l'element qui le precede et celui qui le suit sont plus
petit (il peut ne pas y avoir d'element qui precede ou qui suit). si l'element qui le suit est plus grand alors on recherche un nouveau milieu a gauche , si l'element qui le precede est plus grand alors on va a
droite si les deux element a droite et a gauche sont plus grand alors y ira a droite (on peut aller a gauche si on veux ca change pas)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r :
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        
        return l
    
