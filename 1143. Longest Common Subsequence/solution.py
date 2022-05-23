"""
INTRO :
A subsequence of a string is a new string generated from the original string with the possibility (pas obliger cad on peut supprimer aucun ca reste une subsequence) of deleting some 
characters without changing the relative order of the remaining characters .
For example, "ACE" is a subsequence of "AbCdE" but "AEC" is not a subsequence of "AbCdE" since the order was not preserved.

Tout les solutions qu'on va voir sont baser sur l'idee que chaque lettre fait partie on non du common subsequence : 
explication : soit 2 strings:  txt1= 'actg' , txt2= 'tgact' on recherche les common subsequences , on doit donc parcourir une string et la comparer avec la deuxieme .
on va comparer txt1 avec txt2 , chaque lettre de txt1 peut etre ou non dans le common subsequence avec txt2:
 -> Cas ou on considere la lettre comment fesant partie de la common subsequence : 
        Par exemple la premiere lettre de txt1 'a' si on considere qu'elle est une lettre de la common subsequence alors il faut qu'on cherche 'a' dans 'tgact' et donc dans notre 
        cas on continue sur txt1='actg' et txt2='gact' car on a pas encore trouver 'a'.
 -> Cas ou on ne considere pas la lettre comment fesant partie de la common subsequence : 
        Par exemple la premiere lettre de txt1 'a' si on ne considere pas qu'elle est une lettre de la common subsequence alors on ne doit pas chercher cette lettre dans txt2 donc on 
        va s'avancer dans txt1 sans s'avancer dans txt2 (car on ne cherche pas 'a' dans txt2) cad dans notre cas on continue sur txt1='ctg' et txt2='tgact'.
De plus a chaque fois qu'on trouve une lettre en commun alors on avance dans txt1 et txt2 car on a trouver la lettre de txt1 dans txt2 donc forcement on s'avance dans txt1 et txt2 
exemple si on a txt1='tg' et txt2='tac' alors 't' est en commun donc LenghtCommonSubsequence += 1 et on continue sur txt1='g' et txt2='ac'.

ccl : 
il existe 2 cas : 
-1er cas : les lettres en debut des strings sont les memes donc LenghtCommonSubsequence += 1 et on s'avance de 1 dans les 2 strings.
-2em cas : les letres ne sont pas les memes , on aura 2 possibilites :
            - soit on considere la lettre comme etant une lettre de la common subsequence et donc on s'anvance de 1 dans la 2eme strings.
            - soit on ne considere pas la lettre comme etant une lettre de la common subsequence et donc on s'anvance de 1 dans la 1er strings. 
   
   
   
remarque (peu etre dur a comprendre) : 
construisons l'arbre de recursion de l'exemple suivant txt1 = 'ac' txt2= 'cbga'   ( le meme pb se trouve dans tout les cas ) 

                            ("ac", "cbga")
                          /                \
             ("ac", "bga")                  ("c", "cbga") [1]
               /       \                         |
     ("ac", "ga")   ("c", "bga") [2]        ("", "bga")
     
a chaque etape : a gauche le choix de considerer la premiere lettre comme fesant partie de la common subsequence a droite le choix inverse 
                        
comme on peut le voir la recursion [1] va forcement donner une meilleur reponse que [2] car il ya plus de lettre dans txt2 .
je parle de ca car des fois dans les recursion on fait des choix qui sont pas forcement top a chaque etape mais globalement ca va nous donner un bon choix . c'est important quand 
on code d'essayer a avoir qqch de global et pas trop rentrer dans le detaille meme si ca va etre un peu plus optimale car le code devient ilisible si il ya trop de condition . 
                     
"""

