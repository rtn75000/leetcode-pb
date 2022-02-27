"""un complete binary tree est un arbre qui est plein a tout les niveau sauf au dernier ou il peut avoir entre 1 et 2^h nodes (h est la hauteur de l'arbre) qui seront tous cote gauche 
ex :        1
          /   \        ici la hauteur est 2 il ya donc entre 1 et 2^2 nodes au dernier niveau comme on peut le constater tout les nodes du dernier niveau sont a gauche . 
         2     3
       /  \
      4    5 
 quelque propriete importante :
 -> A Binary Tree is a full binary tree if every node has 0 or 2 children. 
 ex:         18
           /    \   
         15     20    
        /  \       
      40    50   
    /   \
   30   50
 
 
 un perfect binary tree est un binary tree dont tout les niveau sont complet, il a en tout (2^(h+1))-1 nodes, avec h la hauteur de l'arbre . 
 ex:           18
           /       \                     il a 2^(2+1) -1   nodes cad 2^3 -1 = 8 -1 =7 nodes le dernier niveau a 2^h nodes cad 2^2
         15         30  
        /  \        /  \
      40    50    100   40
un perfect binary tree a (2^(h+1))-1 nodes soit n le nombre de nodes donc n=(2^(h+1))-1 <=> n+1 = 2^(h+1) <=> log2(n+1)=log2(2^(h+1)) <=> log2(n+1)= h+1 <=>  log2(n+1)-1=h cad que la hauteur de l'arbre egale a 
log2(n+1)-1 donc on peut dire que la hauteur est O(log2(n))  (car comme n est grand quand on parle d'ordre de grandeur alors : log2(n+1)<=log2(n)+log2(1) donc log2(n+1)-1<=log2(n)+log2(1)-1 or log2(1)=0 doncca revient a : 
log2(n+1)-1<=log2(n)+0-1  cad log2(n+1)-1<=log2(n)-1<log2(n) donc on peut dire que h=log2(n+1)-1 < log2(n) d'ou h est O(log2(n)))

ccl : 
-un perfect binary tree a  n=2^(h+1)-1  nodes et ca hauteur h est O(log2(n)) 
-un complete binary tree a n=2^(h)-1 + x avec x inclu dans [1,2^h]  et ca hauteur est O(log2(n))
"""
"""il nous est demander de resoudre se pb avec un TC inferieur a O(n) mais je vaiscomme meme parler de cette solution car elle est une base importante .
pour savoir combien il y a de node en tout on peut tout simplement traverser tout l'arbre de facon inorder preorder ou postorder (rappel la difference c'est quand on visite le node) ici on va faire preorder
cad on visite le node puis on va recursivement a gauche puis recursivement a droite :
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None :
              return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right) #ou self.countNodes(root.left)+1+self.countNodes(root.right) ou self.countNodes(root.left)+1+self.countNodes(root.right)
TC O(n) car visite 1 fois chaque node  .  SC O(log n) pour le stack de la recursion car uen recursion par exemple self.countNodes(root.left) va au max du root vers un leaf le plus a gauche cad parcours la hauteur 
de l'arbre au max donc le stack sera O(log n)
(une version iterative dans ce cas va avoir le meme Tc et SC car elle utilise un stack pour garder les nodes dont on a pas visiter tout les enfants)
"""

