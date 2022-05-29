"""
INTRO 1:


KNAPSACK Problem :

On a n objects avec chacun un poids et une valeur , on veut remplir un sac pouvant contenir W kilos de telle sorte que la somme des valeurs des objets introduit soit maximale.

Il existe 3 sous-type du probleme Knapsack tres connue (il en existe plus mais il ya 3 tres frequent) : 

- fractionnal knapsack : on peut prendre une partie de chaque object , ce probleme se resolue a l'aide d'un greedy algorithme (on trie les valeur val/weight dans l'ordre decroissant et on 
  prend a chaque fois une partie de l'object (ou tout l'object) qui a le plus grand rapport val/weight ).
  
- 0/1 knapsack : chaque object peut etre selectionne au max une fois (il peut ne pas etre selectionne), ce probleme se resolue a l'aide du dynamic programming.
  
- Unbounded knapsack : chaque object peut etre selectionne un nombre illimite de fois (il peut ne pas etre selectionne), ce probleme se resolue a l'aide du dynamic programming (pas la meme 
  solution que le 0/1 knapsack).
  
  
0/1 KNAPSACK : 
 
# solution 1 : dfs recursion   # TC O(2^n) car arbre binaire de hauteur n (car on fait n recursion vu que a chaque fois on fais index+1).   # SC O(n) car hauteur arbre egale O(n)
# Comme on a vue : chaque objet peut etre selectionner ou non donc on peut faire une recursion ou a chaque fois on peut choisir ou non l'object : 

    def KNAPSACK (values,weights,maxCap) :          # values/weights array of n value/weight of each object, maxCap is the max capacity of the knapsack

        def dfs(idx,W):     # nous rend la valeur maximal du knapsack de capacite W et qui prend en consideration les object A PARTIR de l'index idx jusqu'a l'index n-1

            if idx>len(values)-1 or W==0:       # si on est passer sur tout les objects ou si il ya plus de possibilite d'introduire de nouveau object 
                return 0                        # on retourne 0

            # If weight of the idx-th item is more than Knapsack capacity W, then this item cannot be included in the optimal solution.
            if (weights[idx] > W):
                return dfs(idx+1, W)

            # else return the maximum between if we include the idx-th object or we don't include it 
            # if we include the knapsack capacity change (else : the capacity stay the same)
            return max( values[idx] + dfs(idx+1, W-weights[idx]) ,  dfs(idx+1, W) )

        return dfs(0,maxCap)
 
 
REMARQUE IMPORTANTE : le code suivant marche aussi , mais pour faciliter le passage au dp vaut mieux utiliser le code precedent car j'ai remarque que TOUJOURS il vaut mieux que le base case 
rend une constante car apres c'est plus simple dans le dp bottom up de faire la traduction du base case et du reste .  (SUPER IMPORTANT IL FAUT TOUJOURS ESSAYE DE RENDRE UN CONSTANTE )
 
    def KNAPSACK (values,weights,maxCap) :          # values/weights array of n value/weight of each object, maxCap is the max capacity of the knapsack

        def dfs(idx,W,knapVal):

            if idx>len(values)-1 or W==0:       # si on est passer sur tout les objects ou si il ya plus de possibilite d'introduire de nouveau object 
                return knapVal                  # on retourne la valeur du sac 

            # If weight of the idx-th item is more than Knapsack capacity W, then this item cannot be included in the optimal solution.
            if (weights[idx] > W):
                return dfs(idx+1, W, knapVal)

            # else return the maximum between if we include the idx-th object or we don't include it  
            return max(dfs(idx+1, W-weights[idx], knapVal+values[idx]),dfs(idx+1, W, knapVal))

        return dfs(0,maxCap,0)
    
(pour traduire ce code en dp tabulation c'est tres compliquer , pas intuitive du tout, perso j'ai pas reussi)

# solution 2 : dp top-down/ memoization on rajoute juste un cache pour ce qui a deja etait calculer 
# on va pas ecrire cette sol car elle est simple ...
# TC O(n*maxCap) car il ya deux parametre , le premier parametre a n valeur et le deuxieme a maxCap valeurs.
# SC O(n*maxCap) car il ya n*maxCap combinaison possible


# solution 3 : dp bottom-up/tabulation  #TC O(n*maxCap) car on parcours tout le tableau  #SC O(n*maxCap) du au tableau.
(ca ma pris enormement de temps a le faire de facon intuitive pour qu'il soit exactement l'inverse de la recursion )

IMPORTANT POUR TOUT LES DP TABULATION :

dp bottom-up/tabulation ca veut dire qu'on utilise un tableau pour calculer la recursion de facon iterative , on peut utiliser un tableau 1D ou 2D :

    -Si on utilise un tableau 1D alors ca donne ca :

    dp :  |   |   |   |  ....  |   |      alors on va avoir une iteration qui commence a une des extremites cad de 0 a n ou de n a 0.
            0   1   2            n 
     
    -Si on utilise un tableau 2D alors ca donne ca :
    
         0   1   2         m             Dans ce cas on peut faire 8 iteration differente   :
       -------------     -----              -> en partant d'en haut a gauche on peut parcourir (1) row par row ou (2) col par col  :    
    0  |   |   |   | ... |   |                       (1)   for row in range(n+1):                  |     (2)    for col in range (m+1):
       -------------     -----                                for col in range(m+1):               |               for row in range(n+1):
    1  |   |   | X | ... |   |               
       -------------     -----              -> en partant d'en haut a droite on peut parcourir (1) row par row ou (2) col par col  :
         .   .   .    .    .                         (1)  for row in range(n+1):                   |     (2)    for col in range(m,-1,-1):                                                 
         .   .   .    .    .                                 for col in range(m,-1,-1):            |               for row in range(n+1): 
       -------------     -----                                                     
    n  |   |   |   | ... |   |              -> en partant d'en bas a gauche on peut parcourir (1) row par row ou (2) col par col  :                            
       -------------     -----                       (1)  for row in range(n,-1,-1):               |     (2)    for col in range(m+1):
                                                             for col in range(m+1):                |               for row in range(n,-1,-1): 
                                                             
                                            -> en partant d'en bas a droite on peut parcourir (1) row par row ou (2) col par col  :                 
                                                     (1)  for row in range(n,-1,-1):               |     (2)    for col in range(m,-1,-1):      
                                                             for col in range(m,-1,-1):            |               for row in range(n,-1,-1):
                                                             
      Ce que je veux dire par la c'est que les index du tableau sont TOUJOURS dans cette ordre (c'est logique par exemple pour atteindre la case avec le X c'est tab[1][2] et ca va toujours
      etre le cas), la seul chose qui peut changer c'est comment on parcours le tableau. 
      

Quand on fait un bottom-up il faut essayer de faire l'inverse de la recursion dfs top-down, car ca permet de faire la 'traduction' de facon intuitive car le calcule de la recursion se fait 
en remontant c'est donc cette partie qu'il faut 'traduire' en bottom-up :
La recursion top-down descend la recursion jusqu'au base case et puis la elle arrete les appel recursive et c'est en remontant qu'elle fait les calcules , donc au finale le calcule se fait
en partant du base case et en remontant vers le cas generale. Ici le base case c'est quand idx>n-1 ou quand W==0, et le cas generale (le cas pour lequel on cherche la reponse ) ici c'est
quand on aura pris en consideration tout les object avec un knapsack a capaciter maximale W . Donc au finale la recursion dfs fait le calcule en commancent avec W==0 ou/et idx>n-1.
Dans le bottom up on doit aussi avoir ces base case donc :  un base case ou W==0  (dans ce cas tab[row][col]==0) et un base case ou idx>n-1 (dans ce cas tab[row][col]==0 ). ( On verra par
la suite qu'on va faire un tableau 2D dont row represente l'index de l'objet et col represente la capacite du knapsack , donc on aura une row de 0 qui represente le cas ou idx>n-1, et une col
de 0 qui represente le cas ou W==0 ) . Donc comme dans la recursion le calcule commence par le cas de base : le cas ou W==0 et/ou idx>n-1  (avec n le nbr d'object donc si idx>n-1 ca veut
dire que l'idx n'existe pas donc on selectionne aucun object donc on return 0) alors dans le bottom-up on va commencer par le cas "LE PLUS" de base c'est le cas ou W==0 (cad col==0) ET 
idx>n-1 (cad row==n). Le cas 'le plus' de base correspond au cas ou row==n et col==0 ,puisque le tableau dp est de la forme suivante : 

                                       0   1   2         m              
                                      -------------     -----                  
                                   0  |   |   |   | ... |   |                       
                                      -------------     -----                                
                                   1  |   |   |   | ... |   |               
                                      -------------     -----             
                                        .   .   .    .    .                                                                           
                                        .   .   .    .    .                                
                                      -------------     -----                                                     
                                   n  | X |   |   | ... |   |                                   
                                      -------------     -----       
 
alors ca veut dire que le cas le plus de base ce trouve dans la case ou il ya le X , et donc on doit commencer l'iteration par la bas. on peut parcourir soit row par row soit col par col,
ici dans notre cas on verra qu'on devra parcourir row par row.  

on utilisera un tableau 2D (car 2 parametres) de la facon suivante : les column du tableau auront une valeur de 0 a maxCap (capacite max du knapsack) et les row auront une valeur de 0 
(represente l'idx du premier object) a n (il ya en tt n object , on commence a l'idx 0 donc la derniere valeur est n-1 , n va representer le cas ou idx>n-1 cad il aura la valeur 0).

voici un exemple : maxCap = 3 , et il y'a 2 object (cad n=2) , alors le tableau va etre comme ca :

     0   1   2   3 
   -----------------
0  |   |   |   |   | 
   -----------------
1  |   |   |   |   | 
   -----------------
2  | X |   |   |   | 
   -----------------

On va commencer l'iteration par la case avec le X car c'est "le plus" base case (comme on a vue en haut) . 

Comme dans la recursion ou dfs(idx,W) nous rend la valeur maximal du knapsack de capacite W quand on prend en consideration les object A PARTIR de l'index idx, alors de meme la case tab[row][col] 
nous rend la valeur maximal du knapsack de capacite 'col' quand on prend en consideration les object A PARTIR de l'index 'row' .

Comme dans la recursion, ici aussi on a 2 cas a traiter a chaque fois : 

    - Si le poids de l'object (weights[row]) depasse la capacite du knapsack alors on ne peut pas l'inclure . Comme dans le dfs ou dans ce cas dfs(idx, W) est egale a dfs(idx+1, W) 
    de meme ici tab[row][col] = tab[row+1][col]. L'explication est que comme on ne rajoute pas d'object donc la capacite et la valeur du knapsack ne change pas , cad la valeur du knapsack 
    avec capacite 'col' quand on prend en consideration les object a partir de l'index 'row' ( tab[row][col] ) va etre egale a la valeur du knapsack avec capacite 'col' quand on prend 
    en consideration les object qu'a partir de l'index 'row+1', d'ou tab[row][col] = tab[row+1][col]. 

    - Si le poids de l'object (weights[row]) ne depasse pas la capacite du knapsack alors on doit choisir le max entre (1) si on inclu cette object ou (2) si on l'inclu pas : 
    
      Comme dans la recursion dfs ou dans ce cas dfs(idx,W) est egale a max( values[idx] + dfs(idx+1,W-weights[idx]) ,  dfs(idx+1,W) ) de meme dans le bottom-up :
      tab[row][col] = max ( values[row] + tab[row+1][col-weights[row]] , tab[row+1][col] ) .
      L'explication est que (1) si on inclu l'objet (d'idx row) alors la valeur maximal du knapsack va etre egale a la valeur de l'object plus la valeur maximale du knapsack lorsque
      ca capacite est egale a la capacite actuelle moins la capacite de l'object en prennant en consideration qu'a partir de l'index 'row+1'.  (2) si on inclu pas l'objet
      alors on a vue precedement l'explication pourquoi ca revient a tab[row+1][col] .
      
      
Donc comme on a vu, pour calculer tab[row][col] il va nous falloir : tab[row+1][col-weights[row]]  et/ou  tab[row+1][col]  , donc pour calculer la ligne row il nous faut la ligne row+1 .
Donc il nous faut des valeur de depart qui n'ont pas besoin d'etre calculer avec des valeurs precedente (ce sont les bases cases), pour qu'on puisse ensuite utiliser c'est valeur de depart 
pour calculer le reste ( Dans tout les dp tabulation ca marche comme ca il nous faut des valeur de depart pour 'lancer' le calcule ) ce sont les bases case .
les base case vont etre calculer en premier ce qui va nous permettre de calculer le reste , c'est pour cela qu'on commence l'iteration au "plus" base case possible comme on a vue en haut.

Puisque tab[row][col] peut utiliser tab[row+1][col-weights[row]] il faut donc que toute la row+1 soit calculer avant de calculer tab[row][col] c'est pour cela qu'on va faire l'iteration row 
par row pour que toute la row+1 soit calculer avant row. 
 

LE CODE :
  
  def KNAPSACK (values,weights,maxCap) :          # values/weights array of n value/weight of each object, maxCap is the max capacity of the knapsack
    
        n = len(values)  #nombre d'object
        dp = [[0 for _ in range (maxCap+1)] for _ in range (n+1)]        # tableau de n+1 row et maxCap+1 col
        
        # comme on a vue on doit commencer en bas a gauche et faire l'iteration row par row donc :
        for row in range (n,-1,-1):
            for col in range (maxCap+1):
                # base case : 
                if row>n-1 or col==0 :
                    dp[row][col]=0           # on peut ecrire continue a la place car tout les cases sont deja 0
                    
                elif weights[row]>col :      # (remarque: dans le dfs il ya un if mais en faite avant il ya un return donc le if revient a un elif)
                    dp[row][col] = dp[row+1][col]
                    
                else :
                    dp[row][col] = max (values[row]+dp[row+1][col-weights[row]], dp[row+1][col] )
 
        return dp[0][maxCap]   # IMPORTANT : la raison pour la quelle on return dp[0][maxCap] c'est parceque on a commencer l'iteration en bas a gauche et on a parcouru row par row
                               #             donc on fini l'iteration en haut a droite (logique) ce qui correspond a la case dp[0][maxCap]
 
 
 
# sol 4 #dp bottom-up/tabulation with space optimization #TC O(n*maxCap)  #SC O(2*maxCap) == O(maxCap) .

Comme on a vu, pour calculer tab[row][col] il va nous falloir : tab[row+1][col-weights[row]]  et/ou  tab[row+1][col] donc ca veut dire qu'on utilise que deux row a chaque fois row et row+1
donc on pourra a la place d'utiliser un tableau utiliser 2 row.


def KNAPSACK (values,weights,maxCap) :          # values/weights array of n value/weight of each object, maxCap is the max capacity of the knapsack
    
    n = len(values)  #nombre d'object
    previous = [0 for _ in range (maxCap+1)]        
    current = [0 for _ in range (maxCap+1)] 

    for row in range (n,-1,-1):
        for col in range (maxCap+1):
            # base case : 
            if row>n-1 or col==0 :
                current[col]=0           

            elif weights[row]>col :      # (remarque: dans le dfs il ya un if mais en faite avant il ya un return donc le if revient a un elif)
                current[col] = previous[col]

            else :
                current[col] = max (values[row]+previous[col-weights[row]], previous[col] )

        # a chaque fois qu'on fini la row on swap      
        # previous devient current et current devient previous (il faut que current devient previous car si on fait que previous = current alors quand on va modifier previous
        # ca modifie current car current est un array donc quand on fait previous = current ,previous pointe su la meme adresse que current, ca ne va pas etre juste une copie)
        previous,current=current,previous

    return previous[maxCap]   # previous et pas current car a la fin previous = current et current = previous  

"""




