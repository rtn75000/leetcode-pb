"""remarque : pour un array de la taille n il ya 2^n subsequences . 2^n car chaque element on choisi de le selectionner ou non donc ya 2 possibilite qui se repete n fois : 2*2*...*2*2  = 2^n  . 
                                                                                                                                                                          |-----------|
                                                                                                                                                                             n fois 
cela inclu aussi l'empty subsequence [] . ex arr=[1,2,3] alors on a 2^3=8 subsequences : [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] . 
si on veut que les elements soient consecutifs alors on a n(n+1) * 1/2 possibilitees, ex : arr=[1,2,3] on a 3(3+1)*1/2= 12*1/2=6 possibilites :  [1], [2], [3], [1,2], [2,3], [1,2,3] .
"""

"""
#two pointers #TC O(n log n) for the sort  #SC O(1) in python 

code est explication : https://www.youtube.com/watch?v=xCsIkPLS4Ls&ab_channel=NeetCode

pour resoudre ce pb il nous faut un array ordonnee (ce pb est bien entendue solvable meme avec l'array en desordre mais c'est moins couteux en TC lorsque l'array est ordonnee ).
explication : apres avoir un sort on choisie la premier valeur qui sera notre minimum puis a ce minimum on va voir quels sont les maximum qui peuvent aller avec lui sans depasser le target. 
ex : nums = [3,4,6,8], target = 10   le pointeur left represente le minimum et right le max . donc on a  : 

[ 3, 4, 6, 8 ]      left pointe sur le min , ensuite right est passer de 3 a 4 puis de 4 a 6 car 3+4<target=10 et 3+6<target=10 cad ce sont des max qui vont avec le min 3
  ^     ^           mais on ne peut avance right pour l'instant car 3+8>target=10 
 left  right        

3 est le min ce 3 est donc pas en option il est obligatoire mais apart lui tout le reste (qui sont les max potentiel) est en option car on peut prendre [3] (cad 3 est en meme temps min est en meme temps max)  ou [3,4] ou
[3,6] ou [3,4,6] soit 2^2 possibilite . 3 n'est pas une option donc il reste seulement 4 et 6 en option donc 2^2 car chaqun peut etre present ou non. puisque 2^len(subarray des max) nous donne aussi la empty subsequence
[] on doit normalement donc avoir 5 possibilite [] ou  [3] ou [3,4] ou [3,6] ou [3,3,6] mais comme le pb veux que les non-empty alors ds l'algo le min qui doit etre forcement choisi sera compter dans  le 2^len(subarray
des max) a la place de [] (donc on ne rajoute pas 1 a 2^len(subarray des max) car le min viendra a la place de [] ).
donc res = 4 car pour l'instant 4 possibilites 

maintenant on doit changer de min donc on fait avancer left ce qui nous donne un nouveau min 4 , 4 peut etre min car si on prend que [4] cad que 4 est en meme temps min en meme temps max on est en dessous de target 
car 4+4 < 10 donc 4 peut etre min : 
[ 3, 4, 6, 8 ]      left pointe sur le min 4, right s'arrete a 6 car 4+8>target
     ^  ^             
   left right 
donc on a 2^1 possibilites (4 est le min donc obligatoire puis le reste qui est que 6 est en option donc 2^1) : [4] et [4,6]
res= 2^4 + 2^1 

on ne peut faire avancer le left car 6 ne peut etre min car [6] cad 6+6 n'est pas inf a target, et comme c'est sorted donc c sur que on ne peut trouver de nouveau min donc on a fini . donc en tout on a obtenue res = 6

remarque si l'array n'est pas sorted on aurait bcp plus de mal a trouver les subsequences ex si on a le meme array que precedent mais dans le desordre : 
[6, 3, 8, 4]  alors on a [6,3,4] [6, 3] [3,4] [3] [4] [6,4] bien que on a autant d'option (forcement car sinon le tri fausse le resultat) cela esr impossible d'ecrire un algo pour les trouver a moins que ce soit en
brute force donc couteux...

schema generale: 
si on a par exemple [1,3,5,7,8,9,10,12,15,18,21] avec target =23 alors [1,3,5,7,8,9,10] sont des minimum potentiels (car si on prend chacun il peut etre max est min en meme temps ex [10] ca donne 10+10<23) :
-pour le min 1 on a [3,5,7,8,9,10,12,15,18,21] comme max potentiels donc res+=2^10 , algo pointeur :  [1,3,5,7,8,9,10,12,15,18,21]
                                                                                                       ^                        ^
                                                                                                      left                    right 
-pour le min 3 on a [5,7,8,9,10,12,15,18] comme max potentiels donc res+=2^8 , algo pointeur :  [1,3,5,7,8,9,10,12,15,18,21]
                                                                                                   ^                   ^
                                                                                                 left                right         
-pour le min 5 on a [7,8,9,10,12,15,18] comme max potentiels donc res+=2^7, algo pointeur :  [1,3,5,7,8,9,10,12,15,18,21]
                                                                                                  ^                 ^
                                                                                                 left              right 
-pour le min 7 on a [8,9,10,12,15] comme max potentiels donc res+=2^5, algo pointeur :  [1,3,5,7,8,9,10,12,15,18,21]
                                                                                               ^            ^
                                                                                              left        right 
-pour le min 8 on a [9,10,12,15] comme max potentiels donc res+=2^4, algo pointeur :  [1,3,5,7,8,9,10,12,15,18,21]
                                                                                                 ^        ^
                                                                                                left     right 
-pour le min 9 on a [10,12] comme max potentiels donc res+=2^2, algo pointeur :  [1,3,5,7,8,9,10,12,15,18,21]
                                                                                            ^     ^
                                                                                          left  right 
-pour le min 10 on a [12] comme max potentiels donc res+=2^1, algo pointeur :  [1,3,5,7,8,9,10,12,15,18,21]
                                                                                            ^   ^
                                                                                          left right 
d'ou res=2^10+2^8+2^7+2^5+2^4+2^2+2^1

donc l'algo va commence avec right=len(nums)-1 et left= 0 cad on commence avec min a l'index 0 et le max au dernier comme vu dans le schema generale, car forcement que le min doit etre le plus petit possible et max le
plus grand possible pour trouver le plus grand nombre de possibilite. on fait reculer right si nums[left] + nums[right] > target cad si min+max>target donc on doit essayer un max plus petit avec ce min donc left reste le
meme juste right recule. si nums[left] + nums[right] <= target alors ca veut dire que min et max reponde au critere du pb on peut donc rajoute au res les possibilite qui sont 2 puissance le nombre d'elemnt apres le min
cad apres left soit 2^(left-right)  (remarque: [1,2,3,5] si left=idx1 et right=idx 3 alors 3-1 c'est 2 donc c'est les element 3,5 et pas 2,3,5 cad ca inclu pas left car left est obligatoire donc ne fait pas partie de la 
puissance). on oublie pas de faire modulo a cela comme demander dans l'ennoncee. donc si  nums[left] + nums[right] <= target alors on avance left si  nums[left] + nums[right] > target on recule right , l'algo s'arrete des
que left depasse right cad left>right car ca voudrais dire qu'on a essayer tout les min potentiel avec tout les max potentiel.


"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()                                   # O(n log n)
        res = 0 
        mod = (10**9+7)
        left = 0 
        right = len(nums)-1
        while left <= right:                         # O(n)
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += pow(2, right - left, mod)
                left += 1
        return res % mod
