"""#sliding windows #TC O(n) #SC O(1)
tres simplement : on utilise un sliding windows , on fait avancer right tant que on est inferieur a target et tant que on est superieur a target on fait avancer left.  des qu'on depasse target on voit cbm d'element 
il ya dans la fentre , on compare avec le min obtenue . on return a la fin le min """

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        windowSum, left, ans = 0, 0, n+1
        for right in range(n):
            windowSum += nums[right]
            while windowSum >= target:
                ans = min(ans, right - left + 1)
                windowSum -= nums[left]
                left += 1
        return ans if ans != n+1 else 0  #si on a pas changer ans(cad ans = n+1) ca veut dire que sum(nums)<target donc on return 0 car on ne peut arriver a target avec nums
