'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-18 15:18:19
'''

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

# 你可以假设数组中不存在重复的元素。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 示例 1:

# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:

# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:
                # 前半部分有序
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 后半部分有序
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


if __name__ == '__main__':

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    start_time = datetime.datetime.now()
    solution = Solution()

    result = solution.search(nums, target)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