"""
INTRO 2:

L'idee ici est que pour qu'on puisse avoir deux subset de la meme somme, il faut qu'un subset soit egale a sum(array)/2  (forcement si on a un subset qui est egale a sum(array)/2 l'autre va
aussi etre egale a sum(array)/2 car en tout les deux subset doient valoir sum(array)) .
remarque : si sum(array) ne se divise pas en 2 partie entieres alors il ne peut y avoir deux subset egale car l'array est composer que de nombre entier donc on ne pourra pas le diviser en
deux subset qui auront une somme non-entiere. Pour que sum(array) se divise en 2 parties entieres  il faut que sum(array) soit paire donce que sum(array)%2==0.


Donc au final on doit selectionner ou non des element parmis l'array pour que la somme soit egale a sum(array)/2 , chaque element peut etre selectionner qu'une fois (les elements selectionner
formeront la 1er subsequence, les autres non selectionner formeront la 2e subsequence).
Ca ressemble pas vraiment au problem 0/1 knapsack  car dans 0/1 knapsack on a un array de valeur et un array de poids on recherche que le poids soit inferieur ou egale a target tout en ayant 
une somme de valeur maximal mais ici on recherche si il existe ou non une somme de valeur qui est EGALE a target (il ya pas de contrainte de point et la target et sur la valeur pas le poids). 
On va voire que le dp bottom-up va ressembler a la solution dp bottom-up du 0/1 knapsack. 

"""

