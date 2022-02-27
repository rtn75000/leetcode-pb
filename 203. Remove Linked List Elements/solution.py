"""#iterative solution #TC:O(n) #no extra space
from here : https://leetcode.com/problems/remove-linked-list-elements/discuss/158651/Simple-Python-solution-with-explanation-(single-pointer-dummy-head).
a list of edge cases that we need to consider :
-The linked list is empty, i.e. the head node is None.
-Multiple nodes with the target value in a row.
-The head node has the target value.                                                    |   for those edge cases 
-The head node, and any number of nodes immediately after it have the target value.     |   we will use a dummy
-All of the nodes have the target value.
-The last node has the target value.
""" 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1,head) #creating a ListNode with a val=-1 and that point on head 
        current_node = dummy_head
        while current_node.next != None:  # cad tant qu'on est pas arriver au dernier node
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next   # on avance de node
                
        return dummy_head.next
    
    
"""solution 2  #recursive #TC/SC: O(n)
from here: https://leetcode.com/problems/remove-linked-list-elements/discuss/273908/easy-recursive-in-python

l'idee est la suivante : la recursion se fait de la sorte que chaque node qui a pour valeur val alors ce node sera egale a la recursion de son next (cad ici on supprime ce node car on dit qu'il est egale a la recursion
de son next et pas que son next est egale a la recursion de son next) , alors que si il n'est pas egale a val node.next sera egale a la recursion de son next.
prenons pour exemple la linked-list: node(1)->node(2)->node(3)->None et la val==2 alors la recursion sera :

        removeElements(node(1),2):       node(1).next = removeElements(node(1).next,2) =  removeElements(node(2),2)
                                                                                                ^
                                                                                            return node(3)
3(se lit de bas en haut)==> cad node(1)->node(3)->None , en remontant de la recursion on recoit le node(1) qui est la tete de la nouvelle linked list
       
        removeElements(node(2),2):       node(2) = removeElements(node(2).next,2) = removeElements(node(3),2)
                                                                                           ^
                                                                                     return node(3)
        
        2==> cad node(2)=node(3)->None donc on a supprimer node 2; ensuite en remontant a la fin de la recursion removeElements(node(2),2) retourne node(3)
                                                                                                               
                                                                                                               
                                                                                                               
        removeElements(node(3),2):       node(3).next = removeElements(node(3).next,2) = removeElements(None,2) 
                                                                                               ^
                                                                                           return None  
                                                                                           
        1==> cad node(3)->None  ; ensuite en remontant a la fin de la recursion  removeElements(node(3),2) retourne node(3) 
                                                                                                ^
                                                                                           return None   
        removeElements(None,2) :         return None 



class Solution:
    def removeElements(self, node: Optional[ListNode], val: int) -> Optional[ListNode]:
        if node == None:
            return None
        if node.val == val:
            node = self.removeElements(node.next,val)
        else:
            node.next = self.removeElements(node.next,val)
        return node
"""   
