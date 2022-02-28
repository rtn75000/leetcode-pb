"""#TC O(n)  #SC O(1) 
code et explication d'ici : https://leetcode.com/problems/valid-parenthesis-string/discuss/543521/Java-Count-Open-Parenthesis-O(n)-time-O(1)-space-Picture-Explain
l'idee est la suivante: a chaque fois on prend en compte tout les options on utilisera deux variable (une qui sera la limite inferieur(cmin) et l'autre superieur(cmax)) qui determineront le nombre de parenthese
ouverte (Cad qui n'ont pas de paire). si une variable est superieur a 0 cela veut dire qu'il ya des left parenthese qui ne sont pas ferme, si une variable est inferieur a 0 cela veut dire qu'il ya des right 
parenthese en plus. 0 cela veut dire que la phrase est bien equilibree . les deux variable compte le nombre de de left and right parenthese si on lit '(' on rajoute +1 au deux variable si on lit ')' on enleve au
deux 1 si on lit * alors ca peut etre +1 ou -1 donc on retire 1 a la limite inferieur et on rajoute 1 a la limite superieure .
  ex pour la phrase : '(**'                        (                              cmin=1 et cmax=1 (car 1 option avec left par ouverte)
  
                                       /           |          \                        
                                      /            |           \                  on lit le charactere suivant et voici les options :
                                     /             |            \
                                     
                                    ()  0          (   1        ((   2            cmin=0 cmax=2     
                                
                                 / | \          /  |  \         / | \
                                /  |  \     () 0  ( 1  (( 2    /  |  \
                               /   |   \                      /   |   \
                              /    |    \                    /    |    \          cmin=-1  cmax=3
                             /     |     \                  /     |     \
                            /      |      \                /      |      \
                                
                       ()) -1     () 0    ()( 1        (() 1     (( 2    ((( 3   
                       
    a chaque fois qu'on a une etoile on a 3 options : right parenthese , empty string,  left parenthese 
    si on fini l'algo avec 0 inclu dans [cmin,cmax] alors on rend True . si apres une iteration on a cmax<0 cad que il ya trop de right parenthese (ds toute les option) ex : ) , ())( ... et donc ca sert a rien de
    continue car cela est forcement false. 
    
  
"""

class Solution :
     def checkValidString(self,s) :
        cmin = cmax = 0
        for c in s : 
            if c == '(' :
                cmax+=1
                cmin+=1
            elif c == ')' :
                cmax-=1
                cmin-=1
            elif c == '*' : 
                cmax+=1; # if `*` become `(` then openCount++
                cmin-=1; # if `*` become `)` then openCount--
                # if `*` become `` then nothing happens
                 
            # si apres une iteration on a cmax<0 cad que a ce stade il ya trop de right parenthese ds toute les options donc forcement c'est faux . example: ())(   apres avoir lu ()) on sait que c'est faux
            if cmax < 0 : 
                return False
            
            # a chaque iteration si cmin est inferieur a 0 il faut retirer cette option et donc remetre cmin a 0 car on obtient cmin<0 par ex si on a ()) cmin=-1 donc si on continue les iteration sur ce cas par 
            # exemple on lit apres ) ce qui donne ())) cmin =-2 et disons on apres (( cad ()))(( soit cmin=0 or cette option est fausse donc des que on dessens en dessous de 0 on prend pas en compte cette option 
            # et donc on laisse cmin=0 qui donc supprime la possibilite de continue a prendre en compte des cas comme: ())  qui sont forcement faux (on rend pas false car il ya d'autre option jusqu'a cmax)
            cmin = max(cmin, 0)   
            
        return cmin == 0   # Return true if cmin==0 (cmin peut etre egale a 0 ou plus)
    
