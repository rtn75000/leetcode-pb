"""#my sol #TC O(n+m) #SC O(min(n,m))"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        if len(nums1)<len(nums2) : 
            freq = collections.Counter(nums1)
            for element in nums2 :
                if freq[element] > 0 : 
                    freq[element]-=1
                    res.append(element)
        else :  # if len(nums1) >= len(nums2) : 
            freq = collections.Counter(nums2)
            for element in nums1 :
                if freq[element] > 0 : 
                    freq[element]-=1
                    res.append(element)
        return res
