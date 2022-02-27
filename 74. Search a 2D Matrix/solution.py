"""l solution est de tout simplement faire comme si la matrix etait flatten (on va pas vraiment la flatten) ce qui veut dire que on aura une liste virtuel (car on va pas la flatten vraiment) de taille m*n et on va 
faire un binary search dessus . donc TC O(lg(m*n)) et SC O(1) (petite remarque: de rechercher d'abord la ranger avec BS puis la cologne avec BS ca revient au meme TC car ca vaut log(m)+log(n) qui est egale a log(m*n)).
on flatten pas vraiment car si non on va avoir SC O(m*n)
cette solution est possible du au rangement de la matrix : 
ex :
10 11 12 13   
14 15 16 17     => on fera comme si on a : 10 11 12 13 14 15 16 17 18 19 20 21
18 19 20 21

si on recherche un element a l'idx i dans le flatten matrix ca revient a l'element matrix[i // n][i % n] dans la matrix normale (de la matrix a la flatten matrix : si on a un element matrix[x][y] dans la matrix 2D alors
ca correspond a l'elemnt  a[x * n + y] de la list)
par exemple dans l'exemple au dessus 15 est a l'index 5 dans la flatten matrix il correspond a l'element matrix[5 // 4][5 % 4] cad matrix[1][1] . donc on va faire un binary search sur les index de m*n puis le mid
qu'on obtien on regardera son equivalent dans la 2D matrice  
app :   
10 11 12 13   
14 15 16 17        target=18   m=3 et n=4
18 19 20 21
=> on fait binary search sur [0,m*n=3*4=12] ce qui nous donne 0+12//2=6 on verifie si matrix[6//4][6 % 4] cad matrix[1][2]==16 est sup ou inf donc comme c'est inferieur a target alors le target est forcement a un idx 
superieur donc lo = mid+1 cad lo=7
=> on fait binary search sur [7,12] ce qui nous donne 7+5//2=9 puisque matrix [9//4][9 % 4] cad matrix[2][1]==19 est sup a target donc le target ce trouve avant donc hi = mid-1 cad hi=8
etc.. jusqu'a qu'on trouve le target et on retourne True
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        
        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows * cols - 1
       
        while lo <= hi:
            mid = lo + (hi-lo) // 2     # (on peut aussi faire mid=lo+hi//2 mais la formule precedente permet d'eviter un overflow car lo+hi peut etre tres grand) 
            num = matrix[mid // cols][mid % cols]
            if num == target:
                return True
            elif num < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False
