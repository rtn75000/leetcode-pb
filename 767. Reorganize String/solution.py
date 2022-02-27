""" #hashmap #priority queue #TC O(n log 26) #SC O(26) donc O(1) car maxheap et count sont de taille 26 au max

l'idee est de compter la frequence de chaque lettre puis append au output la lettre la plus frequence ensuite on choisie une autre lettre pas la meme qu'avant car sinon on aura deux l'etre 
identique adjacente donc on prend la plus frequente qui n'est pas la premiere et on l'append au output, ensuite on prend la plus frequente qui n'est pas la precedente puis on l'append et ainsi de 
suite.

ex si on a: aaaaaaabbbbbccc cad 7*'a',5*'b',3*'c' alors on prend 'a' puis la plus frequente qui n'est pas 'a' donc 'b' puis la plus frequente qui n'est pas 'b' donc 'a' puis la plus frequente qui n'est pas 'a' donc 'b',etc...  ce qui nous donne au finale output = 'abababacabacabc' car : 
 7*'a',5*'b',3*'c' --> le plus frequent est 'a' donc output+='a' cad output='a' .
 6*'a',5*'b',3*'c' --> le plus frequent qui n'est pas 'a' c'est 'b' donc output+='b' cad output='ab' .
 6*'a',4*'b',3*'c' --> le plus frequent qui n'est pas 'b' c'est 'a' donc output+='a' cad output='aba' .
 5*'a',4*'b',3*'c' --> le plus frequent qui n'est pas 'a' c'est 'b' donc output+='b' cad output='abab' .
 5*'a',3*'b',3*'c' --> le plus frequent qui n'est pas 'b' c'est 'a' donc output+='a' cad output='ababa' .
 4*'a',3*'b',3*'c' --> le plus frequent qui n'est pas 'a' c'est 'b' donc output+='b' cad output='ababab' .
 4*'a',2*'b',3*'c' --> le plus frequent qui n'est pas 'b' c'est 'a' donc output+='a' cad output='abababa' .
 3*'a',2*'b',3*'c' --> le plus frequent qui n'est pas 'a' c'est 'c' donc output+='c' cad output='abababac' .
 3*'a',2*'b',2*'c' --> le plus frequent qui n'est pas 'c' c'est 'a' donc output+='a' cad output='abababaca' .
 2*'a',2*'b',2*'c' --> le plus frequent qui n'est pas 'a' c'est 'b' donc output+='b' cad output='abababacab' .
 2*'a',1*'b',2*'c' --> le plus frequent qui n'est pas 'b' c'est 'a' donc output+='a' cad output='abababacaba' .
 1*'a',1*'b',2*'c' --> le plus frequent qui n'est pas 'a' c'est 'c' donc output+='c' cad output='abababacabac' .
 1*'a',1*'b',1*'c' --> le plus frequent qui n'est pas 'c' c'est 'a' donc output+='a' cad output='abababacabaca' .
 0*'a',1*'b',1*'c' --> le plus frequent qui n'est pas 'a' c'est 'b' donc output+='b' cad output='abababacabacab' .
 0*'a',0*'b',1*'c' --> le plus frequent qui n'est pas 'b' c'est 'c' donc output+='c' cad output='abababacabacabc' .
 0*'a',0*'b',0*'c' --> fini . 

 
notre algo va marcher de la facon suivante : 

tout d'abord on compte les frequences de chaque lettre , ensuite on va utiliser une priority queue (voir explication : https://leetcode.com/problems/last-stone-weight/submissions/ ) pour avoir a chaque fois la frequence maximal.
Comme python n'a pas de max heap (complete) dans la library heapq on utilisera les fct de la min heap de heapq et pour que ca revient a avoir un max heap on fait *-1 a toute les frequences comme
ca ca va etre comme max heap (ex si on a 12 17 18 alors max heap ca donne [18,17,12] donc si on fait min heap de -12 -17 et -18 ca donne [-18 -17 -12] comme le max heap mais en negatif).
on creera un array qui contient des paires:  [frequence negative , lettre] puis ensuite on transformera cette array en priority queue (la priorite sera plus la frequence est petite) a l'aide de 
la fonction  heapq.heapify(array) qui arrange l'array en min heap.
une fois qu'on a notre heap on doit prendre la lettre avec la plus petite frequence (qui est en faite la plus grande frq mais comme on a fait *-1 ca revient a prendre la plus petite) donc on va
faire heapq.heappop(array) puis on rajoute la lettre du pop a notre output , on doit ensuite reduire la frequence donc on va faire +1 et pas -1 car les valeurs on etaient modifier en negatif .
Comme on peut pas utiliser tout de suite encore une fois cette lettre on va garder la paire [freq,lettre] dans une variable : prev . 
on refait pop ce qui va nous donner la lettre la plus frequente qui n'est pas la lettre precedente on rajoute cette lettre au output on reduit la frequence puis on remet prev dans le heap et maintenant prev devient la paire actuelle qu'on vient de faire pop dessus. On fait ce raisonnement en boucle tant que le heap n'est pas vide. si il reste plus qu'une lettre dans le heap avec une frquence superieur a 1 ca veut dire que forcement elle va etre coller a elle meme est donc on return "" car il ya pas de solution.

"""


