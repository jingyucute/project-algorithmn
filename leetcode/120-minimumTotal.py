'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 16:12:29
'''

# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

#  

# 例如，给定三角形：

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

#  

# 说明：

# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:

    # 回溯法 超时
    def minimumTotal(self, triangle) -> int:
        if not triangle:
            return 0
        min_sum = 9**10
        length = len(triangle)

        def backTrack(index=0, pre_pos=0, path=[], cur_sum=0, data_list=[]):

            if index >= length:
                if cur_sum < data_list[0]:
                    data_list[0] = cur_sum
            else:
                if pre_pos < len(triangle[index]):
                    cur_val = triangle[index][pre_pos]

                    path.append(cur_val)
                    cur_sum += cur_val
                    backTrack(index+1, pre_pos, path, cur_sum, data_list)
                    path.pop()
                    cur_sum -= cur_val
                if pre_pos + 1 < len(triangle[index]):
                    cur_val = triangle[index][pre_pos + 1]
                    path.append(cur_val)
                    cur_sum += cur_val
                    pre_pos += 1
                    backTrack(index+1, pre_pos, path, cur_sum, data_list)
                    path.pop()
                    cur_sum -= cur_val
                    pre_pos -= 1
        data_list = [
            min_sum
        ]
        backTrack(0, 0, [], 0, data_list)

        return data_list[0]

    # dp
    def minimumTotal1(self, triangle) -> int:
        length = len(triangle)
        # dp[i][j] 表示从(0,0) -> (i, j) 的最短距离
        dp = [[0] * length for _ in range(length)]
        dp[0][0] = triangle[0][0]
        for i in range(1, length):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        return min(dp[length-1])


if __name__ == '__main__':

    triangle = [[-1], [2, 3], [1, -1, -3]]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.minimumTotal1(triangle)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
