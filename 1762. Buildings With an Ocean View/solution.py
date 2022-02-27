"""# stack use #TC O(n) #SC O(1) the answer list is not an extra space
code d'ici : https://leetcode.com/problems/buildings-with-an-ocean-view/discuss/1071380/Python3-Simple-O(n)-solution
l'idee est simple on commence par le derniere immeuble qui lui a forcement la vu sur la mer donc on peut le rajouter au resultat directement ensuite on regarde l'immeuble qui le precede si ca taille est superieur alors on le rajoute au resultat il sera donc en dernier du resultat . puis on comparele dernier du resultat avec un immeuble avant si il est grand on le rajoute.
l'idee c'est de comparer le dernier ajouter avec ce qu'il reste. en faite on commence par l'immeuble en front de mere puis apres on doit avoir des immeuble de taille en ordre croissant stricte """
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[res[-1]]:
                res.append(i)
        res.reverse() # on doit reverse la list car on ajoute dans l'ordre inverse de la reponse
        return res
