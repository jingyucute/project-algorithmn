'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 23:05:28
'''

# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1:

# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 示例 2:

# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # 自觉点, 上来就是暴力
        if not matrix:
            return False
        R, C = len(matrix), len(matrix[0])

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    continue
                else:
                    return False
        return False

    def searchMatrix1(self, matrix, target: int) -> bool:
        # 试一下, 将整个二维转为一维的
        if not matrix:
            return False
        datas = []
        for i in range(len(matrix)):
            datas = datas + matrix[i]

        low, high = 0, len(datas) - 1
        while low <= high:
            mid = (low + high) // 2
            if datas[mid] == target:
                return True
            if datas[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False

    def searchMatrix2(self, matrix, target: int) -> bool:
        # 两次二分查询, 类似于块索引
        if not matrix or not matrix[0]:
            return False
        outl, outh = 0, len(matrix) - 1
        while outl <= outh:
            mid = (outl + outh) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                break
            if matrix[mid][0] > target:
                outh = mid - 1
            else:
                outl = mid + 1
        # print(outl, outh, mid)
        inl, inh = 0, len(matrix[mid]) - 1
        while inl <= inh:
            imid = (inl + inh) // 2
            if matrix[mid][imid] == target:
                return True
            if matrix[mid][imid] > target:
                inh = imid - 1
            else:
                inl = imid + 1

        return False

    # 官方二分查找
    def searchMatrix3(self, matrix, target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # 二分查找
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 11
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.searchMatrix3(matrix, target)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
