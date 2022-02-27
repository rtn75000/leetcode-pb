""" #sort #TC O(n*log n) #SC O(1) in python
trier d'apres la distance puis prendre les k premier elements. ici la distance est egale a sqrt(x^2+y^2). on peut utiliser  the squared Euclidean distance (x^2+y^2) 
instead of the precise Euclidean distance, as both will yield the same result. This allows us to remove the square root from each side of the equation which will significantly 
reduce the overall computational time for each comparison made.
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the list with a custom comparator function
        points.sort(key= lambda x : x[0]*x[0] + x[1]*x[1] )  #applique le lambda sur chaque element de points qui sera l'argument x puis sort
        
        # Return the first k elements of the sorted list
        return points[:k]
  
    
"""il ya une aussi une possibilite de resoudre en TC O(nlogk) avec SC O(k) a l'aide d'un heap"""
