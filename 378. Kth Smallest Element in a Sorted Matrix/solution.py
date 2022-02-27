"""l'exo veut que SC soit inferieur a n^2 et si possible O(1)"""

"""# 1er sol   #not my sol #max heap #TC O(n^2*logk) voir explication en bas  #SC O(k)    n==numOfRow==numOfColumn

il suffit que le max heap contient k elements au max car a chaque fois qu'on depasse k element on fait pop ce qui sort le plus grand il nous restera donc dans la maxheap k plus petit element 
que l'element qui vient de sortir, si on repete cela jusqu'a qu'on fini de faire rentrer tout les element les element de la matrix alors les k element qui reste dans la heap sont les k plus petit element et comme on 
veut le k-eme plus petit element il suffit de faire pop ce qui va nous doneer le k-eme plus grand element des k plus petit element . 

on ajoute tout les elements de la matrix a la maxheap row par row .

le pb de cette solution c'est qu'on prend pas en compte le fait que les row et column sont dans l'ordre croissant , donc c'est pas bien. 

app : [[1, 5, 8], [2, 6, 15], [3, 9, 17]] , k=5
ca va faire rentrer -1,-5,-8,-2,-6 dans le minheap : heap=[-8,-6,-5,-2,-1]  ensuite quand on va ajouter 15 ca donne : heap=[-15,-8,-6,-5,-2,-1] comme len(heap)>k==5 donc on fait sortir le max 
comme ca on reste avec k plus petit element dans le heap : donc pop qui donne -15 .
ensuite on fait rentre -3 : heap=[-8,-6,-5,-2,-3,-1] comme len(heap)>k==5 donc on fait sortir le max comme ca on reste avec k plus petit element dans le heap : donc pop qui donne -8 .
ensuite on fait rentre -9 : heap=[-9,-6,-5,-2,-3,-1] comme len(heap)>k==5 donc on fait sortir le max comme ca on reste avec k plus petit element dans le heap : donc pop qui donne -9 .
ensuite on fait rentre -17 : heap=[-17,-6,-5,-2,-3,-1] comme len(heap)>k==5 donc on fait sortir le max comme ca on reste avec k plus petit element dans le heap : donc pop qui donne -17 .
on a fini de rentrer tout les valeurs de la matrix mainteneant notre heap contient les k plus petites valeurs de la matrix : heap=[-6,-5,-2,-3,-1]
maintenant on return le max qui sera la 5eme plus petite valeur : pop ns donne -6. 


TC: comme on peut voir que le heap peut etre au max k+1 donc O(k) donc pop et push coute O(logn). la double boucle coute donc O(m*n*logk)
SC : O(k) car heap max de taille k+1  cette solution n'est donc pas optimal car on veut SC O(1).
"""
class Solution:             
    def kthSmallest(self, matrix, k):
        
        m, n = len(matrix), len(matrix[0])  # For general, matrix doesn't need to be a square  #ds notre cas il suffit de faire  n = len(matrix)
        
        maxHeap = []
        
        for r in range(m):
            for c in range(n):   
                heappush(maxHeap, -matrix[r][c])  #-matrix[r][c] car heapify est pour minheap donc comme on veut max on fait la neg
                if len(maxHeap) > k: 
                    heappop(maxHeap)
                    
        return -heappop(maxHeap)


