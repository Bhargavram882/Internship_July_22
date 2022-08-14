class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")

res = Solution()
print(res.hammingDistance(1,4))