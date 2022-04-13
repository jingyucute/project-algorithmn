'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 00:45:30
'''


# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 示例 1:

# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:

# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：

# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def addStrings(num1: str, num2: str) -> str:
            i, j = len(num1) - 1, len(num2) - 1
            add = 0
            ans = []
            while i >= 0 or j >= 0 or add != 0:
                x = int(num1[i]) if i >= 0 else 0
                y = int(num2[j]) if j >= 0 else 0
                result = x + y + add
                ans.append(str(result % 10))
                add = result // 10
                i -= 1
                j -= 1

            return ''.join(ans[::-1])
        if num1 == '0' or num2 == '0':
            return '0'

        len1, len2 = len(num1), len(num2)
        ans = '0'
        for i in range(len2 - 1, -1, -1):
            add = 0
            y = int(num2[i])
            curr = ['0'] * (len2 - i - 1)

            for j in range(len1 - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = ''.join(curr[::-1])

            ans = addStrings(ans, curr)

        return ans

    def multiply2(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        ansArr = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            x = int(num1[i])
            for j in range(len2 -1, -1, -1):
                y = int(num2[j])
                ansArr[i + j + 1] += x * y
        for i in range(len1 + len2 -1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] = ansArr[i] % 10
        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    num1 = "123"
    num2 = "456"
    result = solution.multiply2(num1, num2)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
