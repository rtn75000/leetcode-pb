""" # ma sol # array  # TC O(n)  # SC O(1)
ce qu'il faut comprendre c'est que le max doit venir apres le min car pour faire un max de profit il faut d'abord acheter au min puis ensuite revendre au max , donc a chaque fois qu'on choisi un min l'ancien
max n'est plus utilisable car il faut un max qui vient apres . Donc mon idee est de faire que quand on choisi un nouveau min car on trouve une valeur plus petite alors on fait min = max = nouvelle valeur.
si le max est inferieur a la valeur actuelle alors il faut update le max , seulement dans ce cas on calcule max-min et on garde la plus grande diff calculer jusqu'a present. 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        
        mini = float('inf') 
        maxi = maxDiff = 0   # maxi=0 car prices > 0 
        
        for idx in range (len(prices))  :
            
            if prices[idx] < mini:
                mini = maxi = prices[idx]
                
            elif prices[idx] > maxi:
                maxi = prices[idx]
                maxDiff=max(maxDiff,maxi-mini)
                
        return maxDiff 
    
