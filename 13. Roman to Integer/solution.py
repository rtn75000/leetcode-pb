"""#ma sol #hasmap #TC O(n) #SC O(1)
on utilise un hashmap qui contient tout les chiffres romain et les combinaisons de deux chiffre romain.
on lit le nbr de gauche a droite , si on trouve une combinaison alors on avance de deux index sinon on a un chiffre romain seulement donc on avance de 1 lettre"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = { 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
                       'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = i = 0
        while i<len(s) :
            #si on trouve une combinaison de deux chiffres romain
            if s[i:i+2] in roman_map :  
                res+=roman_map[s[i:i+2]]  # addition de la valeur correspondent au 2 chiffres romain
                i+=2
            #si on a que un chiffre romain 
            else :
                res+=roman_map[s[i]]      # addition de la valeur correspondent au chiffre romain
                i+=1
        return res
