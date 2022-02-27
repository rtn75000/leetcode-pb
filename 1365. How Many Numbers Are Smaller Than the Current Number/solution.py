class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """resolution en O(n log n)
        l'idee c'est que on fait un tableau qui contient en key les valeur nums[i] et en valeur le nombre de valeur inferieur 
        """
        temp = sorted(nums)
        mapping = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in mapping: 
                mapping[temp[i]] = i
        for i in range(len(nums)):
            result.append(mapping[nums[i]])
        return result
