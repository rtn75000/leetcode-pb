""" #built-in sort #greedy #TC O(nlogn) #SC O(1) for python (use in place sorting)

on va sort l'array en fonction des start. A chaque fois qu'on a un interval qui overlap (cad qui commence avant que les precendant sont terminees) on "supprime" (cad notre end time va etre celui qui se termine plus tot)
celui qui se termine le plus tard pour minimiser le risque d'overlap pour apres.

neetcode (a partir de la 7eme min): https://www.youtube.com/watch?v=nONCGxWoUfM&ab_channel=NeetCode """
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() #sort en fct du 1er element de chaque element donc en fonction du start de chaque element #on peut aussi ecrire intervals.sort(key = lambda x: x[0])
        res=0  # nbr min d'interval a supprimer 
        prevEnd = intervals[0][1] # prevEnd va etre la fin du dernier interval
        for start,end in intervals[1:] : # on commence a partir du deuxieme element 
            if start>=prevEnd : #si pas d'overlap
                prevEnd = end  #prevEnd devient le current end
            else : #si overlap
                res+=1
                prevEnd=min(end,prevEnd) # on prend celui qui se termine en premier entre le current end et le prevEnd
        return res
