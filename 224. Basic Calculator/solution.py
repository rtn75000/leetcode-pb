"""# iterative solution #TC O(n)  #SC O(n) for the stack
le code et explication on ete pris de la solution officiel (compte premium).
l'idee est la suivante :
a chaque fois que on rencontre + ou - on calcul ce qui ce passe a gauch de se signe et on conserve le signe pour la prochaine iteration. quand on ouvre une parenthese on garde le resultat et le signe d'avant la 
parenthese dans le stack puis on reinitialise les variables. si on rencontre la fermeture de la parenthese alors on calcul ce qui est dans la parenthese ce qui va etre garder dans la variable res, puis on applique
sur res le signe qui etait avant la parenthese qui se trouve au top de la stack , puis on rajoute le resultat qui preceder le signe de la parenthese. 
remarque: ici le signe est tout simplement 1 si plus ou -1 si minus car on multipliera par le signe donc ca reviendra au meme.
l'algo calcul A+B-C comme ca: A+B+(-C)
"""
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        num = res = 0
        sign = 1 # 1 cad positive, -1 cad negative  

        for ch in s:
            if ch.isdigit():

                # Forming num, since it could be more than one digit
                num = (num * 10) + int(ch)

            elif ch == '+':

                # calculer l'expression a gauche du '+',
                # avec result qui est le resultat obtenue avant num+qqch, sign c'est le signe avant le num donc celui avant '+', num
                res += sign * num

                # sauvgarder le '+'
                sign = 1

                # Reinitialiser num
                num = 0

            elif ch == '-':
                
                # calculer l'expression a gauche du '-',
                res += sign * num
                
                # sauvgarder le '-'
                sign = -1
                
                num = 0

            elif ch == '(':

                # Push the result and sign that are before '(' to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset sign and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # calculer l'expression a gauche du ')' cad l'expression dans les parenthese
                res += sign * num

                # ')' marks end of expression within a set of parenthesis
                # stack.pop() is the sign before the parenthesis
                res *= stack.pop() #  pop sign

                # Then add the result calculated before this parenthesis
                # (res in stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # pop res of stack

                # Reset the num
                num = 0

        return res + sign * num
    
"""# recursive solution  #TC O(n)  #SC O(n)
le code et explication d'ici (voir solution 2): https://leetcode.com/problems/basic-calculator/discuss/1456850/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
How to deal with brackets : 
If we want to be able to process the brackets properly, all we need to do is to call our calculator recursively! When we see the open bracket (, we call calculator with the rest of our string, and when we see closed 
bracket ')', we give back the value of expression inside brackets and the place where we need to start when we go out of recursion.
[regarder problem 227 basic calculator II ya une expliquation de comment ca marche]
"""
class Solution:
    def calculate(self, s):    
        def calc(idx):
            
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
        
            num, stack, sign = 0, [], "+"
            
            while idx < len(s):
                if s[idx].isdigit():  #calcule le num
                    num = num * 10 + int(s[idx])
                elif s[idx] in "+-":  
                    update(sign, num) #rajoute le num et le signe qui le precede (pas celui apres par defaut le signe est + car le premier nombre n'a pas forcement de signe avant) dans le stack
                    num, sign = 0, s[idx]  
                elif s[idx] == "(":  # 
                    num, j = calc(idx + 1) # calc retourne apres la parenthese qui ferme le resultat de la parenthese et l'index qui est apres la parenthese
                    idx = j - 1 #donne l'index de la parenthese
                elif s[idx] == ")":
                    update(sign, num)
                    return sum(stack), idx + 1
                idx += 1
                
            update(sign, num)
            return sum(stack)

        return calc(0)
