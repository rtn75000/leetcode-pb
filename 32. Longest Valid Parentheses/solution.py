"""ma solution  #O(n) TC # O(n) SC
l'idee est la suivante : 
1er etape : on garde dans un stack l'index des parenthese qui sont en trop [une parenthese et en trop si elle n'a pas de paire]. A chaque fois qu'on lit '(' on ajoute au stack l'index de la parenthese et si on lit ')' 
alors si il ya au top de la stack l'index d'une parenthese '(' [on connaitera la parenthese a l'aide qu'on regarde dans la phrase de base la parenthese qui se trouve a cette index] on pop car on a trouver une paire de
parenthese, mais si il ya au top de la stack l'index d'une parenthese ')' ou la stack est vide alors on ajoute l'indexe de la parenthese ')' qu'on lit car il ya pas de paire.
2eme etape : apres la 1ere etape on a dans le stack les index de toutes les parenthese en trop. donc entre ces indexes on a une phrase de parenthese correcte [=tt les parenthese sont en paire] donc il nous reste juste
a trouver le plus grand ecart entre les indexes presents dans le stack. 
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack,maxi = [],0
        sLen = len(s)
        #1ere etape
        for i in range(sLen):
            if s[i] == '(':
                stack.append(i)
            else:  # cad s[i]==')'
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:  # if stack empty or s[stack[-1]]==')' :
                    stack.append(i)   
                    
        #2eme etape            
        # jai rajouter la ligne suivante pour qu'il y'ai un index qui precede le debut et un indexe qui est apres le dernier index de la phrase car:
        #-si on a pas l'index 0 dans la stack cad que s[0] n'est pas en trop donc pour le contabiliser il faut commencer 1 avant 0 d'ou le -1 ajouter au debut (meme si 0 sera dans le stack ca derenge pas de rajoute le -1
        # car 0-(-1)-1 ca revient a 0 car il ya pas d'index entre -1 et 0 ).
        #-si on a pas l'index len(s)-1 (cad le dernier index) dans la stack alors ca veut dire que s[len(s)-1] n'est pas en trop donc pour le compter on rajoute un index au dessus cad len(s) d'ou le len(s) ajouter a la fin. 
        # (meme si on a len(s)-1 sera dans le stack si on rajoute len(s) ca changera rien car len(s)-(len(s)-1)-1 est egale a 0 car il ya pas d'index entre len(s)-1 et len(s)) 
        # par exemple si on a stack == [4] avec len(s)==7 cad que a l'index 3 il ya une parenthese en trop le reste et correcte donc on a 0-1-2-3 qui est correcte cad 4 parenthese et 5-6 cad 2 parenthese donc il faut
        # calculer la distance entre -1 et 4 pour obtenir 4 et entre 4 et 7 pour obtnenir 2
        stack = [-1] + stack + [sLen]  
        for i in range(len(stack) - 1):  # on calcule les distance entre les index present dans le stack
            maxi = max(maxi, stack[i + 1]-stack[i]-1)
        return maxi
