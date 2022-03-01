"""#ma solution  #array #string #TC SC O(n)
cette algo est plus complexe que la solution 2 car il fait un changement inplace de la phrase .
remarque sur SC :
en python les string sont immutable donc on ne peut faire de changement sur la string meme il va faloir creer une list donc forcement SC O(n).
en cpp les string sont mutable donc on pourra appliquer le meme code sur la phrase meme donc SC va etre O(1).

TC est O(n) car on passe au max 2 fois sur chaque lettres (1 fois possible avec le while interieur une fois sur avec le while exterieur). la raison est que le while interieur fait un swap 
qui met forcement a chaque fois une lettre en place donc si il va faire n iteraction il va mettre n lettres en places , ensuite le while exterieur va repasser sur chaque lettre une fois,
donc le while exterieur va faire une iteration qui lui coute n puis n-1 iterations qui lui coute 1 donc en tout n+n-1 iteration cad O(2n) == O (n) ,voir 2eme app pour comprendre .

1er app :  indices = 3 2 1 0
                 s = e d o c

-idx = 0
    indices = 3 2 1 0                                                                                                                                                                       indices = 0 2 1 3
          s = e d o c    on swap les indices et les lettres tant que l'indice de la lettre qui se trouve a idx ne correspond pas a l'idx , ici on swap donc que une fois est ca donne ca :        s = c d o e
              ^                                                                                                                                                                                       ^
             idx                                                                                                                                                                                     idx==0 
    puisque indices[idx==0]==0 on a fini le while interieur 

-idx = 1
    indices = 0 2 1 3                                                                                                                                                                       indices = 0 1 2 3
          s = c d o e    on swap les indices et les lettres tant que l'indice de la lettre qui se trouve a idx ne correspond pas a l'idx , ici on swap donc que une fois est ca donne ca :        s = c o d e
                ^                                                                                                                                                                                       ^
               idx                                                                                                                                                                                     idx==1 
    puisque indices[idx==1]==1 on a fini le while interieur 
    
-idx=2 
   puisque indices[idx==2]==2 alors on fait pas le while interieur
   
-idx=3 
   puisque indices[idx==3]==3 alors on fait pas le while interieur
   
   
2e app :  indices = 3 0 1 2
                s = e c o d

-idx = 0
    indices = 3 0 1 2                                                                                                                                                                     
          s = e c o d    on swap les indices et les lettres tant que l'indice de la lettre qui se trouve a idx ne correspond pas a l'idx :         
              ^                                                                                                                                                                                        
             idx                                                                                                                                                                                     
                         indices = 2 0 1 3 
                               s = d c o e     puisque  indices[idx==0]==2 != 0 ca veut dire que la lette a l'idx idx==0 n'est pas a ca place donc il faut qu'on la swap
                                   ^
                                  idx

                         indices = 1 0 2 3   
                               s = o c d e     puisque  indices[idx==0]==2 != 0 ca veut dire que la lette a l'idx idx==0 n'est pas a ca place donc il faut qu'on la swap
                                   ^
                                  idx
                                  
                         indices = 0 1 2 3 
                               s = c o d e 
                                   ^
                                  idx            
             
    puisque indices[idx==0]==0 on a fini le while interieur 

-idx = 1                                                                                                                                                                                
    puisque indices[idx==1]==1 on a fait pas le while interieur
    
-idx=2 
   puisque indices[idx==2]==2 alors on fait pas le while interieur
   
-idx=3 
   puisque indices[idx==3]==3 alors on fait pas le while interieur
   
   remarque par rapport au TC : comme on peut le constater les lettres qui sont en place coute O(1) car on ne va pas faire la boucle interieur . seulement les lettres qui sont pas en place peuvent faire plus de O(1)
   iteration , dans ce cas les autres lettres pourront faire O(n-les iterations faites precedement) donc au total on aura max O(n) iteration dans le while interieur en tout .
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s=list(s) 
        idx = 0
        while idx < len(s) :
            while indices[idx] != idx :
                s[indices[idx]],s[idx] = s[idx], s[indices[idx]]    # swap letter in s 
                indices[indices[idx]],indices[idx]=indices[idx],indices[indices[idx]]  # swap indice in indices 
            idx+=1
        return "".join(s)
    
    
"""solution 2 # TC SC O(n)
cette algo meme utilise une liste de la taille de s ou les lettres vont donc mis a l'indexe qui corresponds a leur indices . ici ca nous coutera SC O(n) dans tout les cas meme en cpp car on devra creer une liste en plus 
alors que la premiere sol on a convertit s en list pour pouvoir modifier s mais on ne creer pas une liste vide en plus de s ."""
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        # on passe lettre par lettre dans s et on la range a sa place dans res 
        for index, char in enumerate(s):
            res[indices[index]] = char   #on met chaque lettre dans res a l'index qui lui correspond 
        return "".join(res)
