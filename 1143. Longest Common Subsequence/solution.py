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
        
        def dfs(idx1,idx2):  # nous rend la common subsequence de text1[idx1:] et text2[idx2:]
            
            # si on a fini de lire une des deux string alors on remonte la recursion en retournant 0 qui sera la somme initiale  
            if idx1 > len(text1)-1 or idx2 > len(text2)-1:   
                return 0                # c'est tres important que le base case rend 0 (ou une constante), ca va permettre de traduire facilement le top-down en bottom-up
            
            # cas 1 : si la premiere lettre des deux string est la meme alors on a trouver une lettre de la common subsequence donc on fait +1 
            #         et on s'avance de 1 dans les deux strings. 
            if text1[idx1] == text2[idx2] :
                return 1+dfs(idx1+1,idx2+1)
            
            # cas 2 : si pas cas 1 alors ou on considere que la lettre va faire partie de la common subsequence ou on considere que celle ci ne va pas faire partie de la CS. 
            # au retour de la recursion on va retourner la valeur max des enfant car c'est elle la LONGEST common subsequence 
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

Quand on fait un bottom-up il faut essayer de faire l'inverse de la recursion dfs top-down, car ca permet de faire la 'traduction' de facon intuitive car le calcule de la recursion se fait 
en remontant c'est donc cette partie qu'il faut 'traduire' en bottom-up :
La recursion top-down descend la recursion jusqu'au base case et puis la elle arrete les appel recursive et c'est en remontant qu'elle fait les calcules , donc au finale le calcule se fait
en partant du base case et en remontant vers le cas generale. Ici le base case c'est quand UNE DES DEUX string est vide et le cas generale c'est quand on ce trouve au debut des deux mots.
Donc dans le bottom-up aussi si une des deux phrase et vide (cad si idx1 > n-1 or idx2 > m-1) alors la valeur sera 0 (il va donc avoir une ranger et une colonne de 0 qui 
represente le cas ou les phrases sont vide). Dans le bottom-up on va commencer par le cas "le plus" de base c'est le cas ou LES DEUX phrase sont vide cad que idx1 > n-1 and idx2 > m-1  .
Le cas 'le plus' de base correspond au cas ou row==n et col==m , puisque le tableau dp est de la forme suivante : 

                                       0   1   2         m              
                                      -------------     -----                  
                                   0  |   |   |   | ... |   |                       
                                      -------------     -----                                
                                   1  |   |   |   | ... |   |               
                                      -------------     -----             
                                        .   .   .    .    .                                                                           
                                        .   .   .    .    .                                
                                      -------------     -----                                                     
                                   n  |   |   |   | ... | X |                                   
                                      -------------     -----       
                                      
C'est pour cela qu'on va commencer l'iteration de notre tableau par la case en bas a droite (ou il ya le X) qui est la case qui est le cas 'le plus' base case.  
On doit parcourir tout les case du tableau car chaque case represente un autre subproblems

On utilisera un tableau 2D (car 2 parametres) de la facon suivante : les column du tableau represente idx2 il auront donc une valeur de 0 a m (inclu , m represente le cas ou idx>m-1) 
et les row represente idx2 il auront donc une valeur de 0 a n (inclu , n represente le cas ou idx>n-1) 

prenons pour exemple : txt1='cab' , txt2='ead' alors on aura le tableau suivant :

     0   1   2   3
   -----------------
0  |   |   |   |   |  
   -----------------
1  |   | X |   | Y | 
   -----------------
2  |   |   |   |   |
   -----------------
3  |   |   |   |   |
   -----------------
   
Chaque cellule represente un subproblem , par exemple la cellule avec le X represente dfs(1,1) ( cad dfs("ab","ad") ) ou par exemple la celulle avec le Y represente dfs(1,3) (cad dfs("ab","")).

Comme dans la recursion dfs on a vue que dfs(idx1,idx2) nous rend la common subsequence de text1[idx1:] et text2[idx2:] de meme dans le bottom-up : tab[idx1][idx2] nous rend la common
subsequence de text1[idx1:] et text2[idx2:] .

Comme dans la recursion, ici aussi on a 2 cas a traiter a chaque fois :  

    - la premiere lettre de chaque mot est identique, dans ce cas dans la recursion dfs(idx1,idx2) est egale a 1+dfs(idx1+1,idx2+1) donc de meme dans bottom-up dans ce cas 
    tab[idx1][idx2] est egale a 1+tab[idx1+1][idx2+1] .

    exemple :    soit text1='ab' text2='ad' alors :
    
         0   1   2 
       -------------
    0  | X |   |   |      puisque text1[0] == text2[0] alors tab[0][0] (la case avec le X)  donc tab[0][0] = 1 + tab[0+1][0+1] (cad 1+valeur de la case avec le D)
       -------------      
    1  |   | D |   | 
       -------------
    2  |   |   |   |
       -------------

    - la premiere lettre de chaque mot est pas identique, dans ce cas dans la recursion dfs(idx1,idx2) est egale a max(dfs(idx1,idx2+1),dfs(idx1+1,id2)), donc de meme dans bottom-up dans ce cas 
    tab[idx1][idx2] est egale a max(tab[idx1][idx2+1],tab[idx1+1][idx2])

    exemple :    soit text1='cb' text2='ad' alors :
    
         0   1   2 
       -------------
    0  | X | Y |   |      puisque text1[0] != text2[0] alors tab[0][0] (la case avec le X)  egale a max(tab[0][0+1], tab[0+1][1])  (cad max(Y,Z))
       -------------      
    1  | Z |   |   | 
       -------------
    2  |   |   |   |
       -------------

