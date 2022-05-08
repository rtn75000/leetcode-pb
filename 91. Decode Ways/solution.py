""" # super exercice pour comprendre le dynammic programming , j'ai investie enormement de temps pour que ca soit le plus claire possible et surtout pour que le passage 
de la recursion a top-down dp a bottom-up ce fait de facon la plus simple et logique possible """

""" le fait qu'il ya des 0 cela rajoute de la difficulte . 
ex : - s='30' il ya pas de solution car si on lit 3 puis 0 , le 0 ne correspond a rien de meme que si on lit 2 chiffres en meme temps : '30' ca ne correspond a rien 
     - s='06' il ya pas de solution car si on lit 0 puis 6 , le 0 ne correspond a rien de meme que si on lit 2 chiffres en meme temps : '06' ca ne correspond a rien 
     - s='120' il ya  qu'une combinaisons possible 1 20 car 1 2 0 ou 12 0 ca ne marche pas 
"""




""" # sol1 #TLE # recursion  # dfs  # TC O(2^n) avec n==len(s) # SC O(n) due au stack de la recursion  (la taille de l'arbre et O(n) car au pire a chaque recursion on lit que une lettre ).

on appel de facon recursive la fonction que sur la partie de la phrase qui nous reste a analyser. 

l'idee est de lire une lettre a cahque fois ou deux lire un lettre et aussi deux lettre en meme temps. 

POUR COMPRENDRE LE CODE AINSI QUE TC ET SC IL FAUT VOIR L'ARBRE DE RECURSION SUR GITHUB (schema 1). 
"""
 
class Solution:
    def numDecodings(self, s:str) -> int:
        
        def dfs(string):    
            
            # si on a fini de lire tout les chiffres alors on retourne 1 car on a trouver une combinaison valide car si elle ne l'etait 
            # pas on ne pourra arriver a une situation ou on a lu tout les chiffres (car on va faire return des que ca ne marche pas) 
            if not string :   
                return 1     
            
            # si on lit un 0 seul ca veut dire que la combinaison est pas valide est donc on return 0 
            # un zero ce retrouve seul si on a pas combinait avec lui la lettre d'avant 
            if string[0] == '0':
                return 0   
                
            # lecture de deux chiffre en meme temps, ca fait une double recursion : 
            # une recursion pour comme si on a lu qu'un chiffre et une recursion 
            # pour comme si on a lu 2 chiffres en meme temps 
            # condition pour lire deux chiffres :
            # -> il faut que ce qui nous reste a lire soit sup egale a 2. 
            # -> il faut que les deux chiffres soit 1 ou 2 ou 3 ,...., ou 26 car sinon on ne peut les combiner
            if len(string)>1 and (string[0] == '1' or string[0] == '2' and int(string[1]) <= 6):
                return dfs(string[1:]) + dfs(string[2:])  # double appel rec un pour la lecture que d'un chiffre, un pour la lecture de deux chiffres.
            
            # si on ne peut lire deux chiffre en meme temps alors lire que un chiffre 
            else: 
                return dfs(string[1:])   

        return dfs(s)


""" # sol2  #dynamic prgm   #Top-down/memoization(recursive)  # TC O(n) avec n==len(s)   # SC O(n) due au stack de la recursion .

on fait tout simplement la meme recursion faite ds la sol1 sauf qu'on garde les resultat deja calculer. 

POUR COMPRENDRE LA NECESSITE DU DP TOP-DOWN/MEMOIZATION AINSI QUE TC/SC IL FAUT VOIR L'ARBRE DE RECURSION SUR GITHUB (schema 2). 

"""

class Solution:
    def numDecodings(self, s:str) -> int:
        
        # on utilise un dic qui va garder les dfs/recursion deja calculer 
        # les entrees du dic seront de la forme suivante :  { parametre de la fction de recursion : valeur retourner par dfs(paramtre de la fction de rec) } 
        # ex : si on remonte de dfs('111') avec une valeur de retour de 3 alors on met dans le dic {'111':3}
        memo = {}  
        
        def dfs(string):   
            
             # si la string et dans le dic ca veut dire quelle a deja ete calculer 
             # donc juste on recupere la valeur pas besoin de refaire les appeles recursives
            if string in memo :  
                return memo[string]  # c'est le retour de dfs(string) 
            
            if not string : 
                return 1   # c'est le retour de dfs(string)          
            
            if string[0] == '0':
                return 0          
                
            if len(string)>1 and (string[0] == '1' or string[0] == '2' and int(string[1]) <= 6):
                
                res = dfs(string[1:]) + dfs(string[2:])
                memo[string] = res   # en remontant la recursion on garde le resultat dans le dic ( cad on garde le resultat de dfs(string) )
                return res   # c'est le retour de dfs(string) 
            
            else:
                
                res = dfs(string[1:])
                memo[string] = res   # en remontant la recursion on garde le resultat dans le dic ( cad on garde le resultat de dfs(string) )
                return res  # c'est le retour de dfs(string) 
      
        return dfs(s)

        
