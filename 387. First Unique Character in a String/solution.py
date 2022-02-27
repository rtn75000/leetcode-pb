""" # TC O(n)  #O(1) because English alphabet contains 26 letters.
la solution utilise tout simplement un hashmap (la solution avec queeue est plus longue et inutile).
le code est pris de la solution propose dans le pb .
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
    
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
