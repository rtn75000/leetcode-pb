"""remarque: si on a [5,10] et [10,15] alors on considere que les meeting sont pas en meme temps. 
"""

"""# greedy #built-in sort #not my sol #TC O(n log n)  #SC O(n)
on va utiliser 2 array une array qui contient les start et une qui contient les end on va les sort . on aura deux pointeurs un pointeur sur les start et un sur les end , on fait avancer le pointeur sur les start tant que
start<end si end >= start (on fait aussi egale car si on a par exemple [5,10] et [10,15] alors on considere que les meeting sont pas en meme temps donc on fini d'abord le premier puis on ouvre un room pour le deuxieme) 
alors on fait avancer le pointeur sur les end. A chaque fois qu'on lit un start alors on ouvre une conference room (on incremente le compte de 1) et a chaque fois qu'on lit un end alors on ferme une conference room 
(on decremente le compte de 1). la reponse va etre le maximum de conference room ouvert en meme temps .
ce qui nous interrese c'est de parcourir tout les start car apres les avoir parcourut on sait cbm de conference room on etait ouvert au max . 

neetcode video (voir apartir de la 6e minute) : https://www.youtube.com/watch?v=FdzJmTCVyJU&ab_channel=NeetCode
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([val[0] for val in intervals])  # [val[0] for val in intervals] nous donne une list de tout les start puis on fait sorted dessus ce qui nous sort les start. 
        end = sorted([val[1] for val in intervals])
        
        startIdx = endIdx = res = count = 0
        
        while startIdx < len(start) : 
            if start[startIdx] < end[endIdx] : 
                startIdx += 1  
                count += 1  # on ouvre une conference room
            else :  # if start[startIdx] > = end[endIdx] :
                endIdx += 1 
                count -= 1  # on ferme une conference room 
            res = max(res,count)
        
        return res
