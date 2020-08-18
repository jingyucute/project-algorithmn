'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-18 12:50:54
'''

# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

# 示例 1:

# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:

# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime

# 先粘过来， 这个没太看懂


class Solution:
    # 暴力算法
    def longestValidParentheses(self, s: str) -> int:
        def isValid(ss, start, end):
            stack = []
            for i in range(start, end+1):
                if ss[i] == ")" and stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ss[i])
            if stack:
                return False
            return True
        length = len(s)
        guimo = length
        if length % 2 != 0:
            guimo = length - 1
        max_length = 0
        while guimo > 0:
            for i in range(0, length - guimo + 1):
                start = i
                end = start + guimo - 1
                # print(start, end, s[start:end+1])

                # 判断 start -> end 是否为有效字符串
                if isValid(s, start, end):
                    return guimo

            guimo -= 2

        return max_length

    # 利用栈的思想，由于这个不是简单的判断括号是否匹配，故应记录对应字符下标
    def longestValidParentheses1(self, s: str) -> int:

        if not s:
            return 0

        stack = []
        for i, ch in enumerate(s):
            if ch == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)

        stack.append(len(s))
        max_length = stack[0]
        for i in range(1, len(stack)):
            max_length = max(max_length, stack[i] - stack[i-1] - 1)

        return max_length

    # 动态规划
    def longestValidParentheses2(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        # s[i-dp[i-1] - 1] 是 与 s[i] 应该对应的 位置
        # dp[i-dp[i-1] - 2] 表示 前面的有多少有效括号
        for i in range(n):
            if s[i] == ')' and i-dp[i-1] - 1 >= 0 and s[i-dp[i-1] - 1] == '(':
                dp[i] = 2 + dp[i - 1] + dp[i-dp[i-1] - 2]

        return max(dp)


if __name__ == '__main__':

    s = ")()()()))"
    start_time = datetime.datetime.now()
    solution = Solution()

    result = solution.longestValidParentheses2(s)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