"""# 2eme sol meilleur SC  #not my sol  #min-heap #matrix #TC O(k*log(min(k,n))) voir explication en bas  #SC O(min(k,n))    n==numOfColumn==numOfRow

sol d'ici (2eme sol): https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise

l'algo est le suivant on ajoute tout les elements de la premiere column au minheap ensuite on va en boucle :
pop ce qui donne le minimum puis push l'element sur la meme row qui vient apres l'element qui a ete pop , si il ya pas d'element apres on fait que pop et on continue la boucle.(cad il y'aura 2 
pop consecutive). 

l'idee est que au debut on a toute la premiere column ds la heap , il ya forcement le 1er plus petit element qui est le premier element de la matrix donc le pop va nous donner le 1er plus petit
element.
ensuite le 2 eme plus petit element peut etre (ou il ya les X) : 

            pop| X |   |          
             ---------------     donc on ajoute l'element de droite de l'element qui vient d'etre pop car celui d'en bas est deja dans le heap, puis on fait pop disons que ca donne ca :
             X |   |   |   
            --------------- 
               |   |   |  
            ---------------
               |   |   | 
               
               | X |   |          
             ---------------     donc maintenant l'element le plus petit peut etre :
            pop|   |   |   
            --------------- 
               |   |   |  
            ---------------
               |   |   | 
               
               | X |   |          
             ---------------     or le seul element qui n'est pas dans le heap est celui a droite du pop donc on ajoute celui a droite du pop ds le heap puis on fait pop ce qui ns donne le 
            pop| X |   |         2 eme plus petit element, disons que le pop et le suivant:
            --------------- 
             X |   |   |  
            ---------------
               |   |   | 
               
               
               | X |   |          
             ---------------      donc maintenant l'element le plus petit peut etre : 
               |pop|   |         
            --------------- 
             X |   |   |  
            ---------------
               |   |   | 

               | X |   |          
             ---------------      or le seul element qui n'est pas dans le heap est celui a droite du pop donc on ajoute celui a droite du pop ds le heap puis on fait pop ce qui ns donne le  
               |pop| X |          3 eme plus petit element, disons que le pop et le suivant:
            --------------- 
             X |   |   |  
            ---------------
               |   |   | 

               | X |   |          
             ---------------       
               |   |pop|           donc maintenant l'element le plus petit peut etre : 
            --------------- 
             X |   |   |  
            ---------------
               |   |   | 
               
               | X |   |          
             ---------------       
               |   |pop| X        or le seul element qui n'est pas dans le heap est celui a droite du pop donc on ajoute celui a droite du pop ds le heap puis on fait pop ce qui ns donne le  
            ---------------       4 eme plus petit element, disons que le pop et le suivant:
             X |   |   |  
            ---------------
               |   |   | 
               
               | X |   |          
             ---------------       
               |   |   |pop       donc maintenant l'element le plus petit peut etre : 
            ---------------       
             X |   |   |  
            ---------------
               |   |   | 

               | X |   |          
             ---------------       
               |   |   |pop       cad on a pas besoin de rajouter quoi que ce soit ds le heap car tout les options y sont donc on ajoute rien on passe directe au pop: 
            ---------------       
             X |   |   |  
            ---------------
               |   |   | 


app: [[1, 5, 8, 10], [2, 6, 15, 16], [3, 9, 17, 18], [12, 16, 19, 20]] , k=16

-init :on ajoute au minheap 1 2 3 12 :           1 | 5 | 8 | 10         minheap=[1,2,3,12] on pop de minheap ca donne 1 c'est notre premier plus petit element  
                                                ---------------
                                                 2 | 6 | 15| 16 
                                                --------------- 
                                                 3 | 9 | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20
                                                   
-on ajoute au minheap 5 (la droite du pop):        | 5 | 8 | 10         minheap=[2,3,5,12] on pop de minheap ca donne 2 c'est notre 2e plus petit element
                                                ---------------
                                                 2 | 6 | 15| 16 
                                                --------------- 
                                                 3 | 9 | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20
                                                   
-on ajoute au minheap 6 (la droite du pop):        | 5 | 8 | 10        minheap=[3,5,6,12]  on pop de minheap ca donne 3 c'est notre 3e plus petit element
                                                ---------------
                                                   | 6 | 15| 16 
                                                --------------- 
                                                 3 | 9 | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20                     
                                                       
-on ajoute au minheap 9 (la droite du pop):        | 5 | 8 | 10        minheap=[5,6,9,12]  on pop de minheap ca donne 5 c'est notre 4e plus petit element
                                                ---------------
                                                   | 6 | 15| 16 
                                                --------------- 
                                                   | 9 | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20                     
                                                       
-on ajoute au minheap 8 (la droite du pop) :       |   | 8 | 10        minheap=[6,8,9,12]  on pop de minheap ca donne 6 c'est notre 5e plus petit element
                                                ---------------
                                                   | 6 | 15| 16 
                                                --------------- 
                                                   | 9 | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20        
                                                
-on ajoute au minheap 15 (la droite du pop):       |   | 8 | 10        minheap=[8,9,12,15]  on pop de minheap ca donne 8 c'est notre 6e plus petit element
                                                ---------------
                                                   |   | 15| 16 
                                                --------------- 
                                                   | 9 | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20       
                                                
-on ajoute au minheap 10 (la droite du pop):       |   |   | 10        minheap=[9,10,12,15] on pop de minheap ca donne 9 c'est notre 7e plus petit element
                                                ---------------
                                                   |   | 15| 16 
                                                --------------- 
                                                   | 9 | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20  
             
-on ajoute au minheap 17 (la droite du pop) :      |   |   | 10         minheap=[10,12,15,17] on pop de minheap ca donne 10 c'est notre 8e plus petit element
                                                ---------------
                                                   |   | 15| 16 
                                                --------------- 
                                                   |   | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20  
                                                
-on ajoute rien car il ya rien a droite du pop:    |   |   |            minheap=[12,15,17] on pop de minheap ca donne 12 c'est notre 9e plus petit element
                                                ---------------
                                                   |   | 15| 16 
                                                --------------- 
                                                   |   | 17| 18 
                                                ---------------
                                                12 |16 | 19| 20  
                                                
-on ajoute 16 (la droite du pop):                  |   |   |            minheap=[15,16,17] on pop de minheap ca donne 15 c'est notre 10e plus petit element
                                                ---------------
                                                   |   | 15| 16 
                                                --------------- 
                                                   |   | 17| 18 
                                                ---------------
                                                   |16 | 19| 20  
                                                   
-on ajoute 16(la droite du pop):                   |   |   |            minheap=[16,16,17] on pop de minheap ca donne 16 c'est notre 11e plus petit element
                                                ---------------
                                                   |   |   | 16 
                                                --------------- 
                                                   |   | 17| 18 
                                                ---------------
                                                   |16 | 19| 20  

-on ajoute 19 (la droite du pop):                  |   |   |            minheap=[16,17,19] on pop de minheap ca donne 16 c'est notre 12e plus petit element
                                                ---------------
                                                   |   |   | 16 
                                                --------------- 
                                                   |   | 17| 18 
                                                ---------------
                                                   |   | 19| 20  
                                                   
-on ajoute rien car il ya rien a droite du pop:    |   |   |            minheap=[17,19] on pop de minheap ca donne 17 c'est notre 13e plus petit element
                                                ---------------
                                                   |   |   |  
                                                --------------- 
                                                   |   | 17| 18 
                                                ---------------
                                                   |   | 19| 20        
                                                   
-on ajoute 18 (la droite du pop):                  |   |   |            minheap=[18,19] on pop de minheap ca donne 18 c'est notre 14e plus petit element
                                                ---------------
                                                   |   |   |  
                                                --------------- 
                                                   |   |   | 18 
                                                ---------------
                                                   |   | 19| 20    
                                                   
-on ajoute rien car il ya rien a droite du pop:    |   |   |            minheap=[19] on pop de minheap ca donne 19 c'est notre 15e plus petit element
                                                ---------------
                                                   |   |   |  
                                                --------------- 
                                                   |   |   |   
                                                ---------------
                                                   |   | 19| 20   
                                                   
-on ajoute 20 (la droite du pop):                  |   |   |            minheap=[20] on pop de minheap ca donne 20 c'est notre 16e plus petit element
                                                ---------------
                                                   |   |   |  
                                                --------------- 
                                                   |   |   |   
                                                ---------------
                                                   |   |   | 20             
                                                   
                                                   
 TC : comme on peut le constater le heap ne sera max de la taille min(k,m) car au debut on l'initialise avec min(k,m) valeurs puis on fait pop et push ou que pop seul donc on va jamais depasser 
 min(k,m) valeurs . donc chaque pop ou push est log(min(k,m)) donc le premier for coute O(min(k, m)*log(min(k,m))) et le deuxieme coute O(k*2*log(min(k,m))) (*2 car pop et push) 
 donc O(k*log(min(k,m))) donc au total on a O(min(k, m)*log(min(k,m))+k*log(min(k,m))) qui est egale a O(k*log(min(k,m))) car si k min alors ca revient a O(k*log(min(k,m))+k*log(min(k,m))) 
 donc ca revient a O(k*log(min(k,m))) et si m est min ca rvien a O(m*log(min(k,m))+k*log(min(k,m))) et comme m<k donc ca revient a  O(k*log(min(k,m))).  (remarque si k=n^2 alors TC = O(n^2*logn))
 
 SC le heap est de taille max min(k,m) donc SC O(min(k,m)).
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square  ,  m==numOfRow  n=numOfColumn
        minHeap = []  # contient des tuples (val,row,column)
        
        # ajout de la premiere column a heap 
        # on rajoute jusqu'a la row (min(k,m)) car si k>m il faut rajouter m car si on rajoute k on va depasser la taille de la matrix et si k<m alors on a pas besoins plus de k row car 
        # forcement ds notre cas les k premiers elements sont dans les k premieres row 
        for r in range(min(k, m)):   
            heappush(minHeap, (matrix[r][0], r, 0))

        ans = -float('inf')  # si la matrix est vide return - l'infini si non return valeur entre -10^9 et 10^9
        for _ in range(k):  # pop puis rajout de l'element a droite du pop si il y'en a un 
            ans, r, c = heappop(minHeap)
            if c+1 < n: #si il ya encore un element a droite
                heappush(minHeap, (matrix[r][c + 1], r, c + 1))  # remarque: le r est le r du pop ca permet a ajouter l'element de la meme row aue le pop a chaque fois
        return ans
    
    
""" # 3e solution TC et SC optimal  #not my sol  #binary search  #optimal sol  #TC O(n * log(A)), where A is difference between maximum and minimum values in our matrix.   #SC O(1)

