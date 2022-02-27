class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
            dict = {}
            for key in arr:
                if key in dict : 
                    dict[key]+=1
                else: 
                    dict[key]=1
            count=0
            for key in dict:
                if dict[key]==1:
                    count+=1
                    if count==k:
                        return key 
            return ""  
            
    
""" solution sans hash map:

class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
          
          #The count() method returns the number of times the specified element appears in the list.
	    arr = [i for i in arr if arr.count(i) == 1]
        
	    return "" if k > len(arr) else arr[k - 1] 
        """ 
