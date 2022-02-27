"""la solution brute force sera de faire une double boucle . ex d'application :
[1,2,3,4] la premiere iteration de la premier boucle creer les groupe [1],[1,2],[1,2,3],[1,2,3,4] la deuxieme iteration de la premiere boucle creer les groupes [2],[2,3],[2,3,4] la 3eme iteration: [3],[3,4] la 4eme iteration: [4].
a chaque iteration de la boucle interieur qui nous donne un subarray on rajoute au resultat le min du sub array.
cette solution est O(n^3) TC car les boucles c'est n^2 et le min c'est n car pour trouver le min sur la array il doit la parcourir . on recevra time limite exceed 
la solution sera la suivante:"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res=0
        for i in range (0,n):
            for j in range(i,n):
                res += min(arr[i:j+1])
        return res%(10**9 + 7) 

"""
cette algo est compliquer a decortique je conseigne de pas le faire !!!! (j'ai passer plus de 24heure pour le comprendre je les compris mais il n'est pas du tout intuitif donc impossible a retenir a logique de l'algo ne pas perdre le temps)


cette solution utilise un stack   # TC O(n) #SC O(n)
soit arr=[3,1,2,4] alors :
- 3 est minimum dans les subarray : [3] 
- 1 est minimum dans les subarray : [1] , [3,1] , [1,2], [3,1,2]  , [1,2,4] , [3,1,2,4]
- 2 est minimum dans les subarray : [2] , [2,4]
- 4 est minimum dans les subarray : [4]
pour savoir le nombre de sub array ou un nombre est le minimum de ces subarray il faut savoir combien il ya de nombre plus grand que lui a ca gauche et combien il ya de nombre plus grand que lui a ca droite (on rajoutera au 2 le nombre lui meme). Dans l'exemple precedent si on prend 1 il a 1 nombre plus grand que lui a ca gauche et 2 nombre plus grand que lui a ca droite. la formule pour trouver le nombre de subarray ou un nombre est leur minimum est la suivante : (leftLenght+1)*(rightLenght+1) ; dans notre exemple  le 1 sera le minimum de (1+1)*(2+1)=2*3=6 subarray comme on peut voir les subarray en haut. 
si on prend l'exemple precedent 3 est min dans 1*1=1 subarray, le 1 dans 2*3=6 subarray le 2 dans 1*2=2 subarray et le 4 dans 1*1=1 subarray donc la somme des minimum est egale a 3*1+1*6+2*2+4*1= 3+6+4+4=17 donc le resultat sera 17.
dans cette algo on va utiliser un monotonous increase stack cad que les valeur sont garder dans l'ordre croissant si on veut faire rentrer une valeur dans le stack qui est plus petite que le top de la stack alors on pop() de la stack tant que l'element que on veut faire rentree sera plus grand que le top . (ex si on a 1,3,4 dans le stack eton veut faire rentree 2 alors on pop 4 puis 3 puis on append 2 ce qui nous donne 1,2).
comme on a dit lorsqu'on a une valeur plus petite a faire rentrer on fait pop tant que la valeur a faire rentrer sera plus grande que le top , la on la fait rentrer. lorsqu'on fait pop on sait que le nombre qui se trouve apres au top dans le stack est l'index du premier nombre plus petit que le nombre sur lequelle on a fait pop donc la difference entre le nombre pop() (qui est l'index du nombre au top au moment ou on veut faire rentrer une variable plus petite ) et le nombre qui le precede (qui est l'index du premier plus petit nombre qu'on rencontre avant) qui est au top apres le pop, est la taille de leftLenght+1 c'est pour cela q'on a les ligne suivante dans l'algo : 
index = stack.pop()
left_length = index - stack[-1]
quand on lit un nombre plus petit que le top on fait pop, la difference entre l'index du nombre plus petit (qui sera le premier qu'on rencontre car si on rencontre un nombre plus petit on fait pop donc ce qui se trouve au top rencontre forcement pour la premier fois un nombre plus petit) moins l'index du pop nous donne rightLenght+1 car on rencontre un nombre plus petit pour la premier fois donc ce qui est au top etait minimum jusqu'a present. d'ou la ligne suivante right_length = i - index  (i c'est l'index du nombre plus petit et index c'est la valeur de pop cad l'indexe de la valeur minimal )
cette algo est compliquer a decortique je conseigne de pas le faire 
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        result = 0
        arr=[0]+arr+[0]
        for i, val in enumerate(arr):
            while stack and val < arr[stack[-1]]:
                index = stack.pop()
                left_length = index - stack[-1]
                right_length = i - index
                result += left_length * right_length * arr[index]
            stack.append(i)
        return result % (10 ** 9 + 7)
