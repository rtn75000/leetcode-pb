"""#hashmap #set #TC O(n)  #SC O(n)

la consigne est qu'il faut qu'aucun nbr est le meme nombre d'occurence qu'un autre sinon on rend False.

on va donc utiliser un hash table pour compter les frequence de chaque nbr , voir la suite dans le code ."""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counter=collections.Counter(arr)  # nous donne un dic :  {nbr:freq}    #TC SC O(n)
        
        # maintenant on va prendre toutes les frequences 
        freqArray = counter.values() #donne un array des valeurs du dict donc un array des frequence   #SC O(n)
        
        # on veut que il y ai pas de frequence double donc on va convertir freqArray en set (un set ne garde pas les doublons)
        # si il ya pas de doublons alors le set ne supprime aucune valeur est donc la taille du set est egale a la taille de l'array , sinon la taille est differente
        # donc on return la comparaison des taille : si elle sont egale return True sinon False 
        return  len(freqArray)==len(set(freqArray))   # convertir un set en array coute O(n) (car on passe sur tout les elements de l'array)
            
