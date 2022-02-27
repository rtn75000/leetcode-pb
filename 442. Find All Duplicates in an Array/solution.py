"""le code est prix d'ici : https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92444/Python-solution-with-detailed-explanation

   l'explication de ce code viens aussi d'ici : https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/775738/Python-2-solutions-with-O(n)-timeO(1)-space-explained
   
explication: puisque la taille du array de base est N et que tous les nombres contenues dans le array sont inferieur a n, on aura donc un index correspondant a chaque nombre .
l'idee est que si par exemple je lit 4 dans le array alors le nombre qui est a l'index 4-1 (car array commence a 0) je le transforme en un nombre negatif ca sera le signe que
j'ai un 4 donc si je rencontre encore un quatre je me rend a l'index 4-1 je vois que le nombre contenue est negatif je sais donc que 4 est un duplicate je le rajoute donc a la 
reponse"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:
            if nums[abs(x)-1] < 0:   # on met valeur absolue car possible que x qui est un nombre dans le array a ete modifier en negatif car on car l'index ou il se trouve correspond a un nombre que on a deja rencontrer mais comme maintenant on lit x on veut le x d'origine cad ca valeur absolue pour pouvoir se rendre a l'index qui lui correspond. si le nombre contenue a l'index abs(x)-1 est negatif cad qu'on a deja rencontrer x donc c'est un duplicate. (si le nombre est positif alors on fait le else qui changera ce nombre en negatif)
                result.append(abs(x))
            else:
                nums[abs(x)-1] = -1*nums[abs(x)-1]
        return result
