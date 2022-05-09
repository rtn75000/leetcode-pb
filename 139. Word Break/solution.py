"""#ma sol #dp #dfs+memoization /Top-down  # TC et SC pas top l'analyse tres compliquer a trouver la reponse exacte pour ce code 

VOIR APP/ARBRE DE RECURSION GITHUB

TC analyse : a premiere vue puisqu' on aura un arbre m-ary (avec m la taille de wordDict) de hauteur n (car a chaque fois on peut lire que une lettre de s donc la
plus grande profondeur peut etre n) donc TC egale O(m^n) ce qui est enorme mais a l'aide de la memoization est des condition d'arret de cette solution ce code arrive a
ne pas avoir de TLE , en vrai le code est bcp moins que O(m^n) (beat 90%)  (j'ai essayer de trouver sont TC precis mais j'ai pas trouver dans les commentaire car 
leur dfs est different et ce qui on le meme dfs aussi on du mal avec le TC (j'ai chercher tres longtemps donc pas la piene de rechercher a nouveau). 
il y'en a qui mentionne qu'il ya au max O(n^2) mais j'ai pas compris pq ...)
SC analyse : O(n) pour le stack de recurion car la hauteur est O(n) . de plus on doit grader les resulat deja calculer on va garder que les mots qui on un
potentiel cad que les partition de s comme ceci par ex si s=cars alors 'c' ou 'ca' ou 'car' sont les mot a garder , car tout le reste va retourner False et va pas faire de recursion.
donc en tout il ya O(n) patition . donc SC = O(2n) cad O(n). 

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        res = 0
        memo = {}
        # remarque : la nested fct dfs reconnait s, wordDict et memo car quand on ne fait pas d'assignement juste on regarde la variable sans la modifier
        # il ya pas besoin d'utiliser nonlocal (j'ai ecrit dessus dans evernote : https://www.evernote.com/shard/s393/sh/fae53613-e41b-e5dc-7372-d3e53fd748c7/28e56f3fe8d09504fa4634f7add549da)
        def dfs (cur) :  
            nonlocal res  # comme on fait un assignement dans le code on est obliger de faire nonlocal sinon res ne va pas etre reconnue. 
            if cur in memo :
                return memo[cur]
            if cur == s : 
                return 1
            # si le mot obtenue j'usqu'a present ne correspond pas au debut de s alors c'est faux ca sert arien de continuer 
            if cur != s[:len(cur)]: # sans cette condition on aura TLE   # remarque: meme si len(cur)>len(s), s[:len(cur)] marche et retourne s 
                return 0
            for word in wordDict :
                res += dfs(cur+word)
                if res : # pas obliger cette condition c'est juste pour gagner du temps a ne pas faire les autre dfs du for 
                    break
            memo[cur] = res  
            return res #seulemnt apres avoir fait tout les dfs des enfant on return le dfs du pere
        return  bool(dfs(''))

    
"""#sol 1bis  #utilisation de lru_cache"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        res = 0
        @lru_cache
        def dfs (cur) :  #ecrire pq res il faut faire nonlocal et s,wordDict ya pas besoin
            nonlocal res
            if cur == s :
                return 1
            if cur != s[:len(cur)]: # sans cette condition on aura TLE  # remarque: meme si len(cur)>len(s) alors s[:len(cur)] marche et retourne s 
                return 0
            for word in wordDict :
                res += dfs(cur+word)
                if res : # pas obliger cette condition c'est juste pour gagner du temps a ne pas faire les autre dfs du for 
                    break
            return res
        return  bool(dfs(''))

    
"""# sol 2 # not my sol #dp #bottom-up(iterative)/ Tabulation  #TC O(n^3) car les nested loop on O(n^2) iteration que chacune coute O(n) #SC O(n) car on utilise un tableau de taille n+1 .  

Un dp bottom-up commence par la fin (il ya des reponse qui commence par le debut et ca reste un dp car a partir du moment ou on utilise un tableau qui nous 
permet de trouver la solution c'est un dp bottom-up ). 

VOIR APP GITHUB

voir aussi : https://youtu.be/Sx9NNgInc3A?t=555
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        
        dp = [False] * (n+1) #on rajoute un en plus de la taille cad en tout il va avoir n+1 cases 
        
        dp[n] = True  
        
        # dp[i]==T ca veut dire que le mot s[i:len(s)+1] peut etre entrecouper avec des mot de wordDict
        # donc a chaque etape on verifie si s[start:i] est dans wordSet et si s[i:len(s)+1] peut etre entrecouper 
        # si c'est le cas alors s[start:len(s)+1] peut etre entrecouper 
        # on fait ca en boucle jusqu'a que start==0 puis on retourne dp[0] si il est True alors ca veut dire 
        # que s[0:len(s)+1] peut etre entrecoupe est donc c'est True. 
        for start in range(n-1, -1, -1):           #O(n)
            for end in range(start+1, n+1):        #O(n)
                if dp[end] and s[start:end] in wordSet:  #s[start:end] coute O(n) car fait une copie de s 
                    dp[start] = True
                    break
        
        return dp[0]
    

