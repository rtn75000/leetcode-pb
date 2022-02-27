"""#mySolution #hashTable #slidingWindow #onePass #O(n)
l'ide est la suivante : on passe sur la phrase et a chque fois qu'on rencontre une lettre qui est deja dans la sub-sentence on compare la taille avec les autre subsequence trouver puis on deplace le start apres la
lettre qu'on rencontre a nouveau :
app:curr_idx=5    "abcdefbagklmn"    {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
                   S    C            (S:start C:curr_idx) subSentenceLenght=5-0+1=6 , max_len =6
       
     curr_idx=6   "abcdefbagklmn"   {'a': 0, 'b': 6, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
                     S   C          (S:start C:curr_idx) 
                     
     curr_idx=7   "abcdefbagklmn"   {'a': 0, 'b': 6, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
                     S    C          (S:start C:curr_idx) 
                  ici dictio['a']<start(=2) donc meme si dans le dictio c pas grave car pas dans le sub-sequence
              
     curr_idx=7    "abcdefbagklmn"  {'a': 0, 'b': 6, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
                      S         C  (S:start C:curr_idx), subSentenceLenght=12-3+1=10, max_len =10
                  
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = curr_idx = max_len = 0
        dictio = collections.defaultdict(lambda: -1, {}) #cree un dictionnaire ou les valeur des key innexistante sont par default -1
        for curr_idx in range(len(s)):
            if dictio[s[curr_idx]] < start:  # si la lettre n'est pas dans le dict (la valeur est -1) ou il y est mais la valeur est inferieur au debut de la sub-sequence cad il n'est pas dans cette derniere. 
                dictio[s[curr_idx]] = curr_idx
                max_len = max(max_len, curr_idx-start+1)
            else:
                start = dictio[s[curr_idx]] + 1
                dictio[s[curr_idx]] = curr_idx
                
        return max_len

