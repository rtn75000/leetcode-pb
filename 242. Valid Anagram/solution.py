"""# my sol  #TC O(nlogn +mlogm) avec n == len(s) et m == len(t) #SC O(1) in python
on trie chaque mot d'apres l'ordre alphabetique si les mots sont egaux alors on a des anagrams"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t)==sorted(s) # Note that sorted(str) will return a sorted list of all str char  (str.sort() ne marche pas)
    
"""# my idea #hashtable  #TC O(n+m) #SC O(1) car le hashtable est de taille constante au max 26 
on construit le dict avec s puis on reduit la frequence de ce dict a l'aide de t si la frequence descend en dessous de 0 alors il ya plus de cha """

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        # on doit verifier la taille avant car si on a s='ab' et t='a' alors seulement en verifiant le dic ca suffit pas (car ds la deuxiem boucle on va juste faire d['a']-=1 
        # puis on verra pas qu'il y a un b en plus dans s)
        if len(s)!=len(t):  
            return False
        for char in s : 
            d[char]+=1
        for char in t : 
            d[char]-=1   # meme si char n'est pas key ds dict comme c'est un default dict alors la valeur d[char] sera 0 et donc ca va donner -1 et donc ca va rendre false 
            if d[char]<0 :   
                return False 
        return True 
""" #TC O(n+m) #two hasmap SC O(1) car 2*O(26)"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         return collections.Counter(s) == collections.Counter(t)   # counter est built-in il compte la frequence des lettres 
