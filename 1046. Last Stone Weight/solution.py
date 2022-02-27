"""introduction : qu'est ce qu'une priority queue ?

I) PRIORITY QUEUE : 

    1) concept :
    
    une priority queue est une data structure dont les elements ont une priorite , le dequeue() nous donnera l'element qui a la plus grande priorite , si deux elements ont la meme priorite alors 
    le dequeu() nous donnera le premier elements qui est rentrer dans la priority queue (cad ds ce cas la PQ se comporte comme une queue normale cad FIFO (first in first out) donc le premier   
    qui a ete enqueue() ds la PQ c'est lui qui sera dequeue ) . cad au final une PQ est une data structure qui prend en charge les operation suivantes (il peut encore prendre en charge d'autre 
    operation) :
    -insert()/enqueue():insert a new element to the PQ.
    -delete()/dequeue():remove and return the element with the highest priority.
    -peek():return the element with the highest priority.
    
    2) differentes implementations : 
    
    il ya plusieur facon d'implementer une PQ soit avec un array , soit un linked list , soit un heap , soit un binary search tree . Parmis ces implementations le heap est considere comme 
    l'implementation la plus efficace on va donc implementer la PQ a l'aide d'un heap mais avanct cela regardons un peu la difference entre les differentes implementations :

                        peek	 insert	    delete

    Array               O(n)     O(1)       O(n)    # on insert a la fin de larray donc au dernier index donc O(1), delete et peek coute O(n) car on doit parcourir tt l'array pr trouver 
                                                    # l'element avc la plus grd priorite

    Linked List  	    O(1)	 O(n)	    O(1)   # on insert dans l'ordre decroissant donc ca coute O(n) pour trouver la place de l'element en fction de ca priority car on doit parcourir 
                                                   # toute la linked list dans le pire des cas si cette element est le plus petit . peek et delete coute O(1) car comme l'insert fait en sorte 
                                                   # que les  elements soient placees dans l'ordre decroissant donc on a forcement l'element avec la plus grande priorite en tete de la linked list

    Binary Heap	        O(1)	 O(log n)	O(log n)    # regarder l'implementation pour plus de details 

    Binary Search Tree	O(1)	 O(log n)	O(log n)
    
    pour comprendre l'implementation de la PQ a l'aide du heap il faut d'abort voir qu'est ce qu'un heap ...
    

II) HEAP :

    1) COMPLETE BINARY TREE:

  - complete binary tree c'est un arbre dont tout les niveaux sont plein sauf le dernier qui peut l'etre partiellement et dans ce cas tout les nodes sont cotes gauche .
    ex de complete binary tree:                                           |      contre ex : 
            5                     5                    5                  |                       5                                          
           / \                  /   \                /   \                |                      / \                      
          1   7                2     9              2     9               |                     2   8          
         / \                  / \   /              / \   / \              |                        / \                       
        10  2                7   4 3              7   4 3   6             |                       3   4             
        
  - on peut creer un full binary tree a partir d'un array il suffit simplement de prendre comme root le premier element de l'array, les 2 elements a venir seront les enfants du root , les 2 
    autres elements seront les enfant du node de gauche, les 2 autres element les enfant du node de droite , et ainsi de suite ... donc tout simplement le 1er element est le root ensuite on prend
    2 element a chaque fois qui seront les enfant de chaque nodes de gauche a droite :
    ex [5 8 2 9 4 1] ca donne ca :      5 
                                       / \                                                                                     
                                      8   2
                                     /\   /
                                     9 4  1                                                                                                          
    on peut trouver a partir de l'array sans meme avoir besoin de creer le complete binary tree qui est le pere de l'element d'idx i dans le CBT ou qui sont les enfants de l'element d'idx i
    dans le CBT grace aux proprietes suivantes : 
    le pere de l'element d'idx i se trouve a l'idx floor((i-1)/2) cad (i-1)//2 . l'enfant de gauche de l'element d'idx i se trouve a l'indx  2i+1 , l'enfant de droite de l'element d'idx i se
    trouve a l'index 2i+1.                                                                                                                                
                               
                               
    2) HEAP also called binary heap: 
   
  -HEAP is a special tree-based data structure. un binary-tree est considerer un heap si :
    - c'est un complete binary tree (arbre dont tout les niveaux sont plein sauf le dernier qui peut l'etre partiellement et dans ce cas tout les nodes sont cotes gauche).
    - pour le max heap : le pere est plus grand que les enfant (donc le root est max). pour le min heap : le pere est plus petit que les enfants (donc le root est le min) 

  -HEAPIFY est une fct qui permet de transformer un CBT en un max/min heap cad de transformer le CBT en un CBT ou le pere est plus grand/petit que les enfants. Comme on a vu que toute array peut
   etre transformer en un CBT et qu'on peut meme directement travailler sur l'array sans la transformer en CBT grace au proprietes vu en haut ,on pourra donc appliquer la fonction heapify
   directement sur n'importe quel array en utilisant ses proprietes . 
   heapify verifie si le pere est plus grand/petit que les enfants dans le cas ou ce n'est pas le cas le plus grand/petit enfant ferra un swap avec le pere et on appelera heapify de facon
   recursive sur la nouvelle place du pere (pour verifier que dans la nouvelle place il est sup/inf a ses nouveaux enfants). 
   heapify verifie donc si un element i est a ca place (cad qui respect la def de max/min heap) si ce n'est pas le cas alors heapify deplacera cette element de facon recursive tant qu'il ne sera
   pas a ca place.   
  
   ex heapify(max) sur le node d'un arbre  :  
                        5                                 9                                       9
                      /   \                             /   \                                   /   \
                     2     9    =>  heapify(5) :       2     5   => heapify(5):                2     6    => heapify(5): return ; car pas d'enfant 
                    / \   / \     swap(5,9) et        / \   / \      swap(5,6) et appel       / \   / \
                   7   4 3   6    appel recursive    7   4 3   6     recursive               7   4 3   5
                   
   ex heapify(max) sur les elements d'un array directement :   
   nums = [5 2 9 7 4 3 6] prenons pour exemple heapify de l'element i=0 :
   ~ heapify(idx 0) : on doit verifier l'element d'idx 0 face a ses enfants , comme on a vu l'enfant de droit est a l'idx 2i+1 cad 2*0+1 et l'enfant de gauche a l'idx 2i+2 cad 2*0+2 donc on doit 
   comparer nums[1],nums[2] et nums[0]. Dans le cas ou le pere n'est pas le plus grand on met le plus grand enfant a la place donc comme le pere est pas le plus grand et nums[2] est le plus
   grand des enfants alors ont swap(nums[0],nums[2]) ce qui donne nums = [9 2 5 7 4 3 6] puis on verifie recursivement le nouvelle idx du pere cad heapify de l'element d'idx 2.
   ~ recursion heapify(idx 2) : comparaisons entre nums[2]==5, nums[2*2+1]==3 et nums[2*2+2]==6 comme le pere n'est pas le plus grand on swap le pere avc le plus grand donc swap(nums[2],nums[6])
   ce qui donne nums = [9 2 6 7 4 3 5] , puis on verifie recursivement le nouvelle idx du pere cad heapify de l'element d'idx 6 .
   ~ recursion heapify(idx 6) : comme l'idx 6 n'a pas d'enfant on a fini.
   
   code :
           def heapify(self,nums, n, i): 
                    # Find largest among root and children
                    l = 2 * i + 1
                    r = 2 * i + 2

                    largest = i
                    if l < n and nums[largest] < nums[l]: 
                        largest = l 

                    if r < n and nums[largest] < nums[r]: 
                        largest = r 
                    # If root is not largest, swap with largest and continue heapifying
                    if largest != i: 
                        nums[i], nums[largest] = nums[largest], nums[i]
                        self.heapify(nums, n, largest)
   
   -BUILT MAX/MIN HEAP: pour que l'arbre soit un max/min heap il faut faire heapify sur tout les nodes qui ne sont pas des leaf. on a pas besoin de faire heapify sur les leaf car les leaf on 
   forcement un pere et quand on fait heapify sur le pere ca va mettre forcement le plus grand en tant que pere et les enfants seront plus petit. dans un array l'idx n/2-1 est l'idx du dernier 
   node non-leaf apres cette index c'est des leaf. on doit faire heapify en commancent par l'idx n/2-1 et en terminant par l'idx 0 si on fait l'inverse ca ne marche pas , cad pour que 
   ca marche il faut que on fasse heapify sur un element donc les enfants on deja etait heapify , preuve :
   ex heapify en commancent par l'idx 0 et en terminant par n/2-1 (a la fin on ne va pas avoir de max/min heap) :  nums = [2 5 4 8 9 10 11] 
             2                                 5                   5
           /   \                             /   \               /   \
          5     4    =>  heapify(idx 0) :   2     4     =>      9     4       (cad nums =[5 9 4 8 2 10 11] )
         / \   / \               /node 2   / \   / \           / \   / \
        8   9 10 11                       8   9 10  11        8   2 10  11    
          
                             =>  heapify(idx 1) : puisque 9 est max entre 9,8 et 2 dc pas de changement 
                                         /node 9 
                                                               5                   
                                                             /   \               
                                     =>  heapify(idx 2) :   9    11         on a pas de max heap  !! 
                                                 /node 4   / \   / \            
                                                          8   2 10  4          
   ex heapify en commancent par l'idx n/2-1 et en terminant par 0 (a la fin on va avoir un max/min heap) :  nums = [2 5 4 8 9 10 11] 
             2                                 2                 
           /   \                             /   \               
          5     4    =>  heapify(idx 2) :   5    11         (cad nums =[2 5 11 8 9 10 4] )
         / \   / \               /node 4   / \   / \            
        8   9 10 11                       8   9 10  4            
          
                                                       2                   
                                                     /   \               
                             =>  heapify(idx 1) :   9    11        (cad nums =[2 9 11 8 5 10 4] )
                                         /node 5   / \   / \            
                                                  8   5 10  4          
                                                               11                   11
                                                             /   \                /    \
                                     =>  heapify(idx 0) :   9     2     =>       9     10    on obtient un max heap car pere > enfants
                                                 /node 2   / \   / \            / \   /  \
                                                          8   5 10  4          8   5 2    4 

    3) BASIC HEAP OPERATIONS : (ici on va parler de max heap (c la mm chose pour min heap a qqeu details pres))
    
     rappel : une heap peut etre representer par un array ou le pere de l'element i se trouve a l'idx (i-1)//2 et les enfants a l'idx 2i+1 (enfant gauche) et 2i+2 (enfant droite), le pere 
     est forcement plus grand que les enfants. toute les operations du heap sont donc implementer sur un array qui a ses proprietes.
    
    
    -insert :  insertion d'un nouvelle elements dans le heap , on va tout simplement l'inserer en dernier et verifier : si le pere est superieur alors on a pas besoin de rien faire car on
    a conserver les propietes du max heap mais si le pere est inferieur alors il faut swap le pere avec le fils puis refaire (en boucle) cette verification sur le nouvelle idx du fils 
    (cad l'ancien idx du pere) . (remarque: ici on compare de bas en haut un enfant face a so pere , heapify compare de haut en bas un pere face a ses enfant). insert coute donc O(logn) car
    ds le pire des cas un element qui a ete inserer au leaf va etre remonter jusqu'au root donc on va faire O(log n) iteration pour le remonter car un heap est un CBT donc la hauteur est O(logn).
    
    def insert(array,element):
    
        array.append(element)       # ajout de l'element a la fin 
        idx = len(array)-1          # idx de l'element inserer
        
        # tant que on est pas arriver au root ou tant que l'element est superieur au pere (ce qui n'est pas cense etre) alors :
        while (idx > 0 and element>array[(idx-1)//2]) :      # shift up (comparaison de l'enfant face au pere) coute O(log n) car de la racine jusqu'au root .
        
            #swap l'element avec le pere
            array[idx],array[(idx-1)//2] =  array[(idx-1)//2],array[idx]      
            
            #nouvelle index de l'element (qui est l'ancien idx du pere car il ya eu un swap)
            idx = (idx-1)//2                                         
    
    
    -extractMax : remove and return the max value donc cad on doit supprimer et return le root . Pour cela on va faire un swap entre le root et la derniere valeur du heap , on va ensuite
    supprimer la derniere valeur puis faire heapify sur le nouveau root pour arranger le swap qui a ete fait . puisque heapify peut faire descendre un element depuis le root jusqu'au leaf le 
    extractMax coute donc O(logn).
    
    def extractMax (array) : 
        
        if len(array) > 0 :
            root = array [0]  #store root value to return it
            array[0]=array[len(array)-1] # root take the value of the last element
            del array[len(array)-1]  #delete last element 
            heapify(array[0])  #heapify the new root 
            return root
        else : 
            return "nothing to extract empty array"
        
    -peek/getMaxi : cette operation nous return simplement le max donc return le root .
     
     def peek(array) : 
         return array[0]
         
    -delete : supprime n'importe quel element. on va proceder de la maniere suivante : on swap la valeur a supprimer avec le dernier node puis on supprime le dernier node. puisque maintenant 
    on a mit une nouvelle valeur dans l'idx de l'element supprimer il faut rearanger l'array . il ya deux possibilites soit le nouvelle element est sup au pere donc il faut faire monter cette
    element et donc il faut faire monter cette element tant qu'il sera superieur au pere , soit il est inferieur a ses enfants et donc il faut le faire descendre et donc utiliser heapify qui 
    peut fait descendre tant que inf aux enfants . donc le cout est O (log n) car soit on le fait monter tout en haut soit on le fait descendre tout en bas.
    
    def delete(array,idx):                          #idx is the index of the element to delete 
    
            swap(array[idx],array[len(array)-1])    #swap element to delete with last element 
            del array[len(array)-1]
            
            # maintenant array[idx] contient le dernier element , l'element qui a ete deplacer
            # tant que on est pas arriver au root ou tant que l'element est superieur au pere (ce qui n'est pas cense etre car max heap) alors :
            while (idx > 0 and element>array[(idx-1)//2]) :         #shift up

                #swap l'element avec le pere
                array[idx],array[(idx-1)//2] =  array[(idx-1)//2],array[idx]      

                #nouvelle index de l'element (qui est l'ancien idx du pere car il ya eu un swap)
                idx = (idx-1)//2      
            
            if element<array[2*i+1] or element<array[2*i+2] :   # si l'element est plus petit que ses enfant alors heapify  (si on rentre dans le while cette condition sera false)    #shift down
                 heapify(array[idx])


     
III)PRIORITY QUEUE OPERATIONS IMPLEMENTED WITH HEAP :

    1)insert(array,p): Inserts a new element with priority p in heapArray, insert the element at the end and shift it up. cost O(log n)
    
   def insert(array,p) :

        array.append(p) # ajouter le nouvelle element a la fin

        idx = len(array)-1          # idx du dernier element
        
        # shift up (comparaison de l'enfant face au pere) coute O(log n) car de la racine jusqu'au root .
        # tant que on est pas arriver au root ou tant que l'element est superieur au pere (ce qui n'est pas cense etre) alors :
        while (idx > 0 and element>array[(idx-1)//2]) :      # shift up (quand on compare l'enfant face au pere) coute O(log n) car de la racine jusqu'au root .
        
            #swap l'element avec le pere
            array[idx],array[(idx-1)//2] =  array[(idx-1)//2],array[idx]      
            
            #nouvelle index de l'element (qui est l'ancien idx du pere car il ya eu un swap)
            idx = (idx-1)//2    
        
    2)delete : supprime n'importe quel element. on va proceder de la maniere suivante : on swap la valeur a supprimer avec le dernier node puis on supprime le dernier node. puisque maintenant 
    on a mit une nouvelle valeur dans l'idx de l'element supprimer il faut rearanger l'array . il ya deux possibilites soit le nouvelle element est sup au pere donc il faut faire monter cette
    element et donc il faut faire monter cette element tant qu'il sera superieur au pere , soit il est inferieur a ses enfants et donc il faut le faire descendre et donc utiliser heapify qui 
    peut fait descendre tant que inf aux enfants . donc le cout est O (log n) car soit on le fait monter tout en haut soit on le fait descendre tout en bas.
    
    def delete(array,idx):                          #idx is the index of the element to delete 
    
            swap(array[idx],array[len(array)-1])    #swap element to delete with last element 
            del array[len(array)-1]
            
            # maintenant array[idx] contient le dernier element , l'element qui a ete deplacer
            # tant que on est pas arriver au root ou tant que l'element est superieur au pere (ce qui n'est pas cense etre car max heap) alors :
            while (idx > 0 and element>array[(idx-1)//2]) :         #shift up

                #swap l'element avec le pere
                array[idx],array[(idx-1)//2] =  array[(idx-1)//2],array[idx]      

                #nouvelle index de l'element (qui est l'ancien idx du pere car il ya eu un swap)
                idx = (idx-1)//2      
            
            if element<array[2*i+1] or element<array[2*i+2] :   # si l'element est plus petit que ses enfant alors heapify  (si on rentre dans le while cette condition sera false)    #shift down
                 heapify(array[idx]) 
                 
    3)peek:  cette operation nous return simplement la priority max donc return le root . cout O(1)
     
     def peek(array) : 
         return array[0]
     
     
    4)extractMax : return and delete max priority element. Replace the value at the root with the last leaf and delete the last leaf. heapify the element that is now in the root . cout log(n)
     
     def extractMax (array) : 
        
        if len(array) > 0 :
            root = array [0]  #store root value to return it
            array[0]=array[len(array)-1] # root take the value of the last element
            del array[len(array)-1]  #delete last element 
            heapify(array[0])  #heapify the new root 
            return root
        else : 
            return "nothing to extract empty array"



remarque super importante : 
     bien qu'on a dit que construire un heap coute O(n log n) car on fait heapify (O(log n)) sur n/2 elements (O(n)) ce n'est pas vrai, cette analyse est vraie quand on rentre pas dans le detail
     et c'est pour cela que meme certain site considere la constuction d'un heap O(nlogn) mais en verite la construction d'un heap coute O(n) .
     construire un heap (on parle a l'aide d'un heapify sur tout les nodes qui sont pas leaf et pas de faire a chaque fois insert car ca sa coute O(nlogn)) coute O(n) et non O(n*logn)! 
     car bien que en generale heapify on le considere comme O(log n) mais quand on fait un heapify pour construire un heap alors ca coute pas a chaque fois log n car le dernier niveau 
     les leaf on touche pas puis l'avant dernier niveau qui a 2^(h − 1) nodes peux descendre max d'un nivau donc 1*2^(h − 1) iterations, celui en haut qui a 2^(h − 2) nodes peut descendre 
     max de deux niveaux donc 2*2^(h − 2) iterations, celui encore en haut a max 2^(h − 3) nodes et peut descendre max 3 niveaux donc 3*2^(h − 3) , etc .. 
     il ya une preuve mathematique comme quoi c'est O(n) pour plus de details voir cette article : https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
"""


