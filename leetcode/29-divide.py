'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-15 13:50:25
'''
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

#  

# 示例 1:

# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 示例 2:

# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
#  

# 提示：

# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime

# 先粘过来， 这个没太看懂


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # print(dividend // divisor,  2**31-1)
        flag = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            tmp_divisor = divisor
            count = 1
            while tmp_divisor <= dividend:
                dividend -= tmp_divisor
                result += count
                count += count
                tmp_divisor += tmp_divisor

        if flag == False:
            result = -result
            if result < -2**31:
                result = 2**31-1
        else:
            if result > 2**31-1:
                result = 2**31-1

        return result


if __name__ == '__main__':
    dividend = -2147483648
    divisor = -2
    start_time = datetime.datetime.now()
    solution = Solution()
    r = solution.divide(dividend, divisor)
    print(r)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