class Solution:
    def reorganizeString(self, s: str) -> str:  # len(s)==n
        count = Counter(s) # Hashmap, count each char   # TC O(n)   #SC O(26) car 26 lettre au max
        maxHeap = [[-freq, char] for char, freq in count.items()]    #SC O(26) car max 26 lettres
        heapq.heapify(maxHeap) # O(26) (voir explication ici : https://leetcode.com/problems/last-stone-weight/submissions/ )       
        prev = None #contiendra la lettre qui vient d'etre lu
        output = ""
        # le while suivant lit a chaque foit un lettre donc au final il fait O(n) iteration car il passe sur toute les lettres de s
        while maxHeap or prev: #tant que le maxHeap n'est pas vide et tant que prev n'est pas vide car il peut avoir une lettre dans prev la lettre qu'on vient de lire et plus de lettre dans le heap et dans ce cas on veut comme meme rentrer ds le while pour verifier la condition "if prev and not maxHeap" pour retourner "" donc on mais or prev comme ca si la boucle et vide et prev ne l'ai pas alors on rentre qd mm ds le while
            # si prev est pas vide cad qu'on a une lettre dans prev mais que le heap est vide alors ca veut dire que il nous reste plus que une lettre qui est la meme que 
            # la precedente donc on n'a pas de reponse possible
            if prev and not maxHeap:  
                return ""
            # most frequent, except prev
            freq, char = heapq.heappop(maxHeap)   #O(log 26) car la heap de taille 26 max
            output += char
            freq += 1
           
            if prev: # si on a lu une lettre avant alors prev et pas vide et comme on vient de faire pop alors on fait rerentrer prev dans le heap
                heapq.heappush(maxHeap, prev)    #O(log 26) car la heap de taille 26 max
                prev = None
            if freq != 0:  # que si la frequence est diffrente de 0 on met la lettre qu'on vien de faire pop dans prev
                prev = [freq, char]
        return output
    
"TC : O(n log 26) car la boucle qui a n iteration utilise pop/push qui coute log(element dans le heap) donc log(26)"    



"""deuxieme solutions TC et SC O(n) : https://leetcode.com/problems/reorganize-string/discuss/232469/Java-No-Sort-O(N)-0ms-beat-100

si une lettre a une frequence superieur a la moitier arrondie vers le haut du nombre total des lettres +1 elle va forcement etre a cote d'elle meme ex : 'aaaabbc' la moitier egale 7/2=3.5 donc arrrondie vers le haut 4 , comme la frequence de a est pas superieur a 4 alors on peut avoir un output valide : 'ababaca' nais si on a 'aaaaabb' comme la frequence de a est 5 ce qui est superieur a 4 donc on a pas de output valide. 

l'idee est de trouver la lettre la plus frequente de la mettre au index paire 0,2,4.. puis continuer avec les autres lettres une fois qu'on a fini avc les places paires on passe aux places 
impaire. 

ex s='aaaabbbccc' il ya en tout 10 places , au debut on met 'a' car la lettre la plus frequente  : a _ a _ a _ a _ _ _ , ensuite on met le reste donc 'b' : a _ a _ a _ a _ b _ comme on a fini avec les places paire on passe au place impaire a b a b a _ a _ b _, ensuite on met 'c' : a b a b a c a c b c. 
"""


class Solution:
    def reorganizeString(self, s: str) -> str:  # len(s)==n
        
        n = len(s)
        
        count = Counter(s) # Hashmap, count each char { char:freq , .. } # TC O(n)   #SC O(26) car 26 lettre au max 
        
        maxi = 0    #frequence de la lettre la plus frequente
        maxChar = ''#lettre la pluys frequente 
        # recherche de la lettre la plus frequente avec ca frequence 
        for char in count:   # O(26)
            if count[char]> maxi:
                maxi, maxChar = count[char], char
                
        # si la lettre est frequente plus que la moitier arrondie vers le haut alors il ya pas de valid output      
        if maxi > (n+1)//2 :
            return "" 
        
        res = ['']*n  #SC O(n)
        idx = 0
        #on met la lettre la plus frequente dans les places paire
        for _ in range(count[maxChar]):
            res[idx] = maxChar
            idx += 2
        count[maxChar] = 0 #apres avoir mis la lettre la plus frequente la frequence de cette lettre devient 0 car on a tout mis
        # maintenant on met les autres lettres , on fini avec les places paires puis on passe au place impaire 
        # on ajoute au res chaque lettre autant de fois que la frequence de cette lettre.
        for char in count:  # cette boucle coute au max O(n) car fait une iteration pour une unite de frequence cad au total au max elle fait autant d'iteration que la somme des freq de la phrase 
            for i in range(count[char]):   
                if idx >= n:  # si on a fini avec les places paires et donc si idx>len(s) alors on passe au passe impaire donc idx=1
                    idx = 1
                res[idx] = char
                idx += 2
        return ''.join(res)  
       
