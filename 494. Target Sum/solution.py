# CETTE SOLUTION EST LE TOP DU TOP DE MES SOLUTION CONSERNANT LE DP ELLE MA PRIS PLUS DE 3 JOURS ET PLUS DE 2 MOIS D'EXPERIENCE DANS DP !!!

""" #sol 1 # dfs(recursive brute force)  #TC O(2^n)  #SC O(n)

On a chaque fois deux possibilite soit ajouter '+' soit '-' donc on va faire une double recursion une pour chaque choix.
On recherche le nbr d'expressions qui prennent en compte TOUT les elements de nums et qui sont egale a target , donc pour cela une fois qu'on a fini de lire tout les elements de nums
on regarde si l'expression obtenue est egale a target , si oui alors on on doit faire +1 au resultat finale  et si non alors on ne rajoute rien cad 0 au resultat finale.
Au finale on additionne tout les resultat obtenue ce qui va nous donner le nombre total d'expressions qui prennent en compte TOUT les elements de nums et qui sont egale a target.

Analyse SC  :
la hauteur de l'arbre est de taille O(n) (avec n=len(nums)) car a chaque appel rec on avance d'un element (car on fait 'idx+1' ) dans nums et donc au finale la profondeur de la recursion 
va etre egale au nombre d'element dans nums cad n. donc la recursion stack et de taille O(n)

Analyse TC :
on fait a chaque fois une double recursion donc on va obtenir un arbre de recursion binary , de plus comme on a vue dans l'analyse du SC , la hauteur de l'arbre est O(n) , donc TC 
egale O(2^n)

REMARQUE SUPER IMPORTANTE : 
IL FAUT TOUJOURS QUE LES BASE CASE DE LA RECURSION RETOURNE UNE CONSTANTE ET NON UNE VARIABLE POUR QU'ON PUISSE FACILEMENT PASSER DU DFS AU DP BOTTOM-UP
"""
 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        
        def dfs(idx,curSum) :
            
            #base case : si on a fini de lire tout les element de nums alors si l'expression egale target on return 1 sinon on return 0
            if idx>n-1 :
                if curSum == target :
                    return 1 
                else :
                    return 0
                
            # a chaque fois on a le choix entre '-' ou '+'
            return dfs(idx+1,curSum-nums[idx]) + dfs(idx+1,curSum+nums[idx])
        
        return dfs(0,0)
    
"""
# sol 2 #dp top-down/memoization (recursive) # TC O(n*sums(nums)) # SC O(n*sums(nums))  ( on ne prend pas en compte la taille O(n) de la recursion stack car elle est negligeable dans ce cas )

Utilisation d'un cache pour les resultat deja calculer. 

La recursion dfs recoit 2 parametres , le premier parametre index peut avoir une valeur de 0 a n (car on commence le dfs a idx==0 et a chaque appel rec on incremente l'idx de 1 puis quand on 
arrive au cas idx==n alors on ne fait plus d'appel recursive et donc on incremente plus l'idx donc la dernier valeur possible c'est idx==n) , le deuxieme parametre curSum peut avoir une valeur 
entre -sum(nums) (si on met que des '-' entre tout les element) et +sum(nums) (si on met que des '+' entre les elements ). Il y'a donc en tout (n+1)*(2*sum(nums)+1) differente 
combinaison/subproblem .

Analyse SC :

Il nous faut un cache pour garder les (n+1)*(2*sum(nums)+1) different resultat des (n+1)*(2*sum(nums)+1) differente combinaison/subproblem .
La taille du cache va donc etre O(n*sums(nums)) 

Analyse TC :

Comme on utilise un cache alors on ne va pas calculer le meme subproblem plus d'une fois , donc le nombre total de recursion va etre egale au nombre de subprobleme different cad dans le recursive tree on va avoir au max (n+1)*(2*sum(nums)+1) recursion/nodes et puisque chaque recursion/node coute O(1) alors au total TC va etre egale a (n+1)*(2*sum(nums)+1) cad a O(n*(sum(nums)). 

Remarque : il est tres facile de passer du dfs au dp top-down/memoization car on rajoute simplement un cache (ca va tjrs etre un dictio) et on va a chaque recursion regarder si le subprobleme 
et deja dans le cache ou non, de plus a chaque fois qu'on calcule un subprobleme on va ajouter le resultat au cache.

"""    

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        
        cache = {}
        
        def dfs(idx,curSum) :
            
            # before everything take a look if the subproblem is already calculated 
            # cache lookup
            if (idx,curSum) in cache :
                return cache[(idx,curSum)]
                   
            if idx>n-1 :
                if curSum == target :
                    return 1 
                else :
                    return 0
                
            res = dfs(idx+1,curSum-nums[idx]) + dfs(idx+1,curSum+nums[idx])
            cache[(idx,curSum)] = res       # caching result
            return res
        
        return dfs(0,0)


