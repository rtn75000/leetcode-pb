"""#binary search #TC O(logn) #SC O(1)
code et explication d'ici : https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/1587293/Python-3-Simple-Approaches-with-Explanation

nums = [ 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8 ]
         ^     ^     ^     ^  ^     ^     ^     ^
index:   0     2     4     6  7     9     11    13
comme on peut le constatater l'index du premier element de la paire est paire avant qu'on rencontre l'element qui n'a pas de paire, apres l'index du premier element de chaque paire est impaire.
donc on utilisera cette logique avec un binary search . on prend a chaque fois le milieu si il a une paire qui sera avant ou apres lui alors on recommence mais si il a pas de paire alors on a trouver l'element unique. 
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo+(hi-lo)//2 
            if nums[mid] == nums[mid-1]:  # duplicate found , ici mid est le deuxieme element des duplicate
                if mid%2:       # si mid est impaire et son duplicate est a l'idx en dessous cad que le premier duplicate a un idx paire donc ca veut dire que l'element unique se trouve a droite
                    lo = mid+1  #  l'element unique se trouve dans la partie de droite
                else:           # si mid est paire et son duplicate est a l'idx en dessous cad que le premier duplicate a un idx impaire donc ca veut dire que l'element unique se trouve a gauche
                    hi = mid-2  # on saute aussi mid-1 qui est le duplicate
            elif nums[mid] == nums[mid+1]:  # duplicate found in the example the first mid will be 7 so we will enter this case , ici mid est le premier element des duplicate
                if mid%2:       #  si mid est impaire ca veut dire que le premiere element est impaire car c'est mid le premier element donc l'element unique est a gauche
                    hi = mid-1  
                else:           # si mid estpaire alors l'element est a droite 
                    lo = mid+2   
            else:  # no duplicate found, target == mid
                return nums[mid]
        return nums[lo] # dans le cas ou il nous reste que un element (on aurait peu mettre hi c la mm chose)
