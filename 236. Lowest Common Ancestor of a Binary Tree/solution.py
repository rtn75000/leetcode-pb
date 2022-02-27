"""#ma solution #dfs recursive #TC O(n) #SC O(height) height peut etre egale a O(n)
mon idee est de trouver les paths du root au node p et q . une fois qu'on a les paths si le node p/q se trouve sur le path du node q/p alors p/q est LCA, si ce n'est pas le cas alors il faut qu'on compare les deux
passe en commencant par le root, le LCA va etre celui qui precede le premier node qui differe ds le path . explication :

          10       p=4 q=9        pathP = 10->2->4
         /  \                     pathQ = 10->7->3->9                      
        2    7                    comme on peut le voir le dernier node en commun en partant du root est 10 donc 10 est LCA
       / \    \
      8   4    3 
                \
                 9 
                 
          10       p=7 q=9        pathP = 10->7
         /  \                     pathQ = 10->7->3->9                      
        2    7                    comme on peut le voir p se trouve ds le path de q donc p est LCA 
       / \    \
      8   4    3 
                \
                 9 
                 
 remarque : l'algo prend en compte le fait que toute les nodes sont unique que p!=q et que p et q se trouve forcement dans l'arbre
 remarque : cette solution est tres tres lente pr rapport au autre 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        path = []  # pourra etre au max la taille de la hauteur de l'arbre (peut etre O(n))
        
        def dfs(root,target): # TC O(n) car passe sur tout les nodes 
            if not root :
                return []
            if target.val == root.val :
                path.append(root)
                targetpath=copy.deepcopy(path)  # on doit faire un deepcopy car sinon quand la recursion modifie path targetpath va aussi etre modifier 
                path.pop()
                return targetpath
            path.append(root)    # on ajoute le root au path
            res1 =  dfs (root.left,target) 
            res2 =  dfs (root.right,target)
            path.pop() # cette ligne se fait en remontant de la double recursion cad quand on c'est occuper de la gauche et droite de root donc on peut maintenant retirer root
            return res1+res2
        
        pPath=dfs(root,p)
        qPath=dfs(root,q)
        
        # verifion si p/q se trouve dans le path de q/p
        for node in qPath :  #path est au max O(height) peut etre O(n)
            if node.val == p.val: 
                 return p
        for node in pPath : #path est au max O(height) peut etre O(n)
            if node.val == q.val: 
                 return q  
                
        #verifion le dernier node en commun
        i=0
        while True  : #fait au max path donc O(height) peut etre O(n)
            if pPath[i].val!=qPath[i].val:
                return qPath[i-1]
            i+=1
    
"""#bcp plus rapide que la premiere sol la premiere sol donne au mieu 2000ms alors que celle ci donne 60 ms au mieux ! #deuxieme sol #DFS recursive #TC O(n)  #SC O(height) height peut etre egale a O(n)
video explicative : https://www.youtube.com/watch?v=13m9ZCB8gjw&ab_channel=TusharRoy-CodingMadeSimple 

l'algo va fonctionner de la sorte: 
si on arrive a un node qui est egale a p/q alors on return p/q (bien entendue si root est vide on return null (important pour les leaf qui ne sont pas p/q)) un node qui va
avoir le cote droit et gauche qui est pas null cad que il a p d'un cote et q de l'autre donc c'est le LCA et donc il va retourner soit meme . un node qui va avoir que un cote non null alors il return la valeur de se cote.
un node qui va avoir les deux cotes null alors il return null. 
app : 
          10       p=8 q=4        en retournant de la recursion node 8 retourne 8 a node 2 et node 4 retourne 4 a node 2 donc 2 comme les deux recursion lui retourne qqch diff de null alors il se retourne lui  
         /  \                     meme a node 10 . en retournant de la recursion node 9 return null a node 3 qui return null a node 7 qui retourne node a 10. 10 a donc 2 et null qui lui on ete retourne donc il
        2    7                    retourne 2 cad ce qui n'est pas empty  
       / \    \
      8   4    3 
                \
                 9 

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root : #si root None alors : 
            return root # cad return None 
        
        if root == p or root == q : # si on a trouver q/p
            return root    
    
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and  right :   # si les 2 enfants sont pas null donc le root est LCA donc on return root 
            return root
        if not left and not right :  # si les 2 enfants sont null alors on return null
            return left  #cad return null car left est null ds ce cas 
        return right or left   # on arrive ici si un des deux enfant n'est pas null on return l'enfant non null .
    
    
