""" #hashmap #TC O(n^2) #SC O(n^2) pour le hashmap 
on doit seulement retourner le nombre de tuples dont la sum est egale a zero
on va donc tout d'abord calculer la somme des elements nums1[a] + nums2[b] ce qui va nous donner n*n soit n^2 sommes (chaque array est de taille n) ex si on prend [1,2,3] et [4,5,6] alors ca va nous donner 
[1+4,1+5,1+6,2+4,2+5,2+6,3+4,3+5,3+6] cad [5,6,7,6,7,8,7,8,9] on va stocker ces somme dans un hashmap la somme sera la key et la valeur va etre le nombre fois qu'on a cette somme, ici ca va donc donner 
{5:1,6:2,7:3,8:2,9:1} . Ensuite pour chaque somme nums3[c]+nums4[d] on regarde si on a une key dans le hashmap qui est egale a -(nums3[c]+nums4[d]) si oui ca veut dire que nums1[a]+nums2[b] = -(nums3[c]+nums4[d]) 
cad que nums1[a] + nums2[b] + nums3[c] + nums4[d] = 0 et donc on peut rajouter une combinaison valide au res : res+=1

app: nums1=[1,2],nums2=[-2,-1], nums3=[-1,2], nums4=[0,2]

puisque tout les possibilites de nums1[a] + nums2[b] sont egale a  [1-2,1-1,2-2,2-1] =[-1,0,0,1] donc dict={-1:1,0:2,1:1} maintenant on verifie si il y'a des nums3[c] + nums4[d] qui sont egales a -(nums1[a]+nums2[b]) 
si oui la sum nums1[a] + nums2[b] + nums3[c] + nums4[d] sera egale a 0. 
->nums3[0]+nums4[0]=-1+0=-1 , rajoutons a res: dict[-(-1)] car dict[-(-1)] nous donne la frequence que la somme -1 apparait dans nums1[a]+nums2[b] cad le nombre de different a ou b qui donne la meme somme et donc 
dict(-(nums1[a]+nums2[b])) nous donne le nombre de fois qu'on a nums1[a] + nums2[b] + nums3[c] + nums4[d] = 0 pour les ab c et selectionnes . donc ici res+=dict[1] cad res+=1 .
->nums3[0]+nums4[1]=-1+2=1 , rajoutons a res: dict[-(1)] cad res+=dict[-1] cad res+=1 .
->nums3[1]+nums4[0]=2+0=2 , rajoutons a res: dict[-(2)] cad res+=dict[1] cad res+=1 .
->nums3[1]+nums4[1]=2+2=4 , rajoutons a res: dict[-(4)] puisque -4 n'est pas key dans dict (cad il existe pas un  nums1[a]+nums2[b] qui egale a -4) alors par default dict[-4] a la valeur 0 car on a utiliser un 
defaultdict(int) et donc on peut aussi faire res+=dict[-4] car ca revient a faire res+=0.
au final on a donc res==2

remarque SC est O(n^2) car on peut avoir un dict de taille n*n si toutes les sommes de nums1[a]+nums2[b] sont differente 
"""


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res  = 0
        dic = collections.defaultdict(int)
        for a in nums1:        #TC O(n*n) for this double for
            for b in nums2:
                dic[a+b] += 1
        for c in nums3:        #TC O(n*n) for this double for
            for d in nums4:
                #if -(c+d) in dic then dic[-(c+d)] > 0 else it's going to be 0:
                res += dic[-(c+d)]     
        return res