on va faire un binary cherche dans les valeurs de la matrix pour trouver au finale le nombre qui a k nombre de la matrix inferieur ou egale a lui ce nombre est donc le k-ieme plus petit nombre .
le BS va donc etre sur le range [minval,maxval] cad sur [matrix[0][0], matrix[-1][-1]] car la matrix a les row et column sorted donc le min val se trouve au tout debut de la matrix
en haut a gauche et le max val se trouve a la fin de la matrix en bas a droite. le binary cherche fait log(A) iterations ou A est la difference entre maxval-minval . le  binary cherche va 
marcher de la facon suivante on prend un nombre mid qui sera le milieu du range [left,right] , puis on regarde combien de nbr dans la matrix sont inferieur ou egale a mid , on ferra ca 
a l'aide de la fct countLessOrEqual(mid)   (qui coute O(n) explication en bas) , si il ya moins de k nombre inferieur ou egale a mid donc mid n'est pas assez grand il faut un nombre
plus grand que mid pour trouver k nbr ds la matrix inferieur a mid domc naintenant le range pour mid va etre [mid+1,right] . si il ya k nombre superieur a mid ou plus de k nombre superieur a mid 
alors ca veut dire que mid ne doit pas etre superieur au mid actuelle car si il va etre superieur on aura forcement un k ou plus de k nombre sup egale a mid , on doit donc chercher notre 
nouveau mid dans le range [left, mid] (et pas mid-1 car mid peut etre la reponse car ici ds le cas ou il ya k nombre sup ou egal a mid alors mid peut etre une reponse ). ce qu'il faut comprendre c'est que la reponse finale va forcement etre dans la matrix voir application . 


