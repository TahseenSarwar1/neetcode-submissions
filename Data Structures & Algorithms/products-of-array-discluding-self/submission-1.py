class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(nums)):
        #     val = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         else:
        #             val = val * nums[j]
        #     ans.append(val)
        # return ans

        # ans = [0] * len(nums)
        # prd = 1
        # for i in range(len(nums)):
        #     prd = prd * nums[i]
        
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         ans[i] = 0
        #     else:
        #         ans[i] = int(prd/nums[i])
        

        # return ans

        ans = [1] * len(nums)

        product = 1

        # Prefix / left product
        for i in range(len(nums)):
            ans[i] = product
            product *= nums[i]

        product = 1

        # Suffix / right product
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= product
            product *= nums[i]

        return ans