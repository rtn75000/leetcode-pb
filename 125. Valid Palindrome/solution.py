"""# my sol #TC O(n) #SC O(1)
on va prendre en consideration les nombres, les lettres minuscule et les lettres majuscules (respectivement valeurs ASCII entre 48-57 ,65-90 et 97-122).
on va utiliser un pointeur qui commence a l'extreme gauche et un pointeur qui commence a l'extreme droite et on va comparer les deux caracteres si ils sont differents alors on rend False. """

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            leftVal, rightVal = ord(s[left]), ord(s[right])
            # on fait avancer le pointeur de gauche tant qu'il ne pointe pas sur une lettre minuscule ou majuscule ou un nbr
            while not (48 <= leftVal <= 57 or 65 <= leftVal <= 90 or 97 <= leftVal <= 122) and left < right: 
                left += 1
                leftVal = ord(s[left])
            # on fait avancer le pointeur de droite tant qu'il ne pointe pas sur une lettre minuscule ou majuscule ou un nbr
            while not (48 <= rightVal <= 57 or 65 <= rightVal <= 90 or 97 <= rightVal <= 122) and left < right:
                right -= 1
                rightVal = ord(s[right])
            # on compare les caracteres 
            if left <= right and s[left].lower() != s[right].lower():
                return False
            # apres avoir comparer on fait avancer les deux pointeurs pour ne pas comparer les memes lettres a la prochaine iteration
            left += 1
            right -= 1
            
        return True

