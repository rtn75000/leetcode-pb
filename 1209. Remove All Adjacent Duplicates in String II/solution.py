"""#stack #TC O(n) #SC O(n) for the stack
le code est d'ici : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392939/PythonC%2B%2BJava-Stack-Based-Solution-Clean-and-Concise
l'idee est la suivante on utilise un stack et a chaque fois on lit une lettre du string si celle ci ce trouve au top de la stack alors on ajoute 1 a sa frequence, si non on ajoute au stack[char,1]
(1 indique la frequence ). Si la frequence est egale a k on pop la lettre de la stack.
app :  input:  s = "deeedbbcccbdaa", k = 3
(c:0) stack = [[d,1]]
(c:1) stack = [[d,1],[e,1]]
(c:2) stack = [[d,1],[e,2]]
(c:3) stack = [[d,1],[e,3]] => stack = [[d,1]]
(c:4) stack = [[d,2]]
(c:5) stack = [[d,2],[b,1]]
(c:6) stack = [[d,2],[b,2]]
(c:7) stack = [[d,2],[b,2],[c,1]]
(c:8) stack = [[d,2],[b,2],[c,2]]
(c:9) stack = [[d,2],[b,2],[c,3]] => stack = [[d,2],[b,2]]
(c:10) stack = [[d,2],[b,3]] => stack = [[d,2]]
(c:11) stack = [[d,3]] => stack = []
(c:12) stack = [[a,1]] 
(c:13) stack = [[a,2]] 
return "aa"
"""
 
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # pair of (character, frequence)
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1  # Increase the frequency
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:  # If reach enough k duplicate letters -> then remove
                stack.pop()
        return "".join(char * freq for char, freq in stack) #generator expression ex if stack=[['a',1]['b',2]] generator is [a*1,b*2] meaning [a,bb] (The major difference between a list comprehension and a generator expression is that a list comprehension produces the entire list while the generator expression produces one item at a time.)
