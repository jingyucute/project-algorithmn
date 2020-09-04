'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 16:04:26
'''

# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

# 如果小数部分为循环小数，则将循环的部分括在括号内。

# 示例 1:

# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 示例 2:

# 输入: numerator = 2, denominator = 1
# 输出: "2"
# 示例 3:

# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        res = ""
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            res += '-'

        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator // denominator)

        remainer = numerator % denominator

        if remainer == 0:
            return res

        res += '.'
        xuhuan = []
        d = {

        }
        index = 0
        while remainer:
            if remainer in d:
                zindex = d[remainer]
                sx = ""
                for i in range(len(xuhuan)):
                    if i == zindex:
                        sx += '('
                    sx += str(xuhuan[i])
                sx += ')'
                return res + sx
            d[remainer] = index
            remainer *= 10
            xuhuan.append(remainer // denominator)
            remainer %= denominator

            index += 1

        sx = ''
        for i in range(len(xuhuan)):
            sx += str(xuhuan[i])

        return res + sx


if __name__ == '__main__':

    numerator = -50
    denominator = 8
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.fractionToDecimal(numerator, denominator)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
