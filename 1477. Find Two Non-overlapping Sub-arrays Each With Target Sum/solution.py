"""#sliding-windows
le code d'ici : https://www.youtube.com/watch?v=63K9MYDfEEc&ab_channel=RickyCho
L'idee est la suivante :
on va utiliser un array (mins) supplementaire où a l'index i on mettra la valeur de la plus petite sub array obtenue jusqu'a l'index i de l'array de base arr, exemple : arr=[1,1,1,2,2,3] alors mins=[inf,inf,inf,4,3,2]
(inf c'est quand on a pas de sub array jusqu'a l'index i) cad que si on prend la valeur 3 par exemple qui se trouve a l'index 4 ca veut dire que la plus petite sub array trouver jusqu'a l'index 4 est de taille 3.
deuxieme points tres important : pour le resultat (output) on a besoin des deux plus petites sub-array, pour cela on prend la taille de la plus petite sub array trouver jusqu'au debut de la sub-array qu'on traite
actuellement(on prend le debut pour ne pas avoir de overlapping sub-array) puis on additionne a la plus petite sub-array la taille de la sub array actuelle.

app: 1-   arr=[1,1,1,2,2,3,5] ==> mins=[inf,inf,inf,4,inf,inf,inf]
               S     C     (S:start, C:curr_idx)
           
           
          arr=[1,1,1,2,2,3,5] ==> mins=[inf,inf,inf,4,3,inf,inf]
                   S   C     
          ici on obtient une deuxieme sub-array mais comme le debut de celle-ci est a l'index 2 et on sait qu'on a pas de sub-array jusqu'a l'index 2 (mins[2-1]==inf) donc pour l'instant on a pas de paire de sub-array
          


          arr=[1,1,1,2,2,3,5] ==> mins=[inf,inf,inf,4,3,2,inf]
                       S C              
          ici on obtient une autre sub-array (de taille 2) , le debut de celle-ci est a l'index 4 , on voit que mins[4-1]==4 cad qu'il ya une autre sub-array de taille 4 qui fini avant le debut de celle-ci donc la on a deux sub-array petites et compatible donc output=min(inf,4+2)=6

          arr=[1,1,1,2,2,3,5] ==> mins=[inf,inf,inf,4,3,2,1]
                           SC  
           ici on obtient une autre sub-array (de taille 1) , le debut de celle-ci est a l'index 6 , on voit que mins[6-1]==2 cad qu'il ya une autre sub-array de taille 2 qui fini avant le debut de celle-ci donc la on a deux sub-array petites et compatible donc output=min(6,2+1)=3.
           ccl: output =3 
           
          
          
     2-   arr=[3,2,2,1,1,1] ==> mins=[inf,2,inf,inf,inf,inf]
               S C     (S:start, C:curr_idx)
           
           
          arr=[3,2,2,1,1,1] ==> mins=[inf,2,2,2,inf,inf]
                 S   C     (S:start, C:curr_idx)  
          ici on obtient une deuxieme sub-array (de taille 3) mais comme le debut de celle-ci est a l'index 1 et on sait qu'on a pas de sub-array jusqu'a l'index 1 (mins[1-1]==inf) donc pour l'instant on a pas de paire de sub-array         


         arr=[3,2,2,1,1,1] ==> mins=[inf,2,2,2,2,inf]
                  S     C     (S:start, C:curr_idx)             
          ici on obtient une autre sub-array (de taille 4) , le debut de celle-ci est a l'index 2 , on voit que mins[2-1]==2 cad qu'il ya une autre sub-array de taille 2 qui fini avant le debut de celle-ci donc la on a deux sub-array petites et compatible donc output=min(inf,4+2)=6
           ccl: output = 6          
           
"""
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        mins = [float('inf')] * n  
        start = curr_sum = 0
        curr_min = output = float('inf')
        for curr_idx in range (n) : 
            curr_sum += arr[curr_idx]
            while curr_sum > target : # si on depasse le target on retire un element du debut de la somme et on avance l'index du start 
                curr_sum -= arr[start]
                start+=1
            if curr_sum == target : 
                lenght = curr_idx - start + 1   # la taille de a à b c'est toujours b-a+1
                if start != 0 and mins[start - 1]  != float ('inf') :  # on modifie le output (cad les deux plus petite sub-array trouver) que si il ya deux sub-array donc si le start de la sub-array actuelle est egale a 0 ca veut dire que on a pas de sub-array avant car c'est forcement la premiere sub-array trouver. et aussi si il ya pas de sub array trouver avant le debut de la sub-array actuelle (cad que min[start-1] == inf) ca veut dire que on a que une sub-array. donc pas la peine de modifier le resulat (car on compare que des paire entre eux donc des que on a notre premiere paire on modifie le output puis a chaque fois qu'on a d'autre paire on comapre qui est la plus petite paire)
                    output = min( output , mins[start-1] + lenght )
                curr_min = min( curr_min , lenght)  # on prend le min entre la taille de la sub-array actuelle et la taille de la plus petite sub-array rencontrer jusqu'a present.
            mins[curr_idx] = curr_min 
        return output if output != float('inf') else -1   
    