Donc comme on a vu, pour calculer tab[row][col] il va nous falloir : tab[row][col+1],tab[row+1][col]  ou tab[row+1][col+1]  cad pour calculer n'importe qu'elle case il nous faudra 
la case d'en bas, de droite et en diagonale donc il nous faudra parcourir soit row par row (de droite a gauche) soit col par col (de bas en haut), dans les deux cas ca repondra a nos
besoin (dans cette exercice). nous on va choisir de parcourir col par col.
il nous faut des valeur de depart qui n'ont pas besoin d'etre calculer avec des valeurs precedente (ce sont les bases cases), pour qu'on puisse ensuite utiliser c'est valeur de depart 
pour calculer le reste ( Dans tout les dp tabulation ca marche comme ca il nous faut des valeur de depart pour 'lancer' le calcule ) ce sont les bases case .
les base case vont etre calculer en premier ce qui va nous permettre de calculer le reste , c'est pour cela qu'on commence l'iteration au "plus" base case possible comme on a vue en haut.



Maintenant on peut voir le code est comprendre comment il marche , il commence en bas a droit puis remonte colonne par colonne . 

     0   1   2   3  
   -----------------
0  | 0 | 0 | 0 | 0 |
   -----------------
1  | 0 | 0 | 0 | 0 |
   -----------------
2  | 0 | 0 | 0 | 0 |     # on commence par la case avec le X puis on remonte la colonne et ainsi de suite. 
   -----------------
3  | 0 | 0 | 0 | X |
   -----------------
   
   
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n=len(text1)
        m=len(text2)
        
        # Make a grid of 0's with extra column an extra row, for the case where idx1>n-1 and where idx2>m-1
        dp_grid = [[0 for _ in range(m+1)] for _ in range(n+ 1)]
        
        # Iterate up each column, starting from the last one.
        for col in range(m-1,-1,-1):
            for row in range(n-1,-1,-1):
                # base case :
                if row > n-1 or col > m-1:   
                    # on peut mettre juste continue car ca vaut deja 0 toute les cellules, mais c'est pour etre plus claire que j'ai ecrit dp_grid[row][col]=0
                    dp_grid[row][col]=0            
                # If the corresponding characters for this cell are the same :
                elif text1[row]==text2[col] :
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different :
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]
 
        
"""#bonus #sol4 #dp tabulation with less memory utilisation #TC O(n*m) SC O(min(m,n))
comme on a peu le constater chaque case pour etre calculer a besoin de la case diagonal bas (cas 1) ou des cases a droite et en bas (cas 2) donc on a besoin au finale en meme temps que 
de 2 colonnes (ou que deux row mais ici comme on a fait l'iteration col par col alors pour que ca soit la meme chose on va prendre deux col (si on fait l'iteration row par row alors on 
prends 2 row) ) :

par exemple pour cette exemple :

     0   1   2  
   -------------
0  | 0 | 0 | 0 | 
   -------------
1  | 0 | 0 | 0 | 
   -------------
2  | 0 | 0 | 0 |     
   -------------
    

donc :  (remarque : les 0 dans les tableau en bas sont les bases case qui n'utilise pas de valeur precedente pour etre calculer)
                          1   2                                                          0   1                                                        
                        --------                                                       --------                                                                        
                     1  | Z | 0 |                                                   1  | S | Z |                                                                            
                        ---------                                                      ---------                                                        
il suffit d'avoir :  2  | Y | 0 |   pour caluler Y,Z  . puis il suffit d'avoir :    2  | R | Y |   pour calculer R,S.        
                        ---------                                                      ---------                                                       
                     3  | 0 | 0 |                                                   3  | 0 | 0 |                                                                                 
                        ---------                                                      ---------                                               
                                                                                                                                      
                          
remarque: on choisira le mot le plus petit pour les rows car en column on en a deux et les row ca depend du mot donc c'est pour cela que SC egale O(min(n,m))

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        # now text1 is the smallest text
        
        n=len(text1)
        m=len(text2)
        
        # les deux col pour calculer
        previous = [0] * (n + 1)
        current = [0] * (n + 1)
        
        # iterate on col*row subsequence but the table is only previous and current row
        # current c'est la seul colonne qui va etre modifier , on fait l'iteration de haut en bas de la colonne 
        for col in range(m-1,-1,-1):
            for row in range(n-1,-1,-1):
                # base case :
                if row > n-1 or col > m-1:  
                    current[row] = 0        # current est une colonne donc les index sont les row
                # cas 1    
                elif text2[col] == text1[row]:            
                    current[row] = 1 + previous[row + 1]      # previous c'est col+1 par rapport a current donc previous[row+1] ca veut dire avance une colone apres current et descent une case
                # cas 2                                       # donc  previous[row + 1] represente la case en diagonale
                else:                                   
                    # previous[row] ca represente la case a droite 
                    # current[row+1] ca represente la case en bas 
                    current[row] = max(previous[row], current[row + 1])
                    
            # The current column becomes the previous one, and vice versa.
            # il faut que current devient previous car si on fait que previous = current alors quand on va modifier previous ca modifie current 
            # car current est un array donc quand on fait previous = current ,previous pointe su la meme adresse que current, ca ne va pas etre juste une copie.
            # donc comme on a initialiser previous et current comme 2 array diff alors quand on fait le swap elle reste deux array diff 
            previous, current = current, previous
        
        # The original problem's answer is in previous[0] (and not in current since we did a swap). Return it.
        return previous[0]