""" #sol 1 #not my sol #dfs(recursion) (appeler aussi brute-force recursion) #TC O(2^(n+m)) #SC O(n+m) avec len(txt1)==n , len(txt2)==m

voir intro pour comprendre voir aussi arbre de recursion GITHUB. 

chaque lettre peut soit faire partie de la common subsequence soit ne pas faire partie , si on trouve une lettre en commun alors lenghtCommonSubsequence+=1 et on s'avance dans les
deux string.

TC analyse : 
pour la hauteur de l'arbre voir l'analyse du SC , comme on a une double recursion donc notre arbre de recursion est un arbre binaire (au pire des cas c'est un arbre binaire car si il 
ya aucune lettre en commun ca va faire a chaque fois une double recursion), de plus la hauteur est egale a O(n+m) donc TC est O(2^(n+m)) .

SC analyse : 
la taille du stack de recursion est de la taille de la hauteur de l'arbre, la hauteur de l'arbre est egale a O(n+m) (precisement n+m-1) car au pire des cas on lit tout les lettres 
de txt1 et aussi tout les lettres de txt2 (sauf une) car si on voit l'arbre de recursion il va toujours avoir un leaf ('',char) ou (char,'') (ce leaf s'obtien a l'aide qu'on s'avance dans txt1
puis txt2 de facon a parourir tout les lettre et ne pas finir avec qqch comme ('',motAvecPlusieursLettre) en tant que leaf)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(idx1,idx2):
            
            # si on a fini de lire une des deux string alors on remonte la recursion en retournant 0 qui sera la somme initiale  
            if idx1 > len(text1)-1 or idx2 > len(text2)-1:   
                return 0       
            
            # cas 1 : si la premiere lettre des deux string est la meme alors on a trouver une lettre de la common subsequence don on fait +1 
            #         et on s'avance de 1 dans les deux strings. 
            if text1[idx1] == text2[idx2] :
                return 1+dfs(idx1+1,idx2+1)
            
            # cas 2 : si pas cas 1 alors on on considere que la lettre va faire partie de la common subsequence ou on considere que celle ci ne va pas faire partie de la CS. 
            # au retour de la recursion on va retourner le valeur max des enfant car c'est elle la longuest common subsequence 
            return max(dfs(idx1,idx2+1),dfs(idx1+1,idx2))
        
        return dfs(0,0)  # retourne la taille de LCS


""" # sol2  # not my sol  # dp top-down(recursion) / memoization    # TC O(n*m)   # SC O(n*m) du au cache  (voir analyse)
on utilise un cache pour ne pas calculer les recursion deja calculer. 
(on peut voir dans l'arbre de recursion de la solution 1 que il ya bcp de redondance).

TC et SC analyse : 
la fonction recoit deux parametre qui sont la position de la lettre qu'on lit dans txt1 et txt2. il existe n possible position/valeur pour idx1 et m possible position/valeur pour idx2, donc en 
tout il y'a n*m paire de parametres possible cad il ya n*m combinaisons . donc on va avoir un TC egale O(n*m) car on a n*m subproblems et chaque subproblem coute O(1) (car la chaque recursion
coute O(1)) . le cache va etre de taille O(n*m) car on doit cache les n*m subproblems pour ne pas avoir a les recalculer.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}   # chaque key va etre un tuple (idx1,idx2) qui sont les paramtere de la fct 
        
        def dfs(idx1,idx2):
            
            # cache lookup
            if (idx1,idx2) in cache :  # search in dictionnary is O(1)
                return cache[(idx1,idx2)] 
            
            if idx1 > len(text1)-1 or idx2 > len(text2)-1:
                return 0
            
            # cas 1
            if text1[idx1] == text2[idx2] :
                res = 1+dfs(idx1+1,idx2+1)
                cache[(idx1,idx2)] = res
                return res
            
            # cas 2
            res = max(dfs(idx1+1,idx2),dfs(idx1,idx2+1))
            cache[(idx1,idx2)] = res
            return res
        
        return dfs(0,0)

"""
#sol2 bis # dp top-down with lru_cache #TC and SC same as above
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def dfs(idx1,idx2):
            
            if idx1 > len(text1)-1 or idx2 > len(text2)-1:   
                return 0       
        
            if text1[idx1] == text2[idx2] :
                return 1+dfs(idx1+1,idx2+1)
       
            return max(dfs(idx1,idx2+1),dfs(idx1+1,idx2))
        
        return dfs(0,0)   



"""#sol 3 #dp bottom-up/tabulation(iterative) #TC O(n*m) car on parcours tout le tableau qui est de taille n*m   # SC O(n*m) du au tableau 

