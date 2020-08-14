'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-14 11:46:52
'''

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

#  

# 示例：

# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    # 我写的递归， 但时间上没通过
    def generateParenthesis(self, n: int):
        list = []
        current = ""

        def backTrack(index, current):
            if index > n:
                if current not in list:
                    list.append(current)
                else:
                    return
            else:
                # 当前的 括号有多少中选择
                length = len(current)
                for i in range(length):
                    # 第 i 组括号怎样加入原有的内容中
                    temp = current
                    current = current[0:i] + "()" + current[i:]
                    backTrack(index+1, current)
                    current = temp
                temp = current
                current = current + "()"
                backTrack(index+1, current)
                current = temp

        if n > 0:
            backTrack(1, current)

        return list

    # 官方答案， 同样是递归， 人家效率高， 好好看看
    def generateParenthesis1(self, n: int):
        ans = []

        def backtrack(S, left, right):
            # 这里考虑的是单个括号加入， 而我考虑的是一对括号的加入,
            # 这样的话， 会导致我的解在前面有很多的重复，增大了解空间
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.generateParenthesis1(10)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
