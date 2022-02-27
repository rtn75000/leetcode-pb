"""sol 1"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tail = n-1
        head=0 
        help=[0]*n
        for i in range (0,n):
            #si pair mettre au debut de help
            if nums[i]%2==0 :
                help[head]=nums[i]
                head+=1
            else:
                help[tail]=nums[i]
                tail-=1
        return help  
"""
    autre solution avec une 2 boucle qui garde l'ordre: """

    class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        help=[]
        for i in range (0,n):
            #si pair mettre au debut de help
            if nums[i]%2==0 :
                help.append(nums[i])
        for i in range (0,n):
            #si pair mettre au debut de help
            if nums[i]%2!=0 :
                help.append(nums[i])
        return help
 
