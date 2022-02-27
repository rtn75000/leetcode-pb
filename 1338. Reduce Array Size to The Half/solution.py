"""
#ma solution #hashmap  #heap/priority queue #TC O(nlogn) #SC O(n)      n=len(arr)

compter la frequence de chaque nbr puis utiliser une priority queue pour a chaque fois retirer le nbr avec la frequence maximal tant que ce qui nous reste est superieur a la moitier .
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr) #TC O(n) SC O(n)
        output=0
        n = len(arr)
        heap=[-x for x in count.values()]  # heap des frequences on fait moins car python a que min heap donc pour que ca revient a faire max heap on fait moins a toutes les valeurs. #SC O(n)
        heapq.heapify(heap)  #built heap cost O(n)
        deleted = 0 # nombre de nombres supprimer
        # le while suivant peut avoir au max n/2 iteration si les frequence sont egale a 1 a chaque fois (ex ds le cas ou arr=[1,2,3,4,5,6,7,8,9,10,11,12...] ou aucun nbr ce repete) . 
        # chaque pop coute O(logn) donc chaque iteration coute O(logn) donc en tout on a O(n/2logn) soit O(nlogn)
        # tant qu'on a supprimer moins que la moitier il faut supprimer encore (ici la moitier est egale a n/2 car len(n) est paire d'apres les constraints de l'ennoncee.)
        while deleted < (n/2) : 
            deleted -= heapq.heappop(heap)  #on fait mois et pas plus car les frequences sont negatives donc pour rajouter a deleted on fait mois (car -(-x)==+x)
            output+=1
        return output  
    
"""2 eme solution #hashmap #built-in sort #TC O(nlogn) #SC O(n)      n=len(arr)
on compte la frequence puis on trie ordre decroissant, on retire ensuite les frequences en commancant par la plus grande jusqu'a qu'on arrive a avoir moins de la moitier de len(arr)."""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr) #TC O(n) SC O(n)
        frequencies = list(cnt.values())
        frequencies.sort() ##TC O(nlog n) car on peut avoir n frequences differentes (ex ds le cas ou arr=[1,2,3,4,5,6,7,8,9,10,11,12...] ou aucun nbr ce repete) donc pour sort ca coute nlogn .
        output = deleted = 0   #deleted c'est le nombre d'elements supprimes . 
        #l e while suivant peut avoir au max n/2 iteration si les frequence sont egale a 1 a chaque fois (ex ds le cas ou arr=[1,2,3,4,5,6,7,8,9,10,11,12...] ou aucun nbr ce repete) . 
        # le pop de l'array coute O(1) donc le while coute O(1)*n/2 cad O(n)
        # tant qu'on a supprimer moins que la moitier il faut supprimer encore(ici la moitier est egale a n/2 car len(n) est paire d'apres les constraints de l'ennoncee.)
        while deleted < len(arr)/ 2:   # TC O(n)
            output += 1
            deleted += frequencies.pop()
        return output
    
"""3eme solution la meilleur  #hashmap #counting sort # TC/SC O(n)

introduction : 
-> Counting Sort: sorting lineaire TC : O(n+k) . on l'utilise quand le plus grand nbr a trier k n'est pas bcp plus grand que la taille n de l'array.
comme ici on feut trier la frequence or celle-ci est forcement inferieur ou egale a la taille de l'array donc on peut utiliser le counting sort. 
counting sort est un algorithme qui trie des elements en comptant le nbr d'occurence de chaque element , ce compte est stocker dans un array (ici on va l'appeler count) qui va de 0 a k. 
si un nbr x apparait dans l'array d'origine alors on incremente de 1 l'index x de l'array de stockage (count[x]+=1) . donc pour obtenir un trie ds l'ordre decroissant on va parcourir l'array de stockage de
l'index max cad k a l'index min cad 0. on va simplement append au resultat index*valeur de cette index (cad idx*count[idx] car si par exemple le nbr 7 apparait 3 fois alors on l'idx va etre 7
et count[7] va etre 3 ).


ici on va faire un counting sort sur les frequences car on veut avoir les frequence dans l'odre decoissant . donc on va d'abord compter la frequence de chaque nbr puis on va trier 
les frequences obtenue a l'aide du counting sort. le counting sort va utiliser une array qui va de 0 a n car les frequence vont de 0 a n au max. il va incrementer l'index qui correspond au frequence de l'array.
apres cela on commence a lire par la fin de l'array du counting sort (appeler ici counting) pour que on lit les frequences dans l'ordre decroissant . on supprimera une 
recurence de frequence a chaque fois tant qu'on est pas arriver a au moins la moitier du nbr total de frequence. 

app : arr = [3,3,3,3,5,5,5,2,2,7,7,7]  , n==len(arr)==12   la frequence va donc de 0 a 12 
counting sort :  counting = [0 0 1 2 1 0 0 0 0 0 0  0  0  0] (len(counting)==n+1==1 car la frequence va de 0 a 12 donc 13 possibilites) cad on a une frequence egale a 2, deux freq egale a 3 et 
                             0 1 2 3 4 5 6 7 8 9 10 11 12 13                                                                                                              une freq egale a 4 .

on commence par la frequence la plus haute donc idx 13 et on descend : 
-idx= 13 a 5  , c'est idx sont egale a 0 donc on fait rien
-idx=4 : counting[4]==1 cad il ya une frequence qui est egale 4 donc deleted+=4 et output+=1 , ensuite on reduit de 1 le nombre de frq egale a 4 donc counting[4]-=1 cad counting=[0 0 1 2 0 ... 0]
comme counting[4]==0 alors on fait idx-=1
-idx=3 : counting[3]==2 cad il ya 2 frequence qui sont egale 3 donc deleted+=3 et output+=1 , ensuite on reduit de 1 le nombre de frq egale a 3 donc counting[3]-=1 cad counting=[0 0 1 1 0 ... 0]
comme la condition du while devient False car deleted(7)>=n/2(6) donc on a fini on peut return output(2)


"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        cnt = Counter(arr) #TC O(n) SC O(n)
        
        n = len(arr)
        
        counting = [0] * (n + 1) # n+1 car frequence de 0 a n
        
        for freq in cnt.values():  #incrementer la valeur de l'indexe qui correspond a la frequence
            counting[freq] += 1
            
        output = deleted = 0   # deleted c'est le nombre d'elements supprimes .
        
        freq = n  # on commence par l'indexe qui represente la plus grande frequence possible cad n . 
        
        while deleted < n/2:  # TC O(n)
            if counting[freq] == 0 : # si la valeur est egale a 0 alors on passe a un autre index sinon on change pas l'index
                freq -= 1 # on descend d'idx 
                continue 
            deleted += freq
            counting[freq] -= 1
            output += 1
        return output

