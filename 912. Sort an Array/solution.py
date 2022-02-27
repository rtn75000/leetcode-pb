"""cette exercice est primordiale si on nous demande d'implementer le sort sans utiliser de fonction built-in."""

"""introduction: analyse de TC et SC de quelque algorithme majeur de sorting.
 
Time complexity Analysis – 
We will analyse the best, average and worst case complexity of different sorting techniques . 

I)Comparison based sorting – 
In comparison based sorting, elements of an array are compared with each other to find the sorted array. 

    1)Bubble sort and Insertion sort – 
        Average and worst case time complexity: n^2 
        Best case time complexity: n when array is already sorted. 
        Worst case: when the array is reverse sorted. 
 
    2)Selection sort – 
        Best, average and worst case time complexity: n^2 which is independent of distribution of data. 

    3)Merge sort – 
        Best, average and worst case time complexity: nlogn which is independent of distribution of data. 

    4)Heap sort – 
        Best, average and worst case time complexity: nlogn which is independent of distribution of data. 
 
    5)Quick sort – 
        It is a divide and conquer approach .
        Worst case: when the array is sorted or reverse sorted, the partition algorithm divides the array in two subarrays with 0 and n-1 elements. (donc ova faire QS(n-1)+QS(n-2)+...+QS(1)
        cad on aura une somme: 1+2+..+n iterations donc O(n^2)) Therefore, solving this we get, T(n) = O(n^2)
        Best case and Average case: On an average, the partition algorithm divides the array in two subarrays with equal size. we get this tree :
        
                                           n
                                      /         \
                                     /           \
                                  n/2            n/2
                                /    \          /    \
                              n/4    n/4      n/4    n/4
                               .      .        .      .
                               .      .        .      .
                               .      .        .      .
                               1      1        1      1             
        il y'a n branches et la hauteur est log n (car on divise par 2 a chaque fois) cad pr chaque resultat/branche il faut log n operations donc comme il ya n branche il ya en tout O(n log n)
        operations.
                            
                            
        
II) Non-comparison based sorting – 
In non-comparison based sorting, elements of array are not compared with each other to find the sorted array. 

    1)Count sort – 
        Best, average and worst case time complexity: n+k where elements are in range [1,k] . 

    2)Bucket sort –  on ne va pas voir son implementation car pas bcp de question leetcode dessus
        Bucket sort is used when: input is uniformly distributed over a range and there are floating point values.
        Best and average time complexity: n+k where k is the number of buckets. 
        Worst case time complexity: n^2 if all elements belong to same bucket. (cad qd il ya une mauvaise distribution des valeurs)
        
    3)Radix sort – algo peut utiliser et compliquer on ne va pas voir son implementation 
        Best, average and worst case time complexity: nk where k is the maximum number of digits in elements of array (cad si base 10 alors il ya 10 digits possible 0...9). 

 
III) differentes notions de sorting : 

    1)In-place/Outplace technique – 
        A sorting technique is inplace if it does not use any extra memory to sort the array. 
        Among the comparison based techniques discussed, only merge sort is outplaced technique as it requires an extra array to merge the sorted subarrays. 
        Among the non-comparison based techniques discussed, all are outplaced techniques. Counting sort uses a counting array and bucket sort uses a hash table for sorting the array. 

    2)Online/Offline technique – 
        A sorting technique is considered Online if it can accept new data while the procedure is ongoing i.e. complete data is not required to start the sorting operation. 
        Among the comparison based techniques discussed, only Insertion Sort qualifies for this because of the underlying algorithm it uses i.e. it processes the array (not just elements) from
        left to right and if new elements are added to the right, it doesn’t impact the ongoing operation. 

    3)Stable/Unstable technique – 
        A sorting technique is stable if it does not change the order of elements with the same value.       
        Out of comparison based techniques, bubble sort, insertion sort and merge sort are stable techniques. Selection sort is unstable as it may change the order of elements with the same 
        value. For example, consider the array 4, 4, 1, 3. In the first iteration, the minimum element found is 1 and it is swapped with 4 at 0th position. Therefore, the order of 4 with 
        respect to 4 at the 1st position will change. Similarly, quick sort and heap sort are also unstable. 
        Out of non-comparison based techniques, Counting sort and Bucket sort are stable sorting techniques whereas radix sort stability depends on the underlying algorithm used for sorting. 

IV) Analysis of sorting techniques : which one to choose
 
    When the array is almost sorted, insertion/Bubble sort can be preferred.
    When order of input is not known, merge sort is preferred as it has worst case time complexity of nlogn and it is stable as well.
    Counting sort: When you are sorting integers with a limited range.
    Bucket sort: When you can guarantee that your input is approximately uniformly distributed.
   

V)Time and Space Complexity Comparison Table :

  Sorting Algorithm	 |                  Time Complexity	               |    Space Complexity
                                                                      
 	                 |     Best Case    Average Case	Worst Case	   |       Worst Case
                                                                      
  Bubble Sort	     |        Ω(N)	        Θ(N2)	      O(N2)	       |          O(1)          in-place, offline, stable
                                                                      
  Selection Sort     |    	  Ω(N2)	        Θ(N2)	      O(N2)	       |          O(1)          in-place, offline, unstable
                                                                                                                                                                              
  Insertion Sort	 |        Ω(N)	        Θ(N2)	      O(N2)	       |          O(1)          in-place, online, stable
                                                                      
  Merge Sort	     |     Ω(N log N)	 Θ(N log N)	    O(N log N)	   |          O(N)          out-place, offline, stable
  
  Heap Sort          |     Ω(N log N)	 Θ(N log N)	    O(N log N)	   |          O(1)          in-place, offline, unstable
  
  Quick Sort	     |     Ω(N log N)	 Θ(N log N)	      O(N2)	       |        O(log N)        in-place (je sais pas pq mais QS est considerer in-place), offline, unstable
  
  Radix Sort	     |       Ω(Nk)	       Θ(Nk)	      O(Nk)	       |        O(N + k)        out-place, offline, stability depend on underlying algo
     
  Count Sort	     |      Ω(N + k)	  Θ(N + k)	     O(N + k)	   |          O(k)          out-place, offline, stable
  
  Bucket Sort	     |      Ω(N + k)	  Θ(N + k)	      O(N2)	       |          O(N)          out-place, offline, stable 
  
   """

