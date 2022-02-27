"""#divide and conquert #regular recursion #O(4^n/(sqrt(n)))
le code d'ici: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/629328/Python-Elegant-divide-and-conquer-recursive-solution
explication d'ici: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/151979/Divide-and-Conquer-greater-Memoization
l'idee est de diviser l'expression en deux partie differente a chaque fois qu'on rencontre un symbole (+-*) et le faire de facon recursive
exemple :                      
                                                                     1+2+3+4 
                                                                        |
                     -----------------------------------------------------------------------------------------------------------             
                   /----- input[i]=+ -----/                    |---- input[i]=+ ----|                     \------ input[i]=+ ---\
                  /                      /                     |                    |                      \                     \ 
                 /                      /                      |                    |                       \                     \           
                /                      /                       |                    |                        \                     \      
              (1)                   (2+3+4)                  (1+2)                (3+4)                    (1+2+3)                 (4)        
                                  / + / \ + \                 /\                    /\                   / + /  \ + \                                                
                                 /   /   \   \               /  \                  /  \                 /   /    \   \                                            
                                /   /     \   \            (1)  (2)              (3)  (4)              /   /      \   \
                               /   /       \   \                                                      /   /        \   \                                 
                             (2) (3+4)    (2+3) (4)                                                 (1) (2+3)     (1+2) (3)                                           
                                  /\        /\                                                                                                                    
                                 /  \      /  \                                                                                                                  
                                (3) (4)   (2) (3)                                                                                                                    
->  a propos du time complexity :
le resulat final sera composer du n-ieme nombre catalan (la suite de nombre catatlan est 1 1 2 5 14 42 132 429 1430 4862 ...) avec n le nombre d'operateur dans l'expression. si on a 0 ou 1 operateur  le resultat sera 
compose de 1 possibilite, si 2 operateurs 2 possibilites si 3 operateurs 5 possibilites , 4 operateurs 14 possibilites ... cela suit une logique de la serie des nombre catalan (il ya d'autre pb de se genre comme le
nombre de combinaison differente de parenthese voir leetcode pb 22). donc dans notre resultat il yaura le n-ieme nombre catalan de possibilite (avec n le nbr d'operateurs).
pour arriver a chaque resultat on fait n operations (avec n le nombre d'operateur dans le input) car par exemple si on a le 3+2+1+4 alors une des possibilite c'est ((3+2)+1)+4) pour la calculer on fait 3+2=5 puis 5+1=6 
puis 6+4=10 cad on a fait 3 operations soit n=3 operations. donc pour chaqu'une des C(n) (n-ieme nombre catalan) possibilites on fait n operations donc le time complexity est de C(n)*n.
        1   / 2n \                                                      4^n
C(n)= ----- |    |     ~(Asymptotically equale to meaning big-O)  -----------------
       n+1  \ n  /                                                  n^(1.5)*pi^0.5
       
therefore  TC= O(C(n)*n) = O (     4^n        )  * n    = O ( 4^n  )     which is exponenial time (k^x)
                             ----------------               -------     
                               n^(1.5)*pi^0.5)               sqrt(n)
-> space complexity is equal to C(n) puisque a la fin dans le resultat on a conserver les differentes possibilites qui sont egale a C(n).

source pour TC et SC : 
-https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66459/What-is-the-time-complexity-of-divide-and-conquer-method
-https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/303491/C%2B%2B-O(C(N))-Divide-and-Conquer-with-tipexplanation
-https://cs.stackexchange.com/questions/119631/time-complexity-of-combinations-of-n-pairs-of-parentheses
-https://en.wikipedia.org/wiki/Catalan_number
-https://stackoverflow.com/questions/66220496/what-is-the-time-and-space-complexity-of-leetcode-241-different-ways-to-add-par
-https://github.com/mqwu/LeetCode/blob/master/Python/different-ways-to-add-parentheses.py
"""
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        
        res = []
        for i in range(len(input)):           # c'est 2 lignes selectionnent 
            if input[i] in '+-*':             # un nouvelle operateur 
                left = self.diffWaysToCompute(input[:i])   # ce qui se trouve a droite de l'operateur
                right = self.diffWaysToCompute(input[i + 1:])  # ce qui se trouve a gauche de l'operateur
                
        # il peut y avoir plusieur resultat dans left ou right car il peut avoir plusieurs possibilite de calcul
        # ex si left = self.diffWaysToCompute("(1+2*3)") alors on a left = [(1+2)*3,1+(2*3)] = [9,7] . 
        # donc il faut parcourir tout les element de left avec tout ce de right d'ou la double boucle 
                for l in left:      
                    for r in right:
                        res.append(eval(f"{l}{input[i]}{r}"))   #eval("3+2")=>5
        return res
    
    
"""solution n2 : #DP #top-down(memoization) #C(n)<TC<n*C(n) #SC=O(C(n)) 

c'est presque la meme chose que la solution 1 a la seule difference qu'ici on garde les expressions calculer dans un hash table ce qui nous permet de reduire le time complexity qui sera compris entre O(n*C(n)) et
O(C(n)) ( ca reste forcement O(C(n)) car c'est le nombre de solution qu'on recoit au finale donc meme si pour les avoir on a fait O(1) a chaque recursion ca reste O(c(n)) mais juste c'est pas en general inferieur 
a n*C(n) car pour obtenir un resultat on aura pas forcement beson de n interaction car on pourra utiliser des valeurs deja calculer qui sont presente dans le hashtable). le SC reste le meme car il faut stocker toute 
les possibilite qui sont C(n) donc SC=O(C(n)).  
un exemple qui montre que les expression sont reutiliser plusieur fois :

                                                                     2*3-4*5
                                                                        |
                     -----------------------------------------------------------------------------------------------------------             
                   /----- input[i]=* -----/                    |---- input[i]=- ----|                     \------ input[i]=* ---\
                  /                      /                     |                    |                      \                     \ 
                 /                      /                      |                    |                       \                     \           
                /                      /                       |                    |                        \                     \      
              (2)                   (3-4*5)                  (2*3)                (4*5)                    (2*3-4)                 (5)        
                                  / - / \ * \                 /\                    /\                   / * /  \ - \                                                
                                 /   /   \   \               /  \                  /  \                 /   /    \   \                                            
                                /   /     \   \            (2)  (3)              (4)  (5)              /   /      \   \
                               /   /       \   \                                                      /   /        \   \                                 
                             (3) (4*5)    (3-4) (5)                                                 (2) (3-4)     (2*3) (4)                                           
                                  /\        /\                                                                                                                    
                                 /  \      /  \                                                                                                                  
                                (4) (5)   (3) (4)           
                                
comme on peut voir il ya des expression qui revient sur elle meme.
 
 
le code est prix d'ici : https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-concise-solution-with-memorization


class Solution(object):
    def diffWaysToCompute(self, input):
        dic = {}
        return self.dfs(input, dic)
        
    def dfs(self, input, dic):
        if input in dic:
            return dic[input]
        if input.isdigit():
            dic[input] = int(input)
            return [int(input)]
        ret = []
        for i in range(len(input)):           # c'est 2 lignes selectionnent 
            if input[i] in '+-*':             # un nouvelle operateur 
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:      
                    for r in right:
                        ret.append(eval(f"{l}{input[i]}{r}"))   #eval("3+2")=>5
        dic[input] = ret
        return ret

"""
