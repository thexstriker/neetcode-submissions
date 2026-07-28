class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lInd = 0
        rInd = len(nums)-1
        curInd = 0
        while(lInd<rInd):
            curInd = (rInd+lInd)//2
            if(target > nums[curInd]):
                lInd = curInd+1
                curInd = (rInd+lInd)//2
            elif(target < nums[curInd]):
                rInd = curInd-1
                curInd = (rInd+lInd)//2
            else:
                return curInd
        
        print(nums[curInd])
        if(nums[curInd] == target):
            return curInd
        return -1
