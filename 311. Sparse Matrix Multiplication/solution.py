"""# ma solution # math # matrix #TC O(m*k*n) #SC O(1)
pour calculer le produit de la matrice il faut comprendre comment on fait un produit de matrix .
VOIR GITHUB EXPLICATION 
"""

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:       
        m = len(mat1)   # num of row in mat1
        k = len(mat1[0]) # num of col of mat1 == num of row in mat2
        n = len(mat2[0]) # num of col in mat2
        # output will be m*n (row*col) 
        # creation matrice de taille m*n contenant que des 0 
        output = [[0 for _ in range(n)] for _ in range(m) ]
        for row1 in range (m) :  # parcours rangee de mat1
            for col2 in range (n) :  # parcours colonne de mat2
                for col1 in range (k) : # parcours colonne de mat1 qui revient au meme que parcourir les rangees de mat2
                    if mat1[row1][col1] and mat2[col1][col2] :    # si les deux sont diff de zero alors on les calcules
                        output[row1][col2] += mat1[row1][col1]*mat2[col1][col2]
        return output
    
""" follow up :
La plupart des commentaire disent que la question qui etait poser est la suivante : 
sachant que les matrices sont des sparses matrix (cad contiennent majoritairement que des zeros) proposer une data structure pour les compresser , puis calculer 
le produit des matrices a partir de ces matrices compressees .
voir ma solution ici (ce pb parle aussi du meme follow up) : https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

# math #matrix #hash-table # TC egale a O(m*k+k*n) car il faut passer sur les deux matrice pour faire la compression , plus O(p+q) pour le produit des matrices ,with p/q the
number of non zero element in the sparse-matrix/non-sparse-matrix.  # SC O(p+q) to keep the compressed matrix (with p/q the number of non zero element in the sparse-matrix/non-sparse-matrix)  

on va garder les matrices dans un dictionnaire de la facon suivante :
table = {  rowIdx1 : {colIdx1: val1, colIdx2: val2,..., colIdxN: valN } ,  ... }
cad le key va etre l'idx du row est la valeur va etre un dictionnaire qui a pour key la valeur de la col et pour valeur la valeur de matrix[rowIdx][colIdx]
"""
class Solution(object):
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:       
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat1), len(mat2[0])
        table_mat1, table_mat2 = {}, {}
        #compression mat1
        for rowIdx, entireRow in enumerate(mat1):         # mat1 est un 2D array donc chaque element represente un array entier cad une rangee entiere
            for colIdx, element in enumerate(entireRow):  # element va etre une case de la matrix 
                if element: # si element different de 0 
                    if rowIdx not in table_mat1: table_mat1[rowIdx] = {} # on creer un dictionnaire que une fois pour chaque row
                    table_mat1[rowIdx][colIdx] = element   # {rowIdx : {colIdx:element,...} , ... }
        #compression mat2
        for rowIdx, entireRow in enumerate(mat2):
            for colIdx, element in enumerate(entireRow):
                if element:
                    if rowIdx not in table_mat2: table_mat2[rowIdx] = {}
                    table_mat2[rowIdx][colIdx] = element
        #calcule de produit matricielle 
        output = [[0 for j in range(n)] for i in range(m)]
        # pour chaque valeur mat1[row1][col1] on veut trouver une valeur mat2[col1][col2] qui est diff de 0 cad qui se trouve dans le dictionnaire 
        for row1 in table_mat1:
            for col1 in table_mat1[row1]:
                if col1 in table_mat2: 
                    for col2 in table_mat2[col1]:
                        output[row1][col2] += table_mat1[row1][col1] * table_mat2[col1][col2]
                
        return output
    
    
"""follow up 2 :
Then the interviewer might keep follow up: What if one matrix is a sparse matrix and the another one is not ? We could say we can traverse the shorter one and use binary
search to find the matched index in the other vector. Then the run time would be O(m*logn),with m/n the number of non zero element in the sparse-matrix/non-sparse-matrix. 
voir ma solution a ce pb (il ya le meme follow up dans la derniere solution) :  https://leetcode.com/problems/dot-product-of-two-sparse-vectors/ """
