class Solution:
    def isValid(self, s: str) -> bool:
        pairs = ['(', '[', '{', ')', ']', '}']
        stack = []
        for i in range(len(s)):
            cur = s[i]
            if(len(stack) == 0):
                stack.append(cur)
            else:
                if(pairs.index(cur) <= 2):
                    stack.append(cur)
                else:
                    check = stack.pop()
                    if(check != pairs[pairs.index(cur)-3]):
                        return False
        if(len(stack) > 0):
            return False
        return True