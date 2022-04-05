"""#set  #TC O(n+m) #SC O(n+m)
remarque importante : on utilise la conversion en un set car supprime les duplicate et la recherche se fait en O(1) car un set est implementer a l'aide d'un hash table . quand on fait une 
conversion cela coute TC O(n) car on passe sur tout les elements une fois, et SC egale O(n) car un set garde les elements dans un hash table donc utilse forcement un extr space O(n) pour creer
le set"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1) #TC SC O(n)
        nums2 = set(nums2) #TC SC O(m)
        res=[]
        # on verifie quel elements de nums1 apparait dans nums 2 
        for element in nums1 :  #TC O(n)
            if element in nums2 :  #TC O(1)
                res.append(element)  #TC O(1)
        return res
