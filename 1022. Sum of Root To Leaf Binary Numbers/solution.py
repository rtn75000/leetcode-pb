"""# ma solution (j'ai pris tres longtemps a la trouver)  # DFS recursive #TC O(n) #SC O(height) can be O(n) in worst case
cette solution est super importante a comprendre . il est tres important de comprendre comment marche la recursion dans un arbre binaire , comment se fait le retour de la recursion. 
quand on remonte de la recursion les element comme des int retourne a leur etat precedent mais des element comme des list garde le changement meme quand on remonte de la recursion (cela s'explique car une list a
une adresse permanente donc tout changement est permant).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int: 
    
        def dfs(root,path):
            if not root :  # ce cas s'applique aussi quand on a un element que a gauche ou que a droite et donc le pere appel root.left et root.right donc un d'entre eux va etre null ds ce cas on rend 0 pour le fils null
                return 0 
            if not root.left and not root.right :   # si un element a pas d'enfant alors il est leaf
                path.append(str(root.val))
                num = ''.join(path)
                res= int(num,2)   #conversion binaire en decimal
                path.pop()
                return res
            path.append(str(root.val))   #ajout du pere de left et right
            res1 = dfs(root.left,path) 
            res2 = dfs(root.right,path)
            path.pop()   # cette partie ce fait en remontant de la recursion    #retrait du pere apres resultat de left et right 
            return res1+res2
           
        return dfs(root,[])
    
    
"""#pas ma sol  #comme en haut juste je montre une autre facon d'ecrire plus concise 
sol d'ici : https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/1681647/Python3-5-LINES-(-)-Explained

remarque : For building the binary number in the path we use a binary operation (path << 1) which shifts all bits to the left by one bit to free space for the current bit which we simply add to the path. Example:
path=0 => (path<<1) + 1 = 01
path=01 => (path<<1) + 1 = 11
path=11 => (path<<1) + 0 = 110
path=110 => (path<<1) + 1 = 1101

"""

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node: 
                return 0
            path = (path << 1) + node.val  #voir remarque en haut
			
            if not node.left and not node.right:
                return path
            
            return dfs(node.left, path) + dfs(node.right, path)
            
        return dfs(root, 0)

"""#ma sol #2nd sol #iterative DFS  #TC O(n) #SC O(height) can be O(n) in worst case
la version iterative va utiliser un stack qui va se comporter comme le stack de la recursion .
ce qui est important c'est que chaque element dans le stack ait constituer du node et du path jusqu'au root."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int: 
        
        stack=[(root,[str(root.val)])] 
        res=0 
        
        while stack:
            root=stack[-1][0]
            path=stack[-1][1]
            if not root.left and not root.right :
                stack.pop()
                res += int(''.join(path),2)   #conversion binaire en decimal
                continue
            if not root.right :   # si il ya pas un fils a droite on va a gauche 
                stack.pop()
                stack.append((root.left,path+[str(root.left.val)])) 
                continue
            if not root.left :    # si il ya pas un fils a gauche on va a droite 
                stack.pop()
                stack.append((root.right,path+[str(root.right.val)]))           
                continue
            stack.pop()           # on arrive ici si il y'a un fils a gauche et a droite 
            stack.append((root.left,path+[str(root.left.val)]))
            stack.append((root.right,path+[str(root.right.val)]))
            
        return res
    
    
