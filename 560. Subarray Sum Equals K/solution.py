"""# why two pointer is not the solution :
let's generalize the characteristics of the problems that can be solved by two pointers. The summary is simple:
1-If a wider scope of the sliding window is valid, the narrower scope of that wider scope is valid mush hold.
2-If a narrower scope of the sliding window is invalid, the wider scope of that narrower scope is invalid mush hold.
Now let me show you why this problem cannot be solved by two pointers:

In this specific problem, rule 1 doesn't hold, because I can find a specific case such that it doesn't hold, e.g., if K is 3, 1,1,1 sum is 3, so 1,1,1, is valid, but 1,1 sum is 2 which means 1,1 is invalid, so rule 1
breaks.

Rule2 doesn't hold, either, because I can find a specific case such that it doesn't hold, e.g., if K is 2, 1,1,1 sum is 3, so 1,1,1, is invalid, but 1,1,1,-1 sum is 2 which means 1,1,1,-1 is valid, so rule 2 breaks. 

(https://leetcode.com/problems/subarray-sum-equals-k/discuss/301242/General-summary-of-what-kind-of-problem-can-cannot-solved-by-Two-Pointers)
"""

"""solution #hashmap: https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example

the basic idea behind this code is that, whenever the sums has increased by a value of k, we've found a subarray of sums=k.
Example: Let's say our elements are [1,2,1,3] and k = 3.
and our corresponding running sums = [1,3,4,7]
Now, if you notice the running sums array, from 1->4, there is an increase of k=3 and from 4->7 there is also an increase of k=3. So, we've found 2 subarrays of sum=k.
But, if you look at the original array, there are 3 subarrays of sum=k : [1,2],[2,1],[3]
the reason is because we don't have 0 so we didn't take the option 3-0. To account this case, we include 0 to the hash table, se qui nous donne [0,1,3,4,7] (et tout ca on met dans le dict)
we use an hashtable to find if an element (in the running sum) is k away from another one and we can do that by finding a key that equal to element-k (this cost O(1) instead O(n) with an array)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)  # dictionary.get(keyN, val) keyN is the keyname of the item you want to return the value from. val is the value to return if the specified key does not exist. Default value None
            d[sums] = d.get(sums,0) + 1   # la valeur sera toujour 1 pour n'importe quel key
        
        return(count)    
    
