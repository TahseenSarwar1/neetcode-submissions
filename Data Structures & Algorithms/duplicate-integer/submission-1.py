class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Method-1: Brute Force 

        # Method-2: 
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # Method-3
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False