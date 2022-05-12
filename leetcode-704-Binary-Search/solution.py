""" # binary search #TC O(log n) #SC O(1) """

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        left,right=0,len(arr)-1    
        
        while left<=right:
            
            mid =(left+right)//2   # le pivot va etre le milieu
            
            if arr[mid]==target :
                return mid         # retour de l'index du target
            
            elif arr[mid]< target :   # cad le target ce trouve a droite du mid 
                left=mid+1 
                
            else:                     # cad le target ce trouve a gauche du mid
                right = mid-1
                
        return -1   # si target pas trouver retourne -1
