#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return map[nums[i]], i

        return -1, -1
        

