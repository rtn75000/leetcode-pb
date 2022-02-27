"""#TC O(n) #SC O(n)
voir code et explication ici : https://leetcode.com/problems/trapping-rain-water/discuss/1374608/C%2B%2BJavaPython-MaxLeft-MaxRight-so-far-with-Picture-O(1)-space-Clean-and-Concise
l'idee est la suivante : 
chaque bar peut receptionner de l'eau que si ca taille est inferieur a la taille de la plus grande bar a sa gauche et a la taille de la plus grande bar a sa droite. Sa capacite sera: min(la taille de la plus grande bar
a sa gauche,la taille de la plus grande bar a sa droite)-la taille de la bar actuelle.
ex :
                    _   
      _         _  |X|       
     |X|      _| | |X|         la 3e bar peut receptionner  : min (6,7)-4 cad 2 unite d'eau
     |X|  _  | | | |X|  
     |X|_| | | | | |X|  
     |X| | | | | |_|X|         la 6eme bar ne peut rien receptionner car ca taille(6) et pas inferieur a  : maxleft(6) and maxRight(7) 
     |X| | | | | | |X|_          
     |X|_|_|_|_|_|_|X|_|
      6 3 4 0 5 6 2 7 1 
      ^   ^         ^
  maxLeft |      maxRight
      [3-eme bar]

-Premier partie determiner maxLeft et maxRight : 
Pour determiner le maxLeft de chaque bar on parcourt la liste de gauche a droite et a chaque fois que on trouve une plus grand bar ca va etre le maxLeft a partir de cette index. on creera une liste qui conserve les
donne de maxLeft (la valeur de l'indexe i sera la taille de la plus grande bar a gauche de i ).
Pour determiner le maxRight de chaque bar on parcourt la liste de droite a gauche et a chaque fois que on trouve une plus grand bar ca va etre le maxRight a partir de cette index. on creera une liste qui conserve
les donne de maxRight (la valeur de l'indexe i sera la taille de la plus grande bar a droite de i ).
dans notre exemple ca donne ca : 
list:     6 3 4 0 5 6 2 7 1
maxLeft:  0 6 6 6 6 6 6 6 7  (commence toujours par 0 car il ya rien a gauche de la premier bar)
maxRight: 7 7 7 7 7 7 7 1 0   (fini toujours par 0 car il ya rien a droite de la derniere bar)

-Deuxieme etape calculer la capaciter d'eau de chaque bar:
Chaque bar peut receptionner de l'eau que si ca taille est inferieur a la taille de la plus grande bar a sa gauche et a la taille de la plus grande bar a sa droite. capacite=min(la taille de la plus grande bar a
sa gauche,la taille de la plus grande bar a sa droite)-la taille de la bar actuelle.
"""
class Solution:  # 52 ms, faster than 81.89%
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        # premiere etape 
        for i in range(1, n):    # on commence a partir de 1 car indexe 0 a forcement une valeur 0 comme explique en haut
            maxLeft[i] = max(height[i-1], maxLeft[i-1])  #max entre la bar qui precede la bar actuelle et le maxLeft obtenue jusqu'a present (on remplie du debut a la fin)
        for i in range(n-2, -1, -1): # on commence a partir de n-2 car indexe n-1 a forcement une valeur 0 comme explique en haut
            maxRight[i] = max(height[i+1], maxRight[i+1])  #max entre la bar qui est juste apres la bar actuelle et le maxRight obtenue jusqu'a present (on remplie de la fin au debut)
        # deuxieme etape    
        ans = 0
        for i in range(n):         
            waterLevel = min(maxLeft[i], maxRight[i]) # le niveau max d'eau est le plus petit entre la plus grande bar a gauche et la plus grande bar a droite 
            if waterLevel > height[i]:   # que si la bar actuelle est inferieur au niveau max de l'eau alors on pourra la remplir 
                ans += waterLevel - height[i]
        return ans
    
    
