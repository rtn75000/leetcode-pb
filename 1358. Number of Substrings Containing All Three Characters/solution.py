"""solution d'ici dans les commentaire de cette reponse : 
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516973/JavaPython-3-Sliding-Window-O(n)-O(1)-code-w-explanation-and-analysis."""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start= 0
        count= 0 
        d = {'a':0,'b':0,'c':0} # ou d={c : 0 for c in 'abc'}

        # on remplie le dictionnaire avec la frencence d'apparition de chaque lettre:
        for i in range(len(s)):  
            d[s[i]]+=1

            while  all(d.values()): # cad while(count[a] && count[b] && count[c]) cad tant que on a toute les lettre au moins une fois
                count += len(s)-i   # on rajoute la taille de s moins i qui est le dernier index qui nous a permis d'avoir les 3 lettres car si on a par exemple abcabc alors le i va etre 2 (la premier fois) cad on a abc on peut rajouter abc abca abcab abcabc cad 4 combinaison soit len(s)-i cad 6-2 combinaison
                d[s[start]] -= 1  # on retire une apparition de la lettre qui etatit l'index de debut car on s'avance d'une lettre 
                start += 1
      
        return count
            
        
        
