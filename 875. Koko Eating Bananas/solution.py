"""explication : koko mange k bananes par heure , il doit finir toute les piles de banane en h heure . le h nous ai donne nous on doit trouver le k. a chaque fois que dans une pile il reste moins de k bananes 
on devra attendre comme meme la fin de l'heure pour passer a une autre pile 
dans l'exemple qui nous ai donne : piles = [3,6,7,11], h = 8 la reponse est 4 car si k=4 alors ca donne ca : 3 4 2 4 3 4 4 3 cad la premier heure il mange 3 puis 4 puis 2 etc... """

"""#ma solution #Binary search # TC O(n log (max(piles))) #SC O(1) 
k peut etre compris entre 1 et le nbr de banane maximum dans une range car si on a par exemple piles =[3,2,5] aors ca sert a rien d'avoir un k>5 car de toute les facons une fois qu'on fini la rangee on ne peut
passer a une autre rangee dans la meme heure . 
on peut dire donc que k appartient au range [1,max(piles)] (max(piles) coute n car il parcours piles pour trouver le max). on va donc utiliser un binary cherche pour trouver le k . le BS marchera de la facon suivante : 
on trouve un mid potentiel si celui ci permet de finir tout les banane dans les h heures donnees alors on reduira le range des possibilites a : [left,mid] (mid et pas mid-1 car mid dans ce cas est une reponse
potentiel)car il est possible qu'on a un k plus petit qui marche aussi. si mid ne permet pas de finir toutes les bananes en h heures alors il nous faut un mid plus grand donc on peut changer le range de cette facon :
[mid+1,right] (mid+! car mid ne marche pas). pour savoir si mid permet de manger toutes les bananes en h heures il faut parcourir piles en retirant a chaque fois mid bananes de la pile i si il reste moins de mid banane 
on ne passe pas a l'autre pile avant la fin de l'heure. si au finale on a fini toute les bananes alors le mid est une reponse potentiel.
le cout de l'algo est donc O(n+log(max(piles))*n) (log(max(piles))*n car a chaque mid on parcours piles donc pour trouver mid c'est log(max(piles)) puis le parcours c'est n)  cad O(n log (max(piles))).
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
                   
            middle = (left + right) // 2  
            
            hour_spent = 0   # hour_spent stands for the total hour Koko spends.
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            # explication : 
            # par exemple si on a k=4 et piles= [3,6,7,11] alors 3/4=0.75 donc 1 heure 6/4 ca donne 1.5 mais comme il ya que des heures complete donc cad 2, 7/4=1.75 cad 2 , 11/4=2.75 cad 3 
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # if koko eat all the bananas under h hours 
            if hour_spent <= h: 
                right = middle
            else:  # if koko did not eat all the bananas under h hours 
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value
        return right
