""" #TC O(n) #SC O(n)
l'idee est la suivante si on a une parenthese qui n'a pas de paire alors il faut en rajouter une parenthese pour que la phrase soit valide. on utilisera un stack : 
a chaque fois q'on lit une parenthese '(' on l'ajoute dans le stack et a chaque fois qu'on lit une parenthese ')' on pop du stack si le stack et vide ca veut dire que 
il ya une parenthese ')' en plus . si a la fin il ya des parenthese qui reste dans le stack ca veut dire qu'il ya des parenthese '(' en plus.
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        res=0
        for i in range(len(s)) : 
            if s[i]=='(':
                stack.append(s[i])
            elif stack: # if s[i] == ')' and stack non empty
                    stack.pop()
            else : # if if s[i] == ')' and stack empty
                  res+=1
        res+=len(stack)
        return res
    
"""#TC O(n) #SC O(1)
on peut utiliser un counter a la place du stack car on fait rentrer que un element dans le stack '('.  A chaque fois qu'on lit '(' on incremente le counter et a
chaque fois qu'on lit ')' si le counter == 0 alors on rajoute au resultat 1 car cad qu'il ya pas de '(' avant le ')' [donc pas de paire] et si le counter et superieur 
a 0 alors on soustrait 1. a la fin on rajoute le counter au resultat car il represente les '(' qui n'ont pas de paire.
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        counter = res = 0
        for i in range(len(s)) : 
            if s[i]=='(':
                counter+=1
            elif counter>0 : # if s[i] == ')' and counter>0
                    counter-=1
            else : # if if s[i] == ')' and counter==0
                  res+=1
        res+=counter
        return res