app :       k=9
 1 | 5 | 8 | 10         range=[1,79] , mid = 40 , il ya 11 nbr inferieur ou egale a 40 or k=9 donc on a besoin d'un mid plus petit car on a besoin de 9 nbrs inferieur ou egale a mid
---------------         , donc range=[left,mid-1] cad range=[1,39]. 
 15| 22| 29| 39
---------------         range=[1,39] , mid = 20 , il ya 5 nbr inferieur ou egale a 20 or k=9 donc on a besoin un mid plus grand, donc range =[mid,right] cad range=[20,39] 
 30| 40| 43| 50
---------------         range=[20,39], mid = 30 , il ya 8 nbr inf egale a 30 or k=9 donc range=[30,39]
 32| 43| 48| 79
                        range=[30,39], mid= 35  il ya 9 nbr inf egale a 35 donc 35 est une reponse potentiel or 35 n'est pas dans la matrix donc forcement qu'il ya un nombre en dessous qui lui 
                        est dans la matrix qui a aussi 9 nbr inf ou egale a lui , donc c'est pour ca que n'otre algo continue comme meme a chercher un mid ds [left,mid] car on sait pas si le 
                        mid qui a k nbr inf ou egal a lui se trouve dans la matrix si il est dans la matrix alors quand on va chercher dans [left,mid] on va forcement trouver aucun mid 
