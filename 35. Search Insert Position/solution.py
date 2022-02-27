"""cette question est l'appliction simple du binary search qui a un cout TC O(log n) une fois que la list est trier . l'idee du binary search est simple si on a une list trier est on recherche une valeur alors on coupe la liste au milieu puis on voit si la valeur rechercher est egale au milieu , superieur ou iferieur a lui si egale on a fini si inferieur maintenant on regarde que la partie inferieur et on refait la meme chose, si superieur on regarde la partie superieur et on refait la meme chose . il ya deux possibilite d'appliquer l'algo recursive ou iterative , on prendra l'iterative car recursive utilise la stack . 

def binarySearch(arr, l, r, x):

	while l <= r:

		mid = l + (r - l) // 2;   #(r-l) //2 nous donne le milieu si l=0 mais si l>0 alors il faut rajouter l 
                                  # ex : 1 3 5 6 8 9    le milieu egale a 5-0//2 , puis si on prend la 2e partie 6 8 9 si on fait (5-3)//2 ca donne l'index 2 cad la val 5 or nous on veut 
                                         ^         ^                                                             ^   ^                        
		                              left=0   right=5                                                          l=3  r=5
                                  # l'index 4 donc on doit rajouter l cad 3 pour que le milieu soit compter a partir de l'idx 3 et pas appartir de 0
		# Check if x is present at mid
		if arr[mid] == x:
			return mid

		# If x is greater, ignore left half
		elif arr[mid] < x:
			l = mid + 1

		# If x is smaller, ignore right half
		else:
			r = mid - 1
	
	# If we reach here, then the element
	# was not present
	return -1

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        def binarySearch(arr, l, r, x):

                while l <= r:

                    mid = l + (r - l) // 2;

                    # Check if x is present at mid
                    if arr[mid] == x:
                        return mid

                    # If x is greater, ignore left half
                    elif arr[mid] < x:
                        l = mid + 1

                    # If x is smaller, ignore right half
                    else:
                        r = mid - 1

                # If we reach here, then the element
                # was not present. for this exercice we return the index where it would be if it were inserted in order.
                # par exemple si on a 6 8 9 et on cherche 7 alors comme 7<arr[4] donc r=4-1 cad 3 donc 6 8 9 comme mid = 3 donc 7>arr[3](=6) donc on avance left a mid+1 cad l=4 et comme l>r on
                #                     ^   ^                                                            ^                                                                
                #                    l=3  r=5                                                         l=r=3                                         
                # a fini donc si on devait rajouter 7 il aurait du etre entre 4 et 5 cad on aurait du mettre apres l'idx 4 la val 7  . donc l'endroit a rajouter c'est a l'index l a la fin du 
                # while 
                return l
        
        return binarySearch (nums, 0, len(nums)-1, target)
