'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-03 18:16:13
'''

# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

# 示例 1:

# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 示例 2:

# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 想不出来啥， 暴力枚举
    def maxPoints(self, points) -> int:

        def get_gcd(a, b):
            if b == 0:
                return a
            return get_gcd(b, a % b)

        from collections import defaultdict
        n = len(points)
        if n < 3:
            return n
        max_count = 1
        for i in range(n - 1):
            [point1_x, point1_y] = points[i]
            defalut = defaultdict(int)
            for j in range(i+1, n):
                [point2_x, point2_y] = points[j]
                if point1_x == point2_x:
                    if point1_y == point2_y:
                        if "duplicate" not in defalut:
                            defalut['duplicate'] = 1
                        else:
                            defalut['duplicate'] += 1
                    if point1_y != point2_y:
                        if 'special' not in defalut:
                            defalut['special'] = 1
                        else:
                            defalut['special'] += 1
                    continue
                #  这样写的， 精度好像有问题
                # [[0, 0], [94911151, 94911150], [94911152, 94911151]]
                # 这样的点， 实际上结果为2 , 运算得到3
                # slope = (point2_y - point2_y) / (point2_x - point1_x)

                gcd = get_gcd(point2_y - point1_y, point2_x - point1_x)
                slope = ((point2_y - point1_y) / gcd,
                         (point2_x - point1_x) / gcd)
                if slope not in defalut:
                    defalut[slope] = 1
                else:
                    defalut[slope] += 1
            dup_count = 0
            if 'duplicate' in defalut:
                dup_count = defalut['duplicate']

            for k, v in defalut.items():
                if k == 'duplicate':
                    if v + 1 > max_count:
                        max_count = v + 1
                else:
                    if v + dup_count + 1 > max_count:
                        max_count = v + dup_count + 1

        return max_count


if __name__ == '__main__':

    points = [[0, 0], [1, 1], [1, -1]]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.maxPoints(points)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
