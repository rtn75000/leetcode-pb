"""#ma solution # sol1 # backtracking #TC O(m*n*3^l) , l==len(word) #SC O(l)

il faut tout simplement ce deplacer dans une matrice on utilise donc dfs cad il faut faire un appel recursive sur les 4 directions d'une cellule.
a chaque fois qu'on trouve une lettre du mot on avance parcontre si la lettre ne correspond pas on backtrack cad on ne fait plus d'appel rec et donc on retourne en arriere.
ici on parle de backtracking et pas d'un simple dfs car un simple dfs va essayer tout les combinaison possible puis a la fin voir si il a obtenue le mot rechercher 
alors qu'un backtracking lui va s'arreter des qu'une lettre ne correspond pas , il ne va pas continuer dans cette direction. 
VOIR EXPLICATION GITHUB.

TC analyse : 
un dfs peut parcourir au max toute la matrice qu'une fois  (car il va dans toute les directions sans revenir sur les case deja visiter) donc il coute O(m*n) mais dans notre cas le
dfs parcours au maximum la taille du mot rechercher, dans 3 direction a chaque fois (pas 4 (que le premier aura 4 direction tout le reste 3) car on ne revient pas en arriere ) cad on recoit
un arbre de recursion de 3 branche comme ceci par exemple : 

                                             root
                        /             /               \                \                    (que le root va dans 4 direction le reste que dans 3)
                      d1              d2               d3              d4         
                  /   |   \       /   |   \        /    |   \       /   |   \
                 d1  d2   d3     d1   d2   d3     d1   d2   d3     d1   d2   d3 
                /|\  /|\  /|\   /|\  /|\  /|\    /|\  /|\  /|\    /|\  /|\  /|\
                ...  ...  ...   ...  ...  ...    ...  ...  ...    ...  ...  ...
                
on a donc quatre 3-ary recursion tree de hauteur len(word)-1 (car on enleve le root ) donc chaque arbre coute O(3^(l-1)) avec l==len(word) ; 
donc l'arbre de recursion de base coute O(4*3^(l-1)). donc le cout d'un dfs est O(4*3^(l-1)) (car chaque recursion coute O(1)) donc comme dans notre algo on peut lancer un dfs 
de chaque case de la matrice il ya donc m*n dfs cad que l'algo coute en tout O(m*n*4*3^(l-1)) equivalent a O(m*n*3^l) . 

SC analyse : 
O(l) for the recursion stack car la hauteur de l'arbre de recursion est max de la taille du mot .
O(l) for the visited set , car il garde tout les case visiter , et le nbr de case visiter est au max le nombre de lettre qu'il ya dans le mot.


"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = col = 0
        m = len(board[0]) # num of column
        n = len(board)    # num of row
        visited = set()   # keep visited cell 
        
        # on lance le dfs a partir des cell qui sont egale a la premiere lettre du mot
        # le double for nous permet de parcourir toutes les cell de la matrix
        for col in range (m) :
            for row in range (n) :
                if board[row][col] == word[0] :
                    flag = self.dfs(row, col, board, word, visited)
                    if flag :   # flag egale True si on a trouver le mot
                        return True
                    visited=set() # a chaque dfs il faut vider les visited cell car on va commencer un nouveau dfs 
        return False 
    
    def dfs(self, row, col, board,  word,visitedNode) :
        
        if not word :     # si il ya plus de lettre dans le mot ca veut dire qu'on les a tous trouver 
            return True 
        # les 4 premieres conditions sont la pour verifier qu'on ne sort pas des limite de la matrice 
        # la 5e condition et la pour verfier qu'on a pas deja visiter la cellule
        # la 6eme condition et la pour verifier si la lettre de la cellule correspond a la lettre qu'on recherche 
        # donc si la cellule est en dehors des limite de la matrice ou si on la deja visiter ou si la valeur de la cellule n'est 
        # pas la lettre rechercher alors on return False 
        if  row<0 or col<0 or col>len(board[0])-1 or row>len(board)-1 or (row,col) in visitedNode or board[row][col] != word[0]   : 
            return False   
        
        # si on est arriver ici ca veut dire qu'on a trouver la lettre qu'on cherche donc on ajoute la case
        # dans les cases visitees 
        visitedNode.add((row,col)) #O(1)
        
        # chaque dfs retourne True ou False 
        # dfs sur la case de droite 
        right = self.dfs(row, col+1, board,  word[1:], visitedNode)
        # dfs sur la case de gauche
        left = self.dfs(row, col-1, board,  word[1:], visitedNode)
        # dfs sur la case du bas 
        down = self.dfs(row+1, col, board,  word[1:], visitedNode)
        # dfs sur la case du haut 
        up = self.dfs(row-1, col, board,  word[1:], visitedNode)
        
        # on retire la case visiter car cette kigne ce fait qd on a fini tout les dfs qui parte de cette case 
        # car c'est apres qu'on est remonter des recursion , donc il faut retirer cette pour essayer d'autre option
        visitedNode.remove((row,col)) #O(1)
        
        return right or left or down or up #si un des dfs est True alors ca retourne True
    
"""
# sol 2 # meme TC meme SC (meme TC car c'est le meme code quasiment et meme SC car bien qu'il ya pas O(l) pour le set il ya O(l) pour les recursion stack).
meme sol juste a la place d'avoir un set pour les cellule visitees on va remplacer la valeur de la cellule par '#' ce qui permet de ne pas utiliser d'extra space 
remarque : il faut savoir que les interviewer n'aime pas qu'on change le input car dans la vrai vie on ne peut pas changer ...
"""
            


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        
        row = col = 0
        m = len(board[0])
        n = len(board)
        for col in range (m) :
            for row in range (n) :
                if board[row][col] == word[0] :
                    flag = self.dfs(row, col, board, word)
                    if flag : 
                        return True
        return False 
    
    def dfs(self, row, col, board,  word) :
        
        if not word :
            return True 
        if  row<0 or col<0 or col>len(board[0])-1 or row>len(board)-1 or board[row][col] != word[0]   : 
            return False   
        
        # on garde la valeur de la cellule car elle va etre changer et on la besoin pour quand on remonte la recursion
        # pour remettre la valeur initiale dans la cellule
        temp = board[row][col]  
        board[row][col] = '#'   #marquer la cellule comme visite
        
        right = self.dfs(row, col+1, board,  word[1:])
        left = self.dfs(row, col-1, board,  word[1:])
        down = self.dfs(row+1, col, board,  word[1:])
        up = self.dfs(row-1, col, board,  word[1:])
        
        board[row][col] = temp  # on remet la valeur initiale dans la cellule en remontant des dfs 
        
        return right or left or down or up 
    
"""
follow up : Could you use search pruning to make your solution faster with a larger board?

Reponse : 
If the length of the "word" is greater than the size of the "board" (#rows * #cols) we can simply return False. Also, we can check if each character in "word" exists
in "board", if there is at least one character that does not exist in "board" we can simply return False. Performing these two prunings we can return False
immediately instead of computing further.

"""
