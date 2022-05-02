"""#ma solution #Matrix traversal #TC O(n*m) #SC O(1)
on utilisera une delimitation qui nous permettra de savoir quelle row et/ou col on deja ete visite. on ira a droite puis en bas puis a gauche puis en haut et ainsi de suite tant que 
on a pas visiter tout les nodes . 

LRL == lowerRowLimit
LCL == lowerColLimit

initialisation :

             LRL/LCL=-1     c=0      1       2     ...     m-1     upperColLimit=m 
                         
                         -----------------------------------------
                  r=0    |       |      |      |   ...  |        |
                         -----------------------        ----------     
                   1     |       |      |      |        |        |
                         -----------------------   ...  ----------
                   2     |       |      |      |        |        |
                         -----------------------        ----------
                   .         .      .      .       .        .            
                   .         .      .      .       .        .                
                   .         .      .      .       .        .    
                         -----------------------        ----------
                  n-1    |       |      |      |  ...   |        |
                         -----------------------------------------
        upperRowlimit=n           
                  


"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # boundaries initialisation 
        lowerRowLimit = lowerColLimit = -1
        upperRowLimit = n = len (matrix)
        upperColLimit = m = len (matrix[0])
        
        row = col = visited =  0  # row,col will point on the current cell 
        
        res=[matrix[row][col]]  # output, already put first cell
        
        visited+=1     # number of visited cells 
        
        while  visited < n*m :  # we keep doing this until we have visited all cell
            
            while col+1 < upperColLimit  :                      # aller a droite jusqu'au bout # go through a row from left to right 
                col+=1
                visited+=1
                res.append(matrix[row][col])            
            lowerRowLimit +=1      # Since we went through the topmost row we don't want to visit it again so change lower row bound in order to exclude this row for next iterations
            
            while row +1 < upperRowLimit  :                     # aller en bas jusqu'au bout  # go through a col from up to bottom
                row+=1
                visited+=1
                res.append(matrix[row][col])
            upperColLimit-=1       # Since we went through the leftmost col we don't want to visit it again so change upper col bound in order to exclude this col for next iterations   
            
            while col-1 > lowerColLimit and visited < n*m :    # aller a gauche jusqu'au bout  # go through a row from right to left  #add the second condition for this case : matrix=[1,2,3]
                col-=1
                visited+=1
                res.append(matrix[row][col])
            upperRowLimit-=1       # Since we went through the lowest row we don't want to visit it again so change upper row bound in order to exclude this row for next iterations
            
            while row-1 > lowerRowLimit and visited < n*m :    # aller en bas jusqu'au bout # go through a col from bottom to up #add the second condition for this case : matrix=[[1],[2],[3]]
                row-=1
                visited+=1
                res.append(matrix[row][col])
            lowerColLimit+=1       # Since we went through the rightmost col we don't want to visit it again so change upper col bound in order to exclude this col for next iterations
            
        return res
    

    