la fonction recoit deux parametre donc on va utiliser un tableau 2D pour la tabulation , en tout il ya n*m subproblems (car le premier parametre a n valeur possible et le deuxieme
a m valeur possible donc en tout n*m combinaisons/subproblems) donc le tableau sera de cette taille. On commence l'iteration par les plus petit subproblems , on store l'info et ainsi 
on pourra calculer les larger subproblemes qui dependent des smallest subproblems . 

le bottom-up veut juste dire qu'on utilise un tableau , on peut commencer le calcule par le debut ou la fin ca change rien , mais moi je prefere ici commencer par la fin (dans certain cas 
c'est plus intuitive de commencer par le debut) car si on regarde comment la recursion top-down marche (c'est comme ca tout le temps) : elle descend la recursion jusqu'au 
base case et puis la elle arrete les appel recursive et c'est en remontant qu'elle fait les calcules , donc au finale le calcule se fait en partant du base case (ici le base case 
c'est quand une des deux string est vide) et en remontant vers le cas generale (ici le cas le plus generale c'est quand on ce trouve au debut des deux mots).
Donc dans le bottom-up on va commencer par le cas "le plus" de base c'est le cas ou les deux phrase sont vide est donc la valeur est 0 (pour cela on va rajouter une ranger et une colonne
de 0 qui represente le cas ou les phrases sont vide) et on va remonter vers le cas generale (remarque: si on regarde l'algo on remarque qu'il ne s'occupe pas des cas on il ya une des
phrase qui est vide (cad il ya pas une case qui correspond apar exemple ("abd","") ou ("a","")) la raison est que tout c'est cas valent 0 donc on va utiliser la ranger ou ligne des 0 pour les simuler).
C'est pour cela qu'on va commencer l'iteration de notre tableau par la case en bas a droite qui est la case qui vient juste apres les bases cases (remarque: a chaque fois qu'on fait 
un dp tabulation on initialise le tableau avec les valeurs du base case puis on commence par le cas qui vient juste apres le base case) , ici les bases case sont quand on a une des phrases vide 
donc le premier smallest subproblems qui vient apres c'est le cas de 1 lettre dans chaque mot (cad le cas ou on a la dernier lettre de chaque mot seulement) , ce cas est representer par
le case d'en bas a droite. 
On doit parcourir tout les case du tableau car chaque case represente un autre subproblems

prenons pour exemple : txt1='cab' , txt2='ead' alors on aura le tableau suivant :

     c   a   b  
   -------------
e  |   |   |   |  
   -------------
a  |   | X |   | 
   -------------
d  |   |   |   |
   -------------
   
Chaque cellule represente un subproblem , par exemple la cellule avec le X represente lcs("ab","ad") .
comme on a vue dans la recursion qu'il ya deux cas a traiter : 
- la premiere lettre de chaque mot est identique, dans ce cas on a fait dans la recursion 1+dfs(idx1+1,idx2+1), or le calule se fait en remontant donc dfs(idx1,idx2) va etre egale (dans notre 
cas ou txt[idx1]==txt[idx2] ) a 1 plus la valeur retourner par dfs(idx1+1,idx2+1) donc dans notre tableau ca veut dire que la valeur de la case (idx1,idx2) va etre 1 plus la valeur de la case
(idx+1,idx+2)  cad la case en diagonale en bas.

exemple :
     c   a   b 
   -------------
e  |   |   |   |      Dans la case tab[row][col], la case avec le X la premiere lettre des 2 mots "ab","ad" est identique donc tab[row][col] = 1 + tab[row+1][col+1]
   -------------      cad 1+valeur de la case avec le D
a  |   | X |   | 
   -------------
d  |   |   | D |
   -------------

- la premiere lettre de chaque mot est pas identique, dans ce cas on a fait dans la recursion max(dfs(idx1,idx2+1),dfs(idx1+1,id2)), or le calule se fait en remontant donc dfs(idx1,idx2) 
va etre egale (dans notre cas ou txt[idx1]!=txt[idx2] ) a max entre la valeur retourner par dfs(idx1,idx2+1) et la valeur retourner par dfs(idx1+1,idx2) donc dans notre tableau ca veut 
dire que la valeur de la case (idx1,idx2) est egale a max entre la valeur de la case (idx1,idx2+1) et la valeur de la case (idx1+1,idx2)

