class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cur = len(nums)

        seen = set(nums)

        if(cur != len(seen)):
            return True
        else:
            return False