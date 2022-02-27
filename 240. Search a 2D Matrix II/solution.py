"""
il ya la solution qui coute de faire un binary search sur chaque row qui coutera donc en tout O(n*log(m)), cette approche est simple . il ya une approche plus interessante qui coute O(n+m) :
l'algo sera le suivant :
on commence par la derniere rangee premiere element , si la target est superieur alors on va a droite cad on fait column+=1 si target est plus petite on monte  cad row-=1, si on trouve le target on retourne true ,
si on sort des bord de la matrix alors on retourne false cad on a pas trouver. 
app : target=8

1  4  7  11  15
2  5  8  12  19
3  6  9  16  22
10 13 14 17  24
18 21 23 26  30

on commence par 18 cad m[4][0] puisque 8<18 alors on monte dc row-=1 soit m[3][0] cad 10 puisque 8<10 alors on monte row-=1 soit m[2][0] cad 3 puisque 8>3 alors on va a droite dc col+=1 soit m[2][1] cad 6 puisque 
8>6 on va a droite col+=1 soit m[2][2] cad 9 puisque 8<9 alors on monte row-=1 soit m[1][2] cad 8 comme 8==8 donc return True. 
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         
        # Quick response for empty matrix
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        # matrix border to know if we are out of them
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False
        