""" # sol 3  # dp bottom-up/tabulation (iterative)  # TC O(n)*(sum(nums))  puisqu'on parcours chaque case d'un tableau de taille (n+1)*(2*sum(nums)+1)  # SC O(n)*(sum(nums)) car on utilise un 
tableau de taille (n+1)*(2*sum(nums)+1) 

SUPER FACON DE PASSER DE TOP DOWN / MEMOIZATION A DP BORROM-UP /TABULATION :

=> ETAPE 1 : FIXER TAILLE ET DIMENSSION DU TABLEAU EN FONCTION DU NOMBRE DE SUBPROBLEM DIFFERENT ET DU NOMBRE DE PARAMETRE OBLIGATOIRE DE LA RECURSION 

SUPER IMPORTANT POUR LE DP BOTTOM UP (REGLE D'OR): IL FAUT SAVOIR COMBIEN Y'A T-IL DE SUBPROBLEM DIFFERENT ET EN FONCTION DE CELA ON VA CONSTUIRE UN TABLEAU QUI CONTIENT LE MEME NOMBRE DE 
CELLULE QUE LE NOMBRE DE SUBPROBLEM. LA DIMENSION DU TABLEAU DEPEND DU NOMBRE DE PARAMETRE INDISPENSABLE QUE LA RECURSION DFS/BRUTE-FORCE UTILISE. 

La recursion dfs recoit 2 parametres , le premier parametre index peut avoir une valeur de 0 a n (car on commence le dfs a idx==0 et a chaque appel rec on incremente l'idx de 1 puis quand on 
arrive au cas idx==n alors on ne fait plus d'appel recursive et donc on incremente plus l'idx donc la dernier valeur possible c'est idx==n) , le deuxieme parametre curSum peut avoir une valeur 
entre -sum(nums) (si on met que des '-' entre tout les element) et +sum(nums) (si on met que des '+' entre les elements ). Il y'a donc en tout (n+1)*(2*sum(nums)+1) differente 
combinaison/subproblem .
Pour la solution dp bottom up / tabulation, on va donc construire un tableau qui contient (n+1)*(2*sum(nums)+1) cellule , car chaque cellule represente un different subproblem. Pour cela on va 
utiliser un tableau 2D ou les row vont representer les index et les col vont representer la curSum . 

Les col et row du tableau sont forcement dans l'ordre suivant 0,1,2,3,4,5,... car ce sont des indices de tableau a 2 dimension, cad n'importe quelle tableau 2D va etre sous la forme :

                                        0   1   2         y              
                                      -------------     -----                  
                                   0  |   |   |   | ... |   |                       
                                      -------------     -----                                
                                   1  |   |   |   | ... |   |               
                                      -------------     -----             
                                        .   .   .    .    .                                                                           
                                        .   .   .    .    .                                
                                      -------------     -----                                                     
                                   x  |   |   |   | ... |   |                                   
                                      -------------     -----     
                                      
le premier parametre index peut avoir une valeur entre 0 et n (inclu, si idx==n alors c'est le base case) donc la dernier row aura la valeur n .

le deuxieme parametre curSum peut avoir une valeur entre -sum(nums) et +sum(nums) or puisque les valeurs des col sont forcement dans l'ordre 0,1,2,3,... alors doit adapter la valeur de curSum 
(qui varie de -sum(nums) a +sum(nums)) au valeur de col , donc on considerera que :
 -  col==0 represente la valeur curSum=-sum(nums) .
 -  col==1 represente la valeur curSum=(-sum(nums)+1).
 -  col==2 represente la valeur curSum=(-sum(nums)+2).
 -  ...   
 -  col==sum(nums) represente la valeur curSum=(-sum(nums)+sum(nums)) cad curSum=0 .
 -  ... 
 -  col==2*sum(nums) represente la valeur curSum=(-sum(nums)+2*sum(nums)) cad curSum=sum(nums).
Cad que curSum est represente par la col==sum(nums)+curSum (ex si on a curSum=-3 alors la col == sum(nums)-3 represente curSum=-3 ).

(
un peu de logique : 
    
    on a vue que col va de 0 a 2*sum(nums) or on veut adapter curSum qui est compris entre -sum(nums) et sum(nums) au valeur 0 a 2*sum(nums) donc col=0 represente curSum = -sum(nums)
    et col = 2*sum(nums) represente curSum = sum(nums) .
    
    pour savoir par quelle col la valeur curSum==x va etre represente , on reflechie de la sorte puisque curSum egale x ca veut dire que curSum se trouve a x valeur de 0 donc 
    puisque curSum egale 0 est represente par col==sum(nums) donc col==sum(nums)+ x represente curSum=x 

)

ccl : 
row varie de 0 a len(nums) donc il nous faut en tout len(nums)+1 ; col varie de 0 a 2*sum(nums) donc il nous faut en tout 2*sum(nums)+1 col. on va donc obtenir le tableau suivant : 

                                        0   1   2    2*sum(nums)           
                                      -------------     -----                  
                                   0  |   |   |   | ... |   |                       
                                      -------------     -----                                
                                   1  |   |   |   | ... |   |               
                                      -------------     -----                  on a donc : dp = [ [ 0 for _ in range (2*sum(nums)+1) ] for _ in range (len(nums)+1) ]
                                        .   .   .    .    .                                                                           
                                        .   .   .    .    .                                
                                      -------------     -----                                                     
                           len(nums)  |   |   |   | ... |   |                                   
                                      -------------     -----   

Puisque on a adapter la valeur de curSum au valeur de col qui varie de 0 a 2*sum(nums) alors il faut aussi adapter la valeur target(qui est la somme qu'on veut atteindre) au valeur de col :
target se trouve a target valeur par rapport a 0 (ex si target =-2 alors il est a -2 valeur par rapport a 0) donc comme dans notre tableau la somme 0 est representer par col==sum(nums) (comme 
vue precedement) alors la valeur de target adapter a notre tableau est representer par col==sum(nums)+target   (ex: si target=-2 alors la col qui represente target dans le tableau est 
col==sum(nums)+(-2) cad col==sum(nums)-2 ). 
                                     
=> ETAPE 2 : TRADUCTION DES BASE CASE ET DU CAS GENERALE (VALEUR QUI VA ETRE RETOURNER PAR LE DP) DE LA RECURSION 

Quand on fait un bottom-up il faut essayer de faire l'inverse de la recursion dfs top-down, car ca permet de faire la 'traduction' de facon intuitive car le calcule de la recursion se fait 
en remontant c'est donc cette partie qu'il faut 'traduire' en bottom-up :
La recursion top-down descend la recursion jusqu'au base case et puis la elle arrete les appel recursive et c'est en remontant qu'elle fait les calcules , donc au finale le calcule se fait
en partant du base case et en remontant vers le cas generale. Ici le base case c'est quand idx>n-1 (et dans ce cas il ya 2 possibilites si curSum == target alors on return 1 sinon on return 0),
et le cas generale (le cas pour lequel on cherche la reponse ) ici c'est dfs(0,0). 
Dans le bottom up on doit aussi avoir les meme base case que dfs mais 'traduit' , donc puisque dans le tableau du bottum-up :  row represente les index et col represente la curSum alors voici 
la 'traduction' :

        Base case du dfs :                            
        
        def dfs(idx,curSum) :
        
             if idx>n-1 :                             
                if curSum == target :                 
                    return 1                          
                else :                                
                    return 0                          
        
        TRADUCTION BASE CASE POUR DP TABULATION :

        Base case dans dp tabulation :                                      EXPLICATION DE LA TRADUCTION : 
   
              if row>n-1                         # on remplace idx par row car ds notre dp tabulation l' index est represente par les row     
              
                  if col == target :             # on remplace curSum par col car ds notre dp tabulation la curSum est represente par les col
                  
                       dp[row][col] = 1          # dans dfs quand on a return X ca veut dire que la fonction dfs(idx,curSum) va retourner X
                                                 # DP tabulation est un tableau ce n'est pas une fonction donc on retourne pas de valeur a la place on va garder la valeur dans une case 
                                                 # Chaque cellule dp[row][col] represente le resultat retourne par dfs(idx,curSum) 
                                                 # car row represente idx et col represente curSum donc dp[row][col] sera equivalent a la valeur retourner par dfs(idx,curSum)
                  else :                         
                       dp[row][col] = 0                             

La recursion dfs retourne la reponse quand elle revient au cas generale (le cas pour lequel on cherche la reponse ) , ici le cas general est dfs (0,0)  (c'est dfs(0,0) qui nous donne la reponse
du pb) c'est a dire la reponse est retourner quand index egale 0 et quand curSum egale 0. Donc dans notre dp tabulation la reponse va aussi se trouver dans la cellule qui represente l'idx 0 et 
la curSum 0 , or comme on a vue precedement row==0 represente l'index 0 et que col==sum(nums) represente curSum=0 donc a la fin du dp tabulation la reponse va se trouver dans : dp[0][sum(nums)].
on va donc retourne en fin du dp : dp[0][sum(nums)]


=> ETAPE 3 :  FIXER PAR OU ON COMMENCE (QUELLE EXTREMITE DU TABLEAU) A PARCOURIR LE TABLEAU EN FONCTION DES BASE CASE  :

voici les differente facon de commencer le parcours d'un tableau 2D: 

         0   1   2         m             
       -------------     -----              -> en partant d'en haut a gauche (X)
    0  | X |   |   | ... | Y |                       
       -------------     -----              -> en partant d'en haut a droite (Y)        
    1  |   |   |   | ... |   |               
       -------------     -----              -> en partant d'en bas a gauche (W)   
         .   .   .    .    .                                                                       
         .   .   .    .    .                -> en partant d'en bas a droite (Z)                 
       -------------     -----                                                  
    n  | W |   |   | ... | Z |                                  
       -------------     -----                       
                                                             
                                                             
Puisque c'est en remontant des bases case que la recursion dfs fait les calcules donc le calcule commence reelement par les base cases. ici les base case dans le dfs sont les suivant :

            if idx>n-1 :                             
                if curSum == target :                 
                    return 1                          
                else :                                
                    return 0 
                    
ce qui revient a c'est base case ds le dp : 

            if row>n-1 :
                if col == target :            
                   dp[row][col] = 1         
                else :                         
                   dp[row][col] = 0   
                   
Donc dans le bottom-up ca veut dire que le cas de base a pour condition row>n-1, or comme on a explique (au debut de l'etape 1) row varie entre 0 et n donc la seul extrem qui represente la 
condition row>n-1 et la row qui est egale a n. 
De plus il ya aussi une autre condition: col == target , target varie de 0 a sum(nums)*2+1 (comme on a vue apres modification) et comme on doit commencer a une extremite donc soit on 
commence avec col==0 soit avec col==sum(nums)*2+1. moi j'ai choisi ici de commencer a col==sum(nums)*2+1 . (comme ca on commencera au cote droit en bas du tableau, voir apres )

Donc le bottom-up lui va commencer le parcours du tableau par le coin du tableau qui represente TOUT les bases cases , puisque le tableau dp est de la forme suivante : 

                                        0   1   2    2*sum(nums)           
                                      -------------     -----                  
                                   0  |   |   |   | ... |   |                       
                                      -------------     -----                                
                                   1  |   |   |   | ... |   |               
                                      -------------     -----                  
                                        .   .   .    .    .                                                                           
                                        .   .   .    .    .                                
                                      -------------     -----                                                     
                           len(nums)  | Y |   |   | ... | X |                                   
                                      -------------     -----  
                                      
Donc on va commencer par la case avec le X car elle represente la case ou row==n et col==sum(nums)*2+1 (on aurait aussi peu choisir la case avec le Y car elle represente le cas ou row==n et
col==0, mais perso quand on a le choix je prefere commancer par X).


=> ETAPE 4 : TRADUCTION DU RESTE DU DFS (CE QUI N'EST PAS BASE CASE):

il nous reste plus qu'a traduire dans le dfs la ligne suivante : 

    return dfs(idx+1,curSum-nums[idx]) + dfs(idx+1,curSum+nums[idx])     
    
Cad dfs(idx,curSum) retourne dfs(idx+1,curSum-nums[idx]) + dfs(idx+1,curSum+nums[idx]) . 
DP tabulation est un tableau ce n'est pas une fonction donc on retourne pas de valeur, a la place on va garder la valeur dans une case du tableau (cad a la place de 'return' on met
'dp[row][col] = ' )
De plus on a vu que dans le dp tabulation row represente l'idx et col represente curSum . (cad on va remplacer idx par row et curSum pas col)
Donc la ligne precedente se 'traduit' par :
 
    dp[row][col] =  dp[row+1][col-nums[row]] + dp[row+1][col+nums[row]]       
    
=> ETAPE 5 : ANALYSE DU DP TABULATION OBTENUE APRES LA TRADUCTION :

DANS LE DP TABULATION ON VA TOUJOURS PARCOURIR TOUT LE TABLEAU CAD ON VA PASSER SUR TOUTES LES VALEUR POSSIBLE DE ROW ET SUR TOUT LES VALEUR POSSIBLE DE COL.
IL FAUT DONC TOUJOUR ANALYSER LE DP OBTENUE APRES LA TRADUCTION POUR VOIR SI LES VALEURS QUI PEUVENT ETRE OBTENUE RESTE DANS LES LIMITE DU TABLEAU .

notre dfs est le suivant  :

        def dfs(idx,curSum) : 
            if idx>n-1 :
                if curSum == target :
                    return 1 
                else :
                    return 0
            return dfs(idx+1,curSum-nums[idx]) + dfs(idx+1,curSum+nums[idx])
            
la dp bottom up qu'on obtient apres 'traduction' est le suivant : 
           
            if row>n-1 :
                if col == target :            
                   dp[row][col] = 1         
                else :                         
                   dp[row][col] = 0  
            
            # on ajoute 'else' car dans dfs on a un return avant cette ligne cad que si le return s'execute alors cette ligne ne s'execute pas et comme dans dp on 
            # a enlever le return alors il faut qu'on ajoute else pour reproduire le meme code cad que si le if d'avant se produit alors on ne fera pas aussi le else
            else :              
                dp[row][col] =  dp[row+1][col-nums[row]] + dp[row+1][col+nums[row]]   

Comme on a vue dans l'etape 1  :

La recursion dfs recoit 2 parametres , le premier parametre index peut avoir une valeur de 0 a n (car on commence le dfs a idx==0 et a chaque appel rec on incremente l'idx de 1 puis quand on 
arrive au cas idx==n alors on ne fait plus d'appel recursive et donc on incremente plus l'idx donc la dernier valeur possible c'est idx==n) , le deuxieme parametre curSum peut avoir une valeur 
entre -sum(nums) (si on met que des '-' entre tout les element) et +sum(nums) (si on met que des '+' entre les elements ). Il y'a donc en tout (n+1)*(2*sum(nums)+1) differente 
combinaison/subproblem .
Pour la solution dp bottom up / tabulation, on va donc construire un tableau qui contient (n+1)*(2*sum(nums)+1) cellule , car chaque cellule represente un different subproblem. Pour cela on va 
utiliser un tableau 2D ou les row vont representer les index et les col vont representer la curSum, donc row varie de 0 a n et col varie de 0 a 2*sum(nums), CAD QUE SI ON OBTIENT ROW<0 OU ROW<n
OU COL<0 OU COL>2*sum(nums) ALORS CELA REPRESENTE UN SUBPROBLEM QUI N'EXISTE PAS CAR ON A VUE QUE DANS NOS SUBPROBLEM ROW VARIE ENTRE 0 ET n ET QUE COL VARIE ENTRE 0 ET 2*sum(nums).

si on analyse la traduction obtenue on voit que SEULEMENT SI row<=n-1 (car dans ce cas on rentre pas dans le premier if) alors alors on execute :
            else :              
                dp[row][col] =  dp[row+1][col-nums[row]] + dp[row+1][col+nums[row]] 
Dans notre pb row varie entre 0 et n de plus la ligne precedente s'execute que si row<=n-1 donc quand on fait 'dp[row+1]' la valeur row+1 reste entre 0 et n car row et entre 0 et n-1 dans ce cas
donc row+1 et entre 1 et n ce qui est inclu dans les valeur valide de row qui sont entre 0 et n.

continuons l'analyse de la traduction obtenue :
Comme on a vue , la ligne 'dp[row][col] =  dp[row+1][col-nums[row]] + dp[row+1][col+nums[row]]' s'execute si row<=n-1 , la seul condition d'execution de cette ligne c'est si row<n-1 donc ca 
veut dire qu'il ya pas de condition/contrainte sur col , cad que cette ligne s'execute pour toute les valeurs possible de col (cad ,0<=col<=2*sum(nums)). Cela cause 2 pb :

1) quand on fait 'dp[row+1][col-nums[row]]' , la partie '[col-nums[row]]' qui represente l'indice des column varie entre 0-nums[row] et 2*sum(nums)-nums[row] or on a vue que l'indice des column
   peut varier que entre 0 et 2*sum(nums) car sinon cela represente un subproblem qui n'existe pas (car col represente le 2eme parametre qui varie entre 0 et 2*sum(nums) donc une valeur en 
   dessous de 0 n'existe pas dans le 2e parametre). Donc on pourra faire '[col-nums[row]]' que si col-nums[row] >= 0 (car comme on a vue que : col-nums[row] represente l'indice des column qui 
   sont sup egale a 0, donc col-nums[row] >= 0 ).

2) quand on fait 'dp[row+1][col-nums[row]]' , la partie '[col+nums[row]]' qui represente l'indice des column varie entre 0+nums[row] et 2*sum(nums)+nums[row] or on a vue que l'indice des column
   peut varier que entre 0 et 2*sum(nums) car sinon cela represente un subproblem qui n'existe pas (car col represente le 2eme parametre qui varie entre 0 et 2*sum(nums) donc une valeur au 
   dessus de 2*sum(nums) n'existe pas dans le 2e parametre). Donc on pourra faire '[col+nums[row]]' que si col+nums[row] <= 2*sum(nums) (car comme on a vue que : col+nums[row] represente l'indice 
   des column qui sont inf egale a 2*sum(nums), donc col+nums[row] <= 2*sum(nums) ).
   
  ccl : si col-nums[row] >= 0 alors on peut faire '[col-nums[row]]' et si col+nums[row] <= 2*sum(nums) alors on peut faire '[col+nums[row]]' ou plus precisement :
        
        - si col-nums[row] < 0 alors on peut faire QUE '[col+nums[row]]' donc on ajoute la condition :
            
                    if col-nums[row] < 0 :
                        dp[row][col]=dp[row+1][col+nums[row]]

       - si col+nums[row] > 2*sum(nums) alors on peut faire QUE '[col-nums[row]]' donc on ajoute la condition :
            
                    if col+nums[row] > 2*sum(nums) :
                        dp[row][col]=dp[row+1][col-nums[row]]

Donc au final on obtient le code suivant apres l'analyse de traduction :

                if row>n-1 :
                    if col == target :
                        dp[row][col] = 1 
                    else :
                        dp[row][col] = 0
                elif col-nums[row] < 0 :
                    dp[row][col] = dp[row+1][col+nums[row]]
                elif col+nums[row]> 2*sum(nums) :
                    dp[row][col] = dp[row+1][col-nums[row]]    
                else :
                    dp[row][col] = dp[row+1][col-nums[row]] + dp[row+1][col+nums[row]]
                    
# remarque: dp[row][col] ne peut avoir qu'une valeur donc il faut toujours que si on rentre dans une condition ou on fait un assignement a dp[row][col] alors il ne faut pas qu'on puisse
rentrer dans une autre condition avec un autre assignement a dp[row][col] donc c'est pour cela que tout les condition sont des condition 'else' .


=> ETAPE 6 : FIXER COMMENT ON PARCOURS LE TABLEAU (ROW PAR ROW OU COL PAR COL)  :

Puisque dp[row][col] peut utiliser dp[row+1][col-nums[row]] et/ou dp[row+1][col+nums[row]] alors pour calculer dp[row][col] il faut que tout la range row+1 soit deja calculer car 
'[col+nums[row]]' ou '[col-nums[row]]' peut correspondre a n'importe quelle column de la row. C'est pour cela qu'on va parcourir le tableau row par row , pour que a chaque fois 
qu'on calcule un nouvelle row on a deja la row precedente calculer. 
remarque : La row par laquelle on commence le calcule est forcement un base case et donc on a pas besoin d'une row qui la precede pour la calculer (car les valeur des bases case sont toujours
des constantes (et non des variables) )

Puisque notre point de depart dans le tableau est le suivant   : 

                                        0   1   2    2*sum(nums)           
                                      -------------     -----                  
                                   0  |   |   |   | ... |   |                       
                                      -------------     -----                                
                                   1  |   |   |   | ... |   |               
                                      -------------     -----                  X: point de depart      (Y : autre point de depart possible, voir etape 3)
                                        .   .   .    .    .                                                                           
                                        .   .   .    .    .                                
                                      -------------     -----                                                     
                           len(nums)  | Y |   |   | ... | X |                                   
                                      -------------     -----  

Alors pour que l'iteration soit row par row tout en commencant par la cellule de depart : [row==len(nums)][col==2*sum(nums)] , il faut parcourir de droite a gauche en commencant par 
la cellule [row==len(nums)][col==2*sum(nums)] , donc ca donne les boucle suivante : 

    for row in range(len(nums),-1,-1) :        # on commence a la dernier row
        for col in range(2*sum(nums),-1,-1):     # on commence a la derniere col    
        
(
  si on avait choisi le point de depart Y alors le code aurait ete valide aussi et la boucle aurait etait la suivante :
  
    for row in range(len(nums),-1,-1) :        # on commence a la dernier row
        for col in range(2*sum(nums)+1):       # on commence a la premiere col  
)        
        
        
=>  CONCLUSION / CODE : 

on obtient donc le code suivant : 

    target = s + target      # obtenue dans etape 1
    
    dp = [ [ 0 for _ in range (2*sum(nums)+1) ] for _ in range (len(nums)+1) ]          # obtenue dans etape 1
    
    for row in range(len(nums),-1,-1) :            \
                                                    | =>  # obtenue dans etape 3 et 6
        for col in range(2*sum(nums),-1,-1):       /

             if row>n-1 :                   \
                                             \
                if col == target :            \
                                               \
                   dp[row][col] = 1             | =>  # base case # obtenue dans etape 2
                                               /
                else :                        /
                                             /
                   dp[row][col] = 0         / 
                   
             elif col-nums[row] < 0 :                              \
                                                                    \
                    dp[row][col] = dp[row+1][col+nums[row]]          \
                                                                      | =>  # obtenue dans etape 5
            elif col+nums[row] > 2*sum(nums) :                       /
                                                                    /
                dp[row][col] = dp[row+1][col-nums[row]]            /

            else :                                                                        \                        
                                                                                           | => # obtenue dans etape 4        
                dp[row][col] = dp[row+1][col-nums[row]] + dp[row+1][col+nums[row]]        /                         
                
    return dp[0][sum(nums)]     # obtenue dans etape 2 
    
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        s = sum(nums)
        
        target = s + target
        
        dp = [[0 for _ in range (2*s+1)] for _ in range (n+1)]
        
        for row in range(n,-1,-1):
            for col in range(2*s,-1,-1):        
                
                if row>n-1 :
                    if col == target :
                        dp[row][col] = 1 
                    else :
                        dp[row][col] = 0
                        
                elif col-nums[row] < 0 :
                    dp[row][col] = dp[row+1][col+nums[row]]
                    
                elif col+nums[row] > 2*s :
                    dp[row][col] = dp[row+1][col-nums[row]]   
                    
                else :
                    dp[row][col] = dp[row+1][col-nums[row]] + dp[row+1][col+nums[row]]
        
        return dp[0][s]


""" # sol 4  # dp top-down/ tabulation eith space optimization(iterative) # TC O(n)*(sum(nums)) il ne change pas par rapport a la solution 3  # SC O(sum(nums)) car on utilise que deux rangee de
taille 2*sum(nums)+1 donc cad de taille O(sum(nums)) ( donc 2*O(sum(nums)) egale O(sum(nums)) )

