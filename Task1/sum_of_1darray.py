nums = int(input("Enter number of elements: "))
nums=list(map(int, input("elements of array:-").strip().split()))
print(nums)
def solve(prices):
   n=len(nums)
   rs=[nums[0]]
   for i in range(1,n):
      nums[i]+=nums[i-1]
      rs.append(nums[i])
   return rs

print(solve(nums))