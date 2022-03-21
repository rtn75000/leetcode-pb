"""#algo to find next permutation #TC O(n) #SC O(1)
cette solution est pas du tout simple a trouver ou on a le pattern est c'est facile mais si on la pas c'est super complique (dans la solution officiel une enorme partie de la communaute
se plein de la difficulter mais je fais cette exo car il est frequemment demander donc il faut retenir le patern qui est algo connu pour trouver le next permutation.)
pour comprendre voir l'animation de la solution officiel (j'ai aussi mit une photo sur git qui explique tres simplement le pattern.) les etapes de l'algo sont les suivante  : 
- trouver le premier element de la partie decroissante en commancent par la fin.
- trouver le successsor (cad l'element superieur qui vient juste apres) de l'element qui precede le premier element de la partie decroissante .
- swap le succesor et l'element qui precede le premier element de la partie decroissante 
- reverse la partie decroissante 
le resulat va etre le successor. 
remarque: si arr est decroissant tel que par exemple 321 alors la next permutation est la premiere permutation cad 123 cad on fait seulement reverse sur arr.
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        
        #trouver l'idx du premier element de la (premiere) partie decroissante en commancent par la fin 
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
            
        # si i==0 cad il ya pas de partie decroissante donc arr est croissante donc le next permutation est le reverse de arr
        if i == 0:   # nums are in descending order
            nums.reverse()  #TC:O(n) SC:O(1)
            return 
        
        k = i - 1    # index de l'element qui precede l'idx du premier element de la (premiere) partie decroissante en commancent par la fin (on l'appelera pivot)
        # recherche idx du successor (j)
        while nums[j] <= nums[k]:  #O(n)
            j -= 1
            
        # swap between pivot and successor
        nums[k], nums[j] = nums[j], nums[k]  
        
        # reverse the second part
        l, r = k+1, len(nums)-1  
        while l < r:  #O(n)
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
