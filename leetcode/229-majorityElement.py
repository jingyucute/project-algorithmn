'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 17:10:19
'''

# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

# 示例 1:

# 输入: [3,2,3]
# 输出: [3]
# 示例 2:

# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/majority-element-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        import collections
        dc = collections.Counter(nums)
        length = len(nums)
        result = []
        for k, v in dc.items():
            if v > length // 3:
                result.append(k)
        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.majorityElement(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