"""Bubble Sort: works well with datasets where the items are almost sorted.
l'algo marche de la facon suivante : 
on va a chaque fois comparer les elements adjacents si l'element de gauche est superieur (inferieur si on veut ordre decroissant) a l'element de droite on swap.
a la premiere iteration de i on fait ca jusqu'a le dernier index donc on aura a la fin au dernier index le nombre le plus grand (le plus petit si decroissant), cad on va de range [0,n-1].
a la deuxieme iteration de i on va comparer que le range [0,n-2] car a n-1 on a le max , apres cela a n-2 on aura le 2eme max 
a la 3e iteration de i on va comparer les elements adjacents dans le range [0,n-3]
etc...
a la ne iteration on compare le range [0,1]
le TC est donc O(n^2) car on a 1+2+...+n iteration .

app : nums = [-2 45 0 11 -9]
->i=0 :
   j in range (0,n-i-1) (rappel : n-i-1 n'est pas inclus) cad range (0,4) (4 non inclus):
   - j=0 : if nums[0] > nums[0 + 1]: swap , donc comme -2<45 pas de swap nums[j] et nums[j+1],  nums= [-2 45 0 11 -9]
   - j=1 : if nums[1] > nums[1 + 1]: swap , donc comme 45>0 on swap , nums = [-2 0 45 11 -9]
   - j=2 : if nums[2] > nums[2 + 1]: swap , donc comme 45>11 on swap , nums = [-2 0 11 45 -9]
   - j=3 : if nums[3] > nums[3 + 1]: swap , donc comme 45>11 on swap , nums = [-2 0 11 -9 45] (le max se trouve en dernier position)
->i=1 :
   j in range (0,n-i-1) (rappel : n-i-1 n'est pas inclus) cad range (0,5-1-1)  cad range (0,3) (3 non inclus):
   - j=0 : if nums[0] > nums[0 + 1]: swap , donc comme -2<0 pas de swap,  nums= [-2 0 11 -9 45] 
   - j=1 : if nums[1] > nums[1 + 1]: swap , donc comme 0<11 pas de swap,  nums= [-2 0 11 -9 45] 
   - j=2 : if nums[2] > nums[2 + 1]: swap , donc comme 11>-9 on swap , nums =  [-2 0 -9 11 45] 
->i=2 :
   j in range (0,n-i-1) (rappel : n-i-1 n'est pas inclus) cad range (0,5-2-1)  cad range (0,2) (2 non inclus):
   - j=0 : if nums[0] > nums[0 + 1]: swap , donc comme -2<0 pas de swap,  nums= [-2 0 -9 11 45] 
   - j=1 : if nums[1] > nums[1 + 1]: swap , donc comme 0>-9 on swap,  nums= [-2 -9 0 11 45]  
->i=3 :
   j in range (0,n-i-1) (rappel : n-i-1 n'est pas inclus) cad range (0,5-3-1)  cad range (0,1) (1 non inclus):
   - j=0 : if nums[0] > nums[0 + 1]: swap , donc comme -2>-9 on swap,  nums= [-9 -2 0 11 45] 
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
		

"""Selection Sort:   implementation facile, Pas tres utile , utiliser insertion ou bubble a la place qui sont stable .
Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.
etapes de chaque iteration :
1.Set the first element as minimum.
2.Compare minimum with the second element. If the second element is smaller than minimum, then assign minimum to be the idx of the second element, otherwise do nothing . the compare minimum with third element, and so on...
3. after each iteration (de la boucle exterieur cad de i) the min is placed in front of the list with a swap.
4. la boucle interieur (cad celle de j) a un range [i+1,n) cad [1,n) puis [2,n) puis [3,n) ,..., puis [n,n) (quand on a in range(0,0) alors on rentre pas ds la boucle car 0 est exclu)

