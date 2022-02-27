"""ma solution est comme la majorite des solution proposer elle consiste a tout simplement faire 2 fois le binary search un pour trouver la limite inferieur et un pour trouver la limite superieure cad pour trouver 
la limite inferieur si nums[mid]==target alors on va coter gauche mais pour trouver la limite superieur si nums[mid]==target alors on va coter droit"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result = [-1, -1] 
        
        result[0] = self.findStartingIndex(nums, target)
        result[1] = self.findEndingIndex(nums, target)  
        
        return result 
		

    def findStartingIndex(self, nums, target):
        index = -1 
        low, high = 0, len(nums) -1  
        while low <= high: 
            mid = low + (high - low)//2 
            if nums[mid] == target: 
                index = mid 
                high = mid - 1 
            elif nums[mid] > target:  
                high = mid - 1 
            else:   
                low = mid + 1        
        return index

    def findEndingIndex(self, nums, target):
        index = -1
        low, high = 0, len(nums) -1        
        while low <= high :     
            mid = low + (high - low)//2 
            if nums[mid] == target:
                index = mid
                low = mid + 1 
            elif nums[mid] > target: 
                high = mid - 1
            else:
                 low = mid + 1     
        return index
        
        

"""il ya une autre solution d'utiliser un binary search normal que si on trouve ca rend la premiere apparition et si on trouve pas l'element alors on rend la place ou il est cense etre et donc l'idee c'est de le faire 2 fois une fois pour target et une fois pour target+1 car meme si target+1 n'existe pas ca va nous donner la place ou il devrait etre cad une place apres la dernier apparition de target donc a c'ette idx on fait -1 ce qui nous donne la'idx de la dernier apparition de target
code d'ici: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/1054742/Python-O(logn)
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo #meme si on trouve pas ca retourne l'idx ou l'element aurait du etre
        
        lo = search(target)
        hi = search(target+1)-1  
        
        # si target n'est pas la alors lo va nous donne la place ou il est cense etre . dans ce cas search(target+1) va nous donne la meme place que search(target) donc quand on va faire
        # search(target+1)-1 ca va nous donner un idx inferieur a search(target) donc lo>hi ,ce cas de figure est possible que si target n'existe pas, et donc dans ce cas on retourne [-1,-1].
       
        return [lo, hi] if lo <= hi else [-1, -1]
     
