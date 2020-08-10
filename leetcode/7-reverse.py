'''
Description: 
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-10 12:44:36
'''

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:

# 输入: 123
# 输出: 321
#  示例 2:

# 输入: -123
# 输出: -321
# 示例 3:

# 输入: 120
# 输出: 21
# 注意:

# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

import datetime


class Solution:

    def reverse(self, x: int) -> int:
        # 思路很简单， 就是先转化成不带符号的字符串, 然后反转字符串， 然后加符号， 判断是否益处
        # 我感觉这个方法还是有点问题， 比如数太大， 益出范围，我感觉这样写不太妥， 后面再写吧
        s = str(abs(x))
        s = s[::-1]
        if s[0] == '0' and len(s) > 1:
            s = s[1:]
        if x < 0:
            s = '-' + s
        n = int(s)
        if n > 2**31 or n < -2**31:
            n = 0
        return n


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    s = Solution()
    result = s.reverse(0)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
