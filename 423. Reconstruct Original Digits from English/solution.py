"""
# logic #TC O(n)  #SC O(1)

l'idee est de compter le nombre de chaque lettres , ensuite il faut parcourir les nombres dans un ordre precis (le dic digits va etre dans cette ordre) puis on supprime les caractere appartenant a ce nombre .
explication :
on commence par zero c'est le seul qui a la lettre z donc on retire des frequences des lettres z,e,r et o  
two, we have symbol w only in this word, remove all words two.
four, we have symbol u only in this word, remove all words four.
six, we have symbol x only in this word, remove all words six.
eight, we have symbol g only in this word, remove all words eight.
one, we have symbol o only in this word if we look only on the remaining number, remove all words one.
three, we have symbol t only in this word if we look only on the remaining number, remove all words three.
five, we have symbol f only in this word if we look only on the remaining number, remove all words five.
seven, we have symbol s only in this word if we look only on the remaining number, remove all words seven.
nine, we have symbol n only in this word if we look only on the remaining number, remove all words nine.


remarque : Worst time complexity for inserting into list is O(n-i), where n is the length of the list and i is the index at which you are inserting.
So in case if you are inserting at the last index, that makes it O(1).
"""
class Solution:
    def originalDigits(self, s: str) -> str: 
        
        digits = {"zero" : 0 ,"two":2 ,"four":4 ,"six":6 ,"eight":8 ,"one":1 ,"three": 3,"five":5 ,"seven":7, "nine":9 }       # SC O(10)
        letterFreq = collections.Counter(s)   #TC O(n)  # SC O(10)
        found=[0]*10   # cette liste indique le nombre de fois qu'on a trouver chaque nombre , ex: found[1] ca nous donne le nombre de fois que 1 apparait dans s   #SC O(10)
        
        for key in digits :  #cette boucle ce fait dans l'odre des element du dictionnaire c'est pour cela que ca marche   # TC O(10) car il ya 10 key dans digits (chaque iteration coute O(1))
            
            # on veut garder la plus petite frequence des lettres de key car c'est forcement elle qui determine combien de nombres correspondent a ce key.
            count = float("inf") 
            for char in key :        # TC O(5) car key de taille 5 max 
                if letterFreq[char] < count:  
                    count = letterFreq[char] 
                    
            # maintenant on enleve la plus petite frequence trouver de chaque lettre de key
            for char in key :        # TC O(5) car key de taille 5 max 
                letterFreq[char]-=count
                
            # on ecrit le nombre de fois qu'on a le nombre key dans s 
            found[digits[key]]+=count 
            
        return ''.join([str(i)*found[i] for i in range(10)])   
