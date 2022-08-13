
from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for M in nums:
            if len(str(M)) % 2 == 0:
                result += 1
        return result

answer = Solution()
print(answer.findNumbers([12,345,2,6,7896]))