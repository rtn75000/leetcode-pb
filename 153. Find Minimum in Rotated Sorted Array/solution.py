"""pb ressamblant : https://leetcode.com/problems/search-in-rotated-sorted-array/"""

"""#binary search  #TC O (log n) car BS  #SC O(1)
l'array est sorted dans l'ordre croissant donc nums[i]<nums[i+1] ici on doit trouver ce qu'on appel le point pivot cad le point ou il ya le changement d'ordre cad  ou nums[i]>nums[i+1]
exemple si on a [3,4,5,7,0,1,2] le point pivot est 0 .l'interet de trouver ce point est que forcement c'est le min de l'array. on peut facilement le trouver a l'aide d'un binary search : ce point se trouve forcement
dans la partie qui n'est pas sorted et donc si on prend le milieu d'un array il ya un cote qui sera sorted et l'autre qui ne le sera pas . si nums[left]<nums[mid] alors ce cote est sorted (ordre croissant) et donc le
cote [mid,right] ne l'ai pas , et vice-versas. 

l'idee est de prendre a chaque fois la unsorted part  car forcement le min ce trouve la bas , le cote droit est choisi si nums[mid] > nums[right] et puisque nums[mid] > nums[right] alors nums[mid] est forcement pas le 
min car nums[right] donc on peut choisir seulement [mid+1,right]. le cote gauche est choisie si nums[left]>nums[mid] ici nums[mid] peut etre le min car nums[left] est superieur a lui donc on prend le cote [left,mid] . 
au moment ou il nous reste plus que 1 element cad en sortant du while quand left==right alors on va rester avec le min forcement car a chaque fois on retraicit les possibilites jusqu'a ce qui nous reste que le mid 


app: nums=[6,0,1,2,3,4,5]  le non-sorted side  est [6,0,1] car 1<5 donc c'est pas a droite car c'est sorted a droite donc le unsorted side est  gauche :[left,mid] . 
               ^                                                                                            
              mid                                                                   
 nums=[6,0,1]   le non-sorted side  est [6,0,1] car 6>1  cad c'est le cote droit  donc on prend [mid+1,right] (mid+1 car nums[mid]>nums[right] donc nums[mid] ne peut etre le min du array)
       ^
      mid
nums=[0,1]   le non sorted side est pas a droite car 0<1 donc cote droit sorted donc on prend pas le cote droit donc on fait right =mid ce qui nous laisse avec [0] 
      ^ 
     mid           
puisque left==right on a fini , on return nums[left] cad 0     
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
 
        left, right = 0, len(nums)-1
         
        # DO NOT use left <= right because that would loop forever
        while left < right:
            # find the middle value between the left and right bounds (their average);
			# can equivalently do: mid = left + (right - left) // 2,
			# if we are concerned left + right would cause overflow (which would occur
			# if we are searching a massive array using a language like Java or C that has
			# fixed size integer types)
            mid = (left + right) // 2
                        
            if nums[mid] > nums[right]:
                # if nums[mid] > nums[right], we KNOW that the
                # pivot/minimum value must have occurred somewhere to the right of mid the not sorted part

                # example:  [3,4,5,6,7,8,9,1,2] 
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] > nums[right], we know that at some point to the right of mid,
                # the pivot must have occurred, which is why nums[right] is less then nums[mid]

                # we know that the number at mid is greater than at least
                # one number to the right, so we can use mid + 1 because mid is not the min 
                left = mid + 1

            else:
                # here, nums[mid] <= nums[right]:
                # we KNOW the pivot must be at mid or to the left of mid:
                # if nums[mid] <= nums[right], we KNOW that the pivot will not be 
                # to the right of middle because this part is sorted
                            
                # example: [8,9,1,2,3,4,5,6,7]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] <= nums[right], we know the numbers continued increasing to
                # the right of mid, so they are sortde
                # therefore, we know the pivot must be at index <= mid.

                # we know that nums[mid] <= nums[right].
                # therefore,  it is possible for the mid index to be the min, so we do
                # not discard it by doing right = mid - 1. it still might have the minimum value.
                right = mid
                
        # at this point, left and right converge to a single index (for minimum value) since
        # our if/else forces the bounds of left/right to shrink each iteration
        # so we shrink the left/right bounds to one value, that will be return at the end
        return nums[left]
