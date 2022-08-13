class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(n):
            arr.append(start + 2 * i)
        # print (arr)
        xr = 0
        for i in arr:
            xr = xr ^ i
        return xr

result = Solution()
print(result.xorOperation(5,0))