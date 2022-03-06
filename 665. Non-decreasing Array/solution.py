"""#logique,raisonnement #array #TC O(n)  SC O(1)
pour resoudre cette exo il faut analyser tout les options voir photo github : 
cette exo m'a pris enormement de temps il faut analyser tout les possibilite . cette exo ne prepare pas au interview car pas intuitif"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        if n <= 2 :
            return True
        # on arrive ici si on a plus deux troie element dans nums
        count=0 
        for i in range(2,len(nums)): 
            if nums[i-2]>nums[i-1]>nums[i] or count>1 : #cad 3 elements decroissant ou 2 elements modifier  # I voir photo github
                return False
            if nums[i-2]<=nums[i-1]<=nums[i]: # si 3 elements croissant  # II  voir photo github
                continue
            if nums[i-2]<=nums[i-1] and nums[i]<nums[i-2]: # III  voir photo github
                count+=1
                nums[i]=nums[i-1]
            elif nums[i-2]>nums[i-1] and  nums[i-2]>nums[i]: # IV  voir photo github
                count+=1
                nums[i-2]=nums[i-1]
            else: # V voir photo github
                count+=1
                nums[i-1]=nums[i-2]
        return True if count<2 else False
