""" #sol1 # ma sol  # dfs(with backtracking)   # TC O(4^n) voir analyse   # SC O(n) for recursion (and curPath also is O(n) )

A chaque fois on a le choix de mettre soit un parenthese de gauche '(' soit de droite ')' donc on commence par une string vide et on rajoute soit '(' soit ')' a chaque fois . 
Si le nombre de parenthese de droite ')' est superieur au nombre de parenthese de gauche '(' alors la combinaison n'est pas valide. 
Si la condition precedente ne se realise pas et que le nombre de parenthese de gauche '(' est egale au nombre de parenthese de droite ')' alors on a un combinaison valide.
on peut facilement trouver la solution a l'aide d'un arbre de recursion binaire ( 2 choix a chaque fois ou '(' ou ')' ) ou chaque path va etre une combinaison de parenthese. 

VOIR ARBRE DE RECURSION GITHUB 

TC analyse : 
la hauteur de l'arbre est O(2n) car au max une combinaison a n parenthese de gauche '(' et n parenthese de droite ')' .  
( on ne peut avoir une combinaison plus grande car on rajoute n parenthese de gauche '(' et n parenthese de droite ')' au max ; voir code : 'if leftParentheseNum < n: curPath.append("(")' et 
'if rightParentheseNum < n : curPath.append(")")' ) .
De plus c'est un binary tree (2-ary tree) car on fait 2 choix a chaque fois . ccl : TC = O(2^(2n)) cad O((2^2)^n) cad O(4^n)
remarque : voir arbre de recursion il ya une analyse plus approfondie !

SC analyse : 
la hauteur de l'arbre est O(2n) car au max une combinaison a n parenthese de gauche '(' et n parenthese de droite ')' .  
de plus curPath est de taille O(2n) au max .
ccl : SC = O(2n)+O(2n) = O(n)

remarque: backtracking n'a pas forcement de for loop, le backtracking ca veut juste dire que l'algo ne continue pas a faire de recursion si le chemin actuelle mene forcement a une mauvaise reponse.

"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output=[]
        
        def dfs(curPath,leftParentheseNum,rightParentheseNum) : 
            
            if rightParentheseNum>leftParentheseNum : 
                return 
            
            if leftParentheseNum == n and rightParentheseNum == n :
                output.append("".join(curPath))
                return
   
            if leftParentheseNum < n: 
                curPath.append("(")
                dfs(curPath,leftParentheseNum+1,rightParentheseNum)
                curPath.pop()  # en remontant de la recursion on enleve la parenthese ajoute
                
            if rightParentheseNum < n : 
                curPath.append(")")
                dfs(curPath,leftParentheseNum,rightParentheseNum+1)
                curPath.pop()
            
            return         # on est pas obliger d'ecrire return car de toute les facon ca va return mais c'est juste pour comprendre le code 
        
        dfs([],0,0)
        
        return output 
"""
# sol2  # not my sol  # bfs(iterative)  # TC O(4^n) comme dfs  # SC O(n^2) voir analyse 

bfs intro :

au lieu de traverser l'arbre de recursion dans la profondeur comme le dfs , le bfs lui traverse l'arbre de recursion dans la largeur a l'aide d'une queue a laquelle a chaque iteration il va 
pop un element , analyser cette element , puis append tout ses enfants dans le queue, donc l'ordre d'execution est le suivant :

              1             initialisation : queue = [1]          
            /   \                            pop(),analyse de 1, append(2),append(3) ; queue =[2,3]
           2     3                           pop(),analyse de 2, append(4),append(5) ; queue =[3,4,5]     
          / \   / \                          pop(),analyse de 3, append(6),append(7) ; queue =[4,5,6,7]    
         4   5 6   7                         pop(),analyse de 4, (pas d'enfant)      ; queue =[5,6,7] 
      arbre de recursion                     pop(),analyse de 5, (pas d'enfant)      ; queue =[6,7]
                                             etc...                                  ; queue =[]
     
    
    
Pour que le bfs marche il faut que chaque node est sa propre copie du path car on ne peut travailler sur le meme path comme dans dfs , car ici l'ordre de traitement se fait sur la largeur et
pas sur la profondeur donc on peut pas utiliser le meme path puis faire pop . C'est pour cela qu'on utilise ' curPath+")" ' ou ' curPath+"(" ' car ca creer une copie a chaque fois. 

Si on analyse le code on remarque que c'est exactement les meme condition que le dfs . 

app du bfs voir photo github : j'explique comment on va faire rentrer dans le queue niveau par niveau et on va pop de gauche a droite du niveau de l'arbre de recursion. 

analyse TC : 
le bfs fait autant d'iteration que le dfs donc il a le meme TC cad O(4^n) (si on fait une analyse plus approfondi TC est O((4^n)/racineCarre(n)) mais on ne va pas s'attarder dessus)

Analyse SC :
ici contrairement au dfs on fait une copie du path a chaque fois donc le premier niveau constituer de 2^0 node a un path de taille 0 , le 2e niveau constituer de 2^1 node a chacun un path 
de taille 1 (donc +2*1), le 3e niveau constituer de 2^2 node a chacun un path de taille 2 (donc +2*2) et ainsi de suite jusqu'au n-ieme niveau donc SC =  2*1+2*2+2*2*3+...+2*n cad
2(1+2+...+n) cad O(2)*O(n^2) cad O(n^2) . (cette analyse est vrai quand on considere qu'un arbre de recursion binaire de hauteur O(2n) est former , mais si on analyse plus profondement
alors on voit qu'un arbre avec seulement n-th catalan leaf est former donc ca va etre comme le SC du n-th catalan qui est O((4^n)/racineCarre(n)) , mais nous on va prendre l'analyse simple
qui est suffisante ).

VOIR PHOTO GITHUB APPLICATION 
"""   
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        queue = deque([('',0,0)])
        
        while queue:
            
            # on pop l'element a analyser 
            curPath,leftParentheseNum,rightParentheseNum = queue.pop()  
            
            # si le path de cette element est incorrecte, ca ne sert a rien de continuer ce path donc on fait continue cad que on va pas ajouter de parenthese a ce path 
            # et donc on a fini avec ce path (comme dans la recursion ou on fait return , pour ne pas faire de recursion dessus)
            if rightParentheseNum>leftParentheseNum :    
                continue
            
            # si on est arriver a cette ligne ca veut dire que le path est pas incorrecte donc on verifie si on a mit toute les parenthese , si oui on a donc un
            # pass valide a ajouter a l'output
            if leftParentheseNum == rightParentheseNum == n:
                output.append(curPath)
                continue
            
            # si on est arriver a cette ligne ca veut dire que le path est pas incorrecte mais il n'est pas complet
            # on va donc lui ajouter une parenthese de gauche si on a pas depasser le nombre autorise ou/et de droite (2e condition) si on a pas depasser le nombre autorise
            if leftParentheseNum < n:
                queue.append((curPath+"(",leftParentheseNum+1,rightParentheseNum))              
            if rightParentheseNum < n : 
                queue.append((curPath+")",leftParentheseNum,rightParentheseNum+1))
            
        return output    