"""#TC O(n) #SC O(1)
le code d'ici: https://leetcode.com/problems/trapping-rain-water/discuss/1005489/Python-Two-pointer-approach-with-explanation-O(n)-time-O(1)-space

explication:

l'idee est la suivante: si je commence par la gauche et je m'avance vers la droite je peut etre sur que je rencontre avant d'arriver a la n-ieme bar toute les bars qui son a gauche de la n-ieme bar. Meme logique : si 
je commence a droite et m'avance vers la gauche je peut etre sur que je rencontre (en commencant par la droite) avant d'arriver a la n-ieme bar  toute les bars qui son a droite de la n-ieme bar.
on utilisera 2 pointeurs un(left) qui commence a gauche et va vers la droite et un (right) qui commence a droite et va vers la gauche. c'est toujours la meme idee que on peut remplir une bar que jusqu'au min entre la 
bar la plus grande a sa droite et la bar la plus grande a sa gauche.Sauf qu'ici on va le faire sans garder les donnees de la taille des bar dans des listes. 
                       _
         _         _  | |                                      
        | |      _| | | |                                                   
        | |  _  | | | | |  _                                                  
        | |_| | | | | | | | |                                     
        | | | | | | |_| | | |       
        | | | | | | | | |_| |                                       
        |_|_|_|_|_|_|_|_|_|_|      
       
       ----->           <------
   je sais qui        je sais qui
   est le plus        est le plus 
   grand a ma         grand a ma 
   gauche             droite 
 
 
                       _     
         _         _  | |          disons que le schema a gauche est l'etat dans lequel on se trouve alors je sais que left a max_left= 6 et max_right=7 et que right a aussi max_left= 6 et max_right=7.            
        | |      _| | | |          Puisque max_left<max_right je peux etre sur que left peut se remplir que jusqu'a 6 et pas plus car on a decouvert tout les bar a gauche de left et on sais que la plus grande a sa gauche
        | |  _  | | | | |          est 6 donc on peut remplir jusqu'a 6 max (car si on remplie plus ca va deborder a gauche), mais comme max_right>max_left alors je peux pas determiner la limite de right a l'aide de max_right
        | |_| | | | | | |          car max_right et superieur a max_left donc si je remplie jusqu'a max_right ca peut deborder du cote gauche car je sais pas ce qu'il ya apres right si je continue vers la gauche     
        | | | | | | |_| |          c'est possible que la plus grande bar soit 6 ce qui fera un debordement a gauche . Aussi on ne peut determiner la limite de right a l'aide de max_left car si on s'avance vers la gauche c'est 
        | | | | | | | | |          possible que on rencontre une barre plus grande que 6 et donc qu'il y'ai pas de debordement                              
        |_|_|_|_|_|_|_|_|          CCL : que si je connais toute les bars a ma gauche/droite et que la plus grande bar a gauche/droite est inferieur a une bar qui se trouve a ma droite/gauche 
         6 3 4 0 5 6 2 7                 je peut etre sur que ma limite est la plus grande bar a gauche/droite. (ici par exemple si je me trouve a 4 alors je sais que ma limite est 6 car a droite j'ai 7 )
  max_left ^         ^ max_right
         left      right
       --->        <----
        
        
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height)<= 2:  # si ya que 2 il peut pas avoir d'eau 
            return 0
        
        ans = 0
        
        #using two pointers i and j on indices 1 and n-1
        left = 1    # et pas 0 car le premier index et forcement le max de gauche au debut . 
        right = len(height) - 1  # et pas len(height) car le derniere indexe est forcement max de right au debut
        
        #initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        lmax = height[0]
        rmax = height[-1]
        
        while left <=right:
            # check lmax and rmax for left and right positions
            if height[left] > lmax:
                lmax = height[left]
            if height[right] > rmax:
                rmax = height[right]
            
            #fill water upto lmax level for index left and move left to the right
            if lmax <= rmax:
                ans += lmax - height[left]
                left += 1  
				
            #fill water upto rmax level for index right and move right to the left
            else:
                ans += rmax - height[right]
                right -= 1    # minus car on se deplace vers la gauche
                
        return ans
    
    
