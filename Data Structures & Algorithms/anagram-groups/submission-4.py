class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrings = []
        for word in strs:
            temp = []
            for char in word:
                temp.append(char)
            temp.sort()
            cur = "".join(temp)
            sortedStrings.append(cur)

        ans = []
        my_map = {}
        ind = 0
        indOfSubList = 0
        for word in sortedStrings:
            if(my_map.get(word, "") == ""):
                my_map[word] = (str(indOfSubList))
                ans.append([strs[ind]])
                indOfSubList += 1

            elif(int(my_map.get(word, "")) != ""):
                ans[int(my_map[word])].append(strs[ind])
            ind += 1
        return ans





