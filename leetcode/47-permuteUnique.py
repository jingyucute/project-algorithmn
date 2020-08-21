'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 15:28:15
'''

# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

# 示例:

# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def permuteUnique(self, nums):
        n = len(nums)
        result = []
        if n == 0:
            return result

        def backTrack(first=0):
            if first == n:
                # 感觉在这里去重不是很好, 没有优化解空间
                if nums not in result:
                    result.append(nums.copy())
            else:
                for i in range(first, n):
                    if i != first and nums[i] == nums[first]:
                        continue
                    nums[first], nums[i] = nums[i], nums[first]
                    backTrack(first+1)
                    nums[first], nums[i] = nums[i], nums[first]
        backTrack()
        return result

    def permuteUnique1(self, nums):
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:
                    #  判断第 i 个元素是否可以添加到list中
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        # 因为 nums 排过序, 所以重复元素会相邻
                        # 相同元素, 前面没有用过, 这儿就不能用
                        # 为什么: 因为相同元素添加到路径中, 要用也是先用第一个, 不然不能保证不可重复出现。
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


if __name__ == '__main__':
    nums = [2, 2, 1, 1]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.permuteUnique1(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
