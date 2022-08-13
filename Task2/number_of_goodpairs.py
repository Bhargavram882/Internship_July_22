import collections


class Solution(object):
    def numIdenticalPairs(self, nums):
        watch = {}
        res = 0
        for x in nums:
            if x in watch:
                res += watch[x]
                watch[x] += 1
            else:
                watch[x] = 1
        return res

reswer = Solution()
print(reswer.numIdenticalPairs([1,2,3,1,1,3]))