"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
Seen t
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        nums.sort()
        sums_2 = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                sum_2 = nums[i]+nums[j]
                if sum_2 in sums_2:
                    value = sums_2[sum_2]
                    new_value = [i, j]
                    if new_value not in value:
                        sums_2[sum_2].append(new_value)
                else:
                    sums_2.update({sum_2:[[i, j]]})
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 2):
                T = target - nums[i] - nums[j]
                if T in sums_2:
                    for k in sums_2[T]:
                        #import pdb;pdb.set_trace()
                        if k[0] > j:
                            new_comb = [nums[i], nums[j], nums[k[0]], nums[k[1]]]
                            if new_comb not in result:
                                result.append(new_comb)
        return result

if __name__ == "__main__":
    input = [1,0,-1,0,-2,2]
    target = 0
    result = Solution().fourSum(input, target)
    print(result)