"""remarque : en python la library heapq nous donne differentes fct pour les heap queue communement appeler priority queue. cette library utilise un min heap et non un max heap ! il existe 
aussi qqeu fct pour la max heap comme heapq._heappop_max(array) ou  heapq._heapify_max(array) mais d'autre fct elementaire comme heap push n'existe pas . La technique utiliser quand on veut faire
un max heap est de simplement multiplier chaque value par -1 pour que 'ordre soit inverser aini en utilisant un min heap sur les nouvelle valeur revient a utiliser un max heap sur les anciennes valeurs . a la fin quand on retourne les elements ne pas oublier de faire fois -1 pour retrouver la valeur d'origine. """



class Solution:
      def lastStoneWeight(self, stones: List[int]) -> int:
        for i,val in enumerate(stones):   # O(n) voir remarque en haut pq on fait cette boucle
            stones[i]=-val 
        # heapify est une fonction built-in de heapq qui construit un heap a l'aide de heapify sur les nodes qui ne sont pas leaf . 
        # cette fonction coute O(n) (https://stackoverflow.com/questions/51735692/python-heapify-time-complexity), voir remarque super importante en haut sur le cout de construction d'un heap.
        heapq.heapify(stones)  
        while len(stones) > 1 : # tant qu'il ya plus d'une pierre car sinon on a fini, cout O(n)*(log n)  (push et pop coute log n)
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))  #on po 2 pierres on les soustrait puis on push le resultat. 
        return -stones[0]  #on fait moins pour avoir la valeur original avant la modification
    
# TC: O(n log n)    SC: O(1)
    
