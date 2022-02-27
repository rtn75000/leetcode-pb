"""explication de l'ennoncer: 
la fonction serialize doit recevoir un arbre binaire et le transformer en une string et la fonction deserialize doit etre capable de prendre cette string et de la transformer en un arbre binaire. 
"""

""" exercice tres interressant pour comprendre dfs et bfs """

"""
#first sol #not mine #dfs recursive #TC O(n) for serialize and deserialize #SC O(n) for serialize and deserialize for the recursive call of the stack (dans serialize on utilise aussi une list res de la taille O(n))
-serialize : 
  l'idee pour serialize et de tout simplement faire un dfs (inorder) qui va vous donner a la fin une phrase par exemple si on a      1     ca donne 1,2,None,None,3,4,None,None,5,None,None
                                                                                                                                    / \
                                                                                                                                   2   3
                                                                                                                                      / \
                                                                                                                                      4  5   
  le dfs va donc simplement parcourir l'arbre en inorder chaque valeur va etre rajouter au resultat, la condition d'arret et simplement quand le node est null dans ce cas on rajoute 'None,' au res  .  
  
- deserialize :
    le deserialize va reproduire le dfs sur la phrase il va d'abord creer tout les nodes cotes gauche puis des qu'il rencontre un none il return donc remonte la recursion en remontant on appele la recursion cote droit qui
    elle aussi appele la recursion cote gauche puis en remontant appel cote droit et ainsi de suite .
    
    app: si on a     1 
                   /  \ 
                  2    3
                 / \    \
                4  5     6
                
    alors data="1,2,4,N,N,5,N,N,3,N,6,N,N" (N a la place de None) alors deserialize(data) ca donne ca :
    
    queue=collections.deque(data.split(',')) cad queue=[1,2,4,N,N,5,N,N,3,N,6,N,N]
    helper(queue) cad helper([1,2,4,N,N,5,N,N,3,N,6,N,N]) :  
                       
        root = TreeNode(q.popleft()) cad TreeNode(1)                         dc root.left=TreeNode(2)                                        
        root.left = helper([2,4,N,N,5,N,N,3,N,6,N,N]):   <---------------------------------------------------------------                         
                                                                                                                         |                           
                    root = TreeNode(q.popleft()) cad TreeNode(2)           dc root.left=TreeNode(4)                      |                                          
                    root.left = helper([4,N,N,5,N,N,3,N,6,N,N]):    <----------------------------------------------      |
                                                                                                                  |      |
                                root = TreeNode(q.popleft()) cad TreeNode(4)    dc root.left=None                 |      |               
                                root.left = helper([N,N,5,N,N,3,N,6,N,N]):    <------------------                 |      |                       
                                                                                                |                 |      |                                               
                                            queue[0]==N donc on fait queue.popleft() et return None               |      |                                
                                                                                dc root.right= None               |      |                   
                                root.right = helper([N,5,N,N,3,N,6,N,N]):     <------------------                 |      |                                   
                                                                                                |                 |      |                           
                                            queue[0]==N donc on fait queue.popleft() et return None               |      |                       
                                                                                                                  |      |
                               return root cad TreeNode(4)  ------------------------------------------------------       |                       
                                                                         dc root.right=TreeNode(5)                       |                                                   
                    root.right = helper([5,N,N,3,N,6,N,N]):    <--------------------------------------------------       |
                                                                                                                  |      |
                                root = TreeNode(q.popleft()) cad TreeNode(5)    dc root.left=None                 |      |              
                                root.left = helper([N,N,3,N,6,N,N]):          <------------------                 |      |                       
                                                                                                |                 |      |                                               
                                            queue[0]==N donc on fait queue.popleft() et return None               |      |                                
                                                                                dc root.right= None               |      |                   
                                root.right = helper([N,3,N,6,N,N]):           <------------------                 |      |                                   
                                                                                                |                 |      |                           
                                            queue[0]==N donc on fait queue.popleft() et return None               |      |                       
                                                                                                                  |      |
                                return root cad TreeNode(5)  ------------------------------------------------------      |
                                                                                                                         |                           
                    return root cad TreeNode(2) -------------------------------------------------------------------------
                                                                dc root.right=TreeNode(3)
        root.right = helper([3,N,6,N,N]):       <---------------------------------------------------------------          
                                                                                                                |                          
                      root = TreeNode(q.popleft()) cad TreeNode(3)       dc root.left=None                      |                                 
                      root.left = helper([N,6,N,N]):      <----------------------------                         |                              
                                                                                      |                         |    
                                  queue[0]==N donc on fait queue.popleft() et return None                       |
                                                                       dc root.right=TreeNode(6)                |
                      root.right = helper([6,N,N]) :    <---------------------------------------------------    |
                                                                                                           |    |                         
                                   root = TreeNode(q.popleft()) cad TreeNode(6)      dc root.left=None     |    |                                             
                                   root.left = helper([N,N]):        <-------------------------------      |    |
                                                                                                    |      |    |                
                                               queue[0]==N donc on fait queue.popleft() et return None     |    |
                                                                                    dc root.right=None     |    |
                                   root.right = helper([N]):         <-------------------------------      |    |
                                                                                                    |      |    |           
                                               queue[0]==N donc on fait queue.popleft() et return None     |    |
                                                                                                           |    |     
                                   return root cad return Treenode(6)  ------------------------------------     |      
                                                                                                                |                           
                      return root cad TreeNode(3) ---------------------------------------------------------------             
                                                                                                                                                                                    
        return root cad return TreeNode(1) 
        
    
    donc au final on a ca  : 
         
         
     root=TreeNode(1)
        root.left=Treenode(2)
             root.left=Treenode(4)
                   root.left=None
                   root.right=None
             root.right=TreeNode(5)
                   root.left=None
                   root.right=None
        root.right=TreeNode(3)
              root.left=None
              root.right=TreeNode(6)
                   root.left=None
                   root.right=None
                   
     cad on a reconstruit l'arbre    1       a l'aide de  data="1,2,4,N,N,5,N,N,3,N,6,N,N" 
                                   /  \ 
                                  2    3
                                 / \    \
                                4  5     6
        """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root): # cout TC SC O(n) (n nbr de nodes) car parcours tout les nodes et les ajoutes au res.  
        """Encodes a tree to a single string.
        """
        def dfs(root):
            if not root:
                res.append("None,")
                return 
            res.append(str(root.val)+",")
            dfs(root.left)
            dfs(root.right)
            
        res = [] # on utilise une list a laquelle on va append a chaque fois et pas une string car la concatenation avec string coute O(n^2) a la finc car python copy a chaque fois le string puis lui append 
        dfs(root)
        return "".join(res)

    def deserialize(self, data):   #TC O(n)    n == taille de la str data == nbr de node 
        """Decodes your encoded data string to tree.
        """
        def helper(q):
            if q[0] == "None":
                q.popleft()   
                return None
            root = TreeNode(q.popleft())
            root.left = helper(q)
            root.right = helper(q)
            return root
        
        data_list = data.split(",")     # creer une list en compent la phrase a toute les virgules
        data_deque = collections.deque(data_list)  #on utilise deque car si on utilise une liste normal alors popleft (cad pop index 0) coute O(n)
        return helper(data_deque)
    
    
