'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 21:17:34
'''

# 给出一个区间的集合，请合并所有重叠的区间。

#  

# 示例 1:

# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:

# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。

#  

# 提示：

# intervals[i][0] <= intervals[i][1]


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    # 分治法
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        length = len(intervals)
        # print(intervals)

        def mergeList(left, right):
            if left == right:
                return intervals[left:right+1]
            mid = (left + right) // 2
            leftList = mergeList(left, mid)
            rightList = mergeList(mid+1, right)
            # 合并
            # print(leftList, rightList)
            ans = []
            if leftList[-1][-1] < rightList[0][0]:
                for t in leftList:
                    ans.append(t)
                for t in rightList:
                    ans.append(t)
            else:
                lenr = len(rightList)
                for rt in range(lenr - 1, -1, -1):
                    if rightList[rt][0] > leftList[-1][1]:
                        continue
                    else:
                        break
                # 可以合并的部分,要考虑前面的部分能否于后面的后部分进行整合
                leftList[-1][1] = max(leftList[-1][1], rightList[rt][1])
                for t in leftList:
                    ans.append(t)
                for i in range(rt + 1, len(rightList)):
                    ans.append(rightList[i])
            return ans

        return mergeList(0, length - 1)

    # 官方
    def merge1(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == '__main__':
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.merge(intervals)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
