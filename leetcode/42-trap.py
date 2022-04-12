'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-19 19:55:00
'''


# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

# 示例:

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime

class Solution:
    def trap(self, height) -> int:
        # 主要是找每跟柱子两侧的最大值的最小值， 然后这个值减去当前高度， 就是堆积的雨水量
        if not height:
            return 0
        length = len(height)
        max_left = [0] * length
        max_right = [0] * length
        max_left[0], max_right[length - 1] = height[0], height[length - 1]

        for i in range(1, length):
            max_left[i] = max(height[i], max_left[i - 1])
            max_right[length - 1 -
                      i] = max(height[length - 1 - i], max_right[length - i])
        # print(height)
        # print(max_left, max_right)
        total = 0
        for i in range(length):
            hi = height[i]
            min_width_height = min(max_left[i], max_right[i])
            cur_v = min_width_height - hi
            total += cur_v

        return total

    def trap2(self, height) -> int:
        if not height:
            return 0
        total = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0 
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                total += leftMax - height[left]
                left += 1
            else:
                total += rightMax - height[right]
                right -= 1
        return total


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = solution.trap(height)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
