""" #solution recurive+stack  #TC O(n)  #SC O(n)
voir explication dans pb Basic Calculator II et Basic Calculator ce pb et la combinaison des 2 (le code est quasiment le meme) :
- https://leetcode.com/problems/basic-calculator/
- https://leetcode.com/problems/basic-calculator-ii/
code d'ici : https://leetcode.com/problems/basic-calculator-ii/discuss/658480/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
"""
class Solution:
    def calculate(self, s):    
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))
        
            num, stack, sign = 0, [], "+"
            
            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
                
            update(sign, num)
            return sum(stack)

        return calc(0)
    
"""solution iterative : https://leetcode.com/problems/basic-calculator-iii/discuss/159550/Python-short-iterative-solution-with-brief-explanation"""
