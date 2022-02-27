"""remarque si on a pas le droit d'utiliser un extra space ca veut dire que on doit travailler sur le input et pas utiliser un array en plus donc on fait ce qu'on appel un in-place cad on change sur le meme array
que l'input"""

""" # pointers # TC O(n) #SC O(1)  #one pass  #in-place
algo:
on a 3 pointeurs dans cette algo un qui pointe sur l'idx qui viens apres les 0 : p0 , un qui pointe sur l'index qui vient avant les 2 et un qui pointe sur le current. puisque les 0 sont censer etre au debut alors 
on initialise p0=0 cad le premier index, puisque les 2 sont censer etre a la fin on initialise p2=len(nums) - 1 cad le dernier index. on met donc les 2 a la fin et les 0 au debut .
ex : 0 0 1 1 1 2 2   cad p0 vient apres les 0 et p2 viens avant les 2.
         ^   ^ 
        p0   p2
        
app : nums= [ 1 2 2 2 1 0 0 1 1 ]

  1 2 2 2 1 0 0 1 1        nums[cur]==1 donc on avance le cur simplement , cur+=1 :
  ^               ^
p0,cur            p2

  1 2 2 2 1 0 0 1 1        nums[cur]==2 , on doit mettre les 2 a la fin donc on swap nums[cur]==2 avec nums[p2]==1 mais comme ce qu'il ya a nums[p2] n'a pas deja etait pris en consideration car 
  ^ ^             ^        on prend en consideration l'idx cur et forcement comme cur est avant p2 tjrs (car la condition de la boucle de l'algo est que cur<=p2 car apres p2 il ya forcement 
 p0 cur           p2       que des 2 donc on a pas besoin de verifier ce qui ce passe apres p2 donc cur est tjrs inf egale a p2 ) donc ce qu'il ya a nums[p2] n'a pas etait pris en consideration
                           (ce qu'il ya apres p2 c'est des 2 donc pas besoin de prendre en consideration) et comme on fait un swap donc ce qu'il ya a p2 ce trouve maintenant a curr donc il faut
                           prendre en consideration a nouveau cur donc on ne fait pas avancer cur quand nums[cur]==2 car apres le swap il faut verifier a nouveau cette position, par contre il
                           faut faire p2-=1 car on a mit un 2 a p2 donc maintenant il faut reculer p2 car p2 pointe sur la limite inferieur des 2. en resume quand nums[cur]==2 alors on fait 
                           swap puis p2-=1 (on ne fait pas cur+=1)
                          
  1 1 2 2 1 0 0 1 2       nums[cur]==1 donc on avance le cur simplement , cur+=1 : 
  ^ ^           ^        
 p0 cur         p2    

  1 1 2 2 1 0 0 1 2       nums[cur]==2 donc swap(nums[cur],numsp[p2]) puis p2-=1 (on ne fait pas cur+=1) : 
  ^   ^         ^        
 p0  cur        p2 
 
  1 1 1 2 1 0 0 2 2       nums[cur]==1 donc on avance le cur simplement , cur+=1 : 
  ^   ^       ^        
 p0  cur      p2 
 
  1 1 1 2 1 0 0 2 2       nums[cur]==2 donc swap(nums[cur],numsp[p2]) puis p2-=1 (on ne fait pas cur+=1) :
  ^     ^     ^        
 p0   cur     p2 
 
  1 1 1 0 1 0 2 2 2       nums[cur]==2 donc swap(nums[cur],nums[p2]) puis p2-=1 (on ne fait pas cur+=1) :
  ^     ^   ^        
 p0    cur  p2 

  1 1 1 0 1 0 2 2 2       nums[cur]==0, on doit mettre tout les 0 au debut donc on doit swap nums[cur]==0 avec nums[p0]==1 , il ya deux possibilite la premiere: p0==cur la deuxieme : p0<cur .  
  ^     ^   ^             dans le cas ou p0==cur ca veut dire que p0 n'a pas encore etait pris en consideration donc nums[p0] peut etre egale a 0,1,2 donc si dans ce cas nums[cur]=nums[p0]=0 
 p0    cur  p2            alors on fait swap(nums[p0],nums[cur]) ( ce qui ne change rien techniquement car p0==cur) puis on avance p0: p0+=1 et on avance cur car on vien de prendre en 
 consideration nums[cur] qui pouvait etre 0 1 ou 2 (on a pas besoin de reverifier nums[cur] apres le swap car on swap forcement 0 avec 0  donc on sait que apres le swap il ya 0 a nums[cur] ).
 dans le deuxieme cas ou p0<cur , p0 a forcement etait pris en consideration car cur est sup donc nums[p0] peut etre egale a 1 seulement car si il etait egale a 0 alors forcement ca peut pas etre 
 p0 car p0 vient apres le dernier 0 , il ne peut pas etre 2 car comme il a deja etait pris en consideration forcement qu'il se trouve apres cur car a chaque fois que cur rencontre un 2 il le met
 a la fin , donc dans le deuxieme cas forcement que nums[p0]=1 donc quand on lit nums[cur] et on fait swap avec nums[p0] alors maintenant a nums[cur] on a forcement 1 donc on peut faire cur+=1.
 donc dans les 2 cas on voit que on peut forcenment faire cur+=1 apres le swap et qu'on a pas besoin de verifier a nouveau nums[cur] apres le swap . donc en resume quand nums[cur]==0 on fait 
 swap(nums[cur],nums[p0]) on avance p0 car il contient apres le swap le 0 et on fait cur+=1 :
 
  0 1 1 1 1 0 2 2 2       nums[cur]==1 donc on avance le cur simplement , cur+=1 : 
    ^     ^ ^              
   p0   cur p2
   
  0 1 1 1 1 0 2 2 2       nums[cur]==0 donc swap(nums[cur],nums[p0]) , p0+=1, cur+=1 :
    ^       ^              
   p0    cur,p2
   
  0 0 1 1 1 1 2 2 2       puisque cur>p2 on a fini car tout ce qui est apres p2 est forcement 2 (et si on continue on va faire swap(nums[cur],nums[p2])) ce qui va fausser le resultat)
      ^     ^ ^              
     p0    p2 cur
 
                          
TC : comme on peut le voir on passe que une fois sur nums donc O(n)                      
                        """
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0  #pointe apres les 0
        p2 = len(nums) - 1 #pointe vant les 2

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:  # if nums[curr] == 1:
                curr += 1

"""attention : la deuxieme solution est juste pour l'idee elle ne reponds pas au exigences de la consignes !!!!
c'est juste une idee plus facile"""                
                
"""deuxieme sol mais elle est #two pass , la consigne demande un one pass(regarder follow up)!!!!!!! #in-place  #TC O(n) #SC O(1)
on calcule simplement le nombre de 0 , 1 et 2 . ex si il ya 3fois 0 , 2 fois 1 et 2 fois 2 alors on fait nums[0:3] contient que des 0 puis nums[3:5] contient que des 1 et efin nums[5:7] contient que des 2 """
                
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        c0 = 0
        c1 = 0
        c2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] == 1:
                c1 += 1
            else:
                c2 += 1
        
        for i in range(len(nums)):
            if c0 > 0:    #d'abord on vide les 0
                nums[i] = 0
                c0 -= 1
            elif c1 > 0:  #puis on vide les 1
                nums[i] = 1
                c1 -= 1
            else:         #puis on vide les 2
                nums[i] = 2
                c2 -= 1
        
"""a la place du dernier for on peut mettre :
    nums[:c0] = [0] * c0
    nums[c0:c0+c1] = [1] * c1
    nums[c0+c1:] = [2] * c2"""
