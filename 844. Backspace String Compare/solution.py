"""backspace ca supprime un caractere
#TC O(n+m) #SC O(n+m)  (n/m size of s/t) 
le code provient de la solution (1er solution)
la solution est de rentrer les elements dans une stack et faire pop des qu'on a un hashtag a la fin on compare ce qui nous reste si les 2 phrases sont egales alors on rend True. 
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans: #si c==# and stack not empty
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
    
"""#TC O(n+m)  #SC O(1) (si O(1) on aurra pas le droit de conserver une variable avec la phrase modifier car il faut juste rendre true/false (et donc la variable ne fait pas partie de la reponse donc c'est un extra space) )
l'idee est de lire les deux phrase en reverse en meme temps : et de sauter un charactere pour chaque '#' rencontrer . 
le code et explication : https://leetcode.com/problems/backspace-string-compare/discuss/585027/Python-O(N)-Time-O(1)-Space-Solution-or-Explained
"""
class Solution:
	def backspaceCompare(self, S, T):
		
		i = len(S) - 1			# Traverse from the end of the strings
		j = len(T) - 1

		skipS = 0              # The number of backspaces required till we arrive at not a # character
		skipT = 0

		while i >= 0 or j >= 0:
			while i >= 0:					# taking care of s : finding a char to compare
				if S[i] == "#" :
					skipS += 1				
					i = i - 1

				elif skipS > 0:             # if not an '#' but skipS >0 so we need to skip some character of s
					skipS -= 1				
					i = i - 1
 
				else:                       # if it's a char that we don't skip
					break

			while j >= 0:					# taking care of t : finding a char to compare
					if T[j] == "#":
						skipT += 1			
						j = j - 1

					elif skipT > 0:
						skipT -= 1			
						j = j - 1

					else:
						break
                        
			if (i>=0) != (j>=0):		     # il ne faut pas que une phrase fini avant l'autre car ca veut dire que on un char a comparer avec rien cad forcement pas egale
				return False			

			if i>= 0 and j >= 0 and S[i] != T[j]:    # Compare both valid characters. If not the same, return False.
				return False


			i = i - 1
			j = j - 1

		return True					# This means both strings are equivalent.
    
    
