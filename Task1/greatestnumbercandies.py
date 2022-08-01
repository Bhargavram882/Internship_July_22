
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_num = max(candies)
        return [x + extraCandies >= max_num for x in candies]

result = Solution()
print(result.kidsWithCandies([2,3,5,1,3],3))