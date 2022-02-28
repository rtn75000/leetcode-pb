"""#TC O(n) #SC O(n)
voir next grater element I : https://leetcode.com/problems/next-greater-element-i/
ici on doit rendre le next greater element de tout les nombres + l'array doit etre considerer circulaire . 
au meme raisonnement on rajoute juste l'idee que pour obtenir un circular array il suffit de parcourrir 2 fois le array pour avoir fait un tour complet ce qui suffit pour rechercher
qui est le next greater number parceque apres ca revient au meme"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack, res = [], [-1] * n
        for i in range(n * 2) :
            while stack and (nums[stack[-1]] < nums[i%n]):
                res[stack.pop()] = nums[i%n]
            stack.append(i%n)
        return res
