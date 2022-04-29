"""cette question est interressante pour comprendre comment les class marchent """
"""remarque: comme on peut le voir a la fin du code les deux vecteurs sont instancier a l'aide du constructeur definie dans notre class"""

"""# 1er solution # non-optimal solution (the sparse vectore is not efficiently stored in the memory)  # TC O(n)   # SC O(1)"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = nums
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        # on passe sur tout les index meme ceux dont la valeur a cette idx est 0 
        for i in range(len(self.array)):   # rappel: self fait reference a l'object qui appel la fct 
            res += self.array[i] * vec.array[i]
        return res 
      
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

"""#2e sol # optimal #TC O(n) for creating the idx_val list (n its all the vectors elements ) ,It takes O(L1 + L2) for the two pointers walk through (L1 and L2 size of the
2 lists of pairs of each vec).
# O(L) for storing the L non-zero elements. 
on va utiliser une liste qui va garder les paires (idx,val) que lorsque la valeurs est differente de 0 .
puis on passe sut les liste pour faire le produit des idx qui sont les memes. """


class SparseVector:
    
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append((index, value))
                
    # ou : def __init__(self, nums: List[int]):
    #          self.pairs = [(idx, num) for idx, num in enumerate(nums) if num != 0]
    
    def dotProduct(self, vec: 'SparseVector') -> int:

        res = p = q = 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]: # si il ont le meme idx alors on les multiplie
                res += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            # si l'index n'est pas egale alors on doit avancer l'idx le plus petit 
            elif self.pairs[p][0] < vec.pairs[q][0]:  # si idx du vecteur qui a appeler est plus petit que l'idx du vecteur parametre 
                p += 1
            else:       # si self.pairs[p][0] >= vec.pairs[q][0]:
                q += 1

        return res

      
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

""" #follow up #binary search  # TC O( l1 * log(l2) )  # SC O(n) car on garde une array de paires donc si il ya pas de 0 la taille de cette array est n (taille de l'array nums).
ce follow up est tres demander chez facebook de meme que la question de base (la solution voulue a la question de base est la sol 2) (la solution ici proposer est la solution
voulue chez facebook pour le follow up).

follow up : 
What if only one vector is sparse and the other is full of non-zero values?
on utilisera aussi une liste de paires (idx,val) mais cette fois a la place de parcourir tout les idx jusqu'a ce qu'on trouve les memes idx dans les 2 list on va utiliser un
binary search qui va chercher les idx de la sparse vector dans le vecteur qui n'est pas sparse. (vu qu'il y'a moins d'idx dans la sparse vector que dans l'autre car il ya plus de 0 donc
le sparse vector est le vector le plus petit)
ex :
sparse_vec = [(5, 2), (7, 8)]
full_vec = [(1, 2), (2, 4), (3, 5), (4, 6), (7, 19)]
We do binary search to find the idx position 5 in full_vec, since there isn't a tuple with idx = 5 we return 'inf' indicating none valid idx found.
We do binary search to find the idx position 7 in full_vec, we successfully find the tuple with idx = 7 in full_vec has the val = 19. We do res += 8 * 19.

TC analyse : soit l1 la taille du sparse vector (cad la taille du array qui contient les paires) et l2 la taille du non-sparse vector (cad la taille du array qui contient les paires) ,
pour chaque paire dans le sparese vector on chaire une paire dans le non-sparse vector, on cherche l1 paire dans le non sparse vector de taille l2 , cad on doit faire l1 binary search dans 
le non sparxe vector de taille l2 . Dans le non sparse vector chaque binary search coute O(logn) comme on doit en faire l2 fois donc TC = O( l1 * log(l2) ). 
(comme on peut foir on a une boucle for qui parcours le sparse vector donc l1 interaction et a chaque interaction on fait un binary searh dans le non-sparse vector ce qui coute O(log(l2))
donc en tout la boucle coute O(l1*log(l2)). )

"""

class SparseVector:
    
    def __init__(self, nums: List[int]):
        self.pairs = [(idx, num) for idx, num in enumerate(nums) if num != 0]
    
    def dotProduct(self, vec: 'SparseVector') -> int:

        # trouver le sparse vector ---------------------------------------
        # le sparse vecteur est forcement le plus petit donc :
        sparseVec = None
        if len(self.pairs) < len(vec.pairs):
            sparseVec = self 
            notSparseVec = vec 
        else :
            sparseVec = vec 
            notSparseVec = self
        #-------------------------------------------------------------------
        
        # chercher les valeurs dans la non-spare vector qui on les meme idx que les idx du sparse vector , 
        # puis faire le produit val1*val2 (avec (idx,val1) appartenant au sparse vector et (idx,val2) appartenant au non sparse vector. idx est le meme dans les deux paire)
        res= 0
        for pair in sparseVec.pairs :  # on parcours tout les paires du sparse vector 
            # val est la valeur de l'idx ds le vecteur qui n'est pas sparse si cette idx existe pas dans notSparseVec alors val = inf
            val = self.binarySearch(notSparseVec, pair[0])  #on cherche la paire dans le non-sparse vector qui a le meme idx que la paire actuelle du sparse vector
            res += val * pair[1] if val != float('inf') else 0  #on fait le dot product que si une paire du non-sparse vector a le meme idx que la paire actuelle du sparse vector 
        return res
    
    # on utilise binary search car les idx sont forcement ordonner puisque c'est des idx 
    def binarySearch(self,vec,target_idx) :    # cost O(log(size array where we look for the target element))
        start, end = 0, len(vec.pairs) - 1
    
        while start <= end: 
            mid = (start + end) // 2 

            if vec.pairs[mid][0] == target_idx: 
                return vec.pairs[mid][1] # return val qui a le meme idx de la target 
            
            elif vec.pairs[mid][0] > target_idx:  #cad la target ce trouve avant la paire actuelle 
                end = mid -1
                
            else:     #cad la target ce trouve apres la paire actuelle 
                start = mid + 1 
        
        return float('inf')  # si il ya pas de valeur avec le target_idx alors return inf

      
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
