"""remarque: la regle est que la subarray doit etre egale ou superieur a k ("at least k")"""

"""utiliser que un sliding windows ne marchera pas car il ya des valeur negative donc par exemple nums = [-28, 81, -20, 28, -29] et k=87 bien que [-28,81,--20,28]le minimum subbaray avec sum>=87 est [81,-20,28] on ne pourra pas l'avoir a l'aide de sliding windows seulement """

"""on recherche une subbaray avec le moins d'element possible pour que la somme des elements soient egale a k ou plus 

lidee est d'utiliser le prefix sum cad de calculer la somme des elements jusqu'a un element i , cela nous permetra de connaitre la variation entre les element si il ya une variation superieur ou egale a k ca veut dire qu'on a forcement une sub-array qui a la sum supe ou egale a k .
ex : nums = [-28, 81, -20, 28, -29] et k= 87 si on fait le prefix sum de nums (on commence toujours par 0 pour avoir la variation meme du premier element de nums par rapport a 0) on a :
    prefix= [ 0, -28, 53, 33, 61, 39] comme on peut le constater entre -28 et 61 il ya une variation de 89 cad que apres (je dit bien apres!) -28 il ya une sub array dont la somme est egale a 89 donc si on additionne les element de nums qui respresente la variation -28 --> 61 dans le prefix sum on recevra : sum ([81, -20, 28]) = 89  

l'algo fonctionne de la sorte  : la fenetre s'ouvre vers la droite d'un element a chaque fois (chaque iteration de la boucle for aggrandit la fenetre vers la droite) , a chaque fois qu'on ajoute un element on verifie si la fenetre obtenue jusqu'a present a une sum >= k . Si c'est le cas alors on a une reponse potentiel dont la taille de la subarray sera comparer avec d'autre reponse potentiel (on gardera la taille minimale). une fois qu'une reponse potentiel est obtenue cad qu'on a une fenetre avec sum >= k ca ne sert plus d'agrandir la fenetre a gauche car ca va aggrandir le nombre d'element dans la subbaray (or on veut la plus petite subarray possible).seulement ds le cas d'une reponse potentielle on va faire avance le start de la fenetre cad de retrecir la fenetre cote gauche , cela nous permettra d'essayer d'obtenir une subarray plus petite, ex si on a nums = [1,3,2] et k=5 donc au debut start= end= 0 puis ensuite on obtient la fentre [1,3,2] (start=0 , end=2) dont la sum >= 5 avec len=3 maintenant on fait avancer le start : start=1  cad on a la fenetre [3,2] et comme on peut le constater sa sum est >=5 avec len=2 donc on a une meilleur taille , d'ou l'interet de faire avance le start (sans faire avancer le end) tant que la sum de la fenetre est >=k car on obtiendra une plus petite fenetre. Au lieu de faire avancer le start un part un on va avoir une queue qui gardera les start potentiel pour essayer directement les start potentiel est pas incrementer de 1 a chaque fois le start.
on va garder dans une queue les elements dans l'odre croissant cad a chaque fois qu'on fait une iteration for cad qu'on ajoute un nouvelle element on verifie si le prefixSum de cette elements est superieur au prefixSum du top de la queue si oui on l'ajoute (l'ordre croissant est conserver) si il est inferieur il faut retirer tout les element qui on un prefix sum superieur a lui en commencant par le top de la queue jusqu'a que les element qui se trouve dans la queue sont dans l'ordre croissant (si par ex on lit 1 puis 3 puis 4 alors q=[0,1,2] car prefixSum =[1,4,8] si apres on lit -6 alors on retire l'indexe 2 car prefix[2](=8)>prefix[3](=2) ainsi que 1 , puis on rajoute l'index de -6 cad q=[0,3]). 
la raison pour laquelle on garde dans l'ordre croissant est la suivante : 
soit nums = [1, 3 , 4 , -5 , 7 ]  et k=5  donc prefix = [0 1 4 8 3 10 ]
                                               idx :     0 1 2 3 4 5
i=0 : q=[0]
i=1 : q=[0,1] car prefix[1]>=prefix[0] on ne pop pas 0 et puisque prefix[1]-prefix[0]=1 pas >= 5 donc on append tout simplement 1 a queue
i=2 : q=[0,1,2]  car prefix[2]>=prefix[1] on ne pop pas 1 et puisque prefix[2]-prefix[0]=4 pas >= 5 donc on append tout simplement 2 a queue
i=3 : q=[1,2,3] car prefix[3]>=prefix[2] on ne pop pas 2 et puisque prefix[3]-prefix[0]=8 >= 5 donc on a un subarray donc on avance le start donc on retire le 0 de la queue et on append 3 a la fin
i=4 : q = [1,4] car prefix[4]<=prefix[3] on pop 3 puis prefix[4]<=prefix[2] on pop 2 soit q=[1,4] et puisque prefix[4]-prefix[0]=8 >= 5 donc on a un subarray donc on avance le start donc on retire le 0 de la queue et on rajoute 4 a la fin
etc... 
l'idee est que a partir du moment on on lit un element avec un prefix sum inferieur on retire de la queue (cad des start potentiel) les elements qui ont un prefix sum superieur car c'est sur que quand on a un start avec un prefix sum plus petit la somme a venir est plus grande que si on commencer avant ce start la . 


si on a prefix sum : [0,1,3,5,2,6]   avec nums=[1,2,2,-3,4] et k = 5

6                X       quand on va lire 5 cad i=3 alors queue = [0,1,2] on verifie donc la sum de 0 a 3  comme la somme est superieur egale a 5 alors on a len=3 puis on retire 0 
5         X     /        donc on a queue =[1,2] et puisque de 1 a 3 sum==4<=k on ajoute 3 a la queue = [0,1,2,3] on continue le for cad i=4 cad on lit la prefix sum 2 comme 
4        / \   /         il est plus petit que 5 et 3 on retire les indexe correspondant de la queue cad queue = [0,1] car forcement maintenant la sum qu'on aura apres l'index 4 va etre superieur 
3       X   \ /          a la sum obtenue avec l'index 2 3 car c'est plus bas que donc forcement l'augmentation sera plus grande (et si on disait que entre la prefix sum 5 et 6 on atteigner 
2      /     X           n'autre k alors sur que avec le prefix sum 2 et 6 on atteind k car la difference est plus grande et comme il ya moins d'element c'est mieu donc on prefere que start 
1     X                  commence a l'index de prefix sum egale 2 , et si on a pas k entre 5 et 6 alors il ya peut etre k entre 2 et 6 donc on va commencer par 2 et pas par 5 cad on a montrer que 
0    /                   a chaque fois que le prefix sum est en bas vaut mieu commencer a cette index estpas avant)
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans = n + 1    # une sub array peut etre de la taille de n au max 
        
        prefix = [0]                              
        for val in nums:                     #prefix sum list (in idx i we have the sum from index 0 to idx i)
            prefix.append(prefix[-1] + val) 

        deque = collections.deque([0])
        
        for i in range(1, n + 1):
            
            while deque and  prefix[i] <= prefix[deque[-1]]:   # on cree une une queue qui a que des valeurs croissante  
                deque.pop() 
                
            while deque and prefix[i] - prefix[deque[0]] >= k:
                ans = min(ans, i - deque.popleft()) 
                  
            deque.append(i) 
            
        return ans if ans != n+1 else -1