app: nums=[ 20 12 10 15 2 ]
(i va de 0 a n-2 donc de 0 a 3)
->i=0
  set the first element as min : min_idx=0  :  nums=[20 12 10 15 2]
                                                      ^
                                                   min_idx
     for j in range [i+1,n) cad [0+1,5) cad [1,5):
     -j=1: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[0] > nums[1] car 20>12 donc le pointeur du min va pointer sur l'index de j : min_idx = 1. nums=[20 12 10 15 2]
                                                                                                                                                                          ^
                                                                                                                                                                       min_idx
     -j=2: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[1] > nums[2] car 12>10 donc le pointeur du min va pointer sur l'index de j : min_idx = 2. nums=[20 12 10 15 2]
                                                                                                                                                                             ^
                                                                                                                                                                          min_idx
     -j=3: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[2] < nums[3] car 10<15 donc le pointeur du min va pas changer : min_idx = 2. nums=[20 12 10 15 2]
                                                                                                                                                                ^
                                                                                                                                                            min_idx                        -j=4: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[2] > nums[4] car 10>2 donc le pointeur du min va pas changer : min_idx = 4. nums=[20 12 10 15 2]
                                                                                                                                                                    ^
                                                                                                                                                                 min_idx 
      on swap le min avec le premier element :  nums[i], nums[min_idx] = nums[min_idx], nums[i] cad nums[0], nums[4] = nums[4], nums[0] donc : nums=[2 12 10 15 20]                         comme on peut le constater a la fin de chaque iteration on a le min en tete de list.               
  
->i=1
  set the first element as min : min_idx=1 : nums=[2 12 10 15 20]
                                                      ^
                                                   min_idx
     for j in range [i+1,n) cad [1+1,5) cad [2,5):
     -j=2: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[1] > nums[2] car 12>10 donc le pointeur du min va pointer sur l'index de j : min_idx = 2. nums=[2 12 10 15 20]
                                                                                                                                                                            ^
                                                                                                                                                                          min_idx
     -j=3: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[2] < nums[3] car 10<15 donc le pointeur du min va pas changer : min_idx = 2. nums=[2 12 10 15 20]
                                                                                                                                                               ^
                                                                                                                                                            min_idx                        -j=4: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[2] < nums[4] car 10<20 donc le pointeur du min va pas changer : min_idx = 2. nums=[2 12 10 15 20]
                                                                                                                                                               ^
                                                                                                                                                            min_idx  
      on swap le min avec le premier element (cad i) :  nums[i], nums[min_idx] = nums[min_idx], nums[i] cad nums[1], nums[2] = nums[2], nums[1] donc : nums=[2 10 12 15 20] 
      
->i=2
  set the first element as min : min_idx=2 :  nums=[2 10 12 15 20]
                                                          ^
                                                       min_idx
     for j in range [i+1,n) cad [2+1,5) cad [3,5):
    
     -j=3: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[2] < nums[3] car 12<15 donc le pointeur du min va pas changer : min_idx = 2. nums=[2 10 12 15 20]
                                                                                                                                                               ^
                                                                                                                                                            min_idx                        -j=4: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[2] < nums[4] car 12<20 donc le pointeur du min va pas changer : min_idx = 2. nums=[2 10 12 15 20]
                                                                                                                                                               ^
                                                                                                                                                            min_idx  
      on swap le min avec le premier element (cad i) :  nums[i], nums[min_idx] = nums[min_idx], nums[i] cad nums[2], nums[2] = nums[2], nums[2] donc : nums=[2 10 12 15 20] 

->i=3
  set the first element as min : min_idx=3 :  nums=[2 10 12 15 20]
                                                            ^
                                                         min_idx
     for j in range [i+1,n) cad [3+1,5) cad [4,5):
    
     -j=4: if nums[min_idx] > nums[j]:  min_idx = j ; donc comme nums[3] < nums[4] car 15<20 donc le pointeur du min va pas changer : min_idx = 2. nums=[2 10 12 15 20]
                                                                                                                                                                  ^
                                                                                                                                                              min_idx  
      on swap le min avec le premier element (cad i) :  nums[i], nums[min_idx] = nums[min_idx], nums[i] cad nums[3], nums[3] = nums[3], nums[3] donc : nums=[2 10 12 15 20] 
      

TC : comme on peut voir le range de j est [0,n] , [1,n], [2,n], ..., [n-1,n] cad il ya n+(n-1)+(n-2)+...+1 iteration soit 1+2+3+..+n iterations donc n^2
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # Traverse through all array elements
        for i in range(n-1):	       # Find the minimum element in remaining unsorted array      
            min_idx = i
            for j in range(i+1, n):
                if nums[min_idx] > nums[j]:
                    min_idx = j                    
			# Swap the found minimum element with the first element	
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums
  
        

