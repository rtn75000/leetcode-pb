"""reponse prise d'ici :  https://leetcode.com/problems/relative-sort-array/discuss/334931/Python-100-time-and-100-space """

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        r = [] # Hold the resulting relative sort array
        m = {} # Used for counting elements of arr2 that appear in arr1
        diff = [] # Use for tracking elements that don't appear in arr2 but appear in arr1
        
		# Initialize counts
        for num in arr2:
            if num not in m:
                m[num] = 0
        
        for num in arr1:
            if num in m:
                m[num] += 1 # Increment count of elements seen
            else:
                diff.append(num) # Add element to difference list (e.g. nums in arr1 not in arr2)
        
        diff.sort() # Sort the difference
        
        for num in arr2:
            r.extend([num] * m[num]) # Add the number of elements seen to  the result set
        
        r.extend(diff) # Add the rest of the sorted elements
        
        return r
    
"""autre reponse tres interresante: https://leetcode.com/problems/relative-sort-array/discuss/334570/JavaPython-3-O(max(n2-N))-code-similar-to-791-Custom-Sort-String.

# juste pour comprendre counter fait un array ou le chifrre de l'array de base va etre un index dans celui de counter et la valeur va etre celle du nombre d'apparition

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans, cnt = [], collections.Counter(arr1)         # Count each number in arr1
        for i in arr2:
            if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the common numbers in both arrays by the order of arr2. 
        for i in range(1001):               
            if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the numbers only in arr1.
        return ans     
        """     
    
