"""# ma solution  # TC O(n) car on utilise une sliding windows  # SC O(1)
l'idee est de tout simplement avance tant qu'on depasse pas le nombre de 0 autoriser si on depasse alors on reduit la fenetre de gauche a droite et dans ce cas si on 
rencontre un 0 alors on augmente le nbr de 0 autoriser de 1 car on a retirer le 0 de la fenetre puis on recommence a aggrandir la fenetre a gauche encore une fois etc... :

app : 1 1 0 1 1 0 0 1 1 1 1 0 1    k=2
      ^           
  start,end
  
   1 1 0 1 1 0 0 1 1 1 1 0 1      k=0      size = 6-0 = 6    [1 1 0 1 1 0]
   ^           ^           
  start       end
  
   1 1 0 1 1 0 0 1 1 1 1 0 1      k=1       
         ^     ^           
       start  end
       
   1 1 0 1 1 0 0 1 1 1 1 0 1      k=0     size = 11 -3 =8    [1 1 0 0 1 1 1 1]    
         ^               ^           
       start            end
       
  1 1 0 1 1 0 0 1 1 1 1 0 1      k=1     size = 12 -6 =6    [0 1 1 1 1 0 1]    
              ^           ^           
            start        end

  donc max = 8 
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = maxi = 0 
        while end < len(nums) : 
            if k>0 or nums[end]==1:  # car si  nums[end]==1 on peut continuer a lire le pb c'est si on rencontre un autre 0 et que k==0
                if nums[end]== 0 : 
                    k-=1  
                end += 1  
                maxi = max(maxi,end-start)
            else:                    # if k==0 and nums[end]==0 :      
                if nums[start]==0 : 
                    k+=1
                start+=1        
        return maxi
    
"""solution avec meme TC et SC plus courte , meme idee"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]     # si  nums[right]==1 alors 1 - nums[right] ==0 et donc  k -= 1 - nums[right] revient a k-=0 cad on retire rien
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1  
        return right - left + 1 # j'ai pas trop compris pq mais on aura tjrs la plus grande fenetre a la fin
