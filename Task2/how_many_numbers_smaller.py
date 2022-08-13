from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        array = [0]*len(nums)
        
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1       
            array[i] = count
        return array
result = Solution()
print(result.smallerNumbersThanCurrent([8,1,2,2,3]))