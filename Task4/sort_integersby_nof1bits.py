from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        k = []
        for i in arr:
            k.append(bin(i).count('1'))
            l = max(k)
        k = []
        for i in range(l+1):
            for j in arr:
                if i ==(bin(j).count('1')):
                    k.append(j)

        return k

result = Solution()
print(result.sortByBits([0,1,2,3,4,5,6,7,8]))
