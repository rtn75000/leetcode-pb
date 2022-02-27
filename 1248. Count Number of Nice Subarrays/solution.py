"""sliding windows (sans hash table)
l'idee est la suivante : 
-on a deux pointeur un qui represente le cote gauche de la fenetre et l'autre le cote droit. 
-le cote gauche ne bouge pas tant qu'on a pas atteint k nombres impaires a l'aide du pointeur de droit par exemple dans l'exemple nums = [2,2,2,1,2,2,1,2,2,2], k = 2 le pointeur de gauche:left sera egale a 0 alors que 
le pointeur de droite:right sera egale a 6 cad on aura lafenetre suivante [2,2,2,1,2,2,1]
- a partir du moment ou la fenetre contient k nombres impaires on rentre dans la boucle while qui fait avancer le pointeur de gauche jusqu'a qu'il atteigne un nombre impaire (ou il fait odd_cnt-=1 donc la condition
du while devient false) cad dans notre cas la fenetre va etre [2,2,1] a chaque fois qu'on a fait avancer left on rajoute une subfenetre ici on a 4 ([2,2,2,1,2,2,1],[2,2,1,2,2,1],[2,1,2,2,1][1,2,2,1])
-une fois le while fini dans notre cas cur_sub_cnt va etre egale a 4 ce qui va faire que ans+=4 et a chaque fois qu,on s'avance a droit a l'aide du for on fait ans+=4 car a chaque fois qu'on rajoute un element a droite 
on peut le combiner avec un element a gauche : [2,2,2,1,2,2,1,2] donne 4 nouvelle possibilitees : [2,2,2,1,2,2,1,2],[2,2,1,2,2,1,2],[2,1,2,2,1,2] et [1,2,2,1,2]
- au finale on a faite ans+=4 4fois cad 16

la comprehension est prise d'ici :https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/508217/C%2B%2B%3A-Visual-explanation.-O(1)-space.-Two-pointers
le code d'ici:https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/1265615/Python-Two-pointer
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = ans = odd_cnt = cur_sub_cnt = 0

        for right in range(len(nums)):
            
            if nums[right]%2 == 1: #cad si impaire
                odd_cnt += 1 #alors incrementer le nombre d'impaires
                cur_sub_cnt = 0 #remettre a 0 le compte de subsequence car on a une nouvelle fenetre  
                
            while odd_cnt == k:
                if nums[left]%2 == 1:  # si le pointeur de gauche rencontre un impaire cad on reduit la fenetre a gauche du coup on paire un impaire d'ou on reduit le compte d'impaire a la ligne suivante 
                    odd_cnt -= 1
                left += 1    
                cur_sub_cnt += 1 # a chaque fois que on reduit la fenetre a gauche c'est une nouvelle subfenetre
                
                
            ans += cur_sub_cnt # appartient au for a chaque fois qu'on savance a droite on rerajoute le nombre de fentre calculer a gauche 
            
        return ans 
