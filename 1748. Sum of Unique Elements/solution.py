class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dictio = {} 
        for i in nums :
            if i in dictio : 
                dictio[i] += 1 
            else: 
                dictio[i]=1
        sum = 0        
        for key in dictio:
            if dictio[key]==1:
                sum+=key 
        return sum 
