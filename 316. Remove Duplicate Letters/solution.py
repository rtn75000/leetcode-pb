"""#TC O(n) #SC O(1) (res is the result so not extra space and his max size is 26 so even thought it's constant space) 
l'idee est la suivante : 
on veut avoir  "result is the smallest in lexicographical order" (rappel: 'az' est plus petit que 'ba' dans l'ordre lexical car on regarde la premiere lettre et si la premiere est egale on compare la dexieme etc... 
(c'est comme lordre des mots dans un dictionnaire) ) .
Pour cela si je sais qu'une lettre va se repeter alors si la lettre qui vient apres la lettre qui se repete, est plus petite que cette derniere il vaut mieu que on supprime la lettre qui se repete comme ca elle 
viendra apres la lettre qui lui est plus petite est donc avoir un ordre lexicale plus petit. exemple si j'ai 'cbac' quand il faut supprimer le premier 'c' car apres lui y'a 'b' et c se repete ensuite donc vaut mieux
avoir 'b...c' que 'cb...'.
l'algo va passer une premiere fois sur la phrase pour trouver la derniere occurence de chaque lettre ce qui me permettra de savoir quand je suis a un certain index si la lettre de cette index se repete plus tard. 
l'algo va lire un char de la string puis va l'ajouter au resultat si on lit ensuite un char plus petit et que le char rajouter au resultat ce repete plus tard alors on enleve du resultat la lettre rajouter puis on 
rajoute a la fin la nouvelle lettre 
ex si on a 'bcabc' alors :
au debut on garde (dans un dict)la derniere apparution de chaque lettre
- on lit 'b' : res = 'b'
- on lit 'c' : res= 'bc'   (on rajoute 'c' sans supprimer 'b' car b<c donc 'bc...' c'est mieux que 'c....b')
- on lit 'a' : tant que 'a' < res[-1] et que res[-1] ce repete plus tard on retire res[-1] du resultat donc ici 'a'<'c' et 'c' se repete donc on supprime 'c' du res cad res= 'b'  (car c'est mieuc "a..c" que 'ca...').
               puisque 'a'<'b' et que 'b' se repete alors on supprime b (car 'a..b' mieu que 'ba...'). enfin comme res est vide on ajoute 'a' (la boucle tant que s'arrete si res est vide ou si res[-1]<lettre qu'on lit).
               res= 'a'
-on lit 'b' : res='ab'
-on lit 'c' : res='abc'
avant d'ajouter une lettre il faut verifier que celle ci ne se trouve pas deja dans le resultat car si elle se trouve dans le resultat ca veut dire que on a fait le choix de la garder car elle nous donne un ordre
lexical plus petit ex si on a 'cdc' alors :
-on lit 'c' : res = 'c'
-on lit 'd' : res = 'cd' on supprime pas c car 'cd...' c'est mieu que 'd..c'
-on lit 'c' : on ne le rajoute pas au res car on ne veut pas de duplicate ( on supprime le 'c' dans le res car si il est dedans ca veut dire que on a prefere ce 'c' a celui qui vient apres)

le code est d'ici (j'avais l'idee mais j'ai pas penser a la derniere occurence de chaque lettre ...) : https://leetcode.com/problems/remove-duplicate-letters/discuss/76787/Some-Python-solutions
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIdx = {c: i for i, c in enumerate(s)}  # a chaque fois qu'il ya un duplicate ecrase l'index enregistrer precedement donc a la fin il ya l'index de la dernier apparition de chaque lettre
        result = ''
        for i, c in enumerate(s):
            if c not in result:  # TC of this line is constant since result only contain unique elements, so it's bounded by the number of characters in the alphabet (a constant)
                while result and c < result[-1] and i < lastIdx[result[-1]]:
                    result = result[:-1]      # on retire la derniere lettre de result
                result += c 
        return result
