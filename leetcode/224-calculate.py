'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 15:29:31
'''

# 实现一个基本的计算器来计算一个简单的字符串表达式的值。

# 字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

# 示例 1:

# 输入: "1 + 1"
# 输出: 2
# 示例 2:

# 输入: " 2-1 + 2 "
# 输出: 3
# 示例 3:

# 输入: "(1+(4+5+2)-3)+(6+8)"
# 输出: 23
# 说明：

# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = ["#"]
        fuhao = ["#"]
        nums = "0123456789"

        def calc():
            num2, num1 = int(stack.pop()), int(stack.pop())
            op = fuhao.pop()
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                return num1 / num2

        # 判断前面是否是整数
        pre = 0
        for sy in s:
            # print(sy, stack, fuhao)
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
                    if sy in '+-':
                        if fuhao[-1] in "+-*/":
                            # calc
                            opNum = calc()
                            stack.append(opNum)
                        fuhao.append(sy)
                    if sy in "*/":
                        if fuhao[-1] in "*/":
                            # calc
                            opNum = calc()
                            stack.append(opNum)
                        fuhao.append(sy)
            elif sy == '(':
                pre = 0
                fuhao.append(sy)
            elif sy == ')':
                pre = 0
                if fuhao[-1] != "(":
                    opNum = calc()
                    stack.append(opNum)
                fuhao.pop()  # 弹出对称的 '('

        if fuhao[-1] != '#':
            return calc()
        elif stack[-1] != '#':
            return int(stack[-1])


if __name__ == '__main__':
    s = "(1+(41+576+2)-3)+(6+8)"
    s = "(1)"
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.calculate(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