=> ETAPE 1 : OPTIMISATION ET 'TRADUCTION' :

Comme on a vu, pour calculer dp[row][col] il va nous falloir :  dp[row+1][col-nums[row]]  et/ou  dp[row+1][col+nums[row]]  donc ca veut dire qu'on utilise que deux row a chaque fois row et row+1
donc on pourra a la place d'utiliser un tableau utiliser 2 row.

une rangee : previous, qui va representer row+1 qui est la rangee deja calculer et une rangee: current, qui va representer row qui est la range qu'on calcule maintenant .

donc on pourra 'traduire' dp[row+1] par previous et dp[row] par current ,  exemple si on a : dp[row][col] = dp[row+1][col-nums[row]]  alors apres 'traduction' ca donne :
current[col] = previous[col-nums[row]]

Attention : on doit quand meme parcourir tout les subprobleme possible donc on va quand meme faire la double boucle :

    ' for row in range(n,-1,-1):
          for col in range(2*s,-1,-1): '
          
Donc c'est pour cela que le TC ne change pas par rapport a la solution 3 (parcontre Le SC lui change)


=> ETAPE 2 : COMMENT ON 'AVANCER' DANS LE CODE 

apres avoir calculer toute la rangee current a l'aide de la rangee previous pour s'avancer il faut que previous devient current cad que l'ancienne rangee deviennent la nouvelle , de plus si 
previous devient current il faut aussi que current devient previous cad que la nouvelle rangee deviennent l'ancienne, car si on fait que previous=current alors ca donne ca :

    apres avoir fini le calcule de toute la rangee current disons on a les valeurs suivante :
    
                   ---------------------------
    current =      | X1 | X2 | X3 | ... | Xn | 
                   ---------------------------
                  
                   ---------------------------
    previous =     | Y1 | Y2 | Y3 | ... | Yn | 
                   ---------------------------
                   
    puis pour s'avancer on fait previous = current donc :
    
                             ---------------------------
    previous, current =      | X1 | X2 | X3 | ... | Xn | 
                             ---------------------------
                  
                             ---------------------------
                             | Y1 | Y2 | Y3 | ... | Yn | 
                             ---------------------------    
                             
    et donc quand on va modifier current pour faire les nouveau calcule ca va aussi modifier previous et fausser donc le resultat , donc c'est pour ca il faut faire : 
    'previous,current = current,previous', ce qui donne :
    
                   ---------------------------
    previous =     | X1 | X2 | X3 | ... | Xn | 
                   ---------------------------
                  
                   ---------------------------
    current  =     | Y1 | Y2 | Y3 | ... | Yn | 
                   ---------------------------
                   
    donc la en modifiant current avec les nouveau calcule on va pas modifier previous.   
              
ccl : a la fin du calcule de chaque row on ajoute 'previous,current = current,previous' 

"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        s = sum(nums)
        
        target = s + target
        
        previous = [0 for _ in range (2*s+1)]   # rangee precedement calculer 
        current = [0 for _ in range (2*s+1)]    # rangee actuelle
         
        
        for row in range(n,-1,-1):
            
            for col in range(2*s,-1,-1):        
                
                if row>n-1 :
                    if col == target :
                        current[col] = 1 
                    else :
                        current[col] = 0
                        
                elif col-nums[row] < 0 :
                    current[col] = previous[col+nums[row]]
                    
                elif col+nums[row] > 2*s :
                    current[col] = previous[col-nums[row]]   
                    
                else :
                    current[col] =previous[col-nums[row]] + previous[col+nums[row]]
        
            previous,current = current,previous  # apres le calcule de chaque rangee on fait le swap
            
        return previous[s]  # puisque a la fin de la boucle on fait un swap donc la dernier rangee qui contient les derniers calcules va etre previous (et pas current car il a ete swap)
