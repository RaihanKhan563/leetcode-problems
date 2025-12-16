class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            temp = []
            for c, d in zip(prefix, word):
                if c == d:
                    temp.append(c)
                else:
                    break
            prefix = "".join(temp)

            if not prefix:
                return ""

        return prefix
sol=Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))