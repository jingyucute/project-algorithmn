'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-23 17:10:39
'''

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

# 示例 1:

# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
# 示例 2:

# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
# 进阶:

# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 先暴力
    def search(self, nums, target: int) -> bool:
        for num in nums:
            if num == target:
                return True
        return False

    def search1(self, nums, target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return False


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 7
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.search1(nums, target)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