"""#sol 2 #BFS (level order traversal) - iterative #TC/SC O(n)

-serialize:
  fait un bfs sur l'arbre donc si on a par exemple    1     ca donne 1,2,3,None,None,4,5,None,None,None,None,
                                                     / \
                                                    2   3
                                                       / \
                                                       4  5   
  app : q=[root]
        res= 
        while q :
           -iteration : 
               curr = q.popleft() cad curr=TreeNode(1)  , q=[]
               res.append(str(curr.val))  donc res=[1]
               q.append(curr.left)        donc q=[TreeNode(2)]
               q.append(curr.right)       donc q=[TreeNode(2),TreeNode(3)]
           -iteration : 
               curr = q.popleft() cad curr=TreeNode(2) , q=[TreeNode(3)]
               res.append(str(curr.val))  donc res=[1,2]
               q.append(curr.left)        donc q=[TreeNode(3),None]
               q.append(curr.right)       donc q=[TreeNode(3),None,None]
           -iteration : 
               curr = q.popleft() cad curr=TreeNode(3) , q=[None,None]
               res.append(str(curr.val))  donc res=[1,2,3]
               q.append(curr.left)        donc q=[None,None,TreeNode(4)]
               q.append(curr.right)       donc q=[None,None,TreeNode(4),TreeNode(5)]
           -iteration : 
               curr = q.popleft() cad curr=None , q=[None,None,TreeNode(4),TreeNode(5)]
               puisque curr==None donc :
               res.append("None")     donc res=[1,2,3,None]   
           -iteration : 
               curr = q.popleft() cad curr=None , q=[TreeNode(4),TreeNode(5)]
               puisque curr==None donc :
               res.append("None")     donc res=[1,2,3,None,None]       
           -iteration : 
               curr = q.popleft() cad curr=TreeNode(4) , q=[TreeNode(5)]
               res.append(str(curr.val))  donc res=[1,2,3,None,None,4]
               q.append(curr.left)        donc q=[TreeNode(5),None]
               q.append(curr.right)       donc  q=[TreeNode(5),None,None]
           -iteration : 
               curr = q.popleft() cad curr=TreeNode(5) , q=[None,None]
               res.append(str(curr.val))  donc res=[1,2,3,None,None,4,5]
               q.append(curr.left)        donc q=[None,None,None]
               q.append(curr.right)       donc  q=[None,None,None,None]
           -iteration : 
               curr = q.popleft() cad curr=None , q=[None,None,None]
               puisque curr==None donc :
               res.append("None")     res=[1,2,3,None,None,4,5,None] 
           -iteration : 
               curr = q.popleft() cad curr=None , q=[None,None]
               puisque curr==None donc :
               res.append("None")     res=[1,2,3,None,None,4,5,None,None] 
           -iteration : 
               curr = q.popleft() cad curr=None , q=[None]
               puisque curr==None donc :
               res.append("None")     res=[1,2,3,None,None,4,5,None,None,None]
           -iteration : 
               curr = q.popleft() cad curr=None , q=[]
               puisque curr==None donc :
               res.append("None")     res=[1,2,3,None,None,4,5,None,None,None,None] 
               
       puisque q==[] alors on a fini le while 
       return ",".join(res) cad "1,2,3,None,None,4,5,None,None,None,None"
       
-deserialize : 
  
    utilise deux queue : data et q , on lit a chaque un element de q , cette element va etre le root puis on lit deux elemnt de data qui vont etre les enfant de root et vont etre append a q

    app :   reconstruire    1     a l'aide de dataString = "1,2,3,None,None,4,5,None,None,None,None"
                           / \
                          2   3
                             / \
                             4  5   
    
    
        data = collections.deque(data.split(","))    cad data = [1,2,3,None,None,4,5,None,None,None,None] 
        root = TreeNode(int(data.popleft()))         cad root = TreeNode(1), data = [2,3,None,None,4,5,None,None,None,None]
        q = deque([root])                            cad q=[TreeNode(1)]
        
        while q :
        
        -iteration : 
            cur = q.popleft()      cad cur == TreeNode(1) , q=[]
            l = data.popleft()     cad l==2 , data = [3,None,None,4,5,None,None,None,None]
            r = data.popleft()     cad r==3 , data = [None,None,4,5,None,None,None,None]
            cur.left = TreeNode(int(l)) if l != "None" else None       cad cur.left == TreeNode(2)
            cur.right = TreeNode(int(r)) if r != "None" else None      cad cur.left == TreeNode(3)
            q.append(cur.left)     cad q=[TreeNode(2)]
            q.append(cur.right)    cad q=[TreeNode(2),TreeNode(3)]
            
        -iteration : 
            cur = q.popleft()      cad cur == TreeNode(2) , q=[TreeNode(3)]
            l = data.popleft()     cad l==None , data = [None,4,5,None,None,None,None]
            r = data.popleft()     cad r==None , data = [4,5,None,None,None,None]
            cur.left = TreeNode(int(l)) if l != "None" else None       cad cur.left == None
            cur.right = TreeNode(int(r)) if r != "None" else None      cad cur.left == None
            q.append(cur.left)     cad q=[TreeNode(3),None]
            q.append(cur.right)    cad q=[TreeNode(3),None,None]
        
        -iteration : 
            cur = q.popleft()      cad cur == TreeNode(3) , q=[None,None]
            l = data.popleft()     cad l==4 , data = [5,None,None,None,None]
            r = data.popleft()     cad r==5 , data = [None,None,None,None]
            cur.left = TreeNode(int(l)) if l != "None" else None       cad cur.left == TreeNode(4)
            cur.right = TreeNode(int(r)) if r != "None" else None      cad cur.left == TreeNode(5)
            q.append(cur.left)     cad q=[None,None,TreeNode(4)]
            q.append(cur.right)    cad q=[None,None,TreeNode(4),TreeNode(5)]
       
        -iteration : 
            cur = q.popleft()      cad cur == None , q=[None,TreeNode(4),TreeNode(5)]
            puisque cur==None on continue
            
        -iteration : 
            cur = q.popleft()      cad cur == None , q=[TreeNode(4),TreeNode(5)]
            puisque cur==None on continue
            
        -iteration : 
            cur = q.popleft()      cad cur == TreeNode(4) , q=[TreeNode(5)]
            l = data.popleft()     cad l==None , data = [None,None,None]
            r = data.popleft()     cad r==None , data = [None,None]
            cur.left = TreeNode(int(l)) if l != "None" else None       cad cur.left == None
            cur.right = TreeNode(int(r)) if r != "None" else None      cad cur.left == None
            q.append(cur.left)     cad q=[TreeNode(5),None]
            q.append(cur.right)    cad q=[TreeNode(5),None,None]
        
       -iteration : 
            cur = q.popleft()      cad cur == TreeNode(5) , q=[None,None]
            l = data.popleft()     cad l==None , data = [None]
            r = data.popleft()     cad r==None , data = []
            cur.left = TreeNode(int(l)) if l != "None" else None       cad cur.left == None
            cur.right = TreeNode(int(r)) if r != "None" else None      cad cur.left == None
            q.append(cur.left)     cad q=[None,None,None]
            q.append(cur.right)    cad q=[None,None,None,None]
            
      -iteration : 
            cur = q.popleft()      cad cur == None , q=[None,None,None]
            puisque cur==None on continue
    
      -iteration : 
            cur = q.popleft()      cad cur == None , q=[None,None]
            puisque cur==None on continue
            
      -iteration : 
            cur = q.popleft()      cad cur == None , q=[None]
            puisque cur==None on continue
    
      -iteration : 
            cur = q.popleft()      cad cur == None , q=[]
            puisque cur==None on continue 
    
    puisque q==[] alors on a fini le while 
    return root cad TreeNode(1)
  """

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        
        q = collections.deque([root])  # creating queue for bfs
        res = []
        
        while q:
            curr = q.popleft()
            if not curr:  #  if curr==None
                res.append("None")
            else:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
                
        return ",".join(res)  #met une virgule entre chaque element de la list et en fait une phrase 
       
        
    def deserialize(self, dataString):
        if len(dataString) == 0: 
            return None

        data = collections.deque(dataString.split(","))    #creer queue apartir de la string data     
        root = TreeNode(int(data.popleft())) # creation root arbre 
        q = deque([root])
        
        while q :
            cur = q.popleft()
            if cur:
                l, r = data.popleft(), data.popleft()
                cur.left = TreeNode(int(l)) if l != "None" else None
                cur.right = TreeNode(int(r)) if r != "None" else None
                q.append(cur.left)
                q.append(cur.right)
        return root
    
