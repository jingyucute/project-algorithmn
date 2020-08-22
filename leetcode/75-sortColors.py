'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 23:23:48
'''

# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 注意:
# 不能使用代码库中的排序函数来解决这道题。

# 示例:

# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：

# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    # 官网思路， 还是很巧妙。
    # 但是我在想， 如果颜色种类过多， 应该怎么处理？
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        borderL, borderR = 0, len(nums) - 1
        curPos = 0
        while curPos <= borderR:
            if nums[curPos] == 0:
                nums[borderL], nums[curPos] = nums[curPos], nums[borderL]
                borderL += 1
                curPos += 1
            elif nums[curPos] == 2:
                nums[borderR], nums[curPos] = nums[curPos], nums[borderR]
                borderR -= 1
            else:
                curPos += 1


if __name__ == '__main__':
    nums = [1, 2, 0]
    start_time = datetime.datetime.now()
    solution = Solution()
    solution.sortColors(nums)
    print(nums)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
