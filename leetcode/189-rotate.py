'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-12 10:06:23
'''

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:

# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 说明:

# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 果不其然， 超时
    def rotate(self, nums, k) -> None:
        if not nums or k == 0:
            return
        length = len(nums)
        for _ in range(k):
            last = nums[-1]
            for j in range(length - 2, -1, -1):
                nums[j + 1] = nums[j]
            nums[0] = last

    def rotate1(self, nums, k) -> None:
        # 辅助数组
        if not nums or k == 0:
            return
        length = len(nums)
        a = [0] * length

        for i in range(length):
            a[(i + k) % length] = nums[i]
        nums[:] = a[:]
        # for _ in range(k):
        #     last = nums[-1]
        #     for j in range(length - 2, -1, -1):
        #         nums[j + 1] = nums[j]
        #     nums[0] = last

    def rotate2(self, nums, k) -> None:
        # 将后面的k个元素，放到前面
        if not nums or k == 0:
            return

        length = len(nums)

        k = k % length
        if k == 0:
            return

        temp = nums[-k:]
        nums[k:] = nums[0:length-k]
        nums[0:k] = temp[:]


if __name__ == '__main__':

    nums = [3, 3, 5, 0, 0, 3, 1, 4]
    k = 2
    start_time = datetime.datetime.now()
    solution = Solution()
    solution.rotate2(nums, k)
    print(nums)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
