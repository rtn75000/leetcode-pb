"""# ma solution (le code est de qqun d'autre) # soit k egale a sum(weights)-max(weights) alors TC O(nlog(k)) [plus d'explication dans le code] #SC O(1)
l'idee est de faire un BS sur le range [max(weight),sum(weight)] qui est le range possible de capacite que le bateau peut avoir car il doit avoir au minimum le poids du packet le plus
lourd car sinon ce packet ne pourra pas etre transporter et il peut avoir max le la capaciter de la sum des poids de tout les packet si il transporte tout en une fois . donc on va faire un BS
sur le range [max(weight),sum(weight)] ca nous donnera une capacite on essayera de transporter les packert avec la capacite donne on devra parcourir weights et a chaque fois qu'on depasse la capacite 
c'est un nouveau jour si on depasse le nombre de jour de transport autoriser ca veut dire que la capacite est insuffisante donc on ira cote droit de la fenetre si le nombre de jour est trop petit par
rapport au nombre de jours requit alors on ira cote gauche de la fenetre pour abaisser la capaciter .
app : 
wights= [1,2,3,4,5,6,7,8,9,10] days=5 
max.weight==10 total.weight==55 

remarque importante : meme si on a trouver une capacite qui correspond au nombre de jour ce n'est pas forcement la reponse car par exemple [2,4,2] avec day =3 si capacity egale 5 ca me donne 3 jour hors ce n'est pas la bonne reponse car capacity egale 4 donne aussi 3 jour et 4<5 donc 4 la bonne reponse donc meme si on a la reponse il faut continuer a reduire la fenetre coter droit car peut etre il ya une valeur inferieur a mid qui est la reponse optimale

=> on fait  binary search sur [10,55] ce qui donne mid=32 (=(10+55)//2) donc si on a une capacite de 32 ca donne ca :
day 1 : 1,2,3,4,5   (ttl=28)
day 2 : 8,9,10   (ttl=27)
puisqu'on veut en 5 jour ca veut dire que la capacite est trop grande donc on reduit la fenetre du cote droit : [10,32] (on reduit la fenetre a mid et pas mid-1 car pour que l'algorithme ne supprime pas la reponse dans le cas ou on a trouver une reponse on continue a reduire cote droit car possible de trouver une meilleur reponse comme explique en haut mais on garde comme meme la reponse possible dans le range donc a chaque fois que on a un nombre de day superieur ou egale au day qu'on recherche on ferme la fenetre comme ca [left,mid] et pas [left, mid-1] )
=> on fait  binary search sur [10,32] ce qui donne mid=21 donc si on a une capacite de 21 ca donne ca :
day 1 : 1,2,3,4,5,6   (ttl=21)
day 2 : 7,8   (ttl=15)
day 3 : 9,10 (ttl=19)
puisqu'on veut en 5 jour ca veut dire que la capacite est trop grande donc on reduit la fenetre du cote droit : [10,21]
=> on fait  binary search sur [10,21] ce qui donne mid=15 donc si on a une capacite de 15 ca donne ca :
day 1 : 1,2,3,4,5   (ttl=15)
day 2 : 6,7   (ttl=13)
day 3 : 8
day 4 : 9
day 5 : 10
meme si on a trouver une capaciter qui correspond au nombre de jour c'est possible qu'il ya une capaciter plus petite qui correspond au nombre de jour donc on reduit juste la fenetre a droite : [10,15]  (voir en haut pq c possible)
=> on fait  binary search sur [10,15] ce qui donne mid=12 donc si on a une capacite de 12 ca donne ca :
day 1 : 1,2,3,4   (ttl=10)
day 2 : 5,6   (ttl=11)
day 3 : 7 
day 4 : 8
day 5 : 9
day 6 : 10
puisqu'on veut en 5 jour ca veut dire que la capacite est trop petite donc on reduit la fenetre du cote gauche : [13,15] (dans ce cas on fait [mid+1,right] car quand on obtient un nombre de jour sup au nombre de jour requis c'est sur qu'il faut augmenter la capacite)
=> on fait  binary search sur [13,15] ce qui donne mid=14 donc si on a une capacite de 14 ca donne ca :
day 1 : 1,2,3,4   (ttl=10)
day 2 : 5,6   (ttl=11)
day 3 : 7 
day 4 : 8
day 5 : 9
day 6 : 10
puisqu'on veut en 5 jour ca veut dire que la capacite est trop petite donc on reduit la fenetre du cote gauche : [15,15] pusique left<right est false on a le resultat optimal
"""
class Solution:
    def shipWithinDays(self, weights: List[int], maxDays: int) -> int:
        left, right = max(weights), sum(weights)   #cost O(n) each operation so overall O(n)
        while left < right:  # coute O(log(sum(weights)-max(weights)) car on fait BS dans le range [max(weights), sum(weights)])
            mid = (left + right) // 2  #(ou left+(right-left)//2)
            curCap = 0  # la capacite utiliser du bateau
            days = 1    #number of days needed to transport all the packages
            for w in weights: # coute O(n) car on passe sur tout weight 
                # si en rajoutant un nouveau package a la capaciter deja utiliser on depasse la capacite potentiel qui est egle a mid alors on ne peut transporter ce packet il faut un autre jour
                if curCap + w > mid:  
                    days += 1
                    curCap = 0
                curCap += w
            if days > maxDays: # si on a depasse le nombre de jour donc il faut forcement augmenter la capaciter donc nouveau range [mid+1,right]
                left = mid + 1
            else:  # si on a un nombre de jour inferieur ou egale a maxDays ou doit reduire la capacite donc nouveau range [left,mid] (et pas mid-1 car si egale c'est une reponse potentiel)
                right = mid
        return left
    
# soit k egale a sum(weights)-max(weights) alors on a un total cost de O(2n+log(k)*n)=O(n+nlog(k))=O(nlog(k))
