"""#my sol #bult-in sort #TC O(n log n) cout du sort  #SC O(1) en python le list.sort se fait in place cad il n'utilise pas un array supplementaire pour trier l'array d'origine il fait le trie sur le meme array.
en general on ne considere pas l'espace du output comme extra space donc on ne considere pas le space O(n) de res comme extra space 
la solution est tres simple  on trie d'abord l'array ensuite si end(i) et sup egale a start(i+1) ca veut dire que i et i+1 sont overlapping et donc on le merge en un element : [start(i),end(i+1)] si end(i)<end(i+1)
(ex : [1,3] et [2,4] ca donne [1,4]) ou [start(i),end(i)] si end(i)>end(i+1) (ex : [1,4] et [2,3] ca donne [1,4])"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()     # TC O(n*logn)
        res=[intervals[0]]   # we do not consider space required for output, when we analyse space requirement.
        for i in range (1,len(intervals)) :
            if res[-1][1] >= intervals[i][0] :         #si end(i) >=start(i+1) so overlapping
                if res[-1][1]<=intervals[i][1]:        #si end(i)<=end(i+1)
                    res.append([res.pop()[0],intervals[i][1]])   #append([start(i),end(i+1)])
                else :                                 #si end(i)>end(i+1)     
                    hlp=res.pop()                               
                    res.append([hlp[0],hlp[1]])                  #append([start(i),end(i)])
            else :         #si end(i) < start(i+1) no overlapping
                res.append(intervals[i])
        return res
    
"""meme idee code juste plus court, pas le mien"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        merged = [intervals[0]]
        for interval in intervals:
            # if the current interval does not overlap with the previous, simply append it.
            if  merged[-1][1] < interval[0]:  #si end(i) < start(i+1) no overlapping
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
