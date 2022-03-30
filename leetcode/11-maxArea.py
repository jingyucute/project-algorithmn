'''
Description: 
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-10 18:30:42
'''
'''
给定一个长度为 n 的整数数组 height。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出: 49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。


示例 2:

输入: height = [1,1]
输出: 1

'''


import datetime


class Solution:

    # 双指针 min(h[left], h[right]) * (right - left)
    # 向内移动短板， 可能会增加容积， 但是移动长板， 一定不会增加容积
    def maxArea(self, height) -> int:
        length = len(height)
        left = 0
        right = length - 1
        max = 0
        while left < right:
            w = right - left
            if height[left] <= height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            if w * h > max:
                max = w*h
        return max


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
