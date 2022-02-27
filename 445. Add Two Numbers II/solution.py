"""premier solution (simple la deuxieme est meilleur) # TC O(n1+n2)  #SC O(n1+n2)
cette solution utilise 2 stack , on rentre tout simplement tout les chiffres de chaque liste dans une stack, puis a la fin on pop des 2 stack en meme temps et on additionne on prendra en compte les retenue  """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        # mettre les chiffres de chaque list dans leur stack respective
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next         
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        # pop et addition d'un chiffre de s1 et un de s2 en prenant compte de la retenue
        carry, head = 0, None
        while st1 or st2 or carry:    # il faux que au moins un stack ne soit pas vide ou que il ya une retenue et donc meme si il reste plus rien dans les stack il faut la rajouter
            d1, d2 = 0, 0
            d1 = st1.pop() if st1 else 0       # si la stack est vide alors le chiffre sera 0 
            d2 = st2.pop() if st2 else 0
            digit = (d1 + d2 + carry) % 10     
            carry = (d1 + d2 + carry) // 10
            head_new = ListNode(digit)           # ex si le resultat nous donne 7 puis 0 puis 3 alors :
            head_new.next = head                 # 7->None puis 0->7->None puis 3->0->7->None
            head = head_new                      #  ce qui nous donne le nbr 307
              
        return head
    
"""deuxieme solution #TC O(n1+n2) #SC O(1) 
on fait reverse sur les linked list puis on additionne en prennant compte des retenues """

class Solution:
    def reverse(self,head):
        prev = None
        while head:
            nextN = head.next 
            head.next = prev
            prev = head
            head = nextN
        return prev
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        carry, head = 0, None
        while l1 or l2 or carry:
            
            total = carry
            if l1:
                total+=l1.val 
                l1 = l1.next 
            if l2:
                total+=l2.val 
                l2 = l2.next 
                
            carry = total//10 
            # create a list from the end
            head_new = ListNode(total%10)   
            head_new.next = head  
            head = head_new
            
        return head   
