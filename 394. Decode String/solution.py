"""le code a etait pris d'ici: https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
il ya une super explication avec un code diferrent mais quasiment la meme idee ici : https://www.youtube.com/watch?v=qB0zZpBJlh8&ab_channel=NeetCode
l'idee c'est de faire rentrer dans un stack les nombres et lettres et a chaque fois qu'on a un crochet ']' aors on pop les lettres et on les multiplies par le nombre 
"""
"""#iterative   #O(n*O(concatenation of all letters)) TC avec n la taille de s ()  #O(size of decoded string) SC (The maximum stack size would be equivalent to the sum of all the decoded strings )
dans ce code une fois qu'on obtient '[' on met dans le stack le nombre et lettres qui doient etre multiplier """
class Solution:
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''  #curNum contiendra le nombre et curString contiendra les lettres
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c) #*10 pour faire passer le chiffres vers les dizaine centaine etc...
            else:
                curString += c
        return curString       
    
    
"""#recursive # O(n*O(concatenation)) TC  #O(n) SC car on va faire maximun n appel car on ne pourra pas rencontrer plus de n fois le char '[' 
code and explanantion : https://leetcode.com/problems/decode-string/discuss/1167364/Concise-and-simple-recursive-solution"""

class Solution:
    def decodeString(self, s: str) -> str:                         
        
        def recurse(s, pos):       
            result = ""
            i, num = pos, 0
            
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '[':    # If opening bracket, recurse
                    string, end = recurse(s, i + 1)  # recurse return the string and the end index (meaning when the recursion find ']') 
                    result += num * string
                    i = end
                    num = 0
                elif c == ']':
                    return result, i
                else:
                    result += c
                i += 1
            
            return result, i
                
        return recurse(s, 0)[0] # return only the string that recurse return
    
    
    
