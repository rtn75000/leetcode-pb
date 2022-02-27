""" #two pointers #built-in sort #TC O(n^2) #SC O(1) for python 
tout d'abord on sort l'array puis ensuite in cherche la plus petit distance entre la somme de 3 element et target.
on recherche la somme qui est la plus proche du target cad on recherche la somme qui a la plus petite distance avec target on doit donc selectionner a chaque fois la somme dont la distance avec target est la plus petite.
distance entre deux nombre = |a - b|  ex: distance entre -3 et 4 c'est abs(-3-4) cad 7 , la distance entre 7 et 9 c'est abs(7-9) cad 2 
on va faire un for qui choisi un idx i de 0 a len(nums)-1 puis a chaque i chaoisi on va incrementer l ou decrementer r dans le range [i+1,len(nums)-1]
app:  [-6 -2  1  3 10] target = -3

-> i = 0   

    -6 -2  1  3 10    nums[i] + nums[l] + nums[r] (sum) = 2  on calcule la distance avec target : abs(sum - target) cad abs(2-(-3)) = 5 puis on actualise si il le faut la plus petite distance 
     ^  ^        ^    avec target pour cela il faut comparer la distance actuelle avec la plus petite distance enregistrer jusqu'a present et donc si abs(s - target) < abs(ans - target)
     i  l        r    cad que la distance actuelle est plus petite donc la sum actuelle est notre reponse potentiel donc on actualise ans : ans = sum(2) . puisque sum>target pour peut etre trouver une sum avec une
                      plus petite distance de target il faut s'approcher de target donc raptissir la sum donc faire r-=1 car nums[r-1]<nums[r]  ce qui donne :
         
    -6 -2  1  3 10    nums[i] + nums[l] + nums[r] (sum) = -5  on calcule la distance avec target : abs(sum - target) cad abs(-5-(-3)) = 2  on actualise la plus petite distance 
     ^  ^     ^       avec target car abs(s - target) < abs(ans - target) cad que la distance actuelle est plus petite donc la sum actuelle est notre reponse potentiel donc
     i  l     r       on actualise ans : ans = -5 . puisque sum<target pour peut etre  trouver une sum avec une plus petite distance de target il faut s'approcher de target donc augmenter la sum donc faire l+=1 
                      car nums[l]<nums[l+1]  ce qui donne :

     -6 -2  1  3 10    nums[i] + nums[l] + nums[r] (sum) = -2  on calcule la distance avec target : abs(sum - target) cad abs(-2-(-3)) = 1  on actualise la plus petite distance 
      ^     ^  ^       avec target car abs(s - target) < abs(ans - target) cad que la distance actuelle est plus petite donc la sum actuelle est notre reponse potentiel donc on 
      i     l  r       actualise ans : ans = -2
        
     on a fini avec i = 0 car si on avance l ou recule r la condition l<r sera false 
     
-> i = 1

     -6 -2  1  3 10       nums[i] + nums[l] + nums[r] (sum) = 9  on calcule la distance avec target : abs(sum - target) cad abs(9-(-3)) = 12  on actualise pas la plus petite distance 
         ^  ^     ^       car abs(s - target) (12) > abs(ans - target) (1) . puisque sum(9)>target(-3) pour peut etre trouver une sum avec une plus petite distance de target il faut s'approcher 
         i  l     r       de target donc raptissir la sum donc faire r-=1 car nums[r-1]<nums[r]  ce qui donne :

     -6 -2  1  3 10       nums[i] + nums[l] + nums[r] (sum) = 2  on calcule la distance avec target : abs(sum - target) cad abs(2-(-3)) = 5  on actualise pas la plus petite distance 
         ^  ^  ^          car abs(s - target) (5) > abs(ans - target) (1) .  
         i  l  r
     
     on a fini avec i = 1 car si on avance l ou recule r la condition l<r sera false 
    
-> i = 2

     -6 -2  1  3 10      nums[i] + nums[l] + nums[r] (sum) = 14  on calcule la distance avec target : abs(sum - target) cad abs(14-(-3)) = 17  on actualise pas la plus petite distance 
            ^  ^  ^      car abs(s - target) (17) > abs(ans - target) (1) .  
            i  l  r
 
    on a fini avec i = 1 car si on avance l ou recule r la condition l<r sera false 
    

(pas besoin de verifier i=3 et i=4 car il ne reste pas asser d'element apres eux pour avoir en tout 3 elements)


TC explication : 
chaque for selection un i puis parcours [i+1,n-1] :
i=0 alors on cherche l et r ds range = [1,n-1] donc n-1 iteractions
i=1 alors on cherche l et r ds range = [2,n-1] donc n-2 iteractions
i=2 alors on cherche l et r ds range = [3,n-1] donc n-3 iteractions
etc..
donc ca veut dire que on a n-1 + n-2 + n-3 + ... + 1 iteraction soit : 1+2+...+n-1 iteractions . la somme de 1 a n est egale a n(n-1)/2 donc O(n^2) donc ce for coute O(n^2)  """


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int: 
        ans = float('inf')
        nums.sort()    # O(n*logn)            
        for i in range(len(nums)-2):    # on fais moins deux car si i>=len(nums)-2 alors il ya pas deux index apres donc pas de l ,r 
            l, r = i+1, len(nums)-1
            while l < r:                         
                s = nums[i] + nums[l] + nums[r]
                # on compare la distance sum-target avec la plus petite distance enregistrer jusqu'a present et on actualise si la nouvelle dist est plus petite 
                if abs(s - target) < abs(ans - target): 
                    ans=s
                # si la sum est plus petite que target donc pour essayer de se raprocher de target il faut que la somme grandit donc il faut faire l+1 car nums[l]<nums[l+1]
                # (si on raptissit la sum c'est sur qu'on s'eloigne plus de target)
                if s < target:
                    l += 1
                # si la sum est plus grande que target donc pour essayer de se raprocher de target il faut que la somme raptississe donc il faut faire r-=1 car nums[r-1]<nums[r]
                elif s > target:
                    r -= 1
                else: # break early if s == target car on peut trouver une plus petite distance 
                    return  ans 
        return ans