apart mid=mid qui aura k nbr sup ou egal a lui car comme l'ancien mid etait ds la matrix donc en reduissant forcement qu'on aura que des mid avec moins de k nombre inferieur ou egal a  eux donc
l'algo va forcement remonter le mid j'usqu'a lancien mid qui etait ds la matrix et qui avait k nombre inferieur ou egale a lui. mais si le mid qui a k nombre inf ou egale a lui n'est pas ds la
matrix alors quand on va descendre on va trouver un mid qui lui est dans la matrix et qui a k nombre inferieur ou egale a lui car quand on descend de l'ancien mid on retire aucun nombre car ce
nombre n'est pas dans la matrix. tout ca pour dire que l'algo va toujours finir par trouver un mid qui est dans la matrix qui a k nbr inf ou egale a lui car il va augmenter mid dans tout les cas
si mid a pas k nbr inf ou egale a lui et si il a k nbr inf ou egale a lui il va comme meme chercher de voir en desous si il ya un mid qui a lui aussi k nbr inf eou ega et si oui alors il va
encore chercher jusqua que ce mid va forcement etre dans la matrix et donc quand on cherche en dessous de lui on a va forcement remonter jusqu'a lui car a chaque fois on aura un mid qui va pas
avoir k nbr inf ou egae a lui . donc revenons a notre app ici on va comme meme chercher un mid dans [30,35] car on sait pas si 35 est dans la matrix donc c'est possible qu'on va trouver un mid 
inferieur qui a k nbr inf ou egale a lui, et c'est possible que non et dans ce cas quand on va descendre dans [30,35] au final a la fin on va remonter a [35,35] car tout les reponse en 
dessous n'auron pas de k nbr inf ou egal. donc ici notre nouveau range est range=[30,35]

range=[30,35] mid = 32 , il ya 9 nbr inf egale a 32 donc range=[30,32] .

range = [30,32] mid = 31 , il ya 8 nbr inf egale a 31 donc range=[32,32], comme left==right alors on a fini le while et donc 32 est le seul nbr qui se trouve dans la matrix est qui a k==9
nbr inf ou egal a lui c'est donc lui le k-ieme nombre plus petit


remarque la fct countLessOrEqual(x) peut compter combien de nbr sont inf ou egale a x en O(row+column) elle marche de la facon suivant :
elle commence par la premier ligne dernier column si ce nbr est inf a x alors forcement que toute la ligne est inf ou egale a x donc on peut rajouter c (index de la column) nbr au compte des
nbr inf ou egale a x. on descend donc a la deuxieme range toujours a la dernier coumn si cett valeur est sup a x alors on recule d'une coloumn disons maintenenat que la valeur trouver est inf a x on peut etre sur que 
le reste des valeur de la range sont inferieur on peux donc rajouter les c nbr avec c l'index actuelle de la column au compte des nbr inf egale a k. 
ensuite on descent de ranger tout en restant sur la meme column et ainsi de suite (on ne retourne pas a la dernier column car si on a changer de column ca veut dire que on avait un nbr 
sup a x donc forcement ce qui en bas et sup) : 

ex :           |   |   |          la fonction utilise cette logique si le nbr sup>x alors tout les cases avec les X sont forcement sup a x
            ---------------       donc comme sup etait a la column 2 (idx commence a 0) alors maintenant un nombre inf a x peut se trouver que a column-=1 cad column==1 
               |   |sup|X         dans la meme range et dans les ranger inferieur (les ranger sup on deja etait pris en charge) comme ca :
            ---------------       
               |   | X |X  
            ---------------
               |   | X |X 
               
          
               |   |   |          
            ---------------     
            inf|inf|sup|         donc si on trouve dans row 1 column 1 un nombre inf on rajoute 2 au compte puis on desenc a la row 2 en restant sur la mm column cad 1,etc...
            ---------------       
            inf|inf|   |  
            ---------------
            inf|inf|   |  



source  :
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1321862/Python-Binary-search-solution-explained
"""

class Solution:   
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square

        def countLessOrEqual(x):
            cnt = 0
            col = n - 1  # start with the rightmost column
            for row in range(m):
                while col >= 0 and matrix[row][col] > x: col -= 1  # decrease column until matrix[r][c] <= x
                cnt += (col + 1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1] 
        while left < right:  # O(log A) iteration
            mid = (left + right) // 2
            if countLessOrEqual(mid) < k:  # O(row+column) donc ici O(n)
                left = mid + 1  # try to looking for a bigger value in the right side
            else:
                right = mid  # try to looking for a smaller value in the left side
        return left
