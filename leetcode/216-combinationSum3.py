'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-25 19:05:55
'''

# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

# 说明：

# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:

# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:

# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []

        def backTrack(index=0, tk=0, tsum=0, path=[]):
            if tk == k and tsum == n:
                result.append(path[:])
            else:
                for i in range(index+1, 10):
                    if tsum + i <= n:
                        tsum += i
                        tk += 1
                        path.append(i)
                        backTrack(i, tk, tsum, path)
                        tsum -= i
                        tk -= 1
                        path.pop()
                    else:
                        return
        backTrack()
        return result


if __name__ == '__main__':

    k = 3
    n = 9
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.combinationSum3(k, n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
