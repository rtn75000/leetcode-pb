""" #iterative #O(n) TC  #O(1) SC
code et explication d'ici : https://leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained
l'idee et de coupe la liste en 2 (a la moitier, si impaire la moitie sera la moitier superieurex 5 on divise en 3 et 2) puis on inverse la 2eme liste obtenue puis on fusionne (merge) les 2 listes . 
ex 1->2->3->4->5, premiere etape : 1->2->3 et 4->5 2eme etape : 5->4, 3eme etape: 1->5->2->4->3 
pour trouver le milieu de la liste on peut soit faire deux passage le premier qui compte les elements de la liste le deuxieme on repasse sur la liste jusqu'au [nombre de termes] / 2 (arrondire vers le haut si impaire)
node. On peut aussi faire ca en un passage en utiliser 2 pointeur , un qui passe de un en un et l'autre deux node par deux nodes une fois que ceux dernier arrivera a la fin de la liste le premier se trouvera au milieu
de cette liste (dans ce code on utilise la 2eme technique )
Time complexity is O(n), because we first do O(n) iterations to find middle, then we do (O(n/2)=)O(n) iterations to reverse second half and finally we do O(n) iterations to merge lists. Space complexity is O(1)."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #step 1: find middle
        if not head: return []  # if head==None : not head ==true 
        slow, fast = head, head
        #tant qu'il existe encore deux elements 
        while fast.next and fast.next.next:    #verifie qu'il rest au moins encore 2 element apres fast
            slow = slow.next  # avance slow de 1
            fast = fast.next.next  # avance fast de 2
        
        #  1 -> 2 -> 3 -> 4 -> 5 -> 6    
        #  ^         ^         ^
        # head     slow      fast
        
        # step 2: reverse second half
        # imperativement : voir reverse list pb 206 leetcode ya des explication la-bas
        prev, curr = None, slow.next # on veut inverse la 2eme partie seulement donc le premier node a inverser est le premier apres le milieu de la liste initiale 
        while curr:
            
            nextt = curr.next  
            # 1er iteration :                                                                                  | 2eme iteration :                                                                         |3eme iteration:
            
            # 1...3-> 4 -> 5 -> 6               curr: [4,5,6]   head: [1,2,3,4,5,6]    prev: null              |   1->...->4           5 -> 6           curr: [5,6]     fast: [5,6]   head: [1,2,3,4]     |   1->...-> 4 <- 5          6      nextt: None
            #         ^    ^                    fast: [5,6]     nextt: [5,6]           slow: [3,4,5,6]         |           ^           ^    ^           nextt: [6]      prev: [4]     slow: [3,4]         |                 ^          ^   
            #       curr nextt                                                                                 |         prev        curr  nextt                                                          |                prev      curr  
             
            curr.next = prev  
            
            #    1..->4->None   -X-> 5 -> 6      curr: [4]     fast: [5,6]   head: [1,2,3,4]                   |   1->...-> 4 <-------- 5 -X-> 6           curr: [5,4]     fast: [5,4] head: [1,2,3,4]    |   1->...-> 4 <- 5 <- 6
            #         ^              ^           nextt: [5,6]  prev: null    slow: [3,4]                       |            ^           ^      ^           nextt: [6]      prev: [4]   slow: [3,4]        |                 ^    ^
            #       curr           nextt                                                                       |           prev        curr  nextt                                                        |               prev  curr
            
            prev = curr   
             
            #     1..-> 4 ->None    5 -> 6            curr: [4]     fast: [5,6]   head: [1,2,3,4]              |   1->...-> 4 <- 5          6           curr: [5,4]     fast: [5,4]    head: [1,2,3,4]    |   1->...-> 4 <- 5 <- 6
            #           ^           ^                 nextt: [5,6]  prev: [4]    slow: [3,4]                   |                 ^          ^           nextt: [6]      prev: [5,4]    slow: [3,4]        |                      ^
            #      curr,prev     nextt                                                                         |             prev,curr    nextt                                                           |                   prev,curr
            
            curr = nextt   
            
            #       1..-> 4 ->None    5 -> 6        curr: [5,6]     fast: [5,6]   head: [1,2,3,4]              |   1->...-> 4 <- 5          6           curr: [6]       fast: [5,4]    head: [1,2,3,4]    |   1->...-> 4 <- 5 <- 6     curr: None
            #             ^           ^             nextt: [5,6]    prev: [4]     slow: [3,4]                  |                 ^          ^           nextt: [6]      prev: [5,4]    slow: [3,4]        |                      ^
            #            prev     curr,nextt                                                                   |               prev     curr,nextt                                                        |                     prev
            
             
            # after all iteration :
            #    None <- 4 <- 5 -< 6         curr: null   fast: [5,4]    head: [1,2,3,4]
            #                      ^         nextt: null  prev: [6,5,4]  slow: [3,4]    
            #                    prev      
            
            
        #step 3: merge lists    
        slow.next = None       # cad slow : [3]   cad  la liste sera divise en deux 1->2->3 puis 6->5->4 si on divise pas la liste ca va cree une boucle dans la prochaine etape (voir explication dans le prochain while)
 
        head1, head2 = head, prev  # 2 heads pours les 2 moitiers de la liste
        while head2:    # la taille de la 2eme partie est tjrs inferieure ou egale a la taille de la deuxieme donc le premier qui se termine sera head2 
            
            #    1 -> 2 -> 3        6 -> 5 -> 4                    | | si on coupe pas la liste avant ca donne ca :
            #    ^                  ^                              | |      1->2->3->4<-5<-6            |
            #  head1              head2                            | |      ^              ^            |
            #                                                      | |    head1          head2          |
            
            nextt = head1.next
            
            #    1 -> 2 -> 3        6 -> 5 -> 4                    | |     nextt: [2,3,4]               |     nextt : [5,4]          |    nextt: [3,4]             | nextt : [4]             | nextt : [4]       |  nextt : None 
            #    ^    ^             ^                              | |                                  |                            |                             |                         |                   |
            #  head1 nextt        head2                            | |                                  |                            |                             |                         |                   |
             
            head1.next = head2
            
            #    1  -X-> 2 -> 3        6 -> 5 -> 4                 | |     1   2->3->4<-5<-6            |    2->3->4<-5 <-X- 6<-1    |   1->6->2 -X->3->4<-5       |  1->6->2->5 -X-> 4<-3   |  1->6->2->5->3->4 | ici il ya une cycle dans la liste car on 
            #    ^       ^             ^                           | |     |               ^            |    ^               |       |         |           ^       |           |         ^   |                   | dit a 4 de pointer sur 4 donc cela 
            #  head1   nextt        head2                          | |     |               |            |    |               |       |         |           |       |           |         |   |                   | retourne une errreur. 
            #    |                    ^                            | |     -----------------            |    -----------------       |         -------------       |           -----------   |                   |  
            #    |                    |                            | |                                                                                                                                           |  
            #    ----------------------                            | |                                                                                                                                           |
            
            head1 = head2
             
            #   2 -> 3      1-> 6 -> 5 -> 4                        | |     1   2->3->4<-5<-6            |   1->6->2->3->4<-5         |  1->6->2->5->4<-3           |  1->6->2->5->3->4       |  1->6->2->5->3->4   |  1->6->2->5->3->4 
            #   ^               ^                                  | |     |               ^            |         ^                  |           ^                 |              ^          |                 ^   |                 ^
            # nextt        head1,head2                             | |     |           head1,head2      |    head1,head2             |      head1,head2            |         head1,head2     |         head1,head2 |            head1,head2
            #                                                      | |     -----------------
            head2 = nextt
            
            #   2 -> 3      1-> 6 -> 5 -> 4                        | |     1   2->3->4<-5<-6            |  1->6->2->3->4<-5          |  1->6->2->5->4<-3           | 1->6->2->5->3->4        |  1->6->2->5->3->4   |  1->6->2->5->3->4   head2:None (fin while)
            #   ^               ^                                  | |     |   ^           ^            |        ^        ^          |           ^     ^           |             ^  ^        |                 ^   |                 ^
            # head2,nextt     head1                                | |     |  head2      head1          |       head1    head2       |         head1 head2         |          head1 head2    |         head1,head2 |               head1
            #                                                      | |     -----------------            |                            |                             |
            #etc...(loop)
