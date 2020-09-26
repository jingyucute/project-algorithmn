'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 13:27:53
'''

# 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

# 每个矩形由其左下顶点和右上顶点坐标表示，如图所示。


# 示例:

# 输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        if A > E:
            return self.computeArea(E, F, G, H, A, B, C, D)

        # 没有重叠

        total = abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H)

        if B >= H or D <= F or C <= E:
            return total

        # 重叠情况

        down = max(A, E)
        up = min(C, G)
        left = max(B, F)
        right = min(D, H)

        return total - abs(down-up) * abs(left-right)


if __name__ == '__main__':
    A, B, C, D, E, F, G, H = -3, 0, 3, 4, 0, -1, 9, 2
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.computeArea(A, B, C, D, E, F, G, H)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
