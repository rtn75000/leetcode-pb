""" #pointers #not my sol #TC O(n) #SC O(1)

la reponse a la question est pas si simple que ca !

CONSIGNE EXPLICATION : 

il faut trouver le nombre de substings qui on le meme nombre de 0 consectives que de 1 consecutives  , ex : '0011' a deux substring qui on le meme nombre de 0 et de 1 consecutives la 
premiere substring '0011' (2 zero et 2 un consecutives) et la deuxieme substring '01' (1 zero et 1 un consecutive ).


ALGO EXPICATION : 

algo pris d'ici (code + explication ) : 
https://leetcode.com/problems/count-binary-substrings/discuss/1172569/Short-and-Easy-w-Explanation-and-Comments-or-Keeping-Consecutive-0s-and-1s-Count-or-Beats-100

principe utilise : le nombre de substring contenant un meme nombre de 0 et 1 consecutive correspond a la taille minimum entre deux groupe qui se suivent l'un contenant que des 0 l'autre que des 1.
explication du principe avec exemple : '00011100'  , count of consecutive binary characters is :  [3,3,2] cad il ya deux grp de 3 consecutive 1 ou 0 et un grp de 2 consecutive 1 ou 0 . prenons 2 
groupe qui se suivent  a chaque fois donc au debut on prend les 2 groupes  [3,3] , le nombre de substring contenant un meme nombre de 0 et 1 consecutive former par ces 2 groupes est min(3,3)
cad 3 cad avec '000111' on peut former 3 substring contenant un meme nombre de 0 et 1 consecutive : '01' , '0011' et '000111' . prenons maintenant 2 autres grp qui se suivent qui veinnent apres 
les 2 groupes selectionner precedement cad on va prendre les deux grp : [3,2] , le nombre de substring contenant un meme nombre de 0 et 1 consecutive former par ces 2 groupes est min(3,2)
cad 2 cad avec '11100' on peut former 2 substring contenant un meme nombre de 0 et 1 consecutive : '01' et '0011'. 


remarque : dans l'algo au tout debut le prevConsecutive va etre egale a 0 au moment de 'ans += min(prevConsecutive, curConsecutive)' car au debut ce groupe ne contient rien est curConsecutive
           contiendra le premier groupe contenant des 0 ou 1 consecutive  

 """
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        curConsecutive = 1  
        prevConsecutive = 0
        ans = 0
        
        for i in range(1, len(s)):  # O(n)
            if s[i-1] != s[i]:   # si deux lettre consecutive ne sont pas les memes alors la deuxieme lettre est le debut d'un autre groupe de 0/1 consecutive           
                ans += min(prevConsecutive, curConsecutive)   # number of substring formed is minimum of cur and prev count
                prevConsecutive = curConsecutive              # le groupe prevConsecutive devient le groupe curConsecutive 
                curConsecutive = 1                            # important : current streak will be resetted  
            else :
                curConsecutive+=1 
      
        # on fait encore une fois ici 'ans += min(prevConsecutive, curConsecutive)' , car a la fin du for on aura pas comparer le dernier prev et cur (car la comparaison se 
        # fait apres que prev et cur sont update et seulement dans l'iteration d'apres et comme l'iteration d'apres ne se fait pas car on sort du for alors le dernier prev et cur 
        # ne sont pas comparer entre eux )
        ans += min(prevConsecutive, curConsecutive)
        
        return ans
