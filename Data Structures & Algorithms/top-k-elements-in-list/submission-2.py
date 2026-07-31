class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if(map.get(num, 0) == 0):
                map[num] = 1
            elif(map.get(num,0) > 0):
                map[num] += 1

        mySet = set(nums)
        for num in nums:
            mySet.add(num)
        myList = list(mySet)
        
        ans = []
        for i in range(k):
            max = 0
            maxNum = 0
            for j in range(len(myList)):
                if(map[myList[j]] > max):
                    max = map[myList[j]]
                    maxNum = myList[j]
            myList.remove(maxNum)
            ans.append(maxNum)
        return ans
