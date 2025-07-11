class Solution:
    def twoSum(self,nums : list[int], target : int) -> list[int]:
        hasmap = {}
        for  i in range(len(nums)):
            hasmap[nums[i]] = i

        for i in range(len(nums)):
            pelengkap = target - nums[i]
            if pelengkap in hasmap and hasmap[pelengkap] != i:
                return[i, hasmap[pelengkap]]
            

nums = [1,3,5,7,8]
target =12
solusi1 = Solution()
print(solusi1.twoSum(nums,target))