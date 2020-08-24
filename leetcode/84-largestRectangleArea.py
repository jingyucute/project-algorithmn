'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-24 10:12:58
'''

# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

#  


# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

#  


# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

#  

# 示例:

# 输入: [2,1,5,6,2,3]
# 输出: 10


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 暴力算法 超时
    def largestRectangleArea(self, heights) -> int:
        if not heights:
            return 0

        length = len(heights)
        ans = 0
        for left in range(length):
            minHeight = 2**31
            for right in range(left, length):
                minHeight = min(minHeight, heights[right])
                ans = max(ans, minHeight * (right - left + 1))
        return ans

    def largestRectangleArea1(self, heights) -> int:
        ans = 0
        length = len(heights)
        left, right = [0] * length, [0] * length
        stack_left, stack_right = [], []
        for i in range(length):
            l, r = i, length - i - 1
            while stack_left and heights[stack_left[-1]] >= heights[l]:
                stack_left.pop()
            left[i] = stack_left[-1] if stack_left else -1
            stack_left.append(l)

            while stack_right and heights[stack_right[-1]] >= heights[r]:
                stack_right.pop()
            right[r] = stack_right[-1] if stack_right else length
            stack_right.append(r)
        # print(left, right)
        ans = max((right[i] - left[i] - 1) * heights[i]
                  for i in range(length)) if length > 0 else 0

        return ans


if __name__ == '__main__':
    height = [0, 0, 0, 0, 0, 0, 0, 0, 2147483647]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.largestRectangleArea1(height)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
