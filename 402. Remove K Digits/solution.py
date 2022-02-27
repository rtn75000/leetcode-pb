"""# TC : O(n)  (we have the exact (N+k) number of operations. Since 0<k≤N, the time complexity of the main loop is bounded within 2N. For the logic outside the main loop, it is clear to see that their time complexity
is O(N). As a result, the overall time complexity of the algorithm is O(N).)    
#SC O(n) for the stack

l'idee est de suprrimer le premier "pique" que l'on rencontre a chaque fois . exemple de pique : 12316, 321 , 123 dans tt ces ex 3 est un pique .
si on prend l'exemple qui nous ait donner :  num = "1432219", k = 3 on supprime le premier pique de gauche a doite qu'on rencontre on recommencera 3 fois car k=3. en premier on supprime 4 ce qui nous donne : 132219 
puis on supprime 3 ce qui donne 12219 puis on supprime 2 ce qui nous donne 1219.
(on obtient un pique lorsque le chiffre qui vient apres est plus petit).
on utilisera un stack dans lequel on rentrera les chiffre et a chaque fois qu'on rentre un chifrre plus petit que le top on fait pop , si k>0 alors on verifira encore le top si le top est plus grand alors on fera
encore pop etc...

app :
DIGITS = 1, 5, 6, 3    K = 2  res = ""
current_digit = 1, So, res = 1
current_digit = 5, So, res = 15
current_digit = 6, So, res = 156
current_digit = 3, 
		Now, previous digit (6) greater than current digit (3).
		So, del previous digit.
		res = 15  K = 1
		Still previous digit(5) is greater than current digit (3)
		res = 1, K = 0
		Now, K becomes 0
		and add remaining digits to res.
		res = 13
So, smallest number is 13.

code et explication : https://leetcode.com/problems/remove-k-digits/discuss/629860/Java-or-C%2B%2B-or-Python3-or-easy-explanation
video explicative : https://www.youtube.com/watch?v=3QJzHqNAEXs&ab_channel=TECHDOSE
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:    
        stack = []
        for digit in num:         # on fait la boucle suivante pour chaque chiffre 
            while k > 0 and len(stack) > 0 and stack[-1] > digit:  # tant que on doit retirer un chiffre et que la stack n'est pas vide et que le top est superieur au chiffr actuelle alors :
                k -= 1
                stack.pop()  
            stack.append(digit)   # a la fin du while on rajoute le chiffre actuelle 
        
        # si a la fin k est superieur a 0 et donc on doit retirer encore des chiffre ca veut dire que dans notre stack tout les chiffres sont dans un ordre croissant par ex 123 donc, on a pas de pique car on a pas un nombre plus petit qui vient apres un nombre plus grand donc on a pas supprimer de chiffre c'est pour cela que on doit supprimer les k dernier chiffre de notre stack car ce sont les plus grand 
        if k > 0:                
            stack = stack[:-k]   
        
        # si il nous reste un nombre avec un leading 0 cad un 0 en debut ex 012 alors on doit retirer le 0  [string.lstrip(characters): characteres is a set of characters to remove as leading characters]
        # or "0" est la pour si il reste que un 0 dans le nombre alors "".join(stack).lstrip("0")  rend une empty string (qui est interpreter comme False) donc on rajoute or '0' pour que dans ce cas cela rend '0' et pas rien
        return "".join(stack).lstrip("0") or "0"
