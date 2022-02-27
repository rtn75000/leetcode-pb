""" 
# my sol #built-in sort #TC O(nlogn)  #SC O(1) pour python 
on trie l'array donc ca va donner tout les element en double les un apres les autres et donc si on a un doublon alors nums[i]==nums[i+1] et dans ce cas il faut incrementer num[i+1] cad faire un moves . comme on a trier l'array num[i]<=nums[i+1] donc si ce n'est pas le cas ca veut dire que on a modifier nums[i] car il etait en double donc il faut que num[i+1] soit superieur de 1 de nums[i] et donc le nombre de moves qu'on fait sont egale a la nouvelle valeur de nums[i+1] cad nums[i]+1 moins l'ancienne valeur de nums[i+1]
app : nums = [ 3 2 3 2 2 2 ]
->on sort l'array : nums = [2 2 2 2 3 3]
->on traverse l'array :
       [2 2 2 2 3 3]  nums[0]==nums[0+1] donc nums[i+1] est un doublons de nums[i] donc il faut l'incrementer  nums[i+1]+=1 cad on a fait un moves donc count+=1 (count est le nbr de moves).
  i=0 : ^

       [2 3 2 2 3 3]  nums[1]>nums[1+1] or nums etait trier donc ca veut dire que on a du modifier nums[i] car il etait doublon donc tout ce qui vient apres i est qui est plus petit que nums[i]
  i=1 :   ^           doit etre au dessus de 3 pour ne pas avoir de doublons , nums[i+1] doit etre superieur a nums[i] donc nums[i+1]=nums[i]+1(==3+1=4) et donc ca veut dire qu'on a fait
                      a nums[i+1] :(nums[i]+1)(cad 3 qui est la nouvelle valeur de nums[i+1])-nums[i+1](2 qui est la valeur de nums[i+1] avant le changement)==1 moves, il faut donc faire 
                      count+= ((nums[i]+1)-nums[i+1]) cad count+=1 (count==2) on obtient donc :

       [2 3 4 2 3 3]  nums[2]>nums[2+1] donc  count+= ((nums[i]+1)-nums[i+1]) cad count+=(5-2) cad count+=3 et nums[i+1]=nums[i]+1 cad nums[i+1]=5 , ca donne :
  i=2 :     ^  
  
       [2 3 4 5 3 3]  etc...
  i=3 :       ^  
                      """
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count=0   #nbr de moves
        for i in range(len(nums)-1) :
            if nums[i]==nums[i+1]:
                nums[i+1]+=1
                count+=1
            elif nums[i]>nums[i+1]:
                count+= ((nums[i]+1)-nums[i+1])
                nums[i+1]=nums[i]+1
        return count
    
