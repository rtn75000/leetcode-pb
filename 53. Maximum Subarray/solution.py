"""#not my sol (#khadane algo)  #array #TC O(n) #SC O(1)
#pas si simple que ca !
l'idee est de comprendre comment varie la somme si la somme qu'on a eu jusqu'a present est inferieur a notre element alors on choisi l'element en tant que nouvelle somme 
ex: [-2,-1] alors au debut sum=-2 puis si on ajoute -1 ca donne -3 donc vaut mieux garder que -1 ca va donc etre notre nouvelle somme .

app : [-2,-3]

val==-2 cur_val=max(-2,0+(-2) cad cur_val==-2 et donc max_till_now = max(-inf, -2)==-2
val==-3 cur_val=max(-3,-2+(-3)) cad cur_val==-3 et donc max_till_now = max(-2, -3)==-2
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:     
        cur_max, max_till_now = 0, -inf
        for val in nums:
            cur_max = max(val, cur_max + val)  #cette ligne est la plus importante a comprendre
            max_till_now = max(max_till_now, cur_max)
        return max_till_now