""" # sol 1 # dfs  # TC O(2^n) avec n==len(nums) # SC O(n)

Il nous suffit de chercher une seule subsequence dont la somme de ses elements est egale a sum(array)/2 car forcement (voir expliquation INTRO 2 pq) cela veut dire qu'il y'a une deuxieme
subsequence dont la somme de ses elements est egale a sum(array)/2. 
Pour former une subsequence on passe sur l'array et pour chaque element on a le choix entre inclure l'element dans la subsequence et entre ne pas l'inclure. On repete ce choix tant que la somme
des elements est inferieur a sum(array)/2 (qui est notre target) , si la somme des elements est egale a sum(array)/2 alors on a trouver une subsequence qui divise l'array en deux subsequence
egale et donc on peut retourne True, si la somme est superieur a sum(array)/2 ou si il ne reste plus d'element a selectionner ca veut dire que la subsequence obtenue ne divisera pas l'array en 
deux subequence egale donc on peut rendre false .

TC analyse :
on fait deux appele recursif a chaque fois donc on a un arbre de recursion binary tree. La hauteur est O(n) (voir SC analyse ) donc TC = O(2^n)

SC analyse : 
on avance a chaque recursion d'un index dnas nums donc la hauteur de l'arbre est O(n) avec n le nombre d'element dans nums. donc le recursive stack est O(n)

"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # comme on a vu dans intro 2, il faut que la somme de l'array soit paire, sinon on ne pourra pas diviser l'array en deux subsequence dont la somme est egale  :
        ttl = sum(nums)
        if ttl%2!=0 :
            return False 
        
        # pour diviser l'array en deux subsequence dont la somme est egal, il faut que chaque subsequence soit egale a la moitier de la somme de l'array cad a sum(nums)/2
        # ou plus precisement il suffit q'une subsequence soit egale a sum(nums)/2 car forment l'autre sera egale au reste cad a sum(nums)/2. 
        middle = ttl/2 
        
        # il suffit de trouver une subsequence dont la somme est egale a middle. 
        # dfs(idx,curSum) nous rend True si a partir de idx il existe une subsequence qui est egale a middle
        def dfs(idx,curSum) : 
            
            # si la somme des elements est egale a sum(array)/2 alors on a trouver une subsequence qui divise l'array en deux subsequence egale et donc on peut retourne True
            if curSum==middle:        
                return True         
            # si la somme est superieur a sum(array)/2 ou si il ne reste plus d'element a selectionner ca veut dire que la subsequence obtenue ne divisera pas l'array en
            # deux subequence egale donc on peut rendre false
            if idx>len(nums)-1 or curSum>middle:
                return False 
            
            # a chaque fois on a le choix entre selection ou non un element (c'est comme ca qu'on forme une subsequence) 
            # chaque possibilite nous rendra a la fin true ou false donc si une des possibilite nous rend true on veut que dfs nous rend true donc c'est pour cela on utilise 'or'
            return dfs(idx+1,curSum+nums[idx]) or dfs(idx+1,curSum)
        
        return dfs(0,0)
        

"""# sol2  # dp top-down/memoization(recursive)  # TC O(n*(sum(nums)) # SC O()