"""pas ma solution #TC O(n+max(nums)) #SC O(n+max(nums))    rappel: n==len(nums)
on compte la frequence de chaque num dans nums , ensuite on passe sur tout les numero de min(nums) a max(nums)+len(nums) les autres pas besoin . explication : on a pas besoin de passer sur les num en dessous de min(nums) car il sont pas dans nums donc ne peuvent pas etre des doublons , mais de nums(min) il faut verifier tout les nombre jusqu'a max(nums)+len(nums) , on va jusqu'a max(nums)+len(nums) car si max(nums) est un doublons alors on devra increment max(nums) jusqu'a maximum max(nums)+len(nums) ex : [5 5 5 5 5] alors max(nums)=5  mais au finale on aura [5 6 7 8 9] on a du incrementer tout les nombres cad au max on va incrementer jusqu'a len(nums)-1 car si nums contient que des doublons du meme nbr alors on va devoir faire n-1 incrementation (-1 car le premier on l'incremente pas) or comme il ya que un numero il est forcement max(nums) donc on a fait (n-1) incrementation a max(nums) donc on peut avoir maximum max(nums)+(n-1) inclus (donc max(nums)+n pas inclu).c'est pour cela que la boucle ira de min(nums) a max(nums)+(n-1).
l'idee est qu'une fois qu'on a les frequence de chaque nombe alors si la frequence est sup a 1 cad que c'est un doublons on doit donc incrementer les valeurs ex si on a 2:4 (cad 4 fois 2) alors
on doit incrementer 4-1 des 4 numero 2 qu'il ya (4-1 car le premier 2 lui n'est pas un doublons), donc si on les incremente de 1 maintenant on va avoir encore 3 numero 3 car on a incrementer 3 numero 2 donc on peut rajouter plus 3 a la frequence du nbr 3 du au 3 incrementation du nombre 2 . 
app :  nums = [2 5 2 2 2 5]
freq = {2:4, 5:2}
min(nums) == 2 , max(nums)==5 donc on fait une boucle de min(nums) a max(nums)+len(nums)-1 (inclus) cad de 2 a 5+6-1==10 , on verifie la frequence de chaque nbrs de ce range :
->i=2:freq[2]==4 donc freq[2]>1 donc il ya freq[2]-1 doublons cad 3 doublons on les incrementent de 1 donc ca veut dire qu'on fait freq[2]-1 incrementations (car il ya freq[2]-1 doublons)
  donc count+=3 . il faut rajouter les nouveau numero au frequence donc on doit ajouter freq[2]-1 a freq[3] car on a router plus 1 a freq[2]-1 numero 2 donc il faut ajouter freq[2]-1 a la 
  frequence du numero au dessus cad a freq[2+1] donc freq[2+1]+=freq[2]-1 . donc en resumer quand on a freq[i]>1 alors on fait count+=(freq[i]-1) et freq[i+1]+=(freq[i]-1)
  la nouvelle frequence est donc {2:4, 3:3, 5:2} (remarque on a pas besoinde modifier la freq de 2 car de tout les facons on la reutilisera pas car on s'avancedonc meme si on a incrementer les 2
  et donc il ya plus 4 fois le num 2 mais que 1 fois ca change rien car on reutilisera pas cette frequence).
->i=3:freq[3]==3 donc freq[3]>1 donc freq[3+1]+=(freq[3]-1) cad freq[4]+=2 et count+=(freq[3]-1) cad count+=2. donc freq={2:4, 3:3, 4:2, 5:2}.
->i=4:freq[4]==2 donc freq[4]>1 donc freq[4+1]+=(freq[4]-1) cad freq[5]+=1 et count+=(freq[4]-1) cad count+=1. donc freq={2:4, 3:3, 4:2, 5:3}.
->i=5:freq[5]==3 donc freq[5]>1 donc freq[5+1]+=(freq[5]-1) cad freq[6]+=2 et count+=(freq[5]-1) cad count+=2. donc freq={2:4, 3:3, 4:2, 5:3, 6:2}.
->i=6:freq[6]==2 donc freq[6]>1 donc freq[6+1]+=(freq[6]-1) cad freq[7]+=1 et count+=(freq[6]-1) cad count+=1. donc freq={2:4, 3:3, 4:2, 5:3, 6:2, 7:1}.
->i=7:freq[7]==1 comme freq[7]<=1 donc ce n'est pas un doublons.
->i=8:freq[8]==0
...
->i=10:freq[10]==0   (on peut remarque que a partir du moment ou on a depasser max(nums) et qu'un des frequence est egale a 0 alors tout les autres frequences au dessus seront 0 car puisque la seul possibilite que la frequence qui est au dessus de max(nums) soit differente de 0 c'est si max(nums) est un doublons est donc on incremente a chaque fois de 1 mais a partir du moment ou une frequence est egale a 0 on ne va pas rencontrer encore un nombre au dessus car on a depasser max(nums) ex : [1 2 3 4 8 8] ,max(nums)==8 , le range de verification est de 1 jusqu'a 8+6-1 cad 13 mais comme je sais que max(nums)==8 et donc apres cela si je rencontre des frequences sup a 0 c'est du au doublons de 8 donc si freq[10]==0 ya pas encores des numero de nums donc forcement que toute les frequence a venir seront egale a 0 donc on peut economiser des iterations avec la condition : if i > max(nums) and freq[i]==0 : return count )
return count
"""

    
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        count=0 #compte les moves 
        maxi=-1 #initialise -1 car 0 <= nums[i]
        mini=float('inf') #initialise infini comme ca des qu'on rencontre un nombre ca sera le nouveau min
        for val in nums :    #O(n)
            freq[val]+=1
            mini=min(mini,val)
            maxi=max(maxi,val)
        
        for i in range(maxi+len(nums)) : # pas -1 car maxi+len(nums) n'est pas inclus 
            if i > maxi and freq[i]==0 :
                return count
            elif freq[i]<=1:
                continue
            else : # if freq[i]>1 il ya des doublons
                freq[i+1]+=(freq[i]-1)
                count+=(freq[i]-1)
        return count
