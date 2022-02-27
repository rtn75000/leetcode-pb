"""premier solution : #ma solution #built-in sort #TC O(nlogn) #SC O(1) in python  #n==len(nums)
cette solution est tres simple on trie simplement l'array dans l'ordre decroissant puis on return la valeur de l'idx k ."""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)   # nlogn
        return nums[k-1]  #k-1 car commence a 0 
    
"""2e solution : #ma solution #priority queue #maxheap #TC O(n+klogn)  #SC O(1)
on utilise un max heap on fait pop k fois et on return le dernier pop"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #on veut max heap donc comme python a que min heap on transforme les valeur en negatif comme ca ca nous donne un max heap
        for i,val in enumerate(nums): #O(n)
            nums[i]=-val 
        heapify(nums)  # O(n)
        for _ in range(k-1) : #commence a 0 jusqu'a k-2 inclu donc k-1 iterations en tout
            heapq.heappop(nums)
        return -heapq.heappop(nums)

    

    
"""#not my sol #quick-select #TC average O(n) worst-case O(n^2) #SC O(n)

solution d'ici : https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained

We are going to discuss Quick Select: 

-First, we need to choose so-called pivot and partition element of nums into 3 parts: elements, smaller than pivot, equal to pivot and bigger than pivot. (sometimes two groups enough: less and 
more or equal).
-Next step is to see how many elements we have in each group: if k <= L, where L is size of left, than we can be sure that we need to look into the left part. If k > L + M, where M is size of
mid group, than we can be sure, that we need to look into the right part.
-Finally, if none of these two condition holds, we need to look in the mid part, but because all elements there are equal, we can immedietly return mid[0].

Complexity: time complexity is O(n) in average (look at quick sort complexity). Space complexity is O(n) as well.
petite remarque sur le space : ici on cree a chaque iteration 3 nouveau array qui font en tout n puis n/2 puis n/4 puis n/8 etc.. donc la somme des allocations est egale a : 
n+n/2+n/4+...+1 == 2n-1 == O(n). tout ca est vrai si on considere que en moyenne le pivot partage en deux partie plus ou moine egale
"""
class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = nums[(len(nums))//2]
        left =  [x for x in nums if x > pivot]   #on creer un array qui aura toute les valeur unferieur au pivot
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
        
