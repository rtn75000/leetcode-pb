"""#TC O(n) #SC O(n)
le code est inspirer d'ici (la bas il met les index a la place de la valeur dans les queues): 
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609708/Python-Clean-Monotonic-Queue-solution-with-detail-explanation-O(N)
video illustrative : https://www.youtube.com/watch?v=LDFZm4iB7tA&t=10s&ab_channel=LeadCodingbyFRAZ
l'idee est la suivante de combiner le sliding windows avec 2 queues.

the absolute difference between any two elements of this subarray =>cad :  "Absolute difference between min and max elements of subarray"
car si on veut que la difference entre n'importe quelle de elements de la subsequence soient en dessous de la limit ca revient a dire que meme la difference entre les extremes soit en dessous de la limit . 
donc a chque fois on prend une fenetre et on fait la difference entre le max et le min.
 
la fenetre s'agrandit vers la droite a chaque fois que le max absolute diff est en dessous de la limit. des que on est au dessus de la limite la fenetre se retrecit a gauche cad on ferme la fenetre de la gauche 
vers la droite.

on utilisera 2 queues une max et une min qui vous contenir en tete de la queue respectivment la valeur max et la valeur min de la sub array .
pour cela la queue max va etre dans l'ordre decroissant comme ca en tete il ya le max et la queue min va etre en ordre croissant comme ca en tete ya le min. 


app: [8,2,4,7]   max: 8   =>  [8,2,4,7]     max: 8,2          max absolute diff= |8-2|=6>limit=4 donc on reduira la fenetre 
      ^          min: 8        ^ ^               ^
     l,r                       l r              head         
                                            min:2 (on a retire 8 car on veut dans l'ordre croissant pour avoir le min dans le head)
                 
                          =>   [8,2,4,7]     max: 2          max absolute diff= |2-2|=0<limit=4 donc on augmentera la fenetre  
                                  ^          min:2     
                                 l,r          
                                 
                          =>   [8,2,4,7]     max: 4 (on supprime deux car on veut ordre decroissant pour avoir max en head)          
                                  ^ ^        min: 2,4         max absolute diff= |4-2|=2<limit=4 donc on augmentera la fenetre                
                                  l r 
                          =>   [8,2,4,7]     max: 7 (on supprime 4 car on veut ordre decroissant pour avoir max en head)          
                                  ^   ^      min: 2,4,7         max absolute diff: |7-2|=5 > limit=4 donc on reduira la fenetre   
                                  l   r 
                          =>   [8,2,4,7]     max: 7           
                                    ^ ^      min: 4,7         max absolute diff: |7-4|=2 < limit=4 donc on augmentera la fenetre   
                                    l r 
                         comme on ne peux plus augmenter la fenetre on a fini et le max size windows == 2

"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = r = 0
        ans = 0  # contient le max size de la windows
        
        while r < len(nums):  # tant que on peut augmenter la fenetre sans depasser la taille du array 
            
#cette partie s'occupe de bien arranger les 2 queues:

# tant que min_dequeu est pas vide (si il est pas vide on doit faire attention que ca reste dans l'ordre croissant/decroissant si il est vide on sans fou car c'est sur que ca change pas l'ordre croissant/decroissant
#si on met qqch dans la queue) et tant que le numero qu'on lit est inferieur/superieur au dernier numero qui est rentrer dans le queue cad que si on met le nouveau num ca va pas etre dans l'ordre croissant/decroissant , 
#on fera pop (qui retire le dernier element introduit) puis apres le while on introduit le nouveau num

            while min_deque and nums[r] < min_deque[-1]:  
                min_deque.pop()
            while max_deque and nums[r] > max_deque[-1]:
                max_deque.pop()
            min_deque.append(nums[r])
            max_deque.append(nums[r])
            
# cette partie s'occupe de trouver le max size windows avec le max absolute diff en dessous de la limite             
# tant que le max (qui se trouve a la tete de la max_queue) moins le min (qui se trouve a la tete de la min_queue) est superieur a la limit on ferme la fenetre de gauche a droite donc on fait avance l (left)
            while max_deque[0] - min_deque[0] > limit: 
               
            # si nums[l] est egale a min_deque[0] cad au minimum de la fenetre alors on doit le retirer de la min_queue 
                if nums[l] == min_deque[0]:
                    min_deque.popleft()
                if nums[l] == max_deque[0]:
                    max_deque.popleft()
                    
                l += 1
                
            ans = max(ans, r - l + 1)
            r += 1
                
        return ans
        
