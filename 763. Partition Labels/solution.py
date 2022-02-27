# solution d'ici : https://leetcode.com/problems/partition-labels/discuss/298474/Python-two-pointer-solution-with-explanation
class Solution:
    def partitionLabels(self,S):

        rightmost = {c:i for i, c in enumerate(S)} # cree dictionnaire avec position==key:lettre===val
        left, right = 0, 0

        result = []
        
          # a chaque fois qu' on lit une letrre on change de limite a droite si rightmost[letter] (cad la limite de la lettre actuelle) est superieur a la limite existante 
            
        for i, letter in enumerate(S):
      
            right = max(right,rightmost[letter])

            if i == right:
                result += [right-left + 1]
                left = i+1

        return result
