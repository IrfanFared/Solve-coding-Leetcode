class Solution:
    def twoSum(self,nums : list[int],target : int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []

nums = [1,8,8,6,5]
target = 9
solusi = Solution()
solusi.twoSum(nums,target)
print(solusi.twoSum(nums ,target))