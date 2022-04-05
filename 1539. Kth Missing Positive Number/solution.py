"""# my sol #logics #TC O(n) #SC O(1)"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        num = 1 # missing possitive number 
        while k>0 :
            if i>len(arr)-1 or arr[i] != num :  
                k-=1
            else :
                i+=1
            num+=1
        return num-1
    
