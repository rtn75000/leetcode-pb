"""#TC O(len(nums)) #SC O(k) the max size of the queue that correspond to the sie of the windows. 
le code et explication d'ici: https://leetcode.com/problems/sliding-window-maximum/discuss/951683/Python-Decreasing-deque-short-explained
voir aussi ma solution a ce pb qui a des idees ressamblante : https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
l'idee est d'utiliser une decreasing queue cad que a en tete on aura toujours le max,  si on rajoute une valeur superieur a la precedente on devra supprimer la precedente jusqu'a ce que on conserve l'ordre decroissant .
ici on va conserver l'index des valeurs dans le max_queue : l'index qui se trouve en tete sera celui de la valeur max de la fenetre 
"""

class Solution:
    def maxSlidingWindow(self, nums, k):
        max_queue = deque()
        ans = []
        #la fenetre sera de r-k a r (r sera le dernier index a droite)
        for r in range (len(nums)):
            
            # tant que le max_queue n'est pas vide et que la valeur en tete de max_queue qui est l'index de la valeur max dans notre fenetre, est inferieur a l'index le plus a gauche de la fenetre on devra donc retirer cette index de max_queue car il est mainteneant en dehors de notre fentre 
            while max_queue and max_queue[0] <= r - k:
                max_queue.popleft()
                
            # tant que max_queue n'est pas vide et que la valeur a droite qu'on veut introduire (son indexe) dans max_queue est superieur a la derniere valeurs(cad indexe) introduit dans le max_queue on supprime cette derniere valeur introduit pour conserver un ordre decroissant
            while max_queue and nums[r] >= nums[max_queue[-1]] :
                max_queue.pop()
                # une fois avoir supprimer toute les indexe des valeurs inferieur a notre nouvelle valeur on peut introduire l'indexe de notre nouvelle valeur
            max_queue.append(r)
            
            ans.append(nums[max_queue[0]])
            
        # les k-1 premiere valeurs rajouter sont avant qu'on est une fentre complete donc on les retourne pas 
        #(exemple si on a : [3,1,2,4] avec k=3 alors notre algo donne ans=[3,3,3,4] donc on retourne que ans[3-1:] cad [3,4] )
        return ans[k-1:]
