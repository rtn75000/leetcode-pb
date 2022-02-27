"""
ici on nous demande de faire TC O(nlogn) avec un SC de O(1) , normalement cela correspond a heap sort mais avec une linked list heap sort coutera n^2logn car pour trouver un element dans la 
linked list ca coute O(n) pas comme dans la list normale et si on convertie la linked list en list en copiant les elements de la linked list dans une liste alors SC O(n) car on utilise un extra
n space pour la list , donc heap sort n'est pas la solution. merge sort sur la list quand a lui coute O(nlogn) mais le merge sort standard cad la recursion top down qu'on connait coute O(logn) 
d'extra space pour le stack de la recursion, donc ici techniquement ca ne correspond pas . il ya une version de merge sort qui est bottom up qui marche de facon iterative et non recursive et donc
utilise pas d'extra space pour le stack , cette version est donc complatible avec les exigences de la consigne.

moi je vais comme meme ecrire le merge sort top-down cad le recursive qui coute O(log n) en extra space car c'est un cas basique pour le sort d'une linked list. 
comme dans le merge sort de la list (voir ma solution : https://leetcode.com/problems/sort-an-array/) ici aussi on doit d'abord diviser en deux de facon recursive la linked list j'usqu'a qu'on 
obtient des linked list composer d'un seul membre, puis ensuite on doit fusionner ces linked list en les trinant a chaque fois (fct merge). dans les linked list il ya pas d'idx donc pour
trouver le milieu de la linked list on utilisera la technique du slow et fast pointers. on aura dans notre algorithme 3 fonction : 
la fonction principal sortList qui s'appel de facon recursive sur les deux moitier de la linked list. cette fct utilise une fction get mid pour trouver le milieu de la linked list puis 
s'appel recursivement sur chaque moitier et apres utilise la fonction merge qui permet de fusionner deux linked list en conservant l'ordre croissant.
le code et explication d'ici : https://leetcode.com/problems/sort-list/discuss/892759/Python-O(n-log-n-log-n)-merge-sort-explained

TC : O(n*logn) car on divise par 2 a chaque fois donc logn iteration et chaque teration coute n du a la fonction merge et SC O(n) car merge utilise une nouvelle linked list ou les elements seront
fusionner. 

je vais pas implementer bottom-up car il est bcp plus compliquer rare sont les chances d'avoir cette question en interview.
quelque article sur bottom-up : 
https://www.interviewbit.com/tutorial/merge-sort-algorithm/
https://www.geeksforgeeks.org/iterative-merge-sort/
https://leetcode.com/problems/sort-list/discuss/46712/Bottom-to-up(not-recurring)-with-o(1)-space-complextity-and-o(nlgn)-time-complextity
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:       # condition d'arret: si vide ou que un element retourner vide ou un element (car c'est forcement trier)
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:  # cad tant qu'il ya encore deux element apres fast
            slow = slow.next                 # on avancera slow de une position
            fast = fast.next.next            # on avancera fast de deux positions
        # a la fin de la boucle slow sera a la moitier de fast qui pointera sur le dernier (si nombre impaire d'element) ou avant dernier (si nbr impaire d'element) element
        # ex si on a 6 elements (paire): 
        #    1 -> 2 -> 3 -> 4 -> 5 -> 6   alors si fast avance de deux et slow de 1 a la fin ca donne  1 -> 2 -> 3 -> 4 -> 5 -> 6   donc slow pointe sur le 3e elements soit la moitier de 6
        #                                                                                                        ^         ^                                                       
        #                                                                                                      slow       fast                      
        # ex si on a 5 elements (impaire): 
        #    1 -> 2 -> 3 -> 4 -> 5    alors si fast avance de deux et slow de 1 a la fin ca donne  1 -> 2 -> 3 -> 4 -> 5    donc slow pointe sur le 3e elements c'est donc l'element qui
        #                                                                                                    ^         ^        se trouve exactement a la moitier (2 elements de chaque cote)   
        #                                                                                                   slow       fast       
        
        mid = slow.next  # cad dans le cas impaire mid va etre le premier element de la deuxieme partie chaque partie aura le meme nombre d'element , dans le cas impaire mid sera le premier
                         # element de la deuxieme partie qui aura un element de moins que la premiere .
            
        slow.next = None # cette ligne est tres importante car elle permet de couper la list en deux , car maintenant slow.next pointe sur null donc il ya plus de continuite mid va etre le head
                         # de la 2e partie . si on fait pas cette ligne on va avoir une boucle interminable car on va appeler a l'infi la recursion car on va jamais atteindre la condition 
                         # d'arret vu que a chaque fois on fait a nouveau la recursion sur toute la liste sans vraiment la diviser en deux.
        return mid
    
    def merge(self, head1, head2):
        
        dummy = tail = ListNode(None)  # creation d'une nouvelle list ou les elements des 2 linked list seront fusionner donc extra space qui peut faire max O(n)
                                       # on cree deux pointeurs qui pointe sur le head de la nouvelle linked list . le pointeur dummy on ne le deplacera pas ca nous permet a la fin de rendre 
                                       # le debut de la nouvelle linked list. le deuxieme pointeur tail lui nous permettra d'avancer dans la nouvelle linked list. 
                
        while head1 and head2:         # cad tant que les 2 linked list a fusionner ont les deux encore des elements a fusionner 
            if head1.val < head2.val:  # si la valeur de l'element actuelle de la premiere linked liste est plus petite que la valeur de l'element actuelle de la deuxieme linked list alors :
                tail.next=head1        # on ajoute l'element de la premiere linked list dans notre nouvelle linked list 
                head1 = head1.next     # on avance d'une element dans la premiere linked list
            else:   # if head1.val >= head2.val:
                tail.next = head2
                head2 = head2.next
            tail = tail.next           # dans tout les cas on doit faire avancer le pointeur de la nouvelle list apres lui avoir ajouter un element.
        
        # on arrive a cette ligne si une des deux linked list a ete entierement fusionner , dans ce cas il suffit simplement d'ajouter tout les autre elements de la linked list qui n'est pas vide 
        # a notre nouvelle linked list sela ce fait en pointant simplement sur le premier elements de la linked list non vide 
        tail.next = head1 or head2     # cad si head1 est vide alors c'est equivalent a False et donc on tail.next = head2 (si head 1 pas vide alors tail.next = head1 )
        return dummy.next #on retourne le premier element la nouvelle linked list qui a fusionner les 2 linked list. 
            
            
                
                
                                                                                                                                                                                            
                    
                    
                    
                    

