from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        z = nums[0]
        for num in z[1:]:
            z^= num
        
result = Solution()
print(result.singleNumber([2,2,1]))