from typing import List
class Solution:
    def subset(self,nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            res = res + [lst + [nums[i]] for lst in res]
        return res

res = Solution()
print(res.subset([1,2,3]))