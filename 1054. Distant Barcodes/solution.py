"""meme solution que la deuxieme solution que j'ai ecris ici : https://leetcode.com/problems/reorganize-string/submissions/
cout TC et SC O(n) avec n=barcodes.lenght
il faut comme dans la reponse du link compter la frequence de chaque nbr puis mettre se nombre dans les place paires puis mettre le reste dans le reste des places paire et ensuite impaire .
(ici pas besoin de verifier il ya forcement un valid output)
remarque : on peut resoudre aussi comme la premiere solution du link.
"""
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
         
        n = len(barcodes)
        
        count = Counter(barcodes) # Hashmap, count each nbr { nbr:freq , .. } # TC O(n)   #SC O(n)
        
        maxi = 0     # frequence du nbr le plus frequent
        maxNbr = '' # nbr le plus frequent
        # recherche du nbr le plus frequent avec sa frequence 
        for nbr in count:   # O(n)
            if count[nbr]> maxi:
                maxi, maxNbr = count[nbr], nbr
                    
        res = [0]*n  # SC O(n)
        idx = 0
        # on met le nbr le plus frequent dans les places paires
        for _ in range(count[maxNbr]):
            res[idx] = maxNbr
            idx += 2
        count[maxNbr] = 0 #apres avoir mis le nbr le plus frequent la frequence de ce nbr devient 0 car on a tout mis
        # maintenant on met les autres nbrs , on fini avec les places paires puis on passe au place impaire 
        # on ajoute au res chaque nbr autant de fois que la frequence de ce nbr.
        for nbr in count:  # cette boucle coute au max O(n) car fait une iteration pour une unite de frequence cad au total au max elle fait autant d'iteration que la somme des freq de la phrase 
            for i in range(count[nbr]):   
                if idx >= n:  # si on a fini avec les places paires et donc si idx>len(s) alors on passe au passe impaire donc idx=1
                    idx = 1
                res[idx] = nbr
                idx += 2
        return res  
       
        
