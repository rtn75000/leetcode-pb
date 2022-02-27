"""#TC O(n)  #SC O(n) car on utilise un stack 
l'idee : est tout simplement de faire rentrer dans un satck les temperatures a chaque fois que l'on rencontre une temperature plus basse que le top de la stack , on ferra pop tant que la temperature au top est inferieur a la temperature actuelle. pour connaitre la difference de jour on calculera la difference des indexes. 
ex : 
 [73,74,75,71,69,72,70,63] 
 stack = [0] puisque 74>73 alors on fait pop (on 1(idx de 74)-0(idx de 73) et on met le resultat (cad 1) dans l'index 0 de la reponse ) puis on rentre l'indexe de 74 dans le stack. res=[1,0,0,0,0,0,0,0]
 stack = [1] puisque 75> 74 alors on fait pop et puis on rentre l'index de 75 dans le stack. res=[1,1,0,0,0,0,0,0]
 stack=[2,3] puisque 72>69 et 72>71  on pop les 2 puis on rentre l'index de 72 dans le stack.ress=[1,1,0,2,1,0,0,0]
 stack=[5,6,7] . res ne change pas 
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res


"""2eme solution : #TC O(n)  #SC O(1)
code(traduit de C++) et explication d'ici : https://leetcode.com/problems/daily-temperatures/discuss/121787/C%2B%2B-Clean-code-with-explanation%3A-O(n)-time-and-O(1)-space-(beats-99.13)
app: temp = [73, 74, 75, 71, 69, 72, 76, 73], l'idee est de commence par la fin, supposons qu'on a obtenue pour i >= 3: res = [?, ?, ?, 2, 1, 1, 0, 0] . Pour trouver le nombre de jour pour i=2 :
si temperatures[2] < temperatures[3], res[i] = 1 mais si temperatures[2] >= temperatures[3] alors dans ce cas on examine res[3] qui egale a 2 se qui veut dire qu'on obtiendra une temperature plus eleve que temperature[3] 2 apres cad a l'index 5, donc puisque temperatures[2] >= temperatures[3] ca veut dire qu'on obtiendra une temperature superieur a temperature[2] au moins 2 jours apres temperature[3] . c'est pour cela qu'on peut aller directement a jour 3 + res[3] cad a l'index 5. 
   
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            j=i+1   #index apres i
            while j < n and temperatures[i] >= temperatures[j]:
                if res[j] > 0:
                    j = j + res [j] #on s'avance a l'index j+res[j]
                else:
                    j = n  #on va directement a la fin donc res[i] sera egale a 0 (car on ne le touche pas)
            # either j == n or temperatures[i] < temperatures[j]
            if j < n : # cad que si temperatures[i] < temperatures[j] et pas que j==n
                res[i] = j - i;
        return res
