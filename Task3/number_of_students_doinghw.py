import itertools
from typing import List
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        C,j = 0,0
        while(len(startTime) > j):
            for i in range(startTime[j],endTime[j] + 1):
                if i==queryTime: 
                  C+=1

            j+=1
        return C

result = Solution()
print(result.busyStudent([1,2,3],[3,2,7],4))