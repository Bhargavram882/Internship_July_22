class Solution(object):
    def numberofSteps(self,num):
        result = 0
        while num:
            result += 2 if num%2 else 1
            num //= 2
        return max(result-1,0)

result = Solution()
print(result.numberofSteps(14))