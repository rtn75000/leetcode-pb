""" #not my sol #logique #TC O(n) #SC O(1)
la difference gas[i]-cost[i] nous donne combien de gas on aura en plus ou en mois en passant par la station i pour arriver a la station i+1. 
par exemple si on a gas = [2,3,1] et cost[i] = [3,1,2] alors diff = [-1,2,-1] cad par exemple si on passe par la station i=1 alors on va prendre +2 de gas dans le reservoire,
si on passe par la station i=0 alors on va prendre -1 dans le reservoire.
pour comprendre la solution il faut comprendre qqeu points importants : 

->  Il existe une solution que si la somme ttl des diff est superieur ou egale a 0, car elle est inferieur a 0 ca veut dire que quand on fait un tour on a un taux de resevoir 
    neg cad on peut pas faire le tour. donc il ya une solution si la somme totale des diff est sup egale a 0.

->  Si la voiture commence a la station A et ne peut atteindre la station Z car la somme des diff entre A et Z est neg alors si elle commence a n'importe quelle station entre 
    A et Z elle ne pourra atteindre Z . 
    ex si on a gas=[...,2,2,5,1,2,...] et cost=[...,1,4,1,6,1,...] cad diff=[...,1,-2,4,-5,1,...]
                        ^   ^   ^      
                        A   B   Z        
    de A a Z on a sumdiff<0 cad on ne peut commencer de A pour aller a Z donc on ne peut pas aussi commencer de B pour aller a Z.
    donc tout les stations entre A et Z ne peuvent etre un point de depart. il faut commencer a une station apres z un nouveau depart 

"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ttl = 0  #somme total des diff
        curttl = 0 #somme des diff du point de depart a la station actuelle 
        start = 0 #point de depart de la voiture 
        for i in range(len(gas)) : 
            diff = gas[i]-cost[i]         
            ttl+=diff 
            curttl += diff
            if curttl < 0: # si la somme des diff est neg alors on doit prendre un nouveau depart 
                curttl = 0 #on recommence a compter car nouveau depart
                start = i+1
    
        return start if ttl>=0 else -1 # on retourn un resultat que si la somme des diff est sup egale a 0 car sinon ca veut dire qu'on ne peut faire un tour complet
            
            
