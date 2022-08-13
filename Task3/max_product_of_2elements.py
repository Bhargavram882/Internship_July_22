class Solution(object):
    def maxProduct(self,nums):
        n1=n2=0
        for num in nums:
            if num > n1:
                n1,n2 = num,n1
            elif num > n2:
                n2 = num
        return (n1-1)*(n2-1)
result = Solution()
print(result.maxProduct([3,4,5,6]))
