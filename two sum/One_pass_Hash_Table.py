class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            
        # Return an empty list if no solution is found
        return []
nums = [1,3,5,7,8]
target =12
solusi1 = Solution()
print(solusi1.twoSum(nums,target))