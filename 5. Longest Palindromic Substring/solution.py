"""#logique de palindrome #2pointers #TC O(n) voir analyse #SC O(1) 

video explicative: https://www.youtube.com/watch?v=IrD8MA054vA&t=347s&ab_channel=TimothyHChang

l'idee est que le milieu d'un palindrome forme une symetrie axial. si une sting est de taille impaire alors le milieu est la lettre du milieu , si la string est de taille paire 
alors le milieu se trouve entre les 2 lettres du milieu.
ex: "abcba" est impaire , 'c' est la lettre du milieu de  "abcba" , "abcba" est un palindrome car son milieu forme une symetrie axiale : a<-b<-c->b->a
ex: "abba" est paire , 'bb' sont les deux lettres du milieu, le milieu est donc entre 'bb' , "abba" est un palindrome car son milieu forme une symetrie axiale : a<-b<-->b->a

dans notre algo on va prendre tout les milieu possible c'est a dire on va considerer toute les lettres comme un milieu potentiel d'un palindrome (qui sera de taille impaire car 
son milieu est une lettre) et toute les entre-deux lettres comme un milieu potentiel d'un palindrome (qui sera de taille paire car son milieu est un entre deux lettre)

app : 

    s="abbaccc"

    on va passer sur chaque lettres et sur chaque entre lettre et on va s'etendre de chaque cote de ses milieu : 

    1e milieu : 'a' , la lettre a droite de 'a' ('b') est differente de la lettre a gauche de 'a' ('') donc 'a' n'est pas le centre d'un palindrome. donc on passe a un autre milieu:
    2e milieu : entre 'a' et 'b' , la lettre a droite de ce milieu est egale a 'b' et la lettre a gauche est egale a 'a' , donc ce milieu n'est pas le centre d'un palindrome .
    3e milieu : 'b', la lettre a droite de 'b' ('b') est differente de la lettre a gauche de 'b' ('a') donc 'b' n'est pas le centre d'un palindrome. donc on passe a un autre milieu 
    4e milieu : entre 'b' et 'b' , la lettre a droite de ce milieu est egale a 'b' et la lettre a gauche est egale a 'b' , donc on a trouver un palindrome , on continue a s'etendre 
                autour de ce milieu : la lettre a doite de 'b'(celui de droite):'a' est egale a la lettre a gauche de 'b'(celui de droite):'a' , donc on continue l'expension .
                la lettre a doite de 'a'(celui de droite):'c' est pas egale a la lettre a gauche de 'a'(celui de droite):'' , donc on a fini ce palindrome qui est de taille 4.
    5 milieu .....    

    au final on va trouver deux palindrome un de taille 4 : "abba" est un de taille 3 : "ccc" . donc on oit return le plus long palindrome cad : return "abba" .

analyse du TC : 

    il ya en tout 2n-1 milieu car il ya n lettre qui sont un milieu et (n-1) entre lettre (ex: si on a 3 lettre alors on a 2 entre-lettres). 
    chaque milieu peut au max s'entendre en O(n) car il peut au max passer sur toute le lettres de la string  (bien que il ya que un milieu qui va faire passer sur n les autres
    sont O(n) cad passe moins que n ).
    donc TC = O(n)*O(2n-1) = O(n)* O(n) = O(n^2)

remarque code : 
l'extension se fait en comparant 2 pointeurs de lettres : si le milieu est une lettre alors AU DEBUT les deux pointeurs vont pointer sur la meme lettre , si le milieu 
est un entre-deux lettres alors AU DEBUT (et aussi apres) les deux pointeurs vont pointer sur deux lettres differentes . 


"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def searchPalindrome (left,right) : #O(n)
            
            while (left>=0 and right<len(s) and s[left]==s[right]):      # on verfie que left et right sont dans les limite de la string et que s[left]==s[right]
                
                left-=1    # on fait avancer le pointeur vers la gauche
                right+=1   # on fait avancer le pointeur vers la droite
                
            return s[left+1:right]    #right n'est pas inclus donc ca nous donne de left+1 a right-1 inclus
                                      # left et right ne sont pas inclus car on les a avancer apres avoir verifier qu'il sont egaux
                                      # donc left et right apres la boucle ne sont pas egaux mais left+1 et rigth-1 sont egaux 
        
        output=""  #contiendra le plus grand palindrome 
        
        for i in range (len(s)):  # a chaque iteration on va prendre en consideration une lettre et l'entre-deux lettre qui vient apres cette lettre   #O(n)
            
            oddPalindrome = searchPalindrome (i,i)    # on verifie les palindromes impaire cad les milieux sont des lettres
            if len(oddPalindrome)>len(output) :      #si le palindrome trover est plus grand que l'output alors update l'output
                output = oddPalindrome
                
            evenPalindrome = searchPalindrome (i,i+1)     # on verifie les palindromes paire cad les milieux sont des entres-deux lettres
            if len(evenPalindrome)>len(output) :     #si le palindrome trover est plus grand que l'output alors update l'output
                output = evenPalindrome
            
        return output 
