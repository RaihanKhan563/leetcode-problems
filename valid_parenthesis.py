class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        par_dict={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for ch in s:
            if ch in par_dict.values():
                stack.append(ch)
            else:
                if not stack or stack[-1]!=par_dict[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
    
print(Solution().isValid("({)}"))
                
        