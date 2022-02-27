"""
=> DFS (and little bit of BFS):

I) INTRODUCTION  : 

DFS et BFS constitues 2 differentes facons de traverser un graphe : 

-DFS soit Depth-first search traverse le graphe dans la profondeur alors que BFS traverse le graphe dans la largeur. 
dans un graph (ou un n-ary tree avec n>2) DFS a 2 variation pre-order et post-order . Quand il s'agit d'un binary tree alors DFS existe sous forme de pre-order (NLR) in-order(LNR) pre-order(LRN) 
(il existe aussi reverse pre-order (NRL) ,reverse in-order(RNL), reverse post-order(RLN)). D'apres mes recherche quand on parle de graph et de DFS de maniere generale on parle de pre-order 
(mais bien entendue que si on est precis alors DFS peut etre pre et post order ds un graph (in order dans un graph d'apres mes recherches n'existe pas ou on ne l'implemente pas car pas adequate)

(leetcode (https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/916/): Note that here is no standard definition for in-order traversal in n-ary trees. It probably only makes sense for binary trees. While there are several different possible ways that one could define in-order traversal for n-ary trees, each of those feels a bit odd and unnatural and probably not terribly useful in practice.)

et si on est dans un binary tree alors il ya pre-order in-order et post-order ) 
-BFS est aussi appeler level-order search (je pense qu'on l'appel comme ca quand on l'implemente ds un binary tree mais sinon ds un graph on l'appel BFS)


app : 
         
               18              DFS :    -pre-order :  18 15 40 8 7 50 9 30 100 40          BFS : 18 15 30 40 50 100 40 8 7 9
           /       \                    -in-order:  8 40 7 15 9 50 18 100 30 40
         15         30                  -post-order:  8 7 40 9 50 15 100 40 30 18                                              
        /  \        /  \                                                                            
      40    50    100   40                                                                  
     /  \   /
    8   7  9 
 

II ) UTILISATION :

In Graph theory, the depth-first search algorithm (abbreviated as DFS) is mainly used to:
-Traverse all vertices in a “graph”;
-Traverse ALL PATHS between any two vertices in a “graph”.


In Graph theory, the primary use cases of the “breadth-first search” (“BFS”) algorithm are:
-Traversing all vertices in the “graph”;
-Finding THE SHORTEST PATH between two vertices in a graph where all edges have equal and positive weights.


III) IMPLEMENTATION : 

->DFS IN BINARY TREE : 

    1) recursive way  : 
 
        def Inorder(root):
            if root:		
                Inorder(root.left)	
                print(root.val)  # print the data of node
                printInorder(root.right)

        def Postorder(root):
            if root:
                Postorder(root.left)
                printPostorder(root.right)	
                print(root.val)  #print the data of node

        def printPreorder(root):
            if root:	
                print(root.val)      # print the data of node
                printPreorder(root.left)
                printPreorder(root.right)

        TC: for all fct is O(n) car on traverse les nodes de l'arbre
        SC: for all fct is O(h) (size of the stack) avec h la hauteur de l'arbre qui peut etre entre logn et n donc ds le pire des cas O(n)

    2) iterative way : 

        on utilisera un stack/LIFO pour implementer DFS de facon iterative 

     --> def preorderIterative(root):  # NLR

            if root : 
                stack = deque()

                # start from root node  
                curr = root  

                # run till stack is not empty or current is not NULL  # current sera l'enfant de gauche a chaque fois
                while stack or curr :

                    # tant que curr n'est pas null
                    while curr:

                        print(curr.data, end = " ")  # visit node

                        if (curr.right != None):    # put right child in stack
                            stack.append(curr.right)

                        curr = curr.left            # go to left child

                    # We reach when curr is NULL (cad on a fini tout les enfant de gauches), so We take out a right child from stack
                    if (len(stack) > 0):
                        curr = stack[-1]
                        stack.pop()

        TC : O(n)
        SC : O(h) avc h hauteur, l'avantage ici c'est que ca n'utilise pas le stack du cpu car pas de recursion donc c'est plus rapide et il ya pas de limitation de call comme avec la recursion.


    --> def inorderIterative(root):   #LNR

            if root :
                stack = deque()

                # start from the root  
                curr = root

                # if the current node is None and the stack is also empty, we are done
                while stack or curr:

                    # if the current node exists, push it into the stack and move to its left child
                    if curr:
                        stack.append(curr)
                        curr = curr.left
                    else:
                        # otherwise, if the current node is None, pop an element from the stack,
                        # print it, and finally set the current node to its right child
                        curr = stack.pop()
                        print(curr.data, end=' ')
                        curr = curr.right

        TC : O(n)
        SC : O(h) avec h hauteur, l'avantage ici c'est que ca n'utilise pas le stack du cpu car pas de recursion donc c'est plus rapide et il ya pas de limitation de call comme avec la recursion.
        
    -->  def postOrderIterative(root):  # LRN    # for more explanation  : https://www.geeksforgeeks.org/iterative-postorder-traversal/
            if root :
                # Create two stacks
                s1 = deque()
                s2 = deque()

                # Push root to first stack
                s1.append(root)

                # Run while first stack is not empty
                while s1:

                    # Pop an item from s1 and append it to s2
                    node = s1.pop()
                    s2.append(node)

                    # Push left and right children of removed item to s1
                    if node.left:
                        s1.append(node.left)
                    if node.right:
                        s1.append(node.right)

                    # Print all elements of second stack
                while s2:
                    node = s2.pop()
                    print(node.data,end=" ")
                    
          TC : O(n)
          SC : O(n)
        
    
          il existe une facon de faire inorder preorder et postorder de facon iterative en O(1) space cette implementation est tres compliquer (Morris traversal) pour en savoir plus :
          https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/?currentPage=1&orderBy=most_votes&query=
          

=> DFS dans graph : 
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles (a node may be visited twice). To avoid processing a node more than once we use a boolean visited array. 
on va parler que du DFS preorder car c'est le plus utiliser. 

   1)recursive way : 
       
        visited = set() # Set to keep track of visited nodes.
        def dfs(visited, graph, node):
            if node not in visited:
                print (node)
                visited.add(node)
                for neighbour in graph[node]:
                    dfs(visited, graph, neighbour)
                    
    TC : O(V+E)  SC : O(V)
    
   2) iterative way : 
    
    # class Graph:
    #	 def __init__(self,V): # Constructor
    #		self.V = V	 # No. of vertices
    #		self.adj = [[] for i in range(V)] # adjacency lists


	prints all not yet visited vertices reachable from s
	def DFS(self,s):		 
		# Initially mark all vertices as not visited
		visited = [False for i in range(self.V)]

		stack = []

		# Push the current source node.
		stack.append(s)

		while stack :
			# Pop a vertex from stack and print it
			s = stack[-1]
			stack.pop()

			# Stack may contain same vertex twice. So
			# we need to print the popped item only
			# if it is not visited.
			if (not visited[s]):
				print(s,end=' ')
				visited[s] = True

			# Get all adjacent vertices of the popped vertex s
			# If a adjacent has not been visited, then push it
			# to the stack.
			for node in self.adj[s]:
				if (not visited[node]):
					stack.append(node)

       
     TC : O(V+E)  SC : O(V)

"""

"""
petit rappel : binary tree c'est un arbre que chaque node a de 0 a 2 node , un binary search tree c'est un binary tree dont les enfants de gauche sont inf ou egale et les enfant de gauche sont sup ou egale 
ex of BST : 
     10
   /   \
  5     40
 /        \
1          50

"""

""" #first sol #Binary search tree #DFS recursive  #TC O(n)  #SC O(h) (function stack call) with h the height of the tree can be in worst case O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:  #pre order dfs (on peut aussi utiliser inorder ou post order car ce qui nous interrese c'est le resultat final l'ordre n'est pas important)
        if not root: 
            return 0
        ans = root.val if root.val >= low and root.val <= high else 0
        if root.val > low:   # dans ce cas il faut aller coter gauche car on a besoin des valeurs plus petites
            ans += self.rangeSumBST(root.left, low, high)
        if root.val < high:  # dans ce cas il faut aller coter droit car on a besoin des valeurs plus grandes
            ans += self.rangeSumBST(root.right, low, high)
        return ans
        
""" #2nd sol #Binary search tree #DFS iterative  #TC O(n)  #SC O(h) with h the height of the tree can be in worst case O(n)
"""       


class Solution(object):
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
