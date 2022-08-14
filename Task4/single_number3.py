from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        array = []
        for i in nums:
            if nums.count(i) == 1:
                array.append(i)
        return array
res = Solution()
print(res.singleNumber([1,2,1,3,2,5]))