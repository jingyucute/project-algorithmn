'''
Description: 
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-10 20:03:00
'''
# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

# 示例 1:

# 输入: 3
# 输出: "III"
# 示例 2:

# 输入: 4
# 输出: "IV"
# 示例 3:

# 输入: 9
# 输出: "IX"
# 示例 4:

# 输入: 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
# 示例 5:

# 输入: 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.


import datetime


class Solution:

    def intToRoman(self, num: int) -> str:
        if num < 1 or num > 3999:
            return ''
        s = str(num)
        length = len(s)
        fenwei = length - 1  # 4位数 最高千分位

        ans = ""
        for i in range(length):
            n = int(s[i])

            if 10**fenwei == 1000:
                for j in range(0, n):
                    ans += "M"
            elif 10**fenwei == 100:
                if n <= 3:
                    for j in range(n):
                        ans += 'C'
                elif n == 4:
                    ans += 'CD'
                elif n >= 5 and n <= 8:
                    ans += 'D'
                    for j in range(n - 5):
                        ans += "C"
                elif n == 9:
                    ans += "CM"
            elif 10**fenwei == 10:
                if n <= 3:
                    for j in range(n):
                        ans += 'X'
                elif n == 4:
                    ans += 'XL'
                elif n >= 5 and n <= 8:
                    ans += 'L'
                    for j in range(n - 5):
                        ans += "X"
                elif n == 9:
                    ans += "XC"
            else:
                if n <= 3:
                    for j in range(n):
                        ans += 'I'
                elif n == 4:
                    ans += 'IV'
                elif n >= 5 and n <= 8:
                    ans += 'V'
                    for j in range(n - 5):
                        ans += "I"
                elif n == 9:
                    ans += "IX"
            fenwei -= 1
        return ans

    def intToRoman1(self, num: int) -> str:
        # 这个是单位按大到小来, 类似于一个单位进制
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                  (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:
            # We don't want to continue looping if we're done.
            if num == 0:
                break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)

    def intToRoman2(self, num: int) -> str:
        # 这种方法就太猥琐了, 但是比我写的第一个方法更能说明问题
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.intToRoman2(1994)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