"""Insertion Sort: use when data almost sorted. this is the only sorting algo that we can add data to it while running whitout restarting the algo.

l'algo marche de la facon suivante il ya une partie qui est sorted (le cote droit qui sera jusqu'a l'idx  j) et une partie qui ne l'ai pas (le cote gauche qui commence a l'idx i 1
idx apres j la valeur de l'idx i est key ), au debut le premier element est considerer sorted tout le reste non-sorted. l'algo prend a chaque iteration le premier element de la 
partie non sorted (key) et il le compare avec les elements de la partie sorted , tant que cette element (key) est inferieur au element de la partie sorted on deplace ces elements 
d'une place vers la droite, si key est superieur a un element ou qu'il est inferieur a tout les elements alors on peut mettre key a la place du dernier element deplacer. a la fin de chaque 
iteration le cote sorted gagne un element alors que le cote non-sorted en perd un (il perd le premier element qui etait a l'index i c'est pour cela que a la prochaine iteration i pointe sur
l'index d'apres). 

app : nums= [12 11 13 5]
i est l'idx du premier elements non-sorted de chaque iteration , i est dans le range [1,n) (on commence par 1 car l'idx 0 est considerer comme sorted au debut)
j est l'idx du dernier element sorted de chaque iteration , j peut aller du range i-1 a 0 (step -1)

->i=1 : 
        key=nums[i] cad key=nums[1] cad key=11          # (1)  (ce referencer au code) 
        
        j=i-1 cad j=1-1 cad j=0             #(2)
        
        donc nums= [12 | 11 13 5]   donc on compare 11 (key) avec les elements deja sorted (cad jusqu'a j)    ('|' fait la separation entre la partie sorted est non-sorted)
                    ^     ^
                    j     i
                    
        while j==0 >= 0 and key==11 < nums[j==0]:                  #(3)
              nums[j+1==1] = nums[j==0]   cad nums[1]=12                    #(4)
              j -= 1    cad  j=-1  donc on refait pas la boucle car j<0                 #(5)
        
        donc on a nums=[12,12,13,5]  en sortant du while
        
        ensuite on mait key a ca place cad apres avoir fini le while j va etre egale a -1 ou j va etre egale a l'idx d'un element superieur a key donc ds ces 2 cas pour avoir l'idx du dernier 
        membre deplacer il faut faire j+1 donc :
        
        nums[j + 1] = key  ,ici j=-1 donc nums[0]=11                        # (6)
        
        donc on obtient nums= [ 11 12 | 13 5 ]
                               sorted  non-sorted
-> i =2 :
        key=nums[i] cad key=nums[2] cad key=13          # (1)  (ce referencer au code) 
        
        j=i-1 cad j=2-1 cad j=1             #(2)
        
        donc nums= [11 12 | 13 5]   donc on compare 13 (key) avec les elements deja sorted (cad jusqu'a j)
                       ^    ^
                       j    i
        
        puisque key==13 > nums[j==1] donc on ne rentre pas dans le while car ca veut dire que key est sup a tout les elements a sa gauche donc key est sorted .    #(3)-#(5)
        
        nums[j+1]=key ici ca change rien car on a pas deplacer le j donc j=i-1 donc j+1==i donc nums[j+1]==nums[i] donc nums[j+1]=key revient ici a dire nums[i]=nums[i] cad ca change rien.  #(6)
        
        donc on obtient nums= [ 11 12 13 | 5 ]
                                 sorted   non-sorted
                                 
-> i =3 :
        key=nums[i] cad key=nums[3] cad key=5          # (1)  (ce referencer au code) 
        
        j=i-1 cad j=3-1 cad j=2             #(2)
        
        donc nums= [11 12 13 | 5]   donc on compare 5 (key) avec les elements deja sorted (cad jusqu'a j)
                           ^   ^
                           j   i
        
        tant que key est inf au element de gauche on deplace d'une place c'est element:    #(3)-#(5)
        cad while j >= 0 and key < nums[j] on fait nums[j + 1] = nums[j]  et j-=1 donc ici :
        j==2 : 2>=0 and 5<13 donc nums[3]=13 donc on obtient nums = [ 11 12 13 13 ]  , j-=1 cad j==1,
        j==1 : 1>=0 and 5<12 donc nums[2]=12 donc on obtient nums = [ 11 12 12 13 ]  , j-=1 cad j==0,
        j==0 : 0>=0 and 5<11 donc nums[1]=11 donc on obtient nums = [ 11 11 12 13 ]  , j-=1 cad j==-1,
        j==-1 : -1<0 adonc on sort du while
        
        nums[j+1]=key cad nums[0]=5 donc on obtient nums = [ 5 11 12 13 |]  .  #(6)
                                                              sorted
        
TC analyse : comme i du for exterieur va de 1 a n et j du while interieur peut aller de i-1 a 0 cad que a chaque i il ya i-1+1 iteration , donc pour i=1 il 1 iteration pour i=2 
2 iterations,..., pour i=n-1 il ya n-1 iteration cad on obtient donc 1+2+3+..+n iterations donc O(n^2)
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
         
        for i in range(1, len(nums)):                      
            key = nums[i]                                 # (1)                          
            j = i-1                                       # (2)
            # cad tant que j est pas neg car il ya pas d'idx neg , et tant que key qui est le 1er element non sorted est inferieur a nums[j] (element sorted) alors:
            while j >= 0 and key < nums[j] :              # (3)  
                    # on deplace nums[j] vers la droite cad un idx de plus
                    nums[j + 1] = nums[j]                 # (4)  
                    # on recule l'idx j 
                    j -= 1                                # (5)                 
            nums[j + 1] = key                             # (6)                                                  
        return nums
	
		
"""Merge Sort: Merge sort is fast in the case of a linked list. it is the fastest stable Comparison based sorting algo. on off the most popular sorting algo.

