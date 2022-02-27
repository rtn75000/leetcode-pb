"""voir ma solution de ce pb ressemblant : https://leetcode.com/problems/3sum/
#two pointers #built-in sort #TC O(n^2)  #SC O(1) python use in-place sort

tout d'abord on fait sort() a l'array , donc si i<l<r alors nums[i]<=nums[l]<=nums[r] forcement .

remarque: dans notre cas on veut aussi les duplicate ex si nums=[-1,-1,0,1] et target = 0 alors (pour i=0) [-1,-1,0] , [-1,-1,1] , [-1,0,1] ,(pour i=1) [-1,0,1]  sont les combinaisons valides donc res=4 et pas 3.

l'algo :
for i in len(nums):
    trouver deux autre index dans le range [i+1,n-1] tel que nums[i] + nums[l] + nums[r] < target
    
algo app : 
nums =[ -6 ,-3, -1, -1, 0, 1, 2, 3, 5,5,5] target=1

-> nums[i]=-6
     
    -6 -3 -1 -1 0 1 2 3 5 5 5     nums[i] + nums[l] + nums[r] = -6-3+5 = -4 < target= 1 ; si on recule r sans bouger le l ca va nous donner encore des combinaison [i,l,r] tel que
     ^  ^                   ^     nums[i] + nums[l] + nums[r] < target car nums[r-1]<num[r] donc forcement que nums[i] + nums[l] + nums[r-1] < nums[i] + nums[l] + nums[r] < target
     i  l                   r     donc on peut directement rajoute r-l combinaison au resultat car si [i,l,r] est une combi valide (cad nums[i] + nums[l] + nums[r] < target) alors forcement 
                                  que [i,l,r-1] est valide (car nums[r-1]<nums[r]) ainsi que [i,l,r-1],[i,l,r-2],[i,l,r-3],....,[i,l,l+1] , donc toute les combinaisons sont [i,l,r]...[i,l,l+1]
                                  soit r-l combinaisons . donc ici on a r-l=10-1=9  donc res+=1. on fait maintenant avancer l car on a fini avec l=-3
                                  
    -6 -3 -1 -1 0 1 2 3 5 5 5     nums[i] + nums[l] + nums[r] = -6-1+5 = -2 < target= 1  donc res+=(r-l) cad res+=(10-2) dc res+=8 ; puis l+=1.
     ^     ^                ^
     i     l                r
     
     ....[etc]....
     
    -6 -3 -1 -1 0 1 2 3 5 5 5     nums[i] + nums[l] + nums[r] = -6+2+5 = 1 >= target= 1  donc comme on veut inf a target si on avance l ca va nous donner un nums[l] superieur au precedent et  
     ^              ^       ^     donc forcement que nums[i] + nums[l] + nums[r] va etre sup a target donc il faut pas avancer l car on veut raptissir la somme nums[i] + nums[l] + nums[r].
     i              l       r     on va donc faire r-=1  puis tant que nums[r] == nums[r+1] on refera r-=1 pour que nums[r] < nums[r+1] et qu'on puisse donc avoir une somme inferieur (donc ici) 
                                  on va faire r-=1 3 fois ce qui donne nums[r]==3 < nums[r+1]==5.

    -6 -3 -1 -1 0 1 2 3 5 5 5     nums[i] + nums[l] + nums[r] = -6+2+3 = -1 < target= 1 donc on a une combinaison valide ([-6,2,3]) donc res+=(r-l) cad res+=1 puis l+=1 .
     ^              ^ ^     
     i              l r
     
     -6 -3 -1 -1 0 1 2 3 5 5 5     on passe au prochain i car la condition l<r est false
     ^                 ^          
     i                l,r     

-> nums[i]=-3
-> nums[i]=-1
-> nums[i]=-1
-> nums[i]=0
-> nums[i]=1
-> nums[i]=2
-> nums[i]=3
-> nums[i]=5
on fait pas les 2 dernier 5 en tant que i car il ne peut avoir l et r car il reste moins que deux elements.


remarque : si on un nouveau l soit l+=1 alors r reste a ca place il ne retourne pas a pointer sur la fin car si r a reculer ca voulais dire que nums[i] + nums[l] + nums[r] >= target  donc forcement pour le nouveau l nums[l] > ancien nums[l] car array dans ordre croissant . donc si deja avec l'ancien l nums[i] + nums[l] + nums[r] >=target et donc on a fait r-=1 alors forcement que avec le nouveau l on aura nums[i] + nums[l] + nums[r] >=target donc le r ne doit pas bouger de sa place car r a ete deplace parceque nums[i] + nums[l] + nums[r] >=target . c'est pour cette raison qu'on parcours [i+1,n-1] que une fois l au debut puis r a la fin a chaque fois on avance l ou on recule r et des qu'il se rencontre on passe a un nouveau i. (pour cette raison on parcours le range [i+1,n-1] que une fois)

TC explication : 
chaque for selection un i puis parcours [i+1,n-1] :
i=0 alors range = [1,n-1] donc n-1 iteractions
i=1 alors range = [2,n-1] donc n-2 iteractions
i=2 alors range = [3,n-1] donc n-3 iteractions
etc..
donc ca veut dire que on a n-1 + n-2 + n-3 + ... + 1 iteraction soit : 1+2+...+n-1 iteractions . la somme de 1 a n est egale a n(n-1)/2 donc O(n^2) donc ce for coute O(n^2)  
"""

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()               # O(n*logn)
        for i in range(len(nums)-2):    # on fais moins deux car si i>=len(nums)-2 alors il ya pas deux index apres donc pas de l ,r 
            #si la target est neg alors meme si nums[i]>target ca veut pas dire que on ne peut avoir de combinaison pour ce i, ex (i=0): [-2 -1 -1],target=-3
            # c'est valide meme que -2>-4   (cette condition permet de gagne du temps)
            if target > 0 and nums[i]>target  :  
                break
            l, r = i+1, len(nums)-1
            while l < r:                         
                s = nums[i] + nums[l] + nums[r]
                if s >= target:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                            r -=1 
                else:   # if s < target:
                    res+=(r-l)
                    l += 1                      
        return res
    
