'''
Description:
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-11 07:11:30
'''
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。


import datetime


class Solution:
    # 逐行比较
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""

        min_length = len(strs[0])
        min_str = strs[0]
        min_n = 0
        for n, s in enumerate(strs):
            if len(s) < min_length:
                min_length = len(s)
                min_n = n
                min_str = s
        max_pre = ""
        for j in range(len(min_str)):
            flag = True
            for n, s in enumerate(strs):
                if n == min_n:
                    continue
                if s[0:j+1] != min_str[0:j+1]:
                    flag = False
            if flag:
                max_pre = min_str[0:j+1]
        return max_pre

    #   分治法 还是蛮好理解的
    def longestCommonPrefix1(self, strs) -> str:
        def lcp(start, end):
            # print("--", start, '--', end, '--')
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            # print("--", start, '--', mid, '--', end, '--')
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            # print(lcpLeft, lcpRight)
            minLen = min(len(lcpLeft), len(lcpRight))
            for i in range(minLen):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            # 两个比较， 短的是长的子串
            return lcpLeft[:minLen]

        if len(strs) == 0:
            return ""
        return lcp(0, len(strs) - 1)

    # 二分法
    def longestCommonPrefix2(self, strs) -> str:
        def isCommonPrefix(length):
            str0, count = strs[0][:(length + 1)], len(strs)
            # if count == 1:
            #     return str0
            return all(strs[j][:(length + 1)] == str0 for j in range(1, count)) 

        if not strs:
            return ""
        minLength = min(len(s) for s in strs)
        low, high = 0, minLength - 1
        while low <= high:
            mid = (high + low) // 2
            if isCommonPrefix(mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:low]


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    l = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix2(l)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
