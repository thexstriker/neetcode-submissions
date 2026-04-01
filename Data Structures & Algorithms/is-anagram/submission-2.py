class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)

        if(len(listS) != len(listT)):
            return False
        
        dictS = {}
        dictT = {}

        for char in listS:
            dictS[char] = dictS.get(char, 0) + 1
        for char in listT:
            dictT[char] = dictT.get(char, 0) + 1
        for i in dictS:
            if(dictS.get(i) != dictT.get(i)):
                return False
        return True



        
        