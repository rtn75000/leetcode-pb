"""#sliding windows#hashtable
solution d'ici: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/425720/Python-dictionary-unrolling
"""

import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        myDictP=collections.Counter(p)
        myDictS=collections.Counter(s[:len(p)]) # on commence par analyser une fenetre dans s de la taille de p 
        res=[]
        start=0
        end=len(p)
        
        while end<=len(s):
            if myDictS==myDictP:
                res.append(start)

            myDictS[s[start]]-=1
            if myDictS[s[start]]==0:
                myDictS.pop(s[start]) # on supprime le key:value du dictionary si ca valeur est egale a 0 pour pouvoir entrer d'autre key sans depasser la taille du dictionaire de P
                
            if end<len(s):    
                 myDictS[s[end]]+=1 #meme si le key s[j] n'existe pas on peut incrementer dans Counter (voir dictionary python dans evernote)
            end+=1
            start+=1
            
        return res
