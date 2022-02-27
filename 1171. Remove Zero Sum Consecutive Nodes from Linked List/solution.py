"""
Tout d'abord comme il est dit dans les parenthese dans la description le input est une linked list cad un enchaimnement de node , bien que dans l'exemple on donne une array/list leetcode le transforme en une linked list.
la solution est la suivante : on s'interesse au prefix sum ([1,2,2,3,1]--> prefix sum : [1,3,5,8,9]) de la linked list pout seula on utilisera un hashtable(dict) ou les keys seront le prefix sum et les valeur seront les 
nodes de la linked list.
on utilise un prefix sum car si on prend par exemple la linked list suivante 1->2->(-3)->3->1 et on fait le prefix sum on recoit [1,3,0,3,4].L'idee c'est que a chaque fois qu'on recoit le meme resultat on a fait un 
variation de 0 , ici par exemple on a 3 puis 0 puis 3 cad que de 3 a 3 il ya une variation dont la somme est egale a 0. Notre dictionnaire est : {1:1,3:2,0:-3,3:3,4:1} on rajoute aussi une paire 0:0 au debut car si on
a une fluctuation dont la somme vaut 0 des le debut on aura pas de nbr qui se repete par exemple dans notre cas  1->2->(-3) est un fluctuation null or le prefix somme nous donne [1,3,0] on a pas de valeur qui revient 
sur soit donc on rajoute 0 au debut ce qui nous donne [0,1,3,0] et on voit que 0 revient sur soit donc on peut suprimmer tout les valeurs dans le dictionnaire qui correspondent au key qui sont apres 0 jusqu'a le zero 
qui se repette inclus :  {0:0,3:3,4:1} . apres avoir supprimer les valeurs dans le dictionnaire on peut construire une linked list avec les valeurs des keys restante. 
intuition from here : https://www.youtube.com/watch?v=tss5biw6ctI&ab_channel=leetuition
code from here : https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head): 
        cur = dummy = ListNode(0) # dummy est un node qui pointera sur le head  de la linked list (c'est le 0 qu'on rajoute) et cur ca va etre le node sur le quel on se situe actuellement 
        dummy.next = head
        prefix = 0 # prefix sum 
        dictio = collections.defaultdict()
        while cur:  # tant que le node cur n'est pas null cad qu'on est pas arrive a la fin 
            prefix += cur.val
            node = dictio.get(prefix, cur) # get(key,val) return the value of the key if doesn't exist val is a value to return if the specified key does not exist, here it's the current node . if the prefixsum already exist in the dictio dictio.get will give us the corresponding node of the first prefix sum (but not the current node that has the prefix that already exist)
            while prefix in dictio: #tant que le prfixsum est key dans le dict faire pop
                dictio.popitem()
            dictio[prefix] = node # on cree des paire prefixsum:node dans le dictio
            node.next = cur = cur.next # on avance le cur car on fait  cur=cur.next
        return dummy.next # on returne que le next du dummy (cad pas le zero qu'on a rajouter)
