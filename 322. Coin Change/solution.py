""" Intro : 
l'approche greedy (sort en ordre decroissant, puis prendre la plus grande piece possible) ne permet pas de resoudre se pb , explication :
par ex si on a coins=[1,3,4,5] et amount = 7 alors si on fait l'approche greedy on prend d'abord 5 puis on peux pas rechoisir 5 car 5+5>7 , on peut pas choisir 4 car 5+4>7 ni 3 car 5+3>7
mais on choisi 1 car 5+1<7 et on rechoisi 1 ce qui donne 5+1+1==7 donc la reponse va etre : 3 pieces.
or il existe une meilleur solution de choisir 4 et 3 car 4+3==7 cad 2 pieces seulement , donc l'approche greedy n'est pas vrai.
"""
        

         
"""#sol 1 #ma sol #dfs #TC=O(n^S) voir analyse  # SC O(S) voir analyse 

A chaque fois on peut choisir une piece parmis les n pieces et soustraire la piece choisi du montant puis refaire ce choix jusqu'a que on depasse le montant voulue (ds ce cas le chemin / les
pieces choisie , ne sont pas la solution donc on return infini ) ou  jusqu'a qu'on est exactement le montant voulu (dans ce cas la hauteur va etre egale au nombre de piece choisi).
on veut avoir le moins de piece possible donc il faut qu'on trouve la plus petite hauteur entre le root est un leaf donc amount == 0 

TC analyse : TC=O(n^S) avec n==len(coins) (cad le nombre de piece dans coins) et S==ammount car n-ary tree de hauteur O(S) car au pire on va faire S recursion car au pire on a une piece de 1 
et donc on descend a chaque fois que de 1 donc S recursion en tout (on peut aussi dire TC= O(n^(S/min(coins))) car au pire on retire a chaque fois de amount min(coins) ce qui va nous donner la
plus grande hauteur O(S/min(coins)) )

SC analyse : SC O(S) car hauteur egale au pire a S car on descend que de 1 a chaque fois dans le pire des cas (on peut etre plus precis et dire que SC = O(S/min(coins)) car au pire
on retire a chaque fois de amount min(coins)  )

VOIR ARBRE DE RECURSION GITHUB 
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(amount):  
            
            # si on a depasser l'amount alors on veut que le chemin ne soit pas choisi donc on return infini car comme ca le chemin va etre egale a infini (car 1+..+1+inf egale inf)  
            if amount<0 :            
                 return float('inf') 
                
            # si on a exactement l'amount alors on veut prendre en compte la hauteur du chemin et donc on return 0 (et donc ca va faire 1+..+1+0 )
            if amount==0 :            
                return 0 
            
            # on veut que chaque node retourn le chemin le plus petit de ses enfant donc au debut res = inf et ensuite apres le for qui fait la recursion sur tout les enfants 
            # res va etre egale au chemin le plus petit des enfants.
            res = float('inf')   
            for coin in coins :
                res = min(res,1+dfs(amount-coin))  # a chaque appel rec on ajoute 1 car comme ca ca nous donne la hauteur 
                                                   # res va etre egale a la plus petite hauteur des enfants
                                                   # remarque : 1+dfs(amount-coin) ou dfs(amount-coin)+1 ca revient au meme car de tout les facons on attend le resultat du 
                                                   # dfs pour pouvoir retourner une valeur donc dans les deux cas le calcule se fait de la fin (voir arbre de recursion) 
                
            return res # super important: le return doit etre en dehors de la boucle car sinon la boucle va s'arreter a la premiere iteration car elle fait return 
                       # la logique est que apres avoir fait la rec sur tout les enfant seulement apres on return res qui sera le plus peit chemin retourne
               
        output = dfs(amount) 
        return output if output != float("inf")  else -1   # si output egale float ca veut dire qu'on apas trouver une combinaison de piece qui permet d'avoir amount==0 a la fin donc return -1

    
    
    
""" # my sol # sol 2 bis  #dp top-down/memoization   # TC=O(S*n) avec n le nombre de piece dans coins et S==ammount, voir analyse  # SC O(S) car hauteur arbre au max O(S) (ds 
le cas ou dfs(S) appele dfs(S-1) qui apelle dfs(S-2) etc.. )

Use a dictionnary to cache already calculated result.

TC analyse : 

