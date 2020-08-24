'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-24 19:45:29
'''

# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

#  

# 说明:

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#  

# 示例:

# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# 输出: [1,2,2,3,5,6]


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()

    def merge1(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur_m, cur_n = 0, 0
        nums1_copy = nums1[:m]
        nums1[:] = []

        while cur_m < m and cur_n < n:
            if nums1_copy[cur_m] <= nums2[cur_n]:
                nums1.append(nums1_copy[cur_m])
                cur_m += 1
            else:
                nums1.append(nums2[cur_n])
                cur_n += 1

        if cur_m < m:
            nums1[cur_m + cur_n:] = nums1_copy[cur_m:]

        if cur_n < n:
            nums1[cur_m + cur_n:] = nums2[cur_n:]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    start_time = datetime.datetime.now()
    solution = Solution()
    solution.merge1(nums1, m, nums2, n)
    print(nums1)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
