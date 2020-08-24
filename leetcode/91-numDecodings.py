'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 01:08:13
'''

# 一条包含字母 A-Z 的消息通过以下方式进行了编码：

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。

# 示例 1:

# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:

# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * length

        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, length):
            if s[i] != '0':
                # 不和前一位进行组合
                dp[i] = dp[i - 1]
            num = 10 * int(s[i-1]) + int(s[i])

            if 10 <= num <= 26:
                #  和前一位进行组合
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[-1]


if __name__ == '__main__':

    s = "123"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.numDecodings(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
