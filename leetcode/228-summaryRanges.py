'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 17:00:12
'''

# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

# 示例 1:

# 输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
# 示例 2:

# 输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/summary-ranges
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        length = len(nums)
        result = []
        start, end = 0, 0
        for end in range(length):
            if end + 1 < length and nums[end + 1] == nums[end] + 1:
                continue
            if start == end:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start])+"->"+str(nums[end]))
            start = end + 1

        return result


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 6, 8, 9]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.summaryRanges(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