This program uses a recursive Divide and Conquer approach to sort the original list. The recursive function mergesort is called on the original list. The function divides the list into two halves
(a left half and a right half) and calls the mergesort routine recursively on each of them. The mergesort function recursively calls on lists that are half the size of the previous list until 
their length is 1, such a list is trivially sorted (car elle contient qu'un element) . puisque toute les list sont trier maintenant on utilise une fct merge qui sait comment fusionner 2 sorted
list en une sorted list. After that all the small lists are merged back into larger lists until the final sorted version of the original list is formed.
donc en conclusion on appele la fonction mergesort de facon recursive j'usqu'a ce qu'on obtient des ist d'un seul element puis en remontant de la recursion on utilise une fonction merge qui va
fusionner 2 sorted list en une.

la fonction merge fonctionne de la facon suivante : il ya 3 pointeurs 1 pointeurs pour chaqu'une des deux list et un pour la list ou vont etre fusionner les elements . on compare donc les current 
element des deux list, le plus petit d'entre eux va etre copier dans la 3eme list. puis on avance le pointeur de la 3eme list et de la list qui avait le current element le plus petit. si on a 
fini de lire une des deux list il suffit de copier dans la 3eme list tous les elements de l'autre list. 
app de merge :  l1=[1 5 10]  l2=[6 9] sorted=[], on a 3 pointeurs i j et k tous egale a 0 au debut donc :
l1=[1 5 10]  l2=[6 11 12 13] sorted=[        ]   puisque l1[i]<l2[j] cad l1[0]<l2[0] cad 1<6 donc sorted[k]=l1[i] cad sorted[0]=l1[0] cad sorted[0]=1, on avance i et k donc :
    ^            ^                    ^
    i            j                    k 
l1=[1 5 10]  l2=[6 11 12 13] sorted=[1       ]   puisque l1[i]<l2[j] cad l1[1]<l2[0] cad 5<6 donc sorted[k]=l1[i] cad sorted[1]=l1[1] cad sorted[1]=5,on avance i et k donc :
      ^          ^                     ^
      i          j                      k  
l1=[1 5 10]  l2=[6 11 12 13] sorted=[1 5     ]   puisque l2[j]<l1[i] cad l2[0]<l1[2] cad 6<10 donc sorted[k]=l2[j] cad sorted[2]=l2[1] cad sorted[2]=6, on avance j et k donc :
        ^        ^                       ^
        i        j                       k 
l1=[1 5 10]  l2=[6 11 12 13] sorted=[1 5 6    ]   puisque l1[i]<l2[j] cad l1[2]<l2[1] cad 10<11 donc sorted[k]=l1[i] cad sorted[3]=l1[2] cad sorted[3]=10,on avance i et k donc :
        ^          ^                       ^
        i          j                       k 
l1=[1 5 10]  l2=[6 11 12 13] sorted=[1 5 6 10    ]   puisque i>len(l1)-1 donc on a fini l1 n peut donc copier tout les lements de l2 ds sorted : sorted=[1 5 6 10 11 12 13]
           ^       ^                          ^
           i       j                          k
           



 schema explicatif de merge sort : 
    
                                              [ 6 5 12 10 9 1 ]                                    |                     
                                           /                    \                                  |                                                    
                                          /                      \                                 |                        
                                [ 6 5 12 ]                        [ 10 9 1 ]                       |    appel recursive de mergesort                                                        
                                /        \                        /        \                       |                
                               |        [5 12]                   |        [9 1]                    |            
                               |        /    \                   |        /   \                    V                                   
                              [6]     [5]   [12]               [10]      [9]  [1]                      
                                \       \    /                   \        \    /                   |                                            
                                 \      [5 12]                    \        [1 9]                   |                                      
                                  \       /                        \        /                      |    retour de la recursion : appel de la fonction merge                                  
                                   [5 6 12]                         [1 9 10]                       |                                
                                           \                       /                               |                         
                                            \                     /                                |                    
                                               [ 1 5 6 9 10 12 ]                                   V    

TC:  Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 
T(n) = 2T(n/2) + θ(n)  (car a chaque recursion on appel recurssivement la fonction 2 fois 1 fois sur chaque moitier et on utilise merge qui coute O(n) ). la fonction a chaque iteration divise en 2 l'input , donc il ya en tout log n iteration chaque itration coute O(n) car elle utilise merge donc on a en tout O(n*logn)

SC: comme on copy nums dans L et R au max on copie tout nums donc O(n)
""" 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: 
        
        if len(nums) > 1:  #len est sup a 1 (condition d'arret)
            mid = len(nums)//2
            L = nums[:mid]   #copie de la 1er partie  
            R = nums[mid:]   #copie de la 2e partie
            # on copie car apres on va modifier nums donc on doit garder les elements originaux de nums ds L et R
            
            self.mergeSort(L)
            self.mergeSort(R)
            
            ### retour de la recursion on fait merge :
            i = j = k = 0
            # Until we reach either end of either L or M : on choisi le plus petit entre L[i] et R[j] et on le rajoute a nums[k],on avance ensuite i ou j (ca depend qui est min) et k :
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i]  # remarque: on s'en fou de ce qu'il ya dans nums[k] avant car on a copier les elements de nums dans L et R et on travail sur eux et pas sur nums, 
                                    # donc on utilise nums[k] pour le resultat de merge  .
                    i+=1            
                else: # si R[j]<=L[i] 
                    nums[k] = R[j] 
                    j+=1
                k+=1
                
            # on copie ce qui reste de L ou de R
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1		

"""heap sort :  When you don't need a stable sort and you care more about worst case performance than average case performance. It's guaranteed to be O(N log N), and uses O(1) auxiliary space

heap sort algorithm requires knowledge of two types of data structures - arrays and complete binary trees.

->COMPLETE BINARY TREE:
    
    quelque rappel dans un binary tree: 
    -le nbr maximum de nodes d'un niveau h est 2^h + 1 si on considere le premier niveau comme 1 si on considere comme 0 alors 2^(h+1) + 1.
    -la hauteur minimal d'un binary tree est O(log n)

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
                                                                                                                                                
-> HEAP also called binary heap: 
   
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

  
  - HEAP SORT : 
    on doit tout d'abord transformer l'array en un max-heap. apres l'avoir fait on a forcement le max de l'array en tete donc on va swap le root cad l'idx 0 qui est le max avec le derniere index.
    donc en dernier position on a le max donc maintenant on va s'occuper de rearranger l'array en un max heap du range [0,n-2] car n-1 qui est le dernier index est le max deja . pour cela on fait
    heapify que sur la partie [0,n-2] ,heapify recoit 3 parametre la list, la taille de la list qui sera prise en compte par heapify (cad on peut prendre en compte que une partie de la list 
    comme ci le reste n'existait pas, remarque on parle de la taille donc le dernier idx pris en charge est taille -1 ) et le 3e parametre et l'index du membre sur lequel on fait heapify. 
    donc on va faire appel a heapify(nums,n-1,0) , explication : n-1 c'est la taille donc le dernier idx pris en charge c'est n-2 (car on commence a 0) et le 0 c'est l'idx du root car il a etait 
    echanger avec le dernier elements donc il faut faire heapify pour creer un nouveau max heap. apres le heapify on a donc un nouveau max en tete on va le mettre a la fin cad a l'idx n-2 et on
    va faire heapify(nums,n-2,0) (n-2 c'est la taille le dernier idx c'est n-3), ce qui nous donne un nouveau max donc on met le max a la fin cad l'idx n-3 puis on fait heapify(nums,n-3,0), etc..
    donc l'idee en faite est de swap le root avec le dernier element cad swap(array[0],array[len(array)-1]) et de faire heapify du nouveau root sur [0,len(array)-1], puis
    swap(array[0],array[len(array)-2]) et heapify du nouveau root sur [0,len(array)-2] , puis swap(array[0],array[len(array)-3]) et heapify du nouveau root sur [0,len(array)-3] etc.. jusqu'a 
    le dernier swap : swap(array[0],array[1]) et heapify du nouveau root sur [0,1] . donc c'est pour cela que dans le code le 2e for va de n-1 a 0 (0 n'est pas inclus).
    
    app :  nums = [2 5 4 8 9 10 11] 
    ~ tout d'abord on construit un max heap en fesant heapify en commencant par l'idx n/2-1 cad de n//2 jusqu'a 0 inclus :
    for i in range(n//2, -1, -1):
                self.heapify(nums, n, i) 
    ca donne :
             2                 11                 
           /   \             /   \               
          5     4    =>     9    10        (pour voir tout le processus voir l'exemple d'avant)    cad nums =[11 9 10 8 5 2 4] 
         / \   / \         / \   / \            
        8   9 10 11       8   5 2   4    
    ~ maintenant on extrait a chaque fois le max en le metant a la fin puis on rearrange  :
    for i in range(n-1, 0, -1):      # i est l'idx du dernier elements pris en compte 
                nums[i], nums[0] = nums[0], nums[i]
                self.heapify(nums, i, 0) 
    ca donne :
    - i=n-1 cad i=6  : nums =[11 9 10 8 5 2 4]  , swap(nums[6], nums[0]) donc nums =[4 9 10 8 5 2 11], puis on fait heapify(nums,i,0) cad heapify(nums,6,0)  (6 est la taille le dernier idx 
      pris en charge est donc 5) cad on prend en compte seulement [4 9 10 8 5 2] donc ca donne nums=[10 9 4 8 5 2 | 11]. (je sais que ca donne ca car j'ai dessiner le CBT du nums et j'ai heapify le 
      root)
    - i=n-2 cad i=5  : nums = [10 9 4 8 5 2 11]  , swap(nums[5], nums[0]) donc nums =[2 9 4 8 5 10 11], puis on fait heapify(nums,i,0) cad heapify(nums,5,0)  (5 est la taille le dernier idx 
      pris en charge est donc 4) cad on prend en compte seulement [2 9 4 8 5] donc ca donne nums=[9 8 4 2 5 | 10 11].                                                      
    - i=n-3 cad i=4  : nums = [9 8 4 2 5 10 11]  , swap(nums[4], nums[0]) donc nums =[5 8 4 2 9 10 11], puis on fait heapify(nums,i,0) cad heapify(nums,4,0)  (4 est la taille le dernier idx 
      pris en charge est donc 3) cad on prend en compte seulement [5 8 4 2] donc ca donne nums=[8 5 4 2 | 9 10 11]. 
    - i=n-4 cad i=3  : nums = [8 5 4 2 9 10 11] , swap(nums[3], nums[0]) donc nums =[2 5 4 8 9 10 11], puis on fait heapify(nums,i,0) cad heapify(nums,3,0)  (3 est la taille le dernier idx 
      pris en charge est donc 2) cad on prend en compte seulement [2 5 4] donc ca donne nums=[5 2 4 | 8 9 10 11].
    - i=n-5 cad i=2 : nums =[5 2 4 8 9 10 11] , swap(nums[2], nums[0]) donc nums =[4 2 5 8 9 10 11], puis on fait heapify(nums,i,0) cad heapify(nums,2,0)  (2 est la taille le dernier idx 
      pris en charge est donc 1) cad on prend en compte seulement [4 2] donc ca donne nums=[4 2 | 5 8 9 10 11].
    - i=n-6 cad i=1 : nums =[4 2 5 8 9 10 11] , swap(nums[1], nums[0]) donc nums =[2 4 5 8 9 10 11], puis on fait heapify(nums,i,0) cad heapify(nums,1,0)  (1 est la taille le dernier idx 
      pris en charge est donc 0) cad on prend en compte seulement [2] donc ca donne nums=[2 | 4 5 8 9 10 11]. on a fini notre array est sorted
      
      
TC : O(n*logn). La premier boucle (max heap built) coute O(n) voir la remarque en bas. 
     [ Dans la deuxieme boucle on fait heapify(nums, n-1, i) ,puis heapify(nums, n-2, i) , puis heapify(nums, n-3, i) ,puis heapify(nums, n-4, i) ,..., puis heapify(nums, 1, i) .
     donc on aurait dit qu' on fait log(n-1)+log(n-2)+log(n-3)+...+log(1) cad log((n-1)*(n-2)*(n-3)*...*1) cad log(n!) , donc on a TC = O(n*logn)+O(log(n!)) mais comme O(log(n!)) < O(n*logn) 
     (car log(n!)==log(1) + log(2) + ... + log(n) <= log(n) + log(n) + ... + log(n)== n*log(n)) donc on a TC = O(n*logn) . mais ce raisonnement n'est pas vrai car log n fait reference a la 
     hauteur de l'arbre or cette hauteur ne ce modifie pas a chaque etape elle se modifie quand on change de niveau , donc faire log(n-1) puis log(n-2), etc.. c'est faux ] . 
     dans la deuxieme boucle pour faire le sort(trie) on retire le max a chaque fois et on le remplace par le dernier element de l'arbre puis on fait heapify sur le nouveau root , dans ce cas
     forcement que on peut dans le pire des cas descendre tout la hauteur dans l'arbre jusqu'au racine . on sait que dans l'arbre il y'a 2 ^h -1 nodes pour un niveau h donnee , 
     un CBT a chaque niveau a : 1+2+4+8+16+32... donc le dernier niveau est constituer de n/2 nodes puis celui au dessus n/4 puis n/8 etc.. . donc disons h et la hauteur maximal de l'arbre 
     donc le nombre total d'iteration est : (h * n/2) + ((h-1) * n/4) + ((h-2)*n/8) + ... + (0 * 1), or (h * n/2) est egale a O (log n) (car la hauteur est log n dans un CBT) fois n/2 donc 
     O(nlogn) puis apres c'est O(n/4 log n/2) puis O(n/8 log n/4) ... ca revient a O(nlogn) car (h * n/2) constitue deja la moitier des iteration les autres sont bcp plus petit a chaque fois
     (si on regarde un CBT 90% des nodes sont dans les 3 dernier niveau : n/2+n/4+n/8= 0.875n, donc la complexity des derniers niveau est bcp plus grande que ce d'en haut donc ici c'est pas
     comme avoir n+n-1+n-2 ... iteration ici on a  O(n/2logn) + O(n/4 log n/2) + O(n/8 log n/4) ... iteration ca descend bcp plus vite donc on considere que c'est que O(n/2logn) 
     (c'est comme si on a O(1000+ 500+250+125+75+37.5+...) toute la partie apres 1000 sera egale max a 1000 donc on a en tout 2*1000 donc O(1000) c'est pour cela qu'ici on considere O(nlogn) 
     et on prend pas en compte le reste).
     donc au finale on a O(n+nlogn) cad O(nlogn). 
     
     remarque super importante  : 
     construire un heap (on parle a l'aide d'un heapify sur tout les nodes qui sont pas leaf et pas de faire a chaque fois insert car ca sa coute O(nlogn)) coute O(n) et non O(n*logn)! 
     car bien que en generale heapify on le considere comme O(log n) mais quand on fait un heapify pour construire un heap alors ca coute pas a chaque fois log n car le dernier niveau 
     les leaf on touche pas puis l'avant dernier niveau qui a 2^(h − 1) nodes peux descendre max d'un nivau donc 1*2^(h − 1) iterations, celui en haut qui a 2^(h − 2) nodes peut descendre 
     max de deux niveaux donc 2*2^(h − 2) iterations, celui encore en haut a max 2^(h − 3) nodes et peut descendre max 3 niveaux donc 3*2^(h − 3) , etc .. 
     il ya une preuve mathematique comme quoi c'est O(n) pour plus de details voir cette article : https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: 

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
        
        def heapSort(self, nums):            
            n = len(nums) 
            # Build max heap cost O(n) voir remarque en haut
            for i in range(n//2, -1, -1):   
                self.heapify(nums, n, i) 
                
            # One by one extract elements   cost O(nlogn) voir remarque TC analyse en haut
            for i in range(n-1, 0, -1):              # i est l'idx du dernier elements pris en compte 
                nums[i], nums[0] = nums[0], nums[i]
                self.heapify(nums, i, 0) 

            return nums


"""QuickSort: when you d'ont need stable algo use it , Quick Sort in is an in-place sort (i.e. it doesn’t require any extra storage) so it is appropriate to use it for arrays.  A good
implementation uses O(log N) auxiliary storage in the form of stack space for recursion.
This program uses a recursive Divide and Conquer approach to sort the original list. A partition subroutine picks an element as pivot , there are many different versions of quickSort that pick pivot in different ways : 
-Always pick first element as pivot.
-Always pick last element as pivot (implemented below)
-Pick a random element as pivot.
-Pick median as pivot.
the partition subroutine then uses swaps to place numbers less than the pivot value to the left of the pivot index and numbers greater than the pivot value to the right of the pivot index. 
At the end of the partition subroutine, we are left with the situation that the value at the pivot index is located at what will be its final position in the sorted output. We then do a
quicksort on these left and right halves and continue this rescursively until we get a list of length 1 which is already sorted. Once all of the quicksort subroutines are completed, 
the entire list is in sorted order and the initial quicksort call completes and we can return the sorted list. In the average case, this method is O(n log n). In the worst case, however,
it is O(n²). 
je ne suis pas rentrer trop dans les details car effort/recompanse faible , pour plus de details et application voir : https://www.programiz.com/dsa/quick-sort"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # function to find the partition position
        def partition(array, low, high):
           # choose the rightmost element as pivot
           pivot = array[high]
           # pointer for greater element 
           i = low - 1

              # traverse through all elements
              # compare each element with pivot
          
           for j in range(low, high):
                if array[j] <= pivot:
                    # if element smaller than pivot is found
                    # swap it with the greater element pointed by i
                    i = i + 1

                    # swapping element at i with element at j
                    (array[i], array[j]) = (array[j], array[i])

           # swap the pivot element with the greater element specified by i
           (array[i + 1], array[high]) = (array[high], array[i + 1])

           # return the position from where partition is done
           return i + 1

        # function to perform quicksort
        def quickSort(array, low, high):
            if low < high:
                # find pivot element such that
                # element smaller than pivot are on the left
                # element greater than pivot are on the right
                # le pivot est une valeur a la fin de partition cette valeur va etre dans la bonne place (celle qu'elle aura ds la sorted array) cette place est l'idx rendu par partition ,
                # donc pi sera l'idx de la valeur pivot dans ca position finale cad celle qu'elle aura ds la sorted array. 
                pi = partition(array, low, high)

                # recursive call on the left of pivot
                quickSort(array, low, pi - 1)

                # recursive call on the right of pivot
                quickSort(array, pi + 1, high)
        
        # ---------------------------------------    
        quickSort(nums,0,len(nums)-1)
        return nums
    
		
"""Counting Sort: sorting lineaire . on l'utilise quand le plus grand nbr a trier k n'est pas bcp plus grand que la taille n de l'array.
Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array. The count is stored in an auxiliary array. 
il ya deux facons de le faire la facon traditionelle qui doit etre modifier pour marcher avec des elements negatif cette facon a a mon avis un TC plus grand que la deuxieme (meme si au final
meme big-O)et est plus compliquer a comprendre que la deuxieme. pour voir la premiere version regarder le link suivant (on va pas s'attarder dessus rapport effort/recompance faible) :
https://www.geeksforgeeks.org/counting-sort/  (voir le deuxieme code de l'article pour nombre neg).
la deuxieme facon qui est bcp plus simple a comprendre et peux aussi etre plus rapide et plus economique en space (car on creer un dictionnaire qui store que les valeurs existante dans l'array 
et on ne creer pas un array de la taille max-min alors que des valeurs ne sont meme pas forcement utiliser). 
tout simplement on va compter la frequence de chaque elements et on va la garder dans un dict : key=value et val=frequence .
apres on fait une boucle qui va de min(array) a max(array) (cad on parcours tout les valeurs possibles de l'array) et qui va copier freq[val] fois la valeur dans l'output.  
TC : O(n+k)
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        freq = collections.Counter(nums)     #TC O(n) pour compter la frequence et SC O(n) car si tout les elements sont diff
        mini=min(nums)
        maxi=max(nums)
        output=[]  #SC O(n) a la fin car output va etre nums sorted
        for val in range(mini,maxi+1):   # maxi+1 pour inclure maxi
            for _ in range (freq[val]):     # freq[val] vaut max len(nums) si il ya que une valeur dans nums mais dans ce cas la boucle exterieur a qu'une iteration car il y'a qu'une valeur 
                output.append(val)   # append cout O(1)
        return output

