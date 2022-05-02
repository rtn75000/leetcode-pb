"""# ma solution  # matrix traversal # baser sur ma solution (tres peu de modif) : https://leetcode.com/problems/spiral-matrix/   # TC O(n*n) # SC O(1) 
l'idee est de faire comme ma solution dans spiral matrix I et simplement remplir avec 1,2,3,...n les cases. """

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
   
        
        # boundaries initialisation 
        lowerRowLimit = lowerColLimit = -1
        upperRowLimit = upperColLimit = n 
        
        row = col = visited =  0  # row,col will point on the current cell 
        res = [[0 for _ in range(n)] for _ in range(n)]  # cree matrix de taille n*n contenant que des 0 
        
        res [0][0]=1 
        val = 2 
        visited = 1 
         
        while  visited < n*n :  # we keep doing this until we have visited all cell
            
            while col+1 < upperColLimit  :  # aller a droite jusqu'au bout # go through a row from left to right 
                col+=1
                visited+=1
                res[row][col] = val 
                val+=1
            lowerRowLimit +=1 # Since we went through the topmost row we don't want to visit it again so change lower row bound in order to exclude this row for next iterations
            
            while row +1 < upperRowLimit  : # aller en bas jusqu'au bout  # go through a col from up to bottom
                row+=1
                visited+=1
                res[row][col] = val 
                val+=1
            upperColLimit-=1  # Since we went through the leftmost col we don't want to visit it again so change upper col bound in order to exclude this col for next iterations   
            
            while col-1 > lowerColLimit  :  # aller a gauche jusqu'au bout # go through a row from right to left   
                col-=1
                visited+=1
                res[row][col] = val  
                val+=1
            upperRowLimit-=1  # Since we went through the lowest row we don't want to visit it again so change upper row bound in order to exclude this row for next iterations
            
            while row-1 > lowerRowLimit  : # aller en haut jusqu'au bout # go through a col from bottom to up  
                row-=1
                visited+=1
                res[row][col] = val  
                val+=1
            lowerColLimit+=1  # Since we went through the rightmost col we don't want to visit it again so change upper col bound in order to exclude this col for next iterations
            
        return res
    
