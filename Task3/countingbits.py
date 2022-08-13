from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(0,n+1):
         y =  bin(i)
         arr.append(y.count("1"))
        return arr

result = Solution()
print(result.countBits(2))