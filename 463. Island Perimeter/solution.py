"""#TC O(row x col) #SC O(1)
ds cette solution on n'utilise pas de dfs ou bfs, on passe par chaque cellule de la matrix si la cellule correspond a de l'eau cad val == 0  alors on fait rien mais si la cellule correspond a la terre cad val==1 
alors dans ce cas on regarde ce qui se passe autour de cette cellule :
une cellule contient 4 cotes, les cotes qui seront comptabiliser dans le perimetre sont les cotes entourer d'eau donc on verifie si il ya de l'eau en haut en bas a droite et/ou a gauche de la cellule .
au debut chaque cellule aura un perimetre 4 est si un cote est pas entourer d'eau alors on reduit de 1 le perimetre.
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    
                    if r == 0:  # donc en haut il ya rien car en dehors des limites , on va considere comme-ci il ya de l'eau (cad on ne reduit pas le perimetre)
                        up = 0
                    else:
                        up = grid[r-1][c] #si c'est de l'eau c'est 0 (cad on retire rien) si c'est la terre c'est 1
                        
                    if c == 0: # donc a gauche il ya rien car en dehors des limites , on va considere comme-ci il ya de l'eau
                        left = 0
                    else:
                        left = grid[r][c-1]
                        
                    if r == rows-1: # donc en bas il ya rien car en dehors des limites , on va considere comme-ci il ya de l'eau
                        down = 0
                    else:
                        down = grid[r+1][c]
                        
                    if c == cols-1: # donc a droite il ya rien car en dehors des limites , on va considere comme-ci il ya de l'eau
                        right = 0
                    else:
                        right = grid[r][c+1]
                        
                    result += 4-(up+left+right+down)
                
        return result
                
