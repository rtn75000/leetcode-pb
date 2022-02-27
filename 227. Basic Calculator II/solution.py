"""petit rappel le * et / se calcule avant le + et - doc 3+2*2 c'est comme 3+(2*2) cad 7 (et pas 10)"""
""" 
# iterative # TC O(n) # SC O(n)
le code et explication : https://leetcode.com/problems/basic-calculator-ii/discuss/658480/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
en faite on rentre dans le stack +x ou -x et des que on a *ou/ on pop de la stack et on fait *x ou /x au pop
exemple d'app sur 3+2*2 : 
idx=1  num=3 sign='+' stack=[3]
idx=3  num=2 sign='+' stack=[3,2]
idx=5  num=3 sign='*' stack=[3,2*2]=[3,4]  (celui la est du au update en dehors de la boucle while)
return sum(stack) cad 7 (3+4)
"""
class Solution:
    def calculate(self, s):    
        def calc(idx):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))
        
            num, stack, sign = 0, [], "+"
            
            while idx < len(s):
                
                if s[idx].isdigit():
                    num = num * 10 + int(s[idx])
                    
                elif s[idx] in "+-*/":  #on calcule et met dans le stack ce qui se trouve a gauche du signe s[idx]
                    update(sign, num) # sign is the sign before the sign of s[idx]
                    num, sign = 0, s[idx]
        
                idx += 1
            
            update(sign, num) # pour le dernier sign rencontrer
            return sum(stack)

        return calc(0)
    
"""#iterative #TC O(n)  #SC O(1) no stack
code (ds commentaire) et explication d'ici  : https://leetcode.com/problems/basic-calculator-ii/discuss/947074/python-simple-concise-fast-wo-extra-space

The idea is that when we see an operator, we must wait until we know what the number on the right side of it is and what is the operator after it (if we have + or -). The left side is pre, right side is cur, and the operator is op. Whenever we get to the next operator, we can start evulating our pre, op, cur combination.

If op is * or a /, we can immediately perform our operation since * or a / have precedence over + or a -. Hence (donc , par consequent) pre = pre*cur if op == '*' else int(pre/cur). However, If op is a + or a -, we cannot discredit the possibilty that the next operator is a * or a /, but we can add the left side of + or - to the result , so we add pre to res. For example:

input: 3-2*4
explanation: (etat des variable a la fin de la boucle)
index 0 (c:3) : pre = 0, cur = 3, op = +,  res = 0
index 1 (c:-) : pre = 3, cur = 0, op = -,  res = 0
index 2 (c:2) : pre = 3, cur = 2, op = -,  res = 0 
index 3 (c:*) : pre = -2, cur = 0, op = *,  res = 3
index 4 (c:4) : pre = -2, cur = 4, op = *,  res = 3
index 5 (c:+) : (car on rajouter + a la fin juste pour faire encore une interaction parceque la boucle a un cout de retard pour calculer afin de voir si il ya un * ou diviser donc on veut refaire la boucle a la fin pour calculer le dernier pre=4) :  pre = -2*4, cur = 4, op = *,  res = 3
return 3 + (-8) = -5"""

class Solution:
    def calculate(self, s: str) -> int:
        op = '+'
        pre = 0; cur = 0; res = 0
        for c in s+'+':   
            
            if c.isdigit():
                cur = 10*cur + int(c)
                
            elif c in '+-*/':
                if op == '+': 
                    res += pre
                    pre = cur
                elif op == '-': 
                    res += pre
                    pre = -cur
                elif op == '*': 
                    pre = pre*cur
                elif op == '/':
                    pre = int(pre/cur)
                cur = 0 
                op = c
                
        return res+pre
