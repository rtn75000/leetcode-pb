"""
# ma solution baser sur ma solution de 3 sum : https://leetcode.com/problems/3sum/
# two pointer #built-in sort 
# TC O(nlog n + n^3) = O(n^3) (voir explication en bas)  
# SC O(1) because output(res) is not extra space and python manage to sort in O(1) SC because python do the sort in-place no copy of array 

tout d'abord on sort l'array et donc si a<b<l<r alors  nums[a]<=nums[b]<=nums[l]<=nums[r] forcement .

app: -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4   target = -10

 on aura a qui va parcourir nums ainsi que b qui va parcourir [a+1,len(nums)-1] et deux autres pointeurs l et r qui parcours ensemble le range [b+1,len(nums)-1]   

-> a = 0 , nums[0]=-8 
  -> b=1 , nums[b]=-6
  
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[a] + nums[b] + nums[l] + nums[r] = -8-6-6+4 = -16 < target(-10) on avance l car il faut que la somme soit plus grande donc on veux un nombre plus grand 
    ^  ^  ^                      ^     que nums[l] (nums[r] est deja max donc ca sert a rien d'avance r) . donc l+=1 :
    a  b  l                      r      
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[a] + nums[b] + nums[l] + nums[r] = -8-6-3+4 = -13 < target(-10) donc on avance l , donc l+=1 :
    ^  ^     ^                   ^    
    a  b     l                   r
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[a] + nums[b] + nums[l] + nums[r] = -8-6-1+4 = -11 < target(-10) donc on avance l , donc l+=1 mais puisque nums[l+1](-1) == nums[l](-1) alors on avance     ^  ^        ^                ^     encore l car c'est le meme nums[l] que le precedent et donc on va forcement avoir la meme combinaison donc il nous faut un nums[l] different. 
    a  b        l                r
      
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[a] + nums[b] + nums[l] + nums[r] = -8-6+0+4 = -10 == target(-10) donc on append [nums[a] , nums[b] , nums[l] , nums[r]]
    ^  ^             ^           ^     puis on avance l et recule r tant nums[l] et nums [r] sont pas diff du nums[l] et nums[r] precedent (voir ds code explication pk on avance et on recule) :
    a  b             l           r
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[a] + nums[b] + nums[l] + nums[r] = -8-6+1+3 = -10 == target(-10) donc on append [nums[a] , nums[b] , nums[l] , nums[r]]
    ^  ^                 ^     ^       puis on avance l et recule r tant nums[l] et nums [r] sont pas diff du nums[l] et nums[r] precedent (voir ds code explication pk on avance et on recule) :
    a  b                 l     r
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     comme l >= r alors on passe au prochain b
    ^  ^                   ^        
    a  b                  l,r

  -> b=2 , nums[b]=-6 mais comme c'est le meme nums[b] qu'avant ca va nous donner les memes combi donc on fait encore b +=1 
  -> b=3 , nums[b]=-3 
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     etc...
    ^        ^  ^                ^
    a        b  l                r
  ->b=4 , nums[b]=-1
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     etc...
    ^           ^  ^             ^
    a           b  l             r
  ->b=5 , nums[b]=-1  mais comme c'est le meme nums[b] qu'avant ca va nous donner les memes combi donc on fait encore b +=1 
  ->b=6 etc...
  ....
  ->b=10 c'est le dernier car apres il ya pas deux idx pr l,r
 
-> a =1
    ->b=2  , l and r in range [3,len(nums)-1]
    ...
    ->b=10 , l and r in range [11,len(nums)-1]
    
-> a=2   on le fait pas car meme que le nums[a] precedent
   ....
-> a = 3 etc..
...
-> a =9 c'est le dernier car apres il ya pas assez d'idx pour b,l et r
   ...
   
   
TC explication : 
le for interieur celui de b selection un b puis parcours  [b+1,n-1] pour trouver l et r :
b=0 alors l et r parcours range = [1,n-1] donc n-1 iteractions
b=1 alors l et r parcours range = [2,n-1] donc n-2 iteractions
b=3 alors l et r parcours range = [1,n-1] donc n-3 iteractions
etc..
b=n-3 alors l et r parcours range = [n-2,n-1] donc 2 iteractions
donc ca veut dire que on a n-1 + n-2 + n-3 + ... + 1 iteraction soit : 1+2+...+n-1 iteractions . la somme de 1 a n est egale a n(n-1)/2 donc O(n^2) donc ce for coute O(n^2)
le for exterieur celui de a selection un a dans n donc coute O(n), donc on a [O(n) du for ext] * [O(n^2) du for interieur] donc TC egale O(n^3)

"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:   
        res = []
        nums.sort()    
        for a in range (len(nums)-3): # jusqu'a len-3 car apres il ya plus delements pour b l et r
            #on verifie que nums[a] != nums[a-1] (nums et sorted donc les nbr egaux sont l'un apres l'autre seulement) car si  nums[a] == nums[a-1] ca voudrais dire qu'on a encore
            #une fois le meme nums[a] ca sert a rien de chercher a nouveau les memes combinaisons, car on veut pas de duplicate.
            if a == 0 or nums[a] != nums[a-1]:
                for b in range(a+1,len(nums)-2): # on fais moins deux car si b>=len(nums)-2 alors il ya pas deux index apres pr l ,r      
                #on verifie que nums[b] != nums[b-1] (nums et sorted donc les nbr egaux sont l'un apres l'autre seulement) car si  nums[b] == nums[b-1] ca voudrais dire qu'on a encore
                #une fois le meme nums[b] ca sert a rien de chercher a nouveau les memes combinaisons, car on veut pas de duplicate.
                # if b == a+1 cad si c'est le premier index apres a il faut le lire (meme si l'index avant a le meme nbr) car on aura un duplicate que si on lit 2 fois le meme numero pour le meme
                #pointeur ex si on a [2,2,2,2,2] et a=0 b=1 l=2 r=4 alors nums[a]=nums[b] ca ya pas de pb mais si apres on lit encore une fois a=1 la ca va nous donner la meme combinaison que a=0
                # car nums[0]=nums[1] et on a deja essayer nums[0] en tant que a donc si on fait nums[1] en tant que a  ca va nous donner un duplicate 
                    if b == a+1 or nums[b] != nums[b-1]:    
                        l, r = b+1, len(nums)-1
                        while l < r:                         
                            s = nums[a] + nums[b] + nums[l] + nums[r]
                            if s < target:  # si inf target il faut que la somme soit plus grande donc l+=1 car nums[l+1]>nums[l]
                                l += 1
                                while l < r and nums[l] == nums[l-1]:
                                    l +=1  
                            elif s > target: # si sup a target alors il faut que la sum soit plus petite pour se rapprocher de target donc r-=1 car nums[r-1]<nums[r]
                                r -= 1
                                while l < r and nums[r] == nums[r+1]:
                                    r -=1 
                            # si s==target on a trouver une combinaison , puis on vait avancer l et reculer r car si on fait qu'avancer l c'est sur qu'on va etre superieur a target 
                            # car on agrandit la sum et comme elle etait egale a target maintenant elle sera forcement sup , donc on fait reculer r pour que peut etre on va avoir encore 
                            # une somme egale a target. si on fesait reculer r sans avancer l alors on aura forcement une sum inferieur a target car elle etait egale a target et en fesant 
                            # reculer r la somme raptissi donc il faut aussi avancer l pour peut etre avoir encore une somme egale a target. 
                            else:  
                                res.append([nums[a] , nums[b] , nums[l] , nums[r]])
                                l += 1 
                                while l < r and nums[l] == nums[l-1]: # tant que le nombre a l'index l est le meme il faut faire avancer l car on a la meme combinaison si c'est le meme nums[l]
                                    l += 1
                                r -= 1
                                while l < r and nums[r] == nums[r+1]:
                                    r -= 1
                        
        return res
    
    
 
