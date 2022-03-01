"""#array #TC O(n) #SC O(1)
voir code tout y es """

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = maxi = 1   #longuest va etre la taille du current continuous increasing subsequence alors que maxi va etre la taille de la plus grande continuous increasing subsequence
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]: #si il ya continuiter 
                longest += 1
                if maxi < longest: #update maxi if needed
                    maxi = longest
            else:  # pas de continuite on remet le count a 1 (1 et pas 0 car on compte nums[i + 1] )
                longest = 1
        return maxi