"""#3eme sol dfs iterative  #TC O(n)  #SC O(n) , car on a le dic qui peut etre O(n) et le stack aussi
code d'ici : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution

app : 
          10       p=8 q=4        en retournant de la recursion node 8 retourne 8 a node 2 et node 4 retourne 4 a node 2 donc 2 comme les deux recursion lui retourne qqch diff de null alors il se retourne lui  
         /  \                     meme a node 10 . en retournant de la recursion node 9 return null a node 3 qui return null a node 7 qui retourne node a 10. 10 a donc 2 et null qui lui on ete retourne donc il
        2    7                    retourne 2 cad ce qui n'est pas empty  
       / \    \
      8   4    3 
                
                 
 initialisation : 
 stack=[10] parent = {10:None} 
 1er while : tant que p et q ne sont pas les deux dans dic faire :
                 -stack.pop == 10
                 -10 a un enfant a gauche donc on le rajoute au stack stack = [2] et on doit update le pere de 2 donc parent = {10:None , 2:10} 
                 -10 a un enfant a droite donc on le rajoute au stack : stack = [2,7] et on doit update le pere de 7 donc parent = {10:None , 2:10 , 7:10} 
            p=8 q=4 pas dans dic donc : 
                 -stack.pop == 7
                 -7 a un enfant a droite donc on le rajoute au stack  : stack = [2,3]  et on doit update le pere de 3 donc parent = {10:None , 2:10 , 7:10 , 3:7} 
            p=8 q=4 pas dans dic donc : 
                 - stack.pop == 3 
                 - comme 3 n'a pas d'enfant donc on fait rien 
            p=8 q=4 pas dans dic donc : 
                 - stack.pop == 2
                 -2 a un enfant a gauche donc on le rajoute au stack stack = [8] et on doit update le pere de 8 donc parent = {10:None , 2:10 , 7:10 , 3:7 , 8:2} 
                 -2 a un enfant a droite donc on le rajoute au stack : stack = [8,4] et on doit update le pere de 4 donc parent = {10:None , 2:10 , 7:10 , 3:7 , 8:2 , 4:2} 
            p=8 q=4 sont dans stack donc on a fini la premier boucle
2eme while : on va ajouter le path de p vers root dans un set tant que le pere va etre diff de null:
            p=8 :  ancestor.add(8)
                   p=parent[8] cad p==2 (voir dic)
            p=2 :  ancestor.add(2)
                   p=parent[2] cad p==10 (voir dic)
            p=10 :  ancestor.add(10)
                   p=parent[10] cad p==None (voir dic)
            p=None donc on a le path de p  : ancestor == (8,2,10)
3eme while : on va comparer le path de q avec le path de p trouver , tant que on trove pas un node en commun on continue 
            -q=4 comme 4 n'est pas dans ancestor alors on continue a moter le path de q : q=parent[4] cad q==2 
            -q=2 comme 2 est dans ancestor alors 2 est le LCA donc on quitte le while
on return q cad 2 qui est LCA .
"""


def lowestCommonAncestor(self, root, p, q):
    
    stack = [root]
    parent = {root: None}   # dic ou chaque key qui represente un node aura pour valeur sont pere 
    
    #ce while coute O(n) car il peut passer sur tout les nodes pour trouver p et q
    while p not in parent or q not in parent:      # cad tant que on a pas trouver p et q car il ne sont pas encore key dans parent alors : (remarque: search ds un dic coute O(1)) 
        node = stack.pop()
        if node.left:   # si node a un enfant alors ce node sera pere de cette enfant 
            parent[node.left] = node
            stack.append(node.left)  
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    #une fois la boucle fini on aura un dictionnaire qui va contenir tout les nodes qui sont dans le path de root vers p/q chaque node va avoir un pere 
    #on pourra retrouver le path en commancent par p on cherche son pere donc parent[p] apres qu'on a son pere pour trouver son grand pere on doit faire parent[parent[p]] etc..
    
    ancestors = set()  # on utilise un set car le search et O(1) (comme il ya pas de duplicate donc le set ne va pas effacer des valeurs)
    
    #ce while coute O(height) car passe sur le path de p donc peut etre O(n)
    while p: # tant que p n'est pas null
        ancestors.add(p)  # on rajoute dans le set le pere de p    (# remarque set n'a pas d'ordre met c'est pas important car apres on monte depuis q des qu'il ya un element en commun ca suffit. )
        p = parent[p] # p devient le pere comme ca on monte a chaque iteration 
    #ce while passe sur ancestor qui est le path de p donc coute O(height) qui peut etre O(n)
    while q not in ancestors:   # ici on commence par q et on monte tant que on trouve pas un node qui est dans set on continue a monter des qu'on trouve un node dans set ca va etre le premier node en commun donc le LCA.
        q = parent[q]
    return q  



