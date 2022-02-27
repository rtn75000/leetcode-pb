"""pour cette exercice ce qui faut comprendre c'est que une lettre qui n'apparait pas dans order alors elle peut etre n'importe ou dans la phrase. donc c'est pour cela que tout d'abord j'ai decider de mettre tout les letres qui sont dans order puis les lettres qui le sont pas """
"""#my sol #hashmap #TC O(len(s))    #SC O(1) car le dict contient max 26 lettres  (le output n'est pas considerer extra space)
algo tres simple :
app : order ="abc" s= "abdccdbea"
d'abord on compte les char de s : d = {'a': 2, 'b': 2, 'd': 2, 'c': 2, 'e': 1}
ensuite on mais dans le output toute les lettre de order fois le nombre de fois qu'il se trouve dans s donc output="aabbcc"
ensuite on rajoute les autres lettre * la frequence d'apparition dans s cad : "aabbccdde"
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d=Counter(s) # O(len(s)) car passe sur s pour compter la frequence des caractere 
        output=''
        for char in order  : # O(len(order)) soit O(26) car order a max 26 char on peut considere comme O(1)
            output+=(d[char]*char) # d[char]==frequence de char ds s donc cad qd on fait d[char]*char ca ns donne x fois la meme lettre char
            d[char]=0
        for char in d :    # O(1)
            output+=(d[char]*char)
        return output
    
