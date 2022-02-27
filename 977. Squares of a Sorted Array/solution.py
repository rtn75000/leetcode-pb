"""#my sol  #two pointers #TC O(n) #SC O(1) if we don't consider output extra space 
l'algo utilisera deux poiteurs , un pointeur qui pointe sur le debut et un pointeur qui pointe sur la fin.  
app : 
   [-5 -3 1 2 3 4]    puisque abs(nums[l])>abs(nums[r]) alors ca veut dire que nums[l]^2>nums[r]^2 donc on append nums[l]^2 a res et on avance l : l+=1 car on a rentrer nums[l] dans res. res=[25]
     ^          ^
     l          r 
     
   [-5 -3 1 2 3 4]    puisque abs(nums[r])>abs(nums[l]) alors ca veut dire que nums[r]^2>nums[l]^2 donc on append nums[r]^2 a res et on recule r : r-=1 car on a rentrer nums[r] dans res. 
        ^       ^     res=[25,16]
        l       r 
        
   [-5 -3 1 2 3 4]    puisque abs(nums[r])==abs(nums[l]) ca change pas qui on choisi. dans l'algo on choisira dans le cas ou c'est egale : r donc r-=1 et res = [25, 16, 9] 
        ^     ^       
        l     r 
              
   [-5 -3 1 2 3 4]     puisque abs(nums[l])>abs(nums[r]) alors ca veut dire que nums[l]^2>nums[r]^2 donc on append nums[l]^2 a res et on avance l : l+=1 et res = [25, 16, 9, 9] 
        ^   ^       
        l   r 
   [-5 -3 1 2 3 4]     puisque abs(nums[r])>abs(nums[l]) alors ca veut dire que nums[r]^2>nums[l]^2 donc on append nums[r]^2 a res et on recule r : r-=1 et res = [25, 16, 9, 9, 4] 
          ^ ^       
          l r 
   [-5 -3 1 2 3 4]     puisque abs(nums[r])==abs(nums[l]) alors on append nums[r]^2 a res et on recule r (comme on a vu que si c egale alors on choisi nums r): r-=1 et res = [25, 16, 9, 9, 4, 1] 
          ^       
         l,r          
comme on veut l'ordre croissant alors on fait reverse() sur r puis on return. cad return  [1,4,9,9,16,25]
         
         
remarque : on n'utilise pas  res.insert(0,nums[l]**2) pour tout simplement inserer au debut car cette opperation coute O(n) , on aurait peu ecrire:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[];l=0;r=len(nums)-1
        while l<=r : 
            if abs(nums[l])>abs(nums[r]):
                res.insert(0,nums[l]**2)
                l+=1 
            else: 
                res.insert(0,nums[r]**2)
                r-=1     
        return res
        mais ca coute n^2 car la boucle coute n est chaque iteration utilise insert qui coute n

"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        l=0
        r=len(nums)-1
        while l<=r :   #O(n) car on parcours nums une fois
            if abs(nums[l])>abs(nums[r]):
                res.append(nums[l]**2)
                l+=1 
            else:    # if abs(nums[r])>=abs(nums[l])
                res.append(nums[r]**2)
                r-=1    
        res.reverse()    # O (n)
        return res
"""solution sans utiliser reversed()  (meme TC/SC) on fait juste rentrer la plus grande valeur en commencant par la fin de l'array 
app:
[-5 -3 1 2 3 4]    puisque abs(nums[l])>abs(nums[r]) alors ca veut dire que nums[l]^2>nums[r]^2 donc res[n-1]=nums[l]^2 et l+=1 . res=[0 0 0 0 0 25]
  ^          ^
  l          r 
 [-5 -3 1 2 3 4]    puisque abs(nums[r])>abs(nums[l]) alors ca veut dire que nums[r]^2>nums[l]^2 donc res[n-2]=nums[r]^2 et r-=1 . res=[0 0 0 0 16 25]
      ^       ^     res=[25,16]
      l       r 
etc...
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result  
