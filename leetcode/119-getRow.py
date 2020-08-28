'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 14:40:10
'''

# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 3
# 输出: [1,3,3,1]
# 进阶：

# 你可以优化你的算法到 O(k) 空间复杂度吗？

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def getRow(self, rowIndex: int):
        kList = []
        for i in range(rowIndex+1):
            kList.append(1)
            for j in range(i, 1, -1):
                # print("i--", i, "j--", j)
                kList[j - 1] += kList[j - 2]
        return kList


if __name__ == '__main__':

    rowIndex = 5

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.getRow(rowIndex)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
