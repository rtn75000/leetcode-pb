"""#first sol #not my sol  #DFS recursive in graph  #TC O(M×N) where M is the number of rows and N is the number of columns. voir explication # SC O(n*m).

le pb peut etre facilement resolue si on regarde ma solution ici : https://leetcode.com/problems/number-of-islands/

quasiment meme code juste petit changement pour compter le area , meme TC SC (voir explication la bas)
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        maxArea = 0    # va garder le max area 
        for row in range(len(grid)):   # row
            for col in range(len(grid[0])):  #column
                if grid[row][col] == 1:  # que si la case est egale a 1 alors elle active un dfs 
                    # dfs return le area de l'ile actuelle                     
                    maxArea=max(maxArea,self.dfs(grid, row, col) )   # remarque: bien que la fct dfs est declarer apres comme c'est une fct de la classe alors elle peut etre declarer apres.
        return maxArea

    def dfs(self, grid, row, col):
        
        # les 4 premieres condition verifie si on est sortie des limites de la matrix , la 5e condition verifie si la case est egale a 1 . donc si egale a 0 ou on est hors des limites alors c'est notre condition d'arret.
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] != 1: 
            return 0           
        
        grid[row][col] = 0   # on change le node visiter en 0 
             
        # on fait dfs sur les voisin cad les cases gauche droite en haut et en bas 
        up=self.dfs(grid, row+1, col) 
        down=self.dfs(grid, row-1, col)
        right=self.dfs(grid, row, col+1)
        left=self.dfs(grid, row, col-1)
        
        
        return 1 + up + down + right + left
    
    
"""#2nd sol #BFS iterative #TC O(M×N) where M is the number of rows and N is the number of columns # SC O(n*m) 

le code est bien expliquer. voir le code 

TC SC explication : meme explication que la premier sol .

"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:      
        
        if not grid:
            return 0

        maxArea = 0    # va garder le max area 
        for row in range(len(grid)):   # row
            for col in range(len(grid[0])):  #column
                if grid[row][col] == 1:  # que si la case est egale a 1 alors elle active un bfs
                    # bfs return le area de l'ile actuelle                     
                    maxArea=max(maxArea,self.bfs(grid, row, col))  
        return maxArea
        

    def bfs(self, grid, row, col):
        
        queue = collections.deque()
        queue.append((row, col))   # ajouter la cas actuelle ds la queue 
        grid[row][col] = 0   # mark as visited
        area = 0 
        
        while queue:
            
            directions = [(0,1), (0,-1), (-1,0), (1,0)]  # droite, gauche , bas , haut 
            r, c = queue.popleft()   # pop le premier entre dans le queue FIFO , cad maintenant on va verifier les voisin de la case matrix[r][c]
            area+=1 
            
            for dr , dc  in directions:     #chaque element dans direction est composer d'un tuple contenant 2 element 1 pour l'ajout de direction sur les row et un ajout de direction sur les columns
                nr, nc = r + dr, c + dc     # la nouvelle direction des row/column nr/nc est egale a l'ancienne direction r/c plus l'ajout de direction de row/column             
                if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and grid[nr][nc] == 1:  # on verifie que nc et nr sont bien ds les limites de la matrix et que la case contient un 1 
                    queue.append((nr, nc))  # si toute les condition sont respecter alors on doit ajouter le voisin a la queue 
                    grid[nr][nc] = 0      # une fois que le voisin est ajouter on peut le marquer comme visited (on s'occupera de lui plus tard quand on va pop de la queue)
        return area
