"""remarque: tout les nombre sont a l'envers dans les listes donc quan on a une linked list : 2->4->3 ca veut dire 342 """

"""1er solution # recursive #TC O(max(len(l1),len(l2))) car chaque fonction fait max(len(l1),len(l2)) appel de O(1).    #SC O(max(len(l1),len(l2))) car on fait max(len(l1),len(l2)) appel (ya aussi la 
creation de la linked list donc c'est deux fois max(len(l1),len(l2)) ce qui revient a O(max(len(l1),len(l2))) .
le code est d'ici : https://leetcode.com/problems/add-two-numbers/discuss/1102/Python-for-the-win
l'idee est de passer sur les deux linked list pour avoir le nbr de chaqu'une de ces dernieres puis les additionner et ensuite de cree une linked list avec le resultat.
pour tensformer un nombre en une linked-list ici on veut  le garder a l'envers dans la linked-list ex si on a 807 alors ca donne 7->0->8. Donc pour cela il va falloir s'occuper des unite puis des dizaine,etc..
pour cela ici on prend le nombre ex 807 est on fait moduler 10 ce qui nous donne 7 puis comme 807>9 il ya aussi des dizaine a s'occuper donc apres avoir cree un node pour 7 sont next sera egale a l'appele de la fction 
sur 807//10 cad sur 80 (en faite l'idee c'est de creer un node pour les unites puis de troncer au dizaine puis recommencer a prendre l'uniter du nombre qu'il reste)"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node):   #transforme la linked list en un nombre
            # si on a 2->4->3 alors on fait 2 + 10*(4+10*(3+10*0)) cad 2+10*(34) cad 342
            return node.val + 10 * toint(node.next) if node else 0 
        def tolist(n): # transforme un nbr en une linked list
            node = ListNode(n % 10)   # creer un node sur l'unite
            if n > 9:    # si n est un nombre composer de au moins deux chiffres 
                node.next = tolist(n // 10)     
            return node 
        return tolist(toint(l1) + toint(l2)) 
    
    
"""2 eme solution #iterative  #un seul passage  #TC O(max(len(l1),len(l2)))  #SC O(max(len(l1),len(l2))) car new linked list.
l'idee est d'additionner les nodes , l'addition peut etre supperieur a 9 cad dans ce cas on aura une retenue pour la prochaine addition.
le code est d'ici (il ya aussi des explications) : https://leetcode.com/problems/add-two-numbers/discuss/352181/Python3-Carry-sum10
"""
class Solution: 
    def addTwoNumbers(self, l1, l2):
        dummy = cur =ListNode(0)  #dummy est cur sont des etiquette pour la meme adresse qui contient une node de valeur 0  (il sont des pointeurs sur la nouvelle liste)
        carry = 0
        while l1 or l2 or carry: # or carry est important car si on a fini l1 et l2 mais il nous reste une retenue on veut comme meme rentrer dans le while
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10) #on fait modulo 10 pour prendre que les unites
            cur = cur.next # on fait avancer cur
            carry //=10  #carry = carry // 10 cad on prend la dizaine 
        return dummy.next  # on return le node apres dummy qui a etait rajouter juste pour faciliter l'algo
