"""la consigne interdit de modifier l'array et permet d'utiliser que O(1) space """


"""#binary search #TC O(n log n) #SC O(1)
tout les numero de la liste sont dans le range [1,n] donc on va faire un binary earch sur ce range , le binary search va nous donner un nombre qui sera le mid de [1,n] , on va regarder ensuite dans nums combien de nombre
sont inferieur a mid si il ya plus que mid nombre inferieur egale a mid ca veut dire qu'il ya un nombre qui se repete exemple soit nums = [4,3,2,6,5,7,8,1,7,10,7] comme il ya 10+1 nombre chaque nombre doit etre dans le 
range [1,10]  si je prend le nombre 10 si il a pas de nbr duplicate inferieur a lui il doit avoir normalement maximum 10 nombres inferieur ou egale car chaque nombre est repeter que une fois donc on doit avoir 
1,2,3,4,5,6,7,8,9,10 e mais dans notre cas on a 11 nombre inf ou egale a 10 donc ca veut dire qu'il ya forcement un duplicate. l'algo est le suivant : 

nums = [4,3,2,6,5,7,8,1,7,10,7]  

--> binary search sur range [1,10] qui donne mid = 5  (=1+(10-1)//2) donc on cherche dans nums tout les nombres inferieur egale a 5 comme il y'en a 5 donc forcement qu'il y'a pas de duplicate dans le range [1,5]. donc 
maintenant le range sur lequel on va faire le binary search va etre [6,10] 

--> binary search sur range [6,10] qui donne mid = 8  (=6+(10-6)//2) donc on cherche dans nums tout les nombres inferieur egale a 8 comme il y'en a 10 donc il ya plus de 8 nombre inferieur egale a 8 cad qu'il ya
forcement un duplicate donc on sait que le duplicate est soit 8 soit un nombre avant 8 donc maintenant on va faire binary search sur le range [6,8]

--> binary search sur range [6,8] qui donne mid = 7  (=6+(8-6)//2) donc on cherche dans nums tout les nombres inferieur egale a 7 comme il y'en a 9 donc forcement qu'il y'a un duplicate qui peut etre 7 ou un nombre 
inferieur. donc maintenant le range sur lequel on va faire le binary search va etre [6,7] 

--> binary search sur range [6,7] qui donne mid = 6  (=6+(7-6)//2) donc on cherche dans nums tout les nombres inferieur egale a 6 comme il y'en a 6 donc il ya pas de duplicate avant 6 inclu donc le nouveau range est 
[7,7] ; comme 7<7 est faux dc c'est le dernier nbr qui nous reste c'est donc lui le duplicate 

code d'ici : https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation)%3A-O(nlog(n))-and-O(n)-time-O(1)-space-without-changing-the-input-array
"""  

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)-1
        
        while low < high:             # ce while coute log n car il fait binary search sur le range [1,n]
            mid = low+(high-low)//2   # binary search sur le range [low,high]
            count = 0
            # compte de nombre inferieur ou egale a mid
            for i in nums:           # cette boucle coute n car on regarde tout les nombre inferieur a mid dans nums donc on parcours tout nums  (cout total : n log n )
                if i <= mid:
                    count+=1
            if count <= mid:   # si il ya moins de mid nombre inferieur ou egale a mid alors il ya pas de duplicate avant mid inclu donc nouveau range [mid+1,high] 
                low = mid+1
            else:              # si il ya plus de mid nombre inferieur ou egale a mid alors il ya un duplicate avant mid ou mid peut etre le duplicate donc nouveau range [low,mid]
                high = mid
        return low   # c'est le dernier nombre qui restera dans le range c'est lui forcement le duplicate
    
    
"""il ya une autre solution qui utilise un algoritme appele Floyd's Cycle Detection qui permet d'avoir un TC O(n) et SC O(1). mais c'est plus compliquer et pas intuitive donc je l'ai pas fait
"""
