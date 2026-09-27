class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted([(num, i) for i, num in enumerate(nums)])
        start = 0
        end = len(nums) - 1
        while start < end:
            current_sum = indexed_nums[start][0] + indexed_nums[end][0]
            if current_sum == target:
                res = [indexed_nums[start][1], indexed_nums[end][1]]
                return sorted(res)
            elif current_sum > target:
                end -= 1
            else:
                start += 1