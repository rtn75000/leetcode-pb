"""first solution : #iterativeSolution #O(4^n)
solution d'ici : https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/326604/My-non-recursive-and-simple-python-solution

-> a propos du time complexity si on regarde l'arbre des interactions :
                                                                 [""]
                             _______________________________________________________________________________
                            /     						          |    				                         \
                          "a"                                    "b"                                           "c"               ici on a 3 interactions (3^1)
        _____________________________            ___________________________________             ____________________________________
	    /      	      |              \          /     	          |                 \           /     	          |                 \
     "aj"            "ak"            "al"      "bj"              "bk"               "bl"      "cj"                "ck"                "cl"    ici 9 (3^2) inter.
     ___________        ___________        ___________                  
    /     |     \      /     |     \      /     |     \             .............         ici on a 27 (3^3) intera.
"ajd"  "aje"  "ajf"  "akd" "ake" "akf"  "ald"  "ale" "alf"  

donc si on prend le pire des cas cad que chaque chiffre represente 4 letre alors dans ce cas on aura 4+4^2+4^3+...+4^n interactions avec n le nombre de chiffre dans digit . donc en time coplexity on a O(4+4^2+4^3+...+4^n) soit O(4^n) .
dans cette article aussi ya ce pb avec ce time complexity : https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28

-> la solution est interative : on commence par une liste qui contient une string vide : result=[""], ensuite on ajoute a chaque fois au membre de result les lettres du chiffre qu'on lit donc au debut  pour l'exemple "253" ca donne : [""+"a",""+"b",""+"c"] (cad result=["a","b","c"]) puis ["a"+"j","b","c"]
idx=0    for 0 in range (3) :
             result = [prev + l for prev in [""] for l in 'abc']   (cad result=[""+"a",""+"b",""+"c"]=["a","b","c"])
idx=1    for 1 in range (3) :
             result = [prev + l for prev in ["a","b","c"] for l in 'jkl']   (cad result=["a"+"j","a"+"k","a"+"l",...]=["aj","ak","al","bj","bk","bl","cj","ck","cl"])
idx=2    for 2 in range (3) :
             result = [prev + l for prev in ["aj","ak","al","bj","bk","bl","cj","ck","cl"] for l in 'def']  (cad rslt=["aj"+'d',"aj"+'e',"aj"+'f',...])   
             
d'ou result =["ajd","aje","ajf","akd","ake","akf","ald","ale","alf","bjd","bje","bjf","bkd","bke","bkf","bld","ble","blf","cjd","cje","cjf","ckd","cke","ckf","cld","cle","clf"]
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for idx in range(len(digits)):
            result = [prev + l for prev in result for l in digit_map[digits[idx]]] 
            # la double loop a l'interieur c comme ci y'avait      for prev in result :
            #                                                              for l in digit_map[digits[idx]]]:
            #                                                                       prev+l
            # donc d'abord on fait toute la 2eme loop sur le 1er element de la 1er loop puis on la refait su le 2eme element de la premiere loop etc...
        return result
    
    
    
    """2nd solution : https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8120/AC-Python-solution
-> same as first solution but without list comprehension :

class Solution:

    def letterCombinations(self, digits):
        dictio = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
                      "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
        result = [""]
        if len(digits) == 0:
            return []
        for digit in digits:
            lst = dictio[digit]
            newresult = []
            for char in lst:
                for str in result:
                    newresult.append(str+char)
            result = newresult
        return result
        
        """
