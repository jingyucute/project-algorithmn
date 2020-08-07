'''
Description: 
Author: jingyu
Date: 2020-08-07 23:38:41
LastEditors: Please set LastEditors
LastEditTime: 2020-08-08 00:22:53
'''

# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

# 你可以假设 nums1 和 nums2 不会同时为空。

# 示例 1:

# nums1 = [1, 3]
# nums2 = [2]

# 则中位数是 2.0
# 示例 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# 则中位数是 (2 + 3)/2 = 2.5

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def getKthElement(k):
            offset1 = 0
            offset2 = 0

            while True:
                if offset1 == len1:
                    return nums2[offset2 + k - 1]
                if offset2 == len2:
                    return nums1[offset1 + k - 1]
                if k == 1:
                    return min(nums1[offset1], nums2[offset2])

                new_offset1 = min(offset1 + k // 2 - 1, len1 - 1)
                new_offset2 = min(offset2 + k // 2 - 1, len2 - 1)

                if (nums1[new_offset1] <= nums2[new_offset2]):
                    k = k - (new_offset1 - offset1 + 1)
                    offset1 = new_offset1 + 1
                else:
                    k = k - (new_offset2 - offset2 + 1)
                    offset2 = new_offset2 + 1
        len1 = len(nums1)
        len2 = len(nums2)
        totalLen = len1 + len2
        if (totalLen % 2 == 1):
            return getKthElement((totalLen + 1) // 2)
        else:
            return (getKthElement(totalLen // 2) + getKthElement(totalLen // 2 + 1)) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2, 4]
    start_time = datetime.datetime.now()
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))
    end_time = datetime.datetime.now()
    print(end_time-start_time)
