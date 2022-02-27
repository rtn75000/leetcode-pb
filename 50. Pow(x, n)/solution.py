"""# recursive    #O(log(n)) TC car on divise a chaque fois n par 2     # O(log(n)) SC 
le code et explication d'ici: https://leetcode.com/problems/powx-n/discuss/738830/Python-recursive-O(log-n)-solution-explained
l'idee est que au lieu de calculer x^n on calcul (x^(n/2))^2 soit x^(n/2) * x^(n/2) .
si n est paire on peut le diviser par 2 donc on calclul (x^(n/2))^2 soit x^(n/2) * x^(n/2).
si n est impaire on calcul alors x^(n//2) car n//2 est impaire dans ce cas puis on multiplie par x cad  x^(n//2) * x^(n//2) * x"""
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:    # si n est negatif alors c'est equivalent a 1/(x^|n|)
            return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0:   # paire
            return lower*lower
        if n % 2 == 1:   # impaire
            return lower*lower*x
