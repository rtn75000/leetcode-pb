"""pour resoudre ce pb il faut simplement savoir que la taille de n'importe quel cote doit etre inferieur a la somme de la taille des deux autres cotes. donc : a, b, c can form a Triangle if and only if a + b > c && a + c > b && b + c > a."""
"""je ne me suis pas attarder sur ce pb car la meilleur solution constitue un linear scan ce n'eatit pas le sujet que je recherche. (j'ai ajouter le code juste pour motrer qu'il est plutot simple et augmenter les state) """
"""ce code a le meilleur TC (O(n^2)) ce n'est pas le mien: https://leetcode.com/problems/valid-triangle-number/discuss/1339340/C%2B%2BJavaPython-Two-Pointers-Picture-Explain-Clean-and-Concise-O(N2)
voir aussi solution du pb dernier solution"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans

