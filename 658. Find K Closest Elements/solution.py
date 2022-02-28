"""#premiere solution: BS+two pointers #TC O(log(n)+k)  #SC O(1))
l'idee est de faire un binary search qui va trouver l'idx de l'element le plus proche de x , cette element peut etre x ou pas . exemple si arr = [1,3,5,8,10] et x=3 alors BS va me donner l'idx 1 qui est l'index de 3 , 
si x=7 alors BS va me donner l'idx 3 aui est l'index de 8 , si x=12 alors BS va donner l'index de 10 cad 4 , si x=-3 alors BS va me donner l'idx de 1 cad 0. 
ce binary search a un cout de O(log(n)). ensuite une fois qu'ona cette element on utilise deux poiteur qui nous donnerons la fenetre reponse . les deux pointeur left et right seront au debut initialiser a etre :
left=BS result idx - 1 (cad 1 avant ce qu'on a trouver a l'aide du BS left peut donc etre egale a -1 si BS nous donne l'idx 0) right = BS result idx. ensuite on trouve qui est le plus proche de x : arr[left] ou 
arr[right] si arr[left] est plus proche alors left=left-1 si arr[right] est plus proche alors right= right+1 . cette operation se fait k fois car on doit trouver les k element les plus proche de x donc O(k).
au total on a un cout de O(log(n)+k) 
app :
      arr = [0,3,5,8,10] et x=3  k=2
               ^
             BS result 
             
      [0,3,5,8,10]
       ^ ^
    left right
    
     [0,3,5,8,10]    since |5-3|<|0-3|
      ^   ^
    left right
    
     [0,3,5,8,10]    since |0-3|<|8-3|
    ^     ^
  left   right
  
  since right-left=2-(-1)==3>k=2 so the result is arr[left + 1:right]=arr[0:2]=[0,3]
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Find the closest element and initialize two pointers
        right = bisect_left(arr, x)   
        left = right - 1

        # until windows size is equal to k
        while right - left <= k:   
            # Be careful to not go out of bounds : if no more possibility to go left then go right only
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]  
    
"""il y'a une deuxieme solution qui est moins intuitive : 
l'idee est de trouver le cote gauche de la fenetre une fois trouver on return simplement : arr[left:left + k]
par exemple si je sais que [1,3,4,5,6] avec k=2 alors la reponse va etre [3,4]
                              ^
                             left
mon left peut se situer entre 0 et len(arr)-k car si left est superieur a len(arr)-k alors il y'aura pas assez de k nombre plus proche de x (ex si j'ai [1,2,3,4] avec k=3 et mon left est a l'index 2 alors la fentre 
[left:left+3] est hors range il ya pas assez d'element dans arr). en partant de cette idee on va juste faire un binary search entre 0 et len(arr)-k pour trouver left comme ca on a la reponse . le cout de l'operation
est donc O(log(n-k)). le BS marchera de la facon suivante : At each operation, calculate mid = (left + right) / 2 and compare the two elements located at arr[mid] and arr[mid + k]. If the element at arr[mid] is closer 
to x, then move the right pointer:right = mid . If the element at arr[mid + k] is closer to x, then move the left pointer: left = mid + 1 . Remember, the smaller element always wins when there is a tie.
                          
                             """


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described    # cost O(log(n-k))
        while left < right:           
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]   # cost O (k)
