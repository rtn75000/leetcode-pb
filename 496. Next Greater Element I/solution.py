"""la consigne est la suivante : on a deux listes la list nums1 et la list nums2. la list num1 contient tout les numero qui apparaissent aussi dans nums2 pour lequels on veut trouver dans nums2 l'index du numero 
superieur qui vient apres . voir exemple c'est facile a comprendre"""

"""#TC O(len(n2)) bien qu'on passe sur nums2 puis sur nums 1 comme nums1 est un subset de nums2 ca donne donc au max 2*len(nums2) soit O(len(nums2))  #SC O(len(nums2)) car la stack contiendra que les num de nums2 
l'algo se fait en 2 etape:
-1er etape faire un dictio qui contient tout les nums de nums2 qui on un nombre superieur apres eux
-2e etape :passer sur num1 pour voir pour quel num on veut connaitre la valeur superieur qui vient apres . a chaque num on rentre le resultat dans output 
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        output = []
        dictio= {} # contiendra paire [val]:[premier num sup apres val]
        for num in nums2 :
            while stack and num>stack[-1] :   #monotonic decrease stack
                dictio[stack.pop()]=num   # add the paire in the dictio
            stack.append(num)
        for num in nums1 : 
            if num in dictio :
                output.append(dictio[num])
            else :
                output.append(-1)
        return output 
