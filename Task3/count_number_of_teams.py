class Solution:
    def numTeams(self, rating):
        result = 0
        for i in range(1, len(rating)-1):
            less, greater = [0]*2, [0]*2
            for j in range(len(rating)):
                if rating[i] > rating[j]:
                    less[i < j] += 1
                if rating[i] < rating[j]:
                    greater[i < j] += 1
            result += less[0]*greater[1] + greater[0]*less[1]
        return result

result = Solution()
print(result.numTeams([2,5,3,4,1]))