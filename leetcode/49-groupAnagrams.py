'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 17:19:54
'''

# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

# 示例:

# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：

# 所有输入均为小写字母。
# 不考虑答案输出的顺序。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def groupAnagrams(self, strs):
        #  官方思路, 将每个str 做乘一个 key -> value 的映射， key 为str中字母的排序元组
        import collections
        dict = collections.defaultdict(list)
        result = []
        for s in strs:
            # print(sorted(s), tuple(s), sorted(tuple(s)), tuple(sorted(s)))
            dict[tuple(sorted(s))].append(s)

        result = list(dict.values())

        return result


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.groupAnagrams(strs)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