""" # sol 2 bis  #dynamic prgrm #Top-down/memoization(recursive) en utilisant @lcu_cache   # TC O(n)  # SC O(n) 
"""

class Solution:
    def numDecodings(self, s:str) -> int:
            
        # keep already calculated result 
        @lru_cache() # permet de faire la memoization 
        
        def dfs(string):         
            
            if not string : 
                return 1       
            
            if string[0] == '0':
                return 0        
                
            if len(string)>1 and (string[0] == '1' or string[0] == '2' and int(string[1]) <= 6):
                return dfs(string[1:]) + dfs(string[2:])
            
            else:
                return dfs(string[1:])

        return dfs(s)
    
           
""" # sol3 # DP # Bottom-up(iterative) #TC O(n) # SC O(n) pour le tableau/list utiliser qui est de taille O(n) 

Dans un bottom-up classique on utilise un tableau pour garder les resultat precedement calculer (car la bottom up approach vient a la place de l'approche recursive, or la 
recursion par nature utilise les calcules precedent pour former une reponse donc le bottom up doit utiliser un tableau pour conserver les calcule precedement fait )
(la dimension du tableau depend du nbr de parametre de la fct de recursion (motre fct elle avait que un parametre)) . 
La resolution ce fait de bas en haut contrairement au top-down (le top down c'est une recursion donc il commence au debut puis des qu'il arrive a la fin il remonte jusqu'au debut 
le bottom up lui commence par la fin pour finir au debut) . 

Super explication comment on passe de top-down a bottom-up (qui est la sol de bas en haut donc l'inverse de top-down) :

-> Comme on a vu dans la solution precedente (top-down) si le premiere caractere est different de 0 alors on fait un ou deux appel rec (car si il est egale 0 alors on fait directement
return 0 donc pas d'appel rec), donc si il est egale a 0 on ne fait pas d'appel rec.

-> les appeles rec de la solution top-down se font de la facon suivante :
    - si on peut lire deux caractere en meme temps (ds le cas ou c'est deux caractere sont valide) alors ca donne dfs(s) = dfs(s[1:])+dfs(s[2:])  ( cad on appele le dfs sur une lettre apres et
      sur deux lettres apres)
    - sinon on lit que une lettre et donc dfs(s)=dfs(s[1:])  ( cad on appele le dfs sur une lettre apres )

-> si on combine les deux point precedent alors ici qu'on fait de bas en haut cad de la fin du mot vers le debut , ca donne ca :

        for i in range(n-1,-1,-1) :  # on va de la fin du mot vers le debut (le dernier index du mot est n-1 (n==len(s)) car le premier idx est 0 )
            
            # si la lettre qu'on lit est differente de 0 alors on reproduit la recursion (soit double rec: une sur la lecture d'une lettre et une sur la lecture de 2 lettres
            # soit simple rec : une sur la lecture que d'une lettre )  Car comme ds le dfs ou  si le chiffre egale 0 il ya pas d'appel rec et on retourne 0
            # donc ici aussi on fait rien comme ca la case reste 0 car elle sont tous egale a 0 au debut.
            
            if s[i] != '0' :   

                # lecture de deux lettre possible :           
                if i < n-1 and (s[i] == '1' or s[i] == '2' and int(s[i+1]) <= 6):

                    dp[i] = dp[i+1] + dp[i+2]      # comme dans dfs que dfs(i)=dfs(i+1)+dfs(i+2) ds le cas ou on peut lire deux lettre 
                                                   # c comme le dfs car quand on voit l'arbre on voit que deux branche monte vers un root 
                                                   # ce root additionne les deux branche donc ici on fait la meme chose i correspond au root et
                                                   # i+1 , i+2 correspondent aux enfants
                
                # lecture que d'une lettre possible 
                else : 

                    dp[i] = dp[i+1]   # comme dans dfs que dfs(i)=dfs(i+1) ds le cas ou on peut lire qu'une lettre
                                      # car comme dans l'arbre de dfs dans ce qu'a il ya que une branche qui monte au root
                                      # ce root sera egale a la valeur de la branche 


VOIR SCHEMA 3 SUR GIT APPLICATION DE CETTE ALGO
"""      
 
