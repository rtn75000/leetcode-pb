"""#logic #array #my sol #TC O(n) #SC O(1)
on doit verifier les places qui sont 0 si il ya un 1 avant ou apres si oui alors on peut pas mettre un 1 a la place du 0 ."""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range (len(flowerbed)) :
            if flowerbed[i] == 0 : 
                if ( i==0 and i+1>=len(flowerbed) ) or ( i==0 and flowerbed[i+1] == 0 )   :
                        flowerbed[i] = 1
                        n-=1
                elif i==len(flowerbed)-1 and flowerbed[i-1] == 0 :
                        flowerbed[i] = 1
                        n-=1
                else :
                     if flowerbed[i-1] == 0  and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n-=1
                if n<=0 :
                    return True 
        return False 
