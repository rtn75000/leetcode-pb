""" #ne respecte pas la consigne , juste la pour comprendre . #ma sol #TC O(n) #SC O(1) car le output n'est pas considerer extra space. 
la consigne dit qu'on ne peut utiliser la division cad on ne peut pas calculer le total est ensuite on divise par nums[i] pour avoir answer[i] 
car si par exemple on a [1,2,3,2] alors ttl=12 donc answer=[12/1,12/2,12/3,12/2]  (car si on a a*b*c et on vet retirer par ex b alors il suffit de faire (a*b*c)/b )
il faut verifier le nombre de 0 : si il y'a plus de deux zero answer[i]=0 pour tout i donc on return [0,0,0,0,0]
si il ya que un zero il faut trouver son idx puis tout les answer[i] sont egale a 0 sauf pour answer[idx du zero] qui va etre egale au total (total dans ce cas ne prend pas en compte le 0). 
(on fait attention au nbr de 0 car si il yen a un on ne peut diviser par lui car x/0 c'est indefini).
voici le code qui est accepter mais qui mne respecte pas la consigne 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ttl = 1
        countOfzero = 0   
        idxOfUniqueZero = 0  # l'idx de 0 nous interresse que si il ya que un zero . 
        for i,element in enumerate (nums) :
            if element == 0 :
                countOfzero+=1
                idxOfUniqueZero = i
                if countOfzero>=2 :
                    return [0 for x in nums] #retourne une liste de 0 de la taille de nums
            else :  # on prend en compte dans le total que les elements qui ne sont pas des 0 . 
                ttl*=element
        res=[]
        if countOfzero==1 :  # si on a que un zero alors tout es egale a 0 sauf answer[idx du zero] qui est egale au totale . 
            res= [0 for x in nums]
            res[idxOfUniqueZero]=ttl
            return res
        for element in nums : 
            res.append(ttl//element)
        return res  
        
"""


"""pour les deux solution a venir cette video est super pour comprendre : https://www.youtube.com/watch?v=bNvIQI2wAjk&ab_channel=NeetCode """


"""#sol 1 #prefix and postfix #TC O(n) #SC O(n)
lidee est la suivante on calcule pour chaque idx le produit de son cote gauche et celui de son coter droit , le resultat est cote gauche fois coter droit (cad 
prefix[i-1]*postfix[i+1] si prefix ou postfix existe pas alors on fait fois 1) :
ex : 
nums    =  [2,  2,  3,  4]
prefix  =  [2,  4,  12, 48]   
postfix =  [48, 24, 12, 4]
res     =  [1*24, 2*12, 4*4, 12*1]  

remarque : prefix[i] => c'est le produit des element de 0 a i INCLUS.
           postfix [i] => c'est le produit des element de i a la fin INCLUS. 
           res [i] = prefix[i-1]*postfix[i+1] (a l'idx 0 il ya donc pas de prefix et au derniere index il ya pas de postfix)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix,  postfix, res = [1]*length, [1]*length, [1]*length
        
        # calcule du prefix
        prefix[0] = nums[0]
        for i in range(1,length): # du debut a la fin
            prefix[i] = nums[i] * prefix[i-1]
            
        #calcule du postfix
        postfix[length-1] = nums[length-1]
        for i in range(length-2,-1,-1):  # de la fin au debut 
            postfix[i] = nums[i] * postfix[i+1]
        
        #calcule du res 
        res[0] = postfix[1]      # il ya pas de prefix
        res[length-1] = prefix[length-2]    # il ya pas de postfixe
        for i in range (1,length-1) :  
            res[i]=prefix[i-1]*postfix[i+1]
            
        return res
            

"""#sol 2 #TC O(n) #SC O(1) (l'output n'est pas considerer extra space)
meme chose que la premiere solution sauf qu'on n'utilise pas deux array en plus tout les calcule se font directement dans res """

class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in range(1, len(nums)): # from left to right #calcul du prefix
            res[i] = res[i-1] * nums[i-1]
        tmp = 1
        for i in range(len(nums)-2, -1, -1): # from right to left #calcul du post fix et resulat en meme temps car on a postfix et prefix
            tmp *= nums[i+1]
            res[i] *= tmp
        return res




