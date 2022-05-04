"""explication de l'ennoncer : tout les chiffres doit etre choisi obligatoirement , parcontre les signes ne sont pas obliger d'etre choisi (car ya ecrit 'or') .
cad si on a par exemple : num = "25", target = 5 alors output =[] car on doit utiliser tout les chiffres donc les combinaisons possible sont les suivantes  : 25, 2+5, 2-5, 2*5 . 
"""
""" #ma sol #TLE(mais c'est une super solution ,en reel interview elle sera surement accepter)   # TC O(4^n*n) voir analyse # SC O(n)

a chaque fois on a 4 possibilite: soit d'additionner soit de soustraire soit de multiplier soit de ne pas rajouter de signe .

la consigne nous dit qu'il ne faut pas qu'il y'ai de 'leading zero' cad on si on a par exemple :
num = "105", target = 5  alors 1*05 n'est pas une reponse valide car on a un leading 0 .
un leading zero est un zero qui vient au debut d'un nbr donc on ne peut ajouter a un zero seul un autre chiffre car on aura un leading 0 , c'est pour cela que 
on ne peut utiliser la 4eme option (qui est d'ajouter juste un chiffre ) quand on a un leading 0 .

TC analyse : (voir mes fiches times complexity page 14 en bas )
a chaque etape on a 4 recursion et la hauteur du tree de recursion est O(n) donc il ya en tout O(4^n) recursion. mais les feafs recursion et les non leaf recursion on pas le meme cout :
la fonction join() coute O(n) mais elle se fait que dans les leafs donc comme il ya O(4^n-1) leaf alors les leaf coute O(4^n-1*n) en tout , le reste des nodes coute O(1) et comme en 
tout il ya O(4^n-1) non-leaf nodes alors les non-leaf node coute en tout O(4^n-1*1) cad O(4^n-1) .
donc le TC coute en tout O(4^n-1*n)+O(4^n-1) equivalent a O(4^n-1*n) equivalent a O(4^n*n)

SC analyse : 
la taille de l'arbre est O(n) donc le stack recursion est de taille O(n).
de plus on utilise cur qui garde le current path qui est O(n) donc O(n) .
au total on a donc O(2n) = O(n)

VOIR PHOTO GITHUB ARBRE DE RECURSION 
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(num, target, output, cur):  # le output va contenir les path qui sont egale a target , cur garde le current path
            
            if not num :   # si il ya plus de chiffre a lire
                if eval("".join(cur)) == target:   # si l'expression est egal a target alors il faut rajouter cela au resultat
                    output.append("".join(cur))
                return     # si on a fini de lire tout les chiffres on remonte la recursion 
           
            # 1er possibilite : addition  
            cur.extend(('+', num[0]))            # list.extend() c'est un list.append() de plusieurs elements
            dfs(num[1:], target, output, cur)    # appel de la recursion sur le chiffre suivant 
            cur.pop();cur.pop()                  # on pop le chiffre et le plus qui ont ete rajouter 
            
            # 2e possibilite : soustraction 
            cur.extend(('-', num[0]))
            dfs(num[1:], target, output, cur)
            cur.pop();cur.pop()
            
            # 3e possibilite : mutiplication 
            cur.extend(('*', num[0]))
            dfs(num[1:], target, output, cur)
            cur.pop();cur.pop()
            
            # 4e possibilite : on ne rajoute pas de signe , on rajoute que le chiffre suivant , on peut faire ca que si on a pas de leading 0
            # on obtient un leading zero si le chiffre precedent est un zero et que ce zero est preceder par un signe car
            # si il est precede par un chiffre different de 0 il est pas un leading 0.
            # donc on a pas de leading zero si le chiffre n'est pas 0 ou meme si c'est 0 mais qu'il a un chiffre avant lui (et pas un signe) 
            # qui n'est pas un 0 alors ce n'est pas un leading 0
            if cur[-1] != '0' or (len(cur) > 1 and cur[-1] == '0' and (cur[-2] != '+' and cur[-2] != '-' and cur[-2] != '*'  ) )   :
                cur.append(num[0])
                dfs(num[1:], target, output, cur)
                cur.pop() # on pop que une fois car on a pas ajouter de signe on a ajoute que un chiffre 

        dfs(num[1:], target, res, [num[0]])
        return res

    
""" la precedente solution fait un TLE ,la solution est de ne pas calculer le path a chaque leaf mais de le calculer tout le long du path pour que on a pas a calculer le path 
a chaque leaf de nouveau.
#not my sol #meme TC et SC que la reponse precedente 
il ya deux pb qd on veut calculer 'on the fly' : 
- s'occuper de la mutiplication 
- ajouter un nombre sans signe avant 
je ne vais pas m'attarder sur cette solution car trop de edge case c'est improbable de l'avoir en interview...."""


class Solution:
    def addOperators(self, num, target):
        def dfs(idx, path, value, last):            
            if idx == n and value == target:
                ans.append(path)
            
            for i in range(idx + 1, n + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != "0"):
                    if last is None :
                        dfs(i, num[idx: i], tmp, tmp)
                    else:
                        dfs(i, path + '+' + num[idx: i], value + tmp, tmp)
                        dfs(i, path + '-' + num[idx: i], value - tmp, -tmp)
                        dfs(i, path + '*' + num[idx: i], value - last + last*tmp, last*tmp)
        
        ans, n = [], len(num)
        dfs(0, "", 0, None)
        return ans
