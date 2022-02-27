"""la question est simple si on pouvait avoir un TC O(n+m) car on aurait fait merge qui coute O(n+m) puis binary search qui coute log(n+m) donc en tout O(n+m+log(n+m)) cad  O(n+m).

explication de la mediane dans un cas normale si on a une liste de nombre qui sont ordonner dans l'ordre croissant alors si on a un nombre paire d'element on separe en deux la liste il y'aura n/2 element de chaque cote
et on fait la moyenne des deux element qui sont au centre ex [2,5,8,10,13,14] la mediane est egale a (8+10)/2=9 . si on a un nombre impaire on peux separer la liste en deux une partie avec (n/2)+1 et une autre (n/2)-1 
et on prend le dernier element de la premier partie ex : [3,4,6,8,14,16,18] on separe en deux : [3,4,6,8] et [14,16,18] la mediane sera 8 le dernier element de la premiere partie.

ici il ya deux list sur lequel on veut trouver la mediane si les deux liste etaient rassemble. on veut que TC soit O(log(n+m)) on va voir un algo meilleur que TC est egale a O(log(min(n,m))) cad il sera egale a log de la plus petite liste. 
explication de l'algo :
comme on a vu precedement la mediane separe en deux partie equitable une liste donc ici il ya len(nums1) + len(nums2) element . il y'aura de chaque cote la moitie si c'est paire(la mediane sera la moyenne des 
deux elements du milieu) et si c'est impaire le cote gauche aura un element en plus du cote droit (cette element sera la mediane). on doit donc avoir (len(nums1) + len(nums2)+1)//2 element du cote gauche car si 
len(nums1) + len(nums2) est paire alors  (len(nums1) + len(nums2)+1)//2 nous donne exactement la meme chose que  (len(nums1) + len(nums2))/2 cad la moitie (ex 4+1//2==4/2 (=2)) et si  len(nums1) + len(nums2) est impaire 
alors (len(nums1) + len(nums2)+1)//2 nous donne aussi l'element qui represente la moitie   (ex : (11+1)//2 = 6 cad ca inclu 6 qui est l'element qui separe en deux partie equitable 11). donc on devra prendre dans notre 
cas des elements (possible 0 element si list1>list2) de la premiere liste et des elements de la deuxieme list (possible 0 element si list1<list2). l'algorithme se concentre sur une liste des deux car une fois qu'on 
sait combien d'element on preleve d'une list on sait que le reste des elements sont a prelever de la deuxieme liste pour avoir (len(nums1) + len(nums2)+1)//2 element (les elements sont ordonnes dans l'ordre croissant
on preleve de gauche a droite bien entendu). on choisira de travailler avec la plus petite liste pour gagne en TC. l'algo coupe cette liste au milieu (cela est repete jusqu'a ce qu'on trouve le nombre exacte d'element 
qui font partie du cote gauche de la mediane) si on voit que le nombre d'element a gauche sont insuffisant pour trouver la mediane il faut donc prelever des element de la deuxieme moitier, on coupera la moitie droite
en deux et on regarde si on a trop d'element alors on prend la moitier de gauche si on en a pas assez on prend celle de droite. sur la moitier prelever on recommence le meme processus jusqu'a qu'on trouve la mediane. 
la mediane est trouver quand on a reussi a couper en deux le total d'elements des deux list de facon que tout les element a gauche sont plus petit que les elements a droite . ex si on a:
l1= a1 a2 a3 a4 a5 et l2=b1 b2 b3 b4 b5 b6 alors si a un moment dans l'algo on a a1 a2 a3 a4 | a5  et  b1 b2 | b3 b4 b5 b6 ou le trait separe entre les element du cote gauche de la mediane et les element du cote droit 
cad qu'on a en faite a1 a2 a3 a4 b1 b2 du cote gauche (on s'en fou de l'ordre car a la fin comme on sait que l1 et l2 sont dans l'odre croissant alors on verifie qui est le max entre a4 et b2 celui qui le plus grand
est forcement le numero qui se trouve le plus a droite de la partie gauche cad c'est lui la mediane dans notre cas qui est impaire (si c'est paire on prend aussi le num le plus a gauche de la partie droite cad le 
min entre a5 et b3 puis on calcule la moyenne entre maxa4,b2 et min a5,b3)) et le reste cote droit :
a1 b2 a3 a4   |  a5                  on doit verifier que a4 soit plus petit que b3 (pas besoin de verifier a4<a5 car l1 est dans l'ordre croissant)
b1 b2         |  b3 b4 b5 b6         on doit verifier que b2 soit pus petit que a5 ((pas besoin de verifier b2<b3 car l2 est dans l'ordre croissant))

si les deux condition sont bonne on a la mediane car on a elements a agauche et a4<b3 ainsi que b2<a5.

app : l1= a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12  
      l2= b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14
      il ya en tout 26 element on doit donc avoir en tout du cote gauche (len(l1) + len(l2)+1)//2 = (26+1)//2 = 27//2 == 13 elements 
      au debut comme l1 est la plus petite liste on prend la moitier des element de l1 cad P1=6 (start(0)+end(12)//2 =6),
      le reste on preleve chez l2 cad P2 = ((total_len + 1) // 2) - P1 = ((26+1)//2)-6 = 13-6 = 7,
      on a donc : l1= a1 a2 a3 a4 a5 a6 | a7 a8 a9 a10 a11 a12              
                      ^                    ^                   ^
                start= idx 0          P1=idx6               end =idx 12 (un apres le drenier qui est 11 car commence a 0)
                
                  l2= b1 b2 b3 b4 b5 b6 b7 | b8 b9 b10 b11 b12 b13 b14  
                                             ^
                                         P2=idx 7
      on doit verifier que a6<b8 et que b7 < a7 : l'element a gauche de la mediane dans l1 sera nommer left_1 a droite right_1 a gauche de la mediane dans l2 sera left_2 a droit right_2 :
      
 -> left_1 = nums1[P1-1] que si P1 est different de 0 car si il vaut 0 ca veut dire que on prend rien dans l1 donc la mediane est comme ceci l1= | a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 donc on va dire que l'element 
 a gauche de la mediane vaut -l'infini comme ca c'est sur que left_1< right_2 . ici left_1 = nums1[6-1] = a6
 -> left_2 = nums2[P2-1] = nums2[7-1] = b7  (si P2 egale 0 cad que on a tout pris dans l1 alors left=-inf comme ca c sur que left_2<right_1)
 -> right_1 = nums1[P1] que si P1 est different de len(nums1) car si P1==len(nums1) ca veut dire que on a pris tout p1 donc la mediane est comme ceci l1= a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 | donc on va dire
 que  l'element a droite de la mediane(right_1) vaut l'infini comme ca c'est sur que left_2 <right_1  . ici right_1 = nums1[P1]=nums1[6]=a7
-> right_2 = nums2[P2] = nums[7]=b8  ( si P2 egale len(nums2) ca veut dire que on a tout pris dans l2 donc on dit que a droite de la mediane cad right_2 vaut l'inf comme ca c'est sur que left_1 < right_2 )

option1:
si left_1 > right_2 soit a6>b8 ca veut dire que on doit prendre moins d'element de l1 et plus de l2 car il ya des element de l2 qui sont du cote droit de la mediane est pourtant plus petit des element de l1 du cote
gauche de la mediane donc on va maintenant coupe en deux l1 et s'occuper de la premier partie c'est pour cela que dans ce cas  end = P1 - 1  d'ou maintenant end=6-1=5:
l1= a1 a2 a3 a4 a5 a6 | a7 a8 a9 a10 a11 a12              
    ^               ^
start= idx 0       end=idx 5          
dans le prochain while P1=(start + end) // 2  cad P1=(0+5)//2 =2 soit :    (P2 vaut ce qui reste a prendre cad P2=(26+1)//2-2=13-2=11 donc l2= b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11|b12 b13 b14)
l1=     a1  a2| a3   a4  a5  a6  a7 a8 a9 a10 a11 a12     ( donc on a pris la premier moitier )                                                                                    ^
         ^       ^            ^                                                                                                                                                   P2=idx11
start= idx 0   P1=idx2    end=idx 5   

option 2 :
si left_2 > right_1 soit b7>a7 ca veut dire que on doit prendre plus d'element de l1 et moins de l2 car il ya des element de l1 qui sont du cote droit de la mediane est pourtant plus petit des element de l2 du cote
gauche de la mediane donc on va maintenant coupe en deux l1 et s'occuper de la deuxieme partie c'est pour cela que dans ce cas  start = P1 + 1 (on fait +1 por que apres quand on calcule P1 ca nous donne l'element apres
la mediane sans le plus un sa nous donne l'element avant)  d'ou maintenant start=6+1=7:
l1= a1 a2 a3 a4 a5 a6 | a7 a8 a9 a10 a11 a12              
                           ^                  ^
                    start= idx7           end =idx 12        
dans le prochain while P1=(start + end) // 2  cad P1=(7+12)//2 =9 soit :    (P2 vaut ce qui reste a prendre cad P2=(26+1)//2-9=13-9=4 donc l2= b1 b2 b3 b4| b5 b6 b7 b8 b9 b10 b11|b12 b13 b14)
l1=     a1  a2  a3   a4  a5  a6  a7  a8  a9| a10   a11  a12     ( donc on a pris la deuxieme moitier )                                                       ^
                                     ^        ^              ^                                                                                            P2=idx4
                                start=idx7   P1=idx9     end=idx 12  

option 3 :
si left_1 <= right_2 and left_2 <= right_1 alors si le nombre totale d'elements et paire alors on doit faire la moyenne entre l'element maximal de gauche et le min de droite de la mediane si tout les element 
sont rassembler cad ici on a d'un cote a1 a2 a3 a4 a5 a6  b1 b2 b3 b4 b5 b6 b7  et de l'autre cote  a7 a8 a9 a10 a11 a12 b8 b9 b10 b11 b12 b13 b14  on doit prendre le plus grand du cote gauche cad max(a6,b7) car on
sait pas qui est plus grand et le plus petit du cote droit cad min(a7,b8) et faire la moyenne (si c'etait impaire par ex l1=a1 a2 a3 et l2=b1 b2 b3 b4  alors on aurait eu d'un cote a1 a2 b1 b2  et de l'autre b3 a3 
b4 alors la mediane egale min entre a2 et b2)

option 1 et 2 peuvent revenir sur elle meme jusqu'a qu'on trouve la mediane a l'aide de option 3

"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1) # comme ca on s'occupe du plus petit array permet de gagner du temps

        start = 0
        end = len(nums1)
        total_len = len(nums1) + len(nums2)

        while True:
            P1 = (start + end) // 2   # P1 est l'idx de la moitier de [nums1[start]...nums1[end]]
            P2 = ((total_len + 1) // 2) - P1 # la taille de la deuxieme partition qui est ce qui reste a prendre dans nums2 (dans un cote de la mediane il ya total//2 donc si on a deja pris P1 element on le retire de total//2) (le +1 : si total len est paire ex 4 alors 4+1//2==4//2 (=2) cad ca change rien mais si total len est impaire ex 5 alors 5+1//2 egle 3 alors que 5//2 egale 2 la mediane sera le 3eme numero (donc si impaire la mediane va etre soit dans p1 ou dans p2 )) 
            
            
            # l1 = a1...left_1|right_1...an
            # l2 = b1...left_2|right_2...bn
            left_1 = float('-inf') if P1 == 0 else nums1[P1 - 1]  

            left_2 = float('-inf') if P2 == 0 else nums2[P2 - 1]

            right_1 = float('inf') if P1 == len(nums1) else nums1[P1]

            right_2 = float('inf') if P2 == len(nums2) else nums2[P2]

            # si tout les condition suivante sont true ca veut dire que on a reussit a separer les element de facon a avoir la mediane au centre
            if left_1 <= right_2 and left_2 <= right_1:
                if total_len % 2 == 0:    # si le nbr d'element est paire alors on doit faire la moyenne entre l'element maximal de gauche et le min de droite 
                    return (max(left_1, left_2) + min(right_1, right_2)) / 2
                else:   # si nbr d'element impaire alors c'est le max des element qui sont a gauche de la mediane
                    return (max(left_1, left_2))
            # si on a pas la mediane car :
            elif left_1 > right_2:  # ca veut dire qu'il faut prendre moins d'element de P1 car le dernier element de P1 qui est cote gauche de la mediane est superieur a un element du cote droit
                # l1 = a1...left_1|right_1...an
                #                    ^         ^
                #                   P1        end
                end = P1 - 1        
                # l1 = a1...left_1|right_1...an     cad maintenant on prend la premiere moitier de P1 (qui va etre diviser en deux dans le prochain while)
                #             ^       ^         
                #            end     P1        
            # si on a pas la mediane car : 
            elif left_2 > right_1: # ca veut dire qu'il faut prendre plus d'element de P1 car le dernier element de P2 qui est cote gauche de la mediane est superieur a un element du cote droit donc cad qu'on a prit trop d'element de P2 il faut prendre plus de P1 
                # l1 = a1...left_1|right_1...an
                #                    ^          ^
                #                   P1         end
                start = P1 + 1
                # l1 = a1...left_1|right_1...an     cad maintenant on prend la deuxieme moitier de P1(qui va etre diviser en deux dans le prochain while)
                #                   ^      ^       
                #                  P1    start 
