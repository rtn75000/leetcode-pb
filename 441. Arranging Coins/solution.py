"""si on veut completer k rows ca revient a faire 1+2+3+...+k qui est une suite arithmetique dont la somme est egale a (k(k+1))/2 exemple si on veut 3 ranges d'escalier ca donne 1+2+3=(3(3+1)/2)=12/2=6 coins donc si on a n coins pour savoir le nombre de range k qu'on peut faire il faut que: (k(k+1))/2 <= n  par exemple si on a 6 coins on peut faire 3 range car (3(3+1)/2)=12/2=6.
on utilisera un binary search pour touver le k qui peut etre dans le range [0,n] (si 0 coins alors k=0 si 1 coins alors k=1=n)

#TC O (log n) #SC O(1)
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r, ans = 1, n, 0
        while l <= r:
            k = (l + r) // 2     
            coinsNeeded = k * (k + 1) // 2   
            if coinsNeeded <= n:      # si la sum est inf alors ca peut etre la bonne reponse donc on garde dans ans le resultat
                l, ans = k + 1, k
            else:           # si la sum est sup ca veut dire qu'on a trop de rows par rapport au coin donc on doit reduire le nombre de rows
                r = k - 1
        return ans
    
""" on peut resoudre de facon mathematique : on sait que pour k rows et n coins on doit avoir l'inequation suivante (k(k+1))/2 <= n , si on isole le k ca donne ca : 
 (K * (K+1))/2 <= N
 K^2 + K <= 2*N
 (K + 1/2)^2- 1/4 <= 2*N 
 (K + 1/2)^2 <= 2*N + 1/4
 K+ 1/2 <= sqrt(2*N + 1/4)
 K <= sqrt(2*N + 1/4) - 1/2
 comme on  veut que k soit le plus grand possible alors si sqrt(2*N + 1/4) - 1/2 est un nombre entier donc k=sqrt(2*N + 1/4) - 1/2 si c'est un float alors k=floor(sqrt(2*N + 1/4) - 1/2) donc on rend tout simplement la partie entier de sqrt(2*N + 1/4) - 1/2
 #TC&SC O(1)"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
