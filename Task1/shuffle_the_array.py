class Solution(object):
    def shuffle(self, m, n):
        def iod(i):
            return 2*i if i < n else 2*(i-n)+1
        for i in range(len(m)):
            j = i

        
            while m[i] >= 0:
                j = iod(j)
                m[i], m[j] = m[j], ~m[i] 
        for i in range(len(m)):
            m[i] = ~m[i]
        return m

result = Solution()
print(result.shuffle([2,5,1,3,4,7],3))

