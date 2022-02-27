"""#ma solution # TC O(n+klogn) #SC O(n)    n=len(nums)  
tout simplement on utilise un max heap.
voir ma solution de ce pb c'est exactement les memes solutions : https://leetcode.com/problems/kth-largest-element-in-an-array/"""

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = [-int(x) for x in nums]
        heapq.heapify(heap)
        for _ in range(k-1) : 
            heapq.heappop(heap)
        return str(-heapq.heappop(heap))
