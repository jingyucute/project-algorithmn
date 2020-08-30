'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-31 01:20:58
'''

# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

# 返回符合要求的最少分割次数。

# 示例:

# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return 0
        check_palindrome = [[False] * length for _ in range(length)]

        for right in range(length):
            for left in range(0, right + 1):
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left+1][right - 1]):
                    check_palindrome[left][right] = True
        # print(check_palindrome)

        dp = [i for i in range(length)]

        for i in range(1, length):
            if check_palindrome[0][i]:
                # 0 -> i 是回文
                dp[i] = 0
                continue
            # 0 -> i 不是回文
            for j in range(0, i):
                if check_palindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[length - 1]


if __name__ == '__main__':

    s = "abbab"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.minCut(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
