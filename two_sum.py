class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 18))


            

        