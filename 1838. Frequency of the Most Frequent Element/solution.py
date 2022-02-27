"""#pas ma solution #sliding windows #TC O(n log n) #SC O(1) in python car ne prend pas nlogn de space pour le sort

super video explicative : https://www.youtube.com/watch?v=vgBrQ0NM5vE&ab_channel=NeetCode 

avant de commencer il nous faut un array sorted car cela permettra de faire notre algorithme . on utilisera deux pointeur pour delimiter le slinding window : left et right  
l'idee est la suivante :  right pointe sur l'element au quel on veux faire valoire tout les autres elements de la window , par ex si on a nums = [1,1,1,2,2,4] avec left pointe sur le premier 1 et right qui pointe sur
le premier 2 alors notre windows est la suivante : [1,1,1,2] comme right pointe sur 2 ca veut dire que on veux que tout les elements de la window  soient egale a 2 donc puisu'il ya 4 element ca veut dire que on a en 
tout 2*4 unites dans la window soient num[right]*lenWindow soit nums[right]*(right-left+1). l'incrementation des elements de la windows depend du nombre de 1 qu'on peut ajouter cad il depend du nbr de k. il faut que 
nums[right]*(right-left+1) <= sum(window)+k car la sum de windows c'est ce qu'on a avant de rajouter les k unites donc c'est combien on a avant la modification a cela on peut rajouter k unites , pour faire valoire tout
les autres elements de la window a nums[right] il nous faut en tout nums[right]*(right-left+1) unites mais si ce nombre est sup a sum(window)+k alors on ne peut faire valoire a nums[right] les elements car on a pas
assez d'unite , donc si c'est sup on doit faire avance le right . a chaque fois qu'on a une fenetre qui satisfait l'inequation nums[right]*(right-left+1) <= sum(window)+k alors on la taille de la fentre est une reponse
possible car ca veut dire que on peut incrementer tout les element de cette fentre afin qu'ils osient tous egaux a nums[right] de la fenetre donc on a lenWindows element qui sont egaus soit (right-left+1) element egaux 
dans cette fentre . on va gardre ce nombre et on va le comparer avec les autres potentiel reponse , on gardera que le max a chaque fois car on veux le max d'elements egaux. 

app : nums = [ 1, 1, 1, 2, 2, 4] avec k=2 

 [ 1, 1, 1, 2, 2, 4]       nums[right]*(right-left+1) <= sum(window)+k  car 1*1<=1+2 donc len([1]) est une reponse potentiel donc res=max(res,(right-left+1)) cad res=max(0,1) donc res=1 
   ^
left/right 

on fait avancer right : 
 [ 1, 1, 1, 2, 2, 4]       nums[right]*(right-left+1) <= sum(window)+k  car 1*2<=2+2 donc len([1,1]) est une reponse potentiel donc res=max(res,(right-left+1)) cad res=max(1,2) donc res=2 
   ^  ^
left right 

on fait avancer right : 
 [ 1, 1, 1, 2, 2, 4]       nums[right]*(right-left+1) <= sum(window)+k  car 1*3<=3+2 donc len([1,1,1]) est une reponse potentiel donc res=max(res,(right-left+1)) cad res=max(2,3) donc res=3 
   ^     ^
left   right 

on fait avancer right : 
 [ 1, 1, 1, 2, 2, 4]       nums[right]*(right-left+1) > sum(window)+k  car 2*4>5+2 donc on reduit la fenetre on fait avance left ce qui donne [ 1, 1, 1, 2, 2, 4]  comme 
   ^        ^                                                                                                                                      ^     ^
left      right                                                                                                                                  left   right
                           nums[right]*(right-left+1) <= sum(window)+k car 2*3 <=4+2 donc len([1,1,2]) est une reponse potentiel donc res=max(res,(right-left+1)) cad res=max(3,3) donc res=3 

on fait avancer right : 
 [ 1, 1, 1, 2, 2, 4]       nums[right]*(right-left+1) <= sum(window)+k  car 2*4<=6+2 donc len([1,1,2,2]) est une reponse potentiel donc res=max(res,(right-left+1)) cad res=max(3,4) donc res=4 
      ^        ^                                                                                                                                      
    left      right   
    
on fait avancer right : 
 [ 1, 1, 1, 2, 2, 4]       nums[right]*(right-left+1) > sum(window)+k  car 4*5>10+2 donc on reduit la fenetre on fait left+=1 tant que nums[right]*(right-left+1) > sum(window)+k, cette condition
      ^           ^        va etre vrai jusqu'a ce qu'on fasse avance left jusqu'au 2eme 2   cad   [ 1, 1, 1, 2, 2, 4]   ou la on a nums[right]*(right-left+1) <= sum(window)+k  car 4*2<=6+2
    left        right                                                                                            ^  ^           ce qui donne len([2,4]) comme reponse potentiel donc
                                                                                                               left right         res=max(res,(right-left+1))  cad res=max(4,2) donc res=4
                                                                                                               
puisque on ne peut plus faire avancer right on a fini .                                                                                                              
"""
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()    #O(nlogn)
        res=winSum=left=right=0
        for right in range(len(nums)) : 
            winSum+=nums[right]   # on update la sum de la fentre a chaque fois qu'on rajoute un element
            # on a pas besoin de rajouter la condition left<len(nums) car forcement quand left va etre egale a right alors nums[right]*(right-left+1) <= winSum+k donc on ne va pas continuer le     
            # while forcement (quand left==right la fentre et de taille une donc on a rien a rajouter donc forcement que on sera inferieur a  winSum+k)
            while nums[right]*(right-left+1) > winSum+k : 
                # on fait avance left donc on doit retire la valeur de left de la fenetre 
                winSum -= nums[left]
                left += 1 
            # si  nums[right]*(right-left+1) <= winSum+k :
            res = max(res,right-left+1)
            right+=1
        return res
