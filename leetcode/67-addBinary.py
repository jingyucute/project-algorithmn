'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 15:55:58
'''
# 给你两个二进制字符串，返回它们的和（用二进制表示）。

# 输入为 非空 字符串且只包含数字 1 和 0。

#  

# 示例 1:

# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:

# 输入: a = "1010", b = "1011"
# 输出: "10101"
#  

# 提示：

# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        lena, lenb = len(a), len(b)
        if lena < lenb:
            a, b, lena, lenb = b, a, lenb, lena
        a, b = list(a), list(b)
        add = 0
        for i in range(lenb):
            cur_a, cur_b = int(a[lena - i - 1]), int(b[lenb - i - 1])
            total = (cur_a + cur_b + add) % 2
            a[lena - i - 1] = str(total)
            add = (cur_a + cur_b + add) // 2

        for i in range(lena - lenb - 1, -1, -1):
            cur_a = int(a[i])
            a[i] = str((cur_a + add) % 2)
            add = (cur_a + add) // 2

        if add:
            a = [str(add)] + a
        return ''.join(a)

    # 官方
    def addBinary1(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


if __name__ == '__main__':
    a = "11010"
    b = "1011"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.addBinary(a, b)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
