                                
""" #logic #string #TC (voir analyse ) #SC O(1)
consigne : ici on parle de 'common PREFIX' , un prefixe est une partie du mot en commencant au debut ex le mot flower alors les prefixes du mot sont les suivants: f,fl,flo,flow,flowe,flower . 
le longuest prefix commun commence en debut de chaque mot et est commun a tout les mots donc il suffit de comparer a chaque fois deux mot de voir quel est leut LCP et de comparer ensuite deux 
autre mot et ainsi de suite. 
on va donc commencer par selectionner le prefix en tant que le premier mot puis update le prefix en comparant le prefix avec les autres mots. 

TC analyse : au pire si tout les mots sont les memes alors on va passer sur chaque lettres de chaque mots une fois, donc TC = O(S) , where S is the sum of all characters in all strings.

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for element in strs[1:]:    # on passe sur tout les mots
            for i in range(len(res)):  # on compare chaque mot avec le longuest common prefix trouver jusqu'a present 
                 # si le mot qu'on compare est plus petit que le LCP alors le LCP est forcement egale a ce mot , si une lettre different alors le LCP est jusqu'a cette lettre 
                if i > (len(element)-1) or element[i] != res[i]:   
                    res = res[:i] 
                    break  
        return res