class Solution:
    def numDecodings(self, s:str) -> int:
         
        n = len(s)
        
        # remarque important : le tableau va etre de la taille de s +1 (il ya n index dans s) la raison est que 
        # qd les deux dernier chiffres du mot forme un nombre valide alors dp[i] (avec i index du premier chiffre) utilise dp[i+1] (avec i+1 index du deuxieme chiffre)
        # et dp[i+2] or i+2 sera en dehors des index de s, donc on rajoute un index en plus pour que i+2 soit un idx ds le tableau
        dp = [0 for _ in range(n+1)]   
        
        # on a vu qu'on reproduit le dfs, donc comme le dfs si on est a la fin de s ca vaux 1 puis on remonte en additionnant 
        # les branches, de meme ici le denier index vaut 1 puis en lisant un ou deux chiffres on va remonter les index et les additionner(ds le cas ou on peut lire 2 chiffre)
        # ou juste les remonter (dans le cas ou on peut lire qu'un chiffre)
        # remarque: on initialise que le dernier index n en 1 car on commence forcement a lire qu'un chiffre au debut car on commence a lire a
        # l'idx n-1 qui est le dernier chiffre de s et comme il ya pas un chiffre apres donc on a pas le cas de figure ou on peut lire deux chiffre en meme
        # temps donc on va juste remonter la valeur 1 de n vers n-1 , ensuite on aura donc n et n-1 avec la valeur 1 et l'idx va etre egale
        # a n-2 donc seulement maintenant on pourra lire 2 chiffre en meme temps 
        dp[-1] = 1
        
        for i in range(n-1,-1,-1) :
            
            if s[i] != '0' :   

                if i < n-1 and (s[i] == '1' or s[i] == '2' and int(s[i+1]) <= 6):

                    dp[i] = dp[i+1] + dp[i+2]

                else : 

                    dp[i] = dp[i+1]
                
        return dp[0]    # correspond au root du dfs c'est la ou tout les calcule precedent sont additionner 
 

 
        
""" # sol4 # DP # Bottom-up(iterative) with optimized space #TC O(n) # SC O(1)

comme on peut le constater dans la sol 3 on utilise maximum que deux valeur (les 2 valeurs apres i : i+1 et i+2) a chaque fois donc on peut optimiser l'espace en gardant
les deux valeur apres i . i correspond a current du code precedent, i+1 correspond a one_after du code precedent et i+2 correspond a two_after du code precedent. 

le for du code prededent permet de s'avancer ds le string et le tableau car le i du for permet de parcourir les deux en meme temps.
ici comme on utilise pas un tableau mais on fait comme si on utilise un tableau en utilisant 3 variables : current , one_after et two_after 
il faut aussi a chaque iteration du faire simuler le recule de c'est variables donc c'est pour cela que a chaque for ,peut importe si s[i] est egale a 0 ou pas, on fait les
3 lines suivantes :
            two_after = one_after    # correspond au recule de i+2 de 1
            one_after = current      # correspond au recule de i+1 de 1
            current = 0              # correspond au recule de i de 1
remarque : current = 0 car comme dans le tableau a chaque fois qu'on recule i la case tab[i] vaut 0 donc ici aussi current qui correspond a tab[i]
           est egale a 0 au moment du recule . 
           
VOIR SCHEMA 4 APPLICATION . 
"""

class Solution:
    def numDecodings(self, s:str) -> int:
         
        n = len(s)
        
        current = 0
        one_after = 1  # one_after = 1 pour la meme raison que dans sol3 on a fait dp[-1]=1 (a la 3e ligne du code) ( ca permet de simuler tab[n]=1 dans le code sol3 )
        two_after = 0 
        
        for i in range(n-1,-1,-1) :  # on loop a travers s et on simule le recule des variables two_after, one_after et current
        
            if  s[i] != '0' :
                
                if i < n-1 and (s[i] == '1' or s[i] == '2' and int(s[i+1]) <= 6):
                    current = one_after+two_after  # lecture de deux chiffre possible 

                else  : 
                    current = one_after  # lecture que d'un chiffre possible

            
            two_after = one_after    
            one_after = current
            current = 0
            
        
        # on return one_after car current en fin de boucle il va etre 'reculer' et donc il va etre egale a 0 
        # (il correspondra a l'idx i=-1 : dp[-1] en fin de boucle , et one_after correspond a dp[0] donc c'est lui qu'on veut)
        return one_after 
    




