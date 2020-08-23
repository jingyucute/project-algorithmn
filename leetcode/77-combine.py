'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-23 12:44:06
'''
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:

# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def combine(self, n: int, k: int):

        result = []

        def backTrack(index, used, path, result):
            if index > k:
                result.append(path.copy())
            else:
                max_used = 0
                for i in range(1, n + 1):
                    if used[i]:
                        max_used = i
                min_i = max_used + 1
                for num in range(min_i, n + 1):
                    used[num] = True
                    path.append(num)
                    backTrack(index+1, used, path, result)
                    used[num] = False
                    path.pop()

        used = [False] * (n + 1)
        backTrack(1, used, [], result)

        return result

    # 官方写的， 感觉简洁多了
    def combine1(self, n: int, k: int):

        def backTrack(first=1, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
            else:
                for i in range(first, n + 1):
                    curr.append(i)
                    backTrack(i + 1, curr)
                    curr.pop()

        output = []
        backTrack()

        return output


if __name__ == '__main__':
    n, k = 4, 2
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.combine1(n, k)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
