""" # recursive  # super analyse du TC et SC de la recursion (mon analyse) #TC O(n^2)   #SC O(n)

il existe une solution O(n) mais ma solution est super pour comprendre la recursion donc on va voir que ma sol (pour voir l'autre sol voir dans les discussions)

analyse du TC et SC : 

    le valeur max de l'array peut soit separer l'array en deux partie egale (ex [3,6,8,7,4] alors max==8 separe l'array en deux partie egale), soit en une partie plus grande que l'autre (ex [3,6,8,9,4] alors max==9 
    separe l'array en 2 partie , une plus grande que l'autre) et dans ce cas on aura au pire des cas une partie qui contient n-1 element et la 2eme partie contient 1 element seulement ( ex [3,6,9,4,10] alors max==10
    separe en deux partie une n-1 : [3,6,8,9] et l'autre 1 : [10]). 

    analyse du cas ou le la fct separe l'array en deux partie egales : F(n) trouve sont max donc O(n) puis fait un double appel recursive de F(n/2) un appel pour chaque moitier donc la relation de recursion
    (voir mes fiche time complexity pour tout comprendre) est : T(n)=2T(n/2)+n qui revient a TC=O(nlogn) (voir mes fiches il ya toutes l'analyse de cette relation de recurrence ) et SC = O(log n) (comme la 
    hauteur de l'arbre de recursion voir fiche).

    analyse du cas ou la fonction separe l'array en une partie plus grande que l'autre : comme on a dit au pire des cas on separer en deux partie une egale a n-1 et un a 1 donc ca veut dire que F(n) trouve sont
    max donc O(n) puis fait un double appel recursive un sur F(n-1) et un sur F(1) masi comme F(1) coute O(1) alors il est negligeable donc ca revient a la relation de recurence suivante : T(n)= T(n-1)+n 
    (on mais pas T(1) car egale O(1) donc negligeable) dans ce cas TC= O(n^2)   (voir mes fiches il ya toutes l'analyse de cette relation de recurrence ) et SC= O(n) (comme la hauteur de l'arbre de recursion voir fiche).

    donc notre TC est entre O(nlogn) et O(n^2)  (nlogn<n^2==n*n (car logn<n)) donc au pire TC egale O(n^2). notre SC est entre O(log n) et n donc au pire O(n)

explication de l'algo :
    
    on cree un node avec la valeur max et on appel de facon recursive l'array de gauche et de droite de max . 

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums):
        if nums: # que si nums pas vide donc si nums vide condition d'arret (in python if a function doesn't specify a return value, it returns None. donc si nums==None return None)
            max_val=max(nums) # TC O(n) car doit passer sur tout les elements pour trouver le max 
            max_idx=nums.index(max_val)  # car on veut prendre les elements qui se trouve a gauche et a droite du max donc il nous faut l'idx de max.  
            node = TreeNode(max_val) # creation du node avec la valeur max 
            node.left = self.constructMaximumBinaryTree(nums[:max_idx])   # recursion sur les elements a gauche du max 
            node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])  # recursion sur les elements a droite du max 
            return node  # cette ce fait en remontant des recursion donc la derniere valeur retourner va etre la valeur du root de l'arbre car ca va etre la derniere recursion remonter. 
        
       