exemple :
     c   a   b 
   -------------
e  | X | Y |   |      Dans la case tab[row][col], la case avec le X la premiere lettre des 2 mots "cab","ead" est pas identique donc tab[row][col] = max(tab[row+1][col],tab[row][col+1])
   -------------      cad max(case avec Z ,case avec Y)
a  | Z |   |   | 
   -------------
d  |   |   | D |
   -------------


Maintenant on peut voir le code est comprendre cmment il marche , il commence en bas a droit puis remonte colonne par colonne . 
rappel: on rajoute une range est une ligne pour les base case , donc le tableau va etre comme ca a l'initialisation :
par exemple pour  txt1='cab' , txt2='ead' alors on aura le tableau suivant :

     c   a   b  
   -------------
e  | 0 | 0 | 0 | 0
   -------------
a  | 0 | 0 | 0 | 0
   -------------
d  | 0 | 0 | X | 0     # on commence par la case avec le X puis on remonte la colonne. 
   -------------
     0   0   0   0

(intuitivement on rajoute la range et colonne de 0 car on a besoin des case de en bas a droite et en diagonale de chaque case pour pouvoir la caluler donc au debut la valeur est 0)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Make a grid of 0's with extra column an extra row, here number of row == len(text1) + 1 and number of column == len(text2) + 1
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Iterate up each column, starting from the last one.
        for col in range(len(text2)-1,-1,-1):
            for row in range(len(text1)-1,-1,-1):
                # If the corresponding characters for this cell are the same :
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different :
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]
                    
        
"""#bonus #sol4 #dp tabulation with less memory utilisation #TC O(n*m) SC O(min(m,n))
comme on a peu le constater chaque case pour etre calculer a besoin de la case diagonal bas (cas 1) ou des cases a droite et en bas (cas 2) donc on a besoin au finale en meme temps que 
de 2 colonnes :
par exemple pour cette exemple :
     c   a   b  
   -------------
e  | 0 | 0 | 0 | 0
   -------------
a  | 0 | 0 | 0 | 0
   -------------
d  | 0 | 0 | 0 | 0    
   -------------
     0   0   0   0

donc :
                          b                                                               a   b                                                          c  a
                        -----                                                           --------                                                       ---------                    
                     e  | Z | 0                                                      e  | Q | Z |                                                    e | V | Q |                        
                        -----                                                           ---------                                                      ---------     
il suffit d'avoir :  a  | Y | 0     pour caluler X,Y,Z . puis il suffit d'avoir :    a  | S | Y |    pour calculer R,S,Q. puis il suffit d'avoir :   a | U | S |   pour calculer T,U,V .           
                        -----                                                           ---------                                                      ---------      
                     d  | X | 0                                                      d  | R | X |                                                    d | T | R |                             
                        -----                                                           ---------                                                      ---------
                          0   0                                                           0   0                                                          0   0
                          
remarque: on choisira le mot le plus petit pour les rows car en column on en a deux et les row ca depend du mot donc c'est pour cela que SC egale O(min(n,m))

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        # now text1 is the smallest text
        
        # The previous and current column starts with all 0's and like 
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        
        # iterate on col*row subsequence but the table is only previous and current row
        # current c'est la seul colonne qui va etre modifier , on fait l'iteration de haut en bas de la colonne (donc on change de row a chaque fois)
        for col in range(len(text2)-1,-1,-1):
            for row in range(len(text1)-1,-1,-1):
                if text2[col] == text1[row]:                # cas 1
                    current[row] = 1 + previous[row + 1]
                else:                                       # cas 2
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one, and vice versa.
            # on s'en fou des valeur du nouveau current car ils vont etre modifier donc meme si elles valent maintenant previous (apres le swap) ca nous derenge pas car
            # on ne l'est regarde pas 
            previous, current = current, previous
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]


