""" #set:
solution n1 : https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak 
l'idee est que on utilise un set qui supprime les duplicates et est implementer a l'aide d'un hash table donc les operation de base sont 0(1) (voir cette article:https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations)
la construction du set est 0(n) car on passe sur tout les membres de l'array est on les met dans le set.
remarque : if x not in set ca revient a chercher si x est dans le set donc ca coute O(1) car c'est implementer avec hash table. """

class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums) # transformer en set
        best = 0  
        for x in nums:
            if x - 1 not in nums:  # on verifie que x est le debut d'une serie car x-1 n'est pas dans le set
                y = x + 1   # y c'est le prochain nombre de la serie 
                while y in nums:  # si y existe 
                    y += 1     # chercher le prochain nombre de la serie
                best = max(best, y - x)  # y est le dernier nombre de la serie ici donc la taille de la serie est x-1
        return best      
    
    
"""remarque: un set c'est comme un dictionnaire mais que avec des key (donc n'a pas de doublons). c'est donc un hash table  """
