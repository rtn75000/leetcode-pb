class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict = {}
        for char in s :
            if char in dict :  #cad si il est key dans le dict 
                dict[char]+=1
            else :
                dict[char]=1
        if  len(set(dict.values())) == 1 : #dict.values() retourne un array de toutes les valeurs du dict 
            return True
        return False 
             
# rappel les set ne garde pas les duplicates donc si la meme valeur dans tout les lettre le set garde que une valeur 
          
            
