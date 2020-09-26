'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 16:36:33
'''

# 实现一个基本的计算器来计算一个简单的字符串表达式的值。

# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

# 示例 1:

# 输入: "3+2*2"
# 输出: 7
# 示例 2:

# 输入: " 3/2 "
# 输出: 1
# 示例 3:

# 输入: " 3+5 / 2 "
# 输出: 5
# 说明：

# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def calculate(self, s: str) -> int:

        stack = ["#"]
        fuhao = ["#"]
        nums = "0123456789"
        pre = 0

        def calc():
            print(stack, fuhao)
            num2, num1 = int(stack.pop()), int(stack.pop())
            op = fuhao.pop()
            if op == "+":
                return str(num1 + num2)
            elif op == '-':
                return str(num1 - num2)
            elif op == '*':
                return str(num1 * num2)
            elif op == '/':
                return str(num1 // num2)

        for sy in s:
            if sy == ' ':
                pre = 0
                continue
            if sy in nums:
                if pre == 0:
                    stack.append(sy)
                    pre = 1
                else:
                    stack[-1] = stack[-1] + sy
            elif sy in "+-*/":
                pre = 0
                if fuhao[-1] == '#':
                    fuhao.append(sy)
                else:
                    if sy in "+-":
                        while fuhao[-1] in "+-*/":
                            opNum = calc()
                            stack.append(opNum)
                    else:
                        if fuhao[-1] in "*/":
                            opNum = calc()
                            stack.append(opNum)
                    fuhao.append(sy)

        while fuhao[-1] != "#":
            opNum = calc()
            stack.append(opNum)

        return int(stack[-1])


if __name__ == '__main__':
    s = "(1+(41+576+2)-3)+(6+8)"
    s = '1*2-3/4+5*6-7*8+9/10'
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.calculate(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
