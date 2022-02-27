""" #two pointers #built-in sort  # TC O(nlog n + n^2) = O(n^2)(voir explication en bas)  #SC O(1) because output(res) is not extra space and python manage to sort in O(1) SC because python do the sort in-place no copy
of array


tout d'abord on sort l'array et donc si i<l<r alors nums[i]<=nums[l]<=nums[r] forcement .

app: -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4 

 on aura i qui va parcourir nums et deux autres pointeurs l et r qui parcours le range [i+1,len(nums)-1]   
 
-> nums[i]=-8
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -8-6+4 <0 on avance l car il faut que la somme soit plus grande donc on veux un nombre plus grand  
    ^  ^                         ^     que nums[l] (nums[r] est deja max donc ca sert a rien d'avance r) . donc l+=1 puisque nums[l](-6) == nums[l-1](-6) alors on avance encore l car c'est le 
    i  l                         r     meme nums[l] que le precedent et donc on va forcement avoir la meme combinaison donc il nous faut un nums[l] different. 
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -8-3+4 <0 donc l+=1  
    ^        ^                   ^     
    i        l                   r
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -8-1+4 <0 donc l+=1  comme nums[l](-1) == nums[l-1](-1) donc on fait encore l+=1
    ^           ^                ^     
    i           l                r
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -8+0+4 <0 donc l+=1  comme nums[l](0) == nums[l-1](0) donc on fait encore l+=1
    ^                ^           ^     
    i                l           r
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -8+1+4 <0 donc l+=1  comme nums[l](0) == nums[l-1](0) donc on fait encore l+=1
    ^                    ^       ^     
    i                    l       r
    
    etc... ici pour nums[i]=-8 il ya pas de l et r tel que  nums[i] + nums[l] + nums[r] == 0
-> nums[i]=-6 

   ... [etapes precedente]...
   
    -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -6+2+4 == 0 donc on rajoute [nums[i], nums[l], nums[r]] au res . maintenant on fait avancer l (on le fait avancer   
        ^                   ^     ^     tant que nums[l]==nums[l-1] car dans ce cas c'est la meme combinaison qu'avant) on doit faire reculer r car on a fait avancer l donc maintenant nums[l] 
        i                   l     r     est plus grand donc forcement que nums[i] + nums[l] + nums[r] > 0 si on reste avec le meme r. donc on fait r-=1 (on fait ca tant que nums[r]==nums[r+1])
    
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -6+3+3 == 0 donc on rajoute [nums[i], nums[l], nums[r]] au res. maintenant on a fini car l+=1 entraine que la condition l<r 
       ^                     ^ ^       n'est plus respecter donc on fait nums[i]=-6 puisque c'est le meme nums[i-1] donc on va pas le refaire l'algo passe a  nums[i]=-3 
       i                     l r
   
   
-> nums[i]=-3

   ... [etapes precedente]...   
 
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -3+0+4 > 0 donc si on fait l+=1 forcement que ca va etre encore superieur a 0 car le nouveau nums[l] va etre sup a l'ancien.
             ^       ^           ^     on cherche a reduire la somme car elle est sup a 0 , on va donc faire r-=1 ,tant que nums[r] == nums[r+1] , pour que nouveau nums[r] < ancien nums[r]. on
             i       l           r     obtient donc :

   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     nums[i] + nums[l] + nums[r] = -3+0+3 == 0  donc on rajoute [nums[i], nums[l], nums[r]] au res . maintenant on fait avancer l (on le fait avancer  
             ^       ^         ^       tant que nums[l]==nums[l-1] car dans ce cas c'est la meme combinaison qu'avant) on doit faire reculer r car on a fait avancer l donc maintenant nums[l] 
             i       l         r       est plus grand donc forcement que nums[i] + nums[l] + nums[r] > 0 si on reste avec le meme r. donc on fait r-=1 (on fait ca tant que nums[r]==nums[r+1])
       
   -8 -6 -6 -3 -1 -1 0 0 1 2 3 3 4     etc...
             ^           ^ ^
             i           l r
             
    etc ...

remarque : si on un nouveau l soitl+=1 alors r reste a ca place il ne retourne pas a pointer sur la fin car si r a reculer ca voulais dire que nums[i] + nums[l] + nums[r] >=0  donc forcement pour le nouveau l 
nums[l] > ancien nums[l] car array dans ordre croissant . donc si deja avec l'ancien l nums[i] + nums[l] + nums[r] >=0  alors forcement que avec le nouveau l on aura nums[i] + nums[l] + nums[r] >=0 donc le r ne doit 
pas bouger de sa place . c'est pour cette raison qu'on parcours [i+1,n-1] que une fois l du debut puis r a la fin a chaque fois on avance ou l ou on recule r et des qu'il se rencontre on passe a un nouveau i.

-> nums[i]=-1 etc..
-> nums[i]=0 etc..
-> nums[i]=1 etc..
-> nums[i]=2 etc..
-> nums[i]=3 etc..
-> nums[i]=4 etc..

return res==[[-6,2,4],[-6,3,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-1,-1,2],[-1,0,1]]
"""
"""TC explication : 
chaque for selection un i puis parcours  [i+1,n-1] pour trouver l et r :
i=0 alors l et r parcours range = [1,n-1] donc n-1 iteractions
i=1 alors l et r parcours range = [2,n-1] donc n-2 iteractions
i=3 alors l et r parcours range = [1,n-1] donc n-3 iteractions
etc..
donc ca veut dire que on a n-1 + n-2 + n-3 + ... + 1 iteraction soit : 1+2+...+n-1 iteractions . la somme de 1 a n est egale a n(n-1)/2 donc O(n^2) donc ce for coute O(n^2)  """


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        res = []
        nums.sort()               
        for i in range(len(nums)-2): # on fais moins deux car si i>=len(nums)-2 alors il ya pas deux index apres donc pas de l ,r      
            if nums[i] > 0:   # cette condition est logique: si nums[i] > 0 alors nums[i] + nums[l] + nums[r] > 0 car i<l<r et nums est sorted donc ca sert a rien de continuer on a fini l'algo.
                break
            #on verifie que nums[i] != nums[i-1] car si  nums[i] == nums[i-1] ca voudrais dire qu'on a encore une fois le meme nums[i] ca sert a rien de chercher a nouveau les memes combinaisons.
            if i == 0 or nums[i] != nums[i-1]:    
                l, r = i+1, len(nums)-1
                while l < r:                         
                    s = nums[i] + nums[l] + nums[r]
                    if s < 0:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l +=1  
                    elif s > 0:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -=1 
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1 
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                        
        return res
    
