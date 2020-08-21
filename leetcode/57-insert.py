'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 23:25:10
'''


# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。

# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。


# 示例 1：

# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：

# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def insert(self, intervals, newInterval):

        if not intervals:
            return [newInterval[:]]
        if newInterval in intervals:
            return intervals
        else:
            intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = []
        # print(intervals)

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]

    newInterval = [4, 8]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.insert(intervals, newInterval)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