""" remarque :  la hauteur du root est 0 donc par ex:     1        h=0
                                                        /   \        
                                                       2     3     h=1
                                                      / \
                                                     4   5         h=2 

"""
"""#recursive #using perfect binary tree property #TC O(log n * log n) avec n nombre de nodes  #SC O(log n) pour le stack qui sera de la taille de la hauteur au max (voir explication en bas)
video explicative: https://www.youtube.com/watch?v=i_r2uKbwHCU&ab_channel=KnowledgeCenter
l'idee est de voir si on a un arbre perfect si on a pas un arbre perfect on voit si les enfant sont des arbres perfect . un arbre est perfect si la hauteur la plus a gauche est egale a la hauteur la plus a droite 
app : 
               1              
          /        \                   
         2          3            
        / \        /  \
       4   5      6    7
      /\   /\    /\    /
     8  9 10 11 12 13 14 
     
->root==node1 : heightLeft=3 != heightRight=2 donc l'arbre n'est pas perfect on va return 1 (pour le root 1) + recursion chez enfants donc return 1 + recursion(root.left) + recursion(root.right)
[ en remontant la rec on obtient : 1+7+6==14 qui est notre resultat final] 
   
   -> recursion(root.left): root==node2 : heightLeft=2 == heightRight=2 donc l'arbre est perfect dc return (2^(leftHeight+1))-1 cad return 2^(2+1)-1 <=> return 7
   -> recursion(root.right): root==node3: heightLeft=2 != heightRight=1 donc l'arbre n'est pas perfect dc return 1 + recursion(root.left) + recursion(root.right)
      [en remontant la rec a la fin ca donne : 1+3+2==6]
      
      -> recursion(root.left): root==node6 : heightLeft=1 == heightRight=1 donc l'arbre est perfect dc return (2^(leftHeight+1))-1 cad return 2^(1+1)-1 <=> return 3
      -> recursion(root.right): root==node7: heightLeft=1 != heightRight=0 donc l'arbre n'est pas perfect dc return 1 + recursion(root.left) + recursion(root.right)
         [en remontant la rec a la fin ca donne  1+1+0==2]
      
          -> recursion(root.left): root==node14 : heightLeft=0 == heightRight=0 donc l'arbre est perfect dc return (2^(leftHeight+1))-1 cad return 2^(0+1)-1 <=> return 1 
          -> recursion(root.right): root==None ca return 0   
          
TC : la recursion peut se faire maximum h fois avec h la hauteur cad elle se fait O(log n) . en effet la recusrion se fait a chaque fois que on a pas un perfect arbre comme on peut le voir dans l'exemple precedent a
chaque fois qu'on fait la recursion on descend d'un niveau dans l'arbre donc on peut max descendre h niveau (dans l'exemple precedent on avait 3 recursion et h==3) chaque recursion coute O(2*log n) car on cherche la 
hauteur de gauche et de droite donc ca revient a O(log n). donc comme on fait la recursion O(log n) et chaque recursion coute O(log n) alors TC est egale a O(log n*log n). SC est egale au nombre maximum de recursion 
dans le stack cad O(log n) car comme on a vu on a max O(log n) recursion .
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        #si l'arbre est vide
        if root == None:     
            return 0     
        
        leftHeight = self.getHeightLeft(root)   # trouve la hauteur du cote gauche de l'arbre coute O(log n) (avec n nombre de node) car va du root jusqu'au leaf  
        rightHeight = self.getHeightRight(root)  # trouve la hauteur du cote droit de l'arbre coute O(log n) (avec n nombre de node) car va du root jusqu'au leaf     
        
        #si leftHeight==rightHight alors ca veut dire que l'arbre qui commence a ce root est un perfect binary tree donc il a (2^(h+1))-1 nodes, avec h la hauteur de l'arbre.
        if leftHeight == rightHeight :
            return (2**(leftHeight+1))-1      
        #else l'arbre en partant de ce root n'est pas perfect on va donc ajoute le root et on va aller recursivement chez ses enfant pour voir si eux ils sont des perfect binary tree
        # la recursion peut se faire au max O(log n) car a chaque niveau on peut faire la recursion 
        else:
            return 1+self.countNodes(root.left) + self.countNodes(root.right) 
    
    def  getHeightLeft(self,root : Optional[TreeNode]) -> int :
        height=0
        while root.left!=None:
            height+=1
            root = root.left
        return height
    
    def  getHeightRight(self, root : Optional[TreeNode]) -> int :
        height=0
        while root.right!=None:
            height+=1
            root = root.right
        return height
    
"""#iterative  #TC O(log n * log n) avec n nbr of nodes  #SC O(1) 
La solution est la suivante : a chaque root on regarde ce qui se passe dans le sub-tree de gauche et dans le sub-tree de droite . si le subtree de gauche est un perfect binary tree cad que leftleftHeight (height cote 
gauche du sub-tree de gauche) == rightleftHeight (height cote droit du sub-tree de gauche) alors on ajoute au ttl, la somme des nodes du sub-tree de gauche cad (2**(leftleftHeight+1))-1 plus 1 pour compter le root , puis
le nouveau root sera le root du sub-tree de droite : root=root.right . Si le subtree de gauche n'est pas un perfect binary tree alors le subtree de droite est forcement perfect donc on ajoute au ttl la somme des nodes du 
subtree de droite cad (2**(rightrightHeight+1))-1 plus 1 pour compter le root , puis le nouveau root sera le root du sub-tree de gauche : root=root.right. il est possible que l'arbre en partant du root soit perfect (pas
le premier root mais dans les autres c possible) si leftleftHeight (height cote gauche du sub-tree de gauche) == rightrightHeight (height cote droit du sub-tree de droit) et donc on peut rajouter au ttl la sum tout les 
nodes de l'arbre cad (2**(leftleftHeight+2))-1 (+2 et pas +1 car leftleftHeight c'est la hauteur a partir du left subtree mais pas apartir du root donc il faut rajouter +1 pour que ca soit la hauteur a partir du root et 
pas juste de root.left)  et on a fini l'algo car on a pas d'autre subtree.