REMARQUE SUPER IMPORTANTE : cette analyse est valable a  chaque fois qu'on utilise dp top-down/memoization , dans les precedents pb j'analyser l'arbre de recursion obtenue apres la memoization
pour connaitre le TC et SC , mais il ya bcp plus simple comme amalyse :
peut importe notre arbre de recursion au total au pire on va appeler S differente recursion  : dfs(S),dfs(S-1),dfs(S-2),...dfs(0) car comme on utilise un cache on a pas besoin de les calculer 
de nouveau a chaque fois donc il va avoir O(S) appel rec , de plus chaque appel rec coute O(n) car il a une boucle "for coin in coins" donc en tout TC = O(S*n).

( 
exemple que cette analyse marche tout le temps : 
prenons pour exemple la recursion de fibonnaci : 

def fib(n):
    if n in dic :
        return dic[n]
    if n<=1 :
        return n 
    return fib(n-1)+fib(n-2)
    
alors TC = O(n) car au max on va calculer fib(n),fib(n-1),fib(n-2),...fib(1) (une fois chacun car ya un cache) et comme chaque rec coute O(1) donc TC=O(n)*O(1) cad O(n)   
)


"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        
        def dfs(amount):  
            
            # verifier si cette recursion a deja ete calculer 
            if amount in cache :
                return cache[amount]
            
            if amount<0 :
                return float('inf')
            
            if amount==0 :
                return 0 
            
            res = float('inf') 
            for coin in coins :
                res = min(res,1+dfs(amount-coin))
            cache[amount] = res      # apres avoir calculer toute les recursion des enfants (cad en remontant de la recursion) garder la valeur caluler pour dfs(amount) dasn le dic
            return res
        
        output = dfs(amount) 
        return output if output != float("inf")  else -1
    
    
""" #sol 2 bis  #dp memoization using lru_cache # same TC and SC as sol 2 """


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)   # si on met que @lru_cache seulement ca fait TLE ! #donc tjrs mettre avec '(None)'
        def dfs(amount):  
            if amount<0 :
                return float('inf')
            if amount==0 :
                return 0 
            res = float('inf') 
            for coin in coins :
                res = min(res,1+dfs(amount-coin))
            return res
        
        output = dfs(amount) 
        return output if output != float("inf")  else -1

    
    
"""#sol 3 #not my sol #dp bottom-up/tabulation(iterative) # TC O(S*n) avec S==amount, n=len(coins) ; car nested loop     # SC O(S) pour le tableau 

comme on a vue dans la solution precedente dfs(amount) ce calcule de la facon suivant tant que amount > 0  : 

'res = float('inf') 
 for coin in coins :
     res = min(res,1+dfs(amount-coin))
 return res     # la valeur retourner par dfs(amount)
 '
donc comme on peut le voir la valeur retourner par dfs(amount) et de base egale a inf puis a l'aide de la boucle on calcule un nouveau res qui va etre retourner par dfs(amount)
(cad qui va donc etre la valeur de dfs(amount)).

donc on va utiliser un tableau dp , dp[i] est equivalent a la valeur retourner par dfs(amount) donc au debut il va etre egale a inf puis on va faire exactement comme dans le top-down
ou dfs(amount) utilise 'dfs(amount-coin) for coin in coins' pour se calculer , ici aussi dp[curAmount] va utiliser 'dp[curAmount-coin] for coin in coins' pour se calculer. 
 
comme on a vu dans le tableau les index vont correspondre a un amount donc comme dp[curAmount] utilise 'dp[curAmount-coin] for coin in coins' pour se calculer , or l'idx curAmount-coin et 
forcement un idx qui vient avant l'idx curAmount donc pour calculer dp[curAmount] il faut calculer tout les amount qui le precede , donc on va calculer le tableau dp en commancent par 
l'index 1 (pas 0 car 0 c'est le base-case) puis en avancant ds les index (car dp[i] a besoin des index precedent pour se calculer)


"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)   # un tableau avec amount+1 case car le premier index est 0 
         
        dp[0]=0      # base-case if ammount==0 alors on retourn 0 (logique)
        
        for curAmount in range (1,amount+1) :    # calcule de dp[curAmount] avec curAmount qui varie de 1 a amount (inclus)   #O(amount)
            
            # pour chaque dp[i] , dp[i]=min([dp[i-coin] for coin in coins])
            for coin in coins :  # O(coins)
                
                # seulement si curAmount-coin >= 0 car sinon ca veut dire qu'on depasse le montant et donc ca nous interesse pas et en plus de cela curAmount-coin va etre un index neg
                if curAmount-coin>=0 :  
                    
                    dp[curAmount] = min(dp[curAmount],1+dp[curAmount-coin])
                    
        return dp[amount] if dp[amount]!=float("inf") else -1   # comme dans dfs ou dfs(amount) coutenait le resultat final ici au dp[amount] contient le resultat final. 
            
    
