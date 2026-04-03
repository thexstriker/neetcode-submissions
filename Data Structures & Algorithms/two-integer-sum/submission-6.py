class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        index = 0
        ind1 = 0
        ind2 = 0
        for num in nums:
            if(target-num in dict):
                ind1 = dict[target-num]
                ind2 = index
            else:
                dict[num] = index
            index += 1
        return [min(ind1, ind2), max(ind1, ind2)]

        