app : 
               1              
          /        \                   
         2          3            
        / \        /  \
       4   5      6    7
      /\   /\    /    
     8  9 10 11 12        
-> root = node1 : leftleftHeight(2) != rightrightHeight(1) donc l'arbre n'est pas perfect il faut verifier les sub-tree de gauche et droite; on commence par celui de gauche (le root est node 2) on verifie si il est 
perfect: puisque leftleftHeight(2) == leftrightHeight(2) alors il est perfect est donc on peut rajouter la somme de ses nodes au total + 1 pr le root : ttl+= (2**(leftleftHeight+1))-1 +1(pour compter le root) cad
ttl+=(2**(leftleftHeight+1)) soit ttl+=(2**2+1) soit ttl+=(2**3) donc ttl=8. maitenant root devient le sub-tree de droite donc root=root.right .
-> root = node3 : leftleftHeight(1) != rightrightHeight(0) donc l'arbre n'est pas perfect il faut dc verifier les sub-tree de gauche et droite; on commence par celui de gauche (le root est node 6) on verifie si il est 
perfect: puisque leftleftHeight(1) != leftrightHeight(0) alors il est pas  perfect donc forcement que le subtree de droite est perfect et donc on peut rajouter la somme des ses nodes au total + 1 pour le root :
ttl+= (2**(rightrightHeight+1))-1 +1(pour compter le root) cad ttl+=(2**(leftleftHeight+1)) soit ttl+=(2**0+1) ttl+=2 donc ttl=10 . maitenant root devient le sub-tree de gauche donc root=root.gauche .
->root = node 6 :  leftleftHeight(0) != rightrightHeight(-1) donc l'arbre n'est pas perfect il faut dc verifier les sub-tree de gauche et droite; on commence par celui de gauche (le root est node 12) on verifie si il
est perfect: puisque leftleftHeight(0) == leftrightHeight(0) alors il est perfect donc ttl+=(2**(leftleftHeight+1)) soit ttl+=(2**0+1) ttl+=2 donc ttl=12.maintenant root devient le sub-tree de droite mais comme
root.right==None cad qu'il ya pas de sub-tree a droite et donc on a fini.
"""


class Solution:
    
    def countNodes(self, root: Optional[TreeNode]) -> int:        
        ttl=0     
        while root != None :    
            leftleftHeight = self.getHeightLeft(root.left)   # trouve la hauteur du cote gauche de l'arbre coute O(log n) (avec n nombre de node) car va du root jusqu'au leaf  
            leftrightHeight = self.getHeightRight(root.left)  # trouve la hauteur du cote droit de l'arbre coute O(log n) (avec n nombre de node) car va du root jusqu'au leaf     
            rightrightHeight = self.getHeightRight(root.right)  # trouve la hauteur du cote droit de l'arbre coute O(log n) (avec n nombre de node) car va du root jusqu'au leaf   
            if leftleftHeight == rightrightHeight :   #if the tree is perfect
                ttl+=(2**(leftleftHeight+2))-1  
                break
            elif leftleftHeight == leftrightHeight :  #if the left subtree is perfect
                ttl += (2**(leftleftHeight+1))
                root = root.right
            else :                                    #if the right subtree is perfect
                ttl += (2**(rightrightHeight+1))
                root = root.left
        return ttl   
              
    
    def  getHeightLeft(self,root : Optional[TreeNode]) -> int :
        if root==None : return -1
        height=0
        while root.left!=None:
            height+=1
            root = root.left
        return height if root !=None else -1
    
    def  getHeightRight(self, root : Optional[TreeNode]) -> int :
        if root==None : return -1
        height=0
        while root.right!=None:
            height+=1
            root = root.right
        return height 
