"""
apres une rotation il ya toujours au moins un cote qui est sorted :

[3, 4, 5, 6, 7, 1, 2]
-> [3, 4, 5] [ 6, 7, 1, 2]
the left side remains sorted

[6, 7, 1, 2, 3, 4, 5]
-> [6, 7, 1] [2, 3, 4, 5]
the right side remains sorted

[1, 2, 3, 4, 5, 6, 7]
-> [1, 2, 3] [4, 5, 6, 7]
Both sides remain sorted.

un cote est sorted si extrem gauche < extrem droite (car ici ordre croissant) (ex [6, 7, 1, 2, 3, 4, 5]-> [6, 7, 1] [2, 3, 4, 5] 6 !< 1 donc [6, 7, 1] pas sorted ). on verifie donc si le target se trouve dans le cote 
sorted , si oui on prendra ce cote si non on choisira l'autre cote.puis on refait la meme chose jusqu'a que A[mid]==targer ou que left>right et ca retournera -1

""" 

class Solution:
    def search(self, A: List[int], target: int) -> int:
        n = len(A)
        left, right = 0, n - 1
       
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                return mid         
            # Check if the left side is sorted
            if A[left] <=A[mid] :
                if A[left] <= target < A[mid]:
                    # target is in the left
                    right = mid - 1
                else:
                    # target is in the right
                    left = mid + 1
                    
            # Otherwise, the right side is sorted
            else:
                if A[mid] < target <= A[right]:
                    # target is in the right
                    left = mid + 1
                else:
                    # target is in the left
                    right = mid - 1
            
        return -1