We cache already computed result. 

TC analyse  : 
la fonction dfs recoit 2 parametres idx et curSum , le premier parametre varie de 0 a n-1  (avec n==len(nums)) il a donc en tout n valeur possibles , le 2e parametre varie de 0 a sum(nums)/2
il a donc sum(nums)/2 valeur possible . On a donc en tout n*(sum(nums)/2) combinaison possible cad on a donc n*(sum(nums)/2) subprobleme different . Comme on utilise un cache (cad on ne va 
pas calculer le meme subproblem plus d'une fois) alors le nombre total de recursion va etre egale au nombre de subprobleme different cad n*(sum(nums)/2). Puisque chaque recursion coute O(1)
le TC va etre egale a O(n*(sum(nums)/2)) cad a O(n*(sum(nums)). 

SC analyse:
Comme expliquer dans le TC il ya n*(sum(nums)/2) subprobleme different donc il va faloir garder dans le cache n*(sum(nums)/2) resultat soit O(n*(sum(nums)).
(ici le recursion stack O(n) est negligeable). 
"""       

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ttl = sum(nums)
        if ttl%2!=0 :
            return False 
        
        middle = ttl/2 
        
        cache = {} 
        
        def dfs(idx,curSum) : 
            
            # cache lookup 
            if (idx,curSum) in cache :
                return cache[(idx,curSum)]
            
            if curSum==middle:        
                return True         
           
            if idx>len(nums)-1 or curSum>middle:
                return False 
            
            res = dfs(idx+1,curSum+nums[idx]) or dfs(idx+1,curSum)
            cache[(idx,curSum)] = res     # caching result 
            return res
        
        return dfs(0,0)
        

"""# sol 3 #dp bottom-up (iterative) #TC O(n*sum(nums)) car on parcours tout le tableau une fois #SC O(n*sum(nums))car on creer un tableau de cette taille.

dp bottom-up/tabulation ca veut dire qu'on utilise un tableau pour calculer la recursion de facon iterative , on peut utiliser un tableau 1D ou 2D :

    -Si on utilise un tableau 1D alors ca donne ca :

    dp :  |   |   |   |  ....  |   |      alors on va avoir une iteration qui commence a une des extremites cad de 0 a n ou de n a 0.
            0   1   2            n 
     
    -Si on utilise un tableau 2D alors ca donne ca :
    
         0   1   2         m             Dans ce cas on peut faire 8 iteration differente   :
       -------------     -----              -> en partant d'en haut a gauche on peut parcourir (1) row par row ou (2) col par col  :    
    0  |   |   |   | ... |   |                       (1)   for row in range(n+1):                  |     (2)    for col in range (m+1):
       -------------     -----                                for col in range(m+1):               |               for row in range(n+1):
    1  |   |   | X | ... |   |               
       -------------     -----              -> en partant d'en haut a droite on peut parcourir (1) row par row ou (2) col par col  :
         .   .   .    .    .                         (1)  for row in range(n+1):                   |     (2)    for col in range(m,-1,-1):                                                 
         .   .   .    .    .                                 for col in range(m,-1,-1):            |               for row in range(n+1): 
       -------------     -----                                                     
    n  |   |   |   | ... |   |              -> en partant d'en bas a gauche on peut parcourir (1) row par row ou (2) col par col  :                            
       -------------     -----                       (1)  for row in range(n,-1,-1):               |     (2)    for col in range(m+1):
                                                             for col in range(m+1):                |               for row in range(n,-1,-1): 
                                                             
                                            -> en partant d'en bas a droite on peut parcourir (1) row par row ou (2) col par col  :                 
                                                     (1)  for row in range(n,-1,-1):               |     (2)    for col in range(m,-1,-1):      
                                                             for col in range(m,-1,-1):            |               for row in range(n,-1,-1):
                                                             
      Ce que je veux dire par la c'est que les index du tableau sont TOUJOURS dans cette ordre (c'est logique par exemple pour atteindre la case avec le X c'est tab[1][2] et ca va toujours
      etre le cas), la seul chose qui peut changer c'est comment on parcours le tableau. 

Comme on peut le constater dans la recursion on a 2 parametre l'index qui varie de 0 a n-1 et la curSum qui varie de 0 a sum(nums)/2. Donc dans le dp bottom/up tabulation on va utiliser
un tableau 2D ou les row (0,1,2,3...n) vont representer les index et les column (0,1,2,....,sum(nums)/2) vont representer la curSum.  (j'ai choisi idx en tant que row et curSum en tant que
column car dfs recoit d'abord idx puis curSum donc aussi dans le tableau il faut que on est tab[idx][curSum] et pas l'inverse pour permetre une traduction intuitive)

Quand on fait un bottom-up il faut essayer de faire l'inverse de la recursion dfs top-down, car ca permet de faire la 'traduction' de facon intuitive car le calcule de la recursion se fait 
en remontant c'est donc cette partie qu'il faut 'traduire' en bottom-up :
La recursion top-down descend la recursion jusqu'au base case et puis la elle arrete les appel recursive et c'est en remontant qu'elle fait les calcules , donc au finale le calcule se fait
en partant du base case et en remontant vers le cas generale. Ici le base case c'est quand idx>n-1 ou quand curSum>middle ou quand curSum==middle , et le cas generale (le cas pour lequel on
cherche la reponse ) ici c'est dfs(0,0). 
Dans le bottom up on doit aussi avoir les meme base case . De plus comme on a vue les column represente la curSum donc la dernier colum va etre le base case ou curSum>middle (cad elle va
etre egale a middle+1 (on va voir apres qu'on va modifier cela)) (le base case curSum==middle est inclu dans c'est column , il ne sera donc pas l'extremite de notre tableau) . De meme on a vu que
les row represente les idx donc la dernier row va etre le base case ou idx>n-1  (cad la derniere row va etre egale a n-1+1 cad a n).
C'est en remontant des bases case que la recursion dfs fait les calcules donc le calcule commence quand curSum>middle ou quand idx>n-1 ou quand curSum==middle. Le bottom-up lui va commencer
l'iteration par le coin du tableau qui represente 'le plus' les bases cases , puisque le tableau dp est de la forme suivante : 

                                       0   1   2         middle+1              
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
 
alors ca veut dire que le cas 'le plus' de base ce trouve dans la case ou il ya le X  car c'est le cas ou curSum>middle et ou idx>n-1 et donc on doit commencer l'iteration par la bas. 

Dans le dfs si ce n'est pas un base case alors dfs(idx,curSum) egale a 'dfs(idx+1,curSum+nums[idx]) or dfs(idx+1,curSum)'  de meme dans le bottom-up si ce n'est pas un base case alors
on devrait avoir : dp[idx][curSum] = dp[idx+1][curSum+nums[idx]] | dp[idx+1][curSum] , le pb c'est que si curSum+nums[idx]>middle+1 on ne va pas avoir de row dans le tableau qui correspond a
curSum+nums[idx] (car la derniere row c'est row==middle+1 (on ne va pas rajouter des row car sinon on a pas de limite car curSum+nums[idx] peut etre tres grand )) (les index sont representer 
par les row, comme on fait a chaque fois +1 donc on on ne pourra pas 'sauter' la row qui correspond au base case idx==n car forcement que pour depasser n-1 il faut passer par idx==n donc 
c'est pour ca que ca suffit de mettre en derniere row : n , car si idx>=n-1 alors il va atteindre d'abord le cas ou idx==n et donc aura deja une reponse (car c'est un base case) et n'aura 
pas besoin de continuer ) 
On va devoir ajouter un condition pour que la curSum ne depasse pas middle: si curSum+nums[idx]>middle alors on ne peut pas inclure nums[idx] car on va forcement depasser middle et donc 
c'est forcement pas une subsequence qui divise l'array en deux subsequence egale , donc on aura que le choix de ne pas inclure nums[idx] cad :
    if curSum+nums[idx]>middle :
        return dfs(idx+1,curSum)
et donc dans le bottom up on le traduit en :
    if curSum+nums[row]>middle :
        dp[row][col] = dp[row+1][col]          # row represente l'idx et col represente la curSum

(de base on aurait peu faire un dfs de la sorte :

def dfs(idx,curSum) : 
            
            if curSum==middle:        
                return True         
           
            if idx>len(nums)-1:
                return False 
            
            if curSum+nums[idx] > middle :     # dans ce cas on ne peut inclure nums[idx]
                return dfs(idx+1,curSum)
           
            return  dfs(idx+1,curSum+nums[idx]) or dfs(idx+1,curSum)
            
puis on aurait fait la traduction vers dp bottom up exactement la meme chose que le dfs sans modif, mais j'ai fait expres de faire un dfs different pour voir comment on fait pour adapter
le bottom up, ce qui permet de comprendre le tableau et ses limites, car pas tout le temps c'est facile de trouver un dfs qui va se traduire parfaitement comme ce dfs )


CCL : Dans le dp bottom up si ce n'est pas un base case on aura:

    if col+nums[row] > middle :     
        dp[row][col] = dp[row+1][col]
    else :
        dp[row][col] = dp[row+1][col+nums[row]] | dp[row+1][col]

Comme on a modifier et on a rajouter le cas "if col+nums[row] > middle : dp[row][col] = dp[row+1][col]"  alors curSum/col ne peut etre superieur a middle donc le base case 
"if row>middle : return False" n'est plus necessaire. Puisque curSum/col est inf egale a middle alors la derniere column du tableau est egale a middle (qui est la dernier valeur que 
curSum/col peut avoir)

J'ai laisser expres le flow et j'ai pas directement dit qu'on utilise un tableau de cette taille pour comprendre comment on arrive a avoir un dp bottom up correcte. 

Puisque dp[row][col] peut utiliser dp[row+1][col+nums[row]]  il faut donc que toute la row+1 soit calculer avant de calculer dp[row][col] (pour qu'on est la column col+nums[row] 
deja calculer dans la ligne row+1) c'est pour cela qu'on va faire l'iteration row par row pour que TOUTE la row+1 soit calculer avant row. 

app :

"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ttl = sum(nums)
        if ttl%2!=0 :
            return False 
        
        middle = ttl//2 
        
        n = len(nums)
        
        #il nous faut un tableau avec col de 0 a middle (inclu) et row de 0 a n(inclu)
        dp = [[False for _ in range (middle+1)] for _ in range(n+1)]  
        
        # on va parcourir row par row en commencant par la case en bas a droite
        for row in range(n,-1,-1):  # row represente l'index
            for col in range (middle,-1,-1):  # col represente le curSum
                if col==middle:       
                    dp[row][col]=True         
                elif row>n-1:
                    dp[row][col]=False
                #si en ajoutant un element de nums on depasse middle alors le seul choix qu'on a c'est de ne pas choisir cette element
                elif col+nums[row] > middle :     
                    dp[row][col] = dp[row+1][col]
                else :
                    dp[row][col] = dp[row+1][col+nums[row]] | dp[row+1][col]
        return  dp[0][0]        

    
"""
# sol 4  # dp bottom-up/tabulation with space optimization  # TC O(n*sum(nums))  # SC O(2*sum(nums)) == O(sum(nums)) .

Comme on a vu, pour calculer dp[row][col] il va nous falloir : = dp[row+1][col+nums[row]]  et/ou  dp[row+1][col]  donc ca veut dire qu'on utilise que deux row a chaque fois row et row+1
donc on pourra a la place d'utiliser un tableau utiliser 2 row.

(autre exemple avec la meme idee (ma sol) : https://leetcode.com/problems/maximal-square/)
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ttl = sum(nums)
        if ttl%2!=0 :
            return False 
        
        middle = ttl//2 
        
        n = len(nums)
        
        previous = [False for _ in range (middle+1)]  
        current = [False for _ in range (middle+1)]  
        
        for row in range(n,-1,-1):
            for col in range (middle,-1,-1):
                if col==middle:        
                    current[col]=True         
                elif row>n-1:
                    current[col]=False
                elif col+nums[row] > middle :     
                    current[col] = previous[col]
                else :
                    current[col] = previous[col+nums[row]] | previous[col]
            previous,current=current,previous        
        return  previous[0]
    
