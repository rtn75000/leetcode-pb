"""#TC : O(n)  #SC : O(n) car on fait un stack qui peut etre de la taille de s si s est par exemple ((( .
le code et l'explication sont d'ici :https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/663204/Super-simple-Python-solution-with-explanation.-Faster-than-100-Memory-Usage-less-than-100
l'idee est d'utiliser une stack qui contiendra l'indexe des parenthese "(" , des que on rencontre une parenthese ")" on fait pop au stack si le stack est vide a ce moment cad que cette parenthes n'a pas de paire avec "(" 
elle doit donc etre supprimer de la phrase (on remplacera cette parenthese par une empty string ""). si apres etre passer sur toute la phrase s le stack est encore plein cad qu'il ya des parenthese "(" qui n'ont pas de
paire avec ")"  alors on doit supprimer ces parenthese "(" de la phrase (donc tout valeurs d'index present dans le stack sera remplacer par une empty string). a la fin ou retourn le rassemblement de toute la list qui nous
reste 

"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s) # transformer la string en list pour pouvoir la modifier 
        stack = deque()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i) #on rajoute l'index de la parenthese dans la stack
            elif char == ')':
                if stack:  #si stack pas vide 
                    stack.pop()
                else:    #si stack vide 
                    s[i] = ''
        while stack:
            s[stack.pop()] = '' #stack pop retourne l'index des parenthese "("
        return ''.join(s)
