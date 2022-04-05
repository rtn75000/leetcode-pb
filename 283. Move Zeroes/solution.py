"""# ma solution #TC O(n) #SC O(1)"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero_idx = -1
        for cur in range(len(nums)):
            if nums[cur] == 0 and first_zero_idx == -1:   #si on trouve le premier 0 de la list 
                first_zero_idx = cur
            elif nums[cur]!= 0 and first_zero_idx != -1:  #si ce n'est pas un 0 est il ya des 0 avant alors on doit swap
                nums[cur],nums[first_zero_idx]=nums[first_zero_idx],nums[cur]
                first_zero_idx += 1 # la place apres l'ancien 0
        
