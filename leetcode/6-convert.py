
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

# 请你实现这个将字符串进行指定行数变换的函数：

# string convert(string s, int numRows);
# 示例 1:

# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:

# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:

# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G

import datetime


class Solution:

    def convert(self, s: str, numRows: int) -> str:
        length = len(s)

        list = [[''for j in range(length)] for i in range(numRows)]

        # start = 0
        direct = 1  # 1 往下, 0 斜上
        col = 0
        row = 0

        if numRows == 0:
            return ''

        if numRows == 1:
            return s

        for i in range(length):
            # print(i, "--", row, '--', col, '--', s[i])
            list[row][col] = s[i]
            if row == 0:
                direct = 1
            if row == numRows - 1:
                direct = 0

            if direct == 0:
                row -= 1
                col += 1
            else:
                row += 1

        result = ''
        for i in range(numRows):
            for j in range(length):
                if list[i][j]:
                    result += list[i][j]

        return result

    # 还是上面的思路， 进行修改 也就是将辅助空间改小， 整合行结果时运算减少
    def convert1(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        length = len(s)
        lh = min(numRows, length)
        list = [""] * lh
        row = 0
        direct = 1
        for i in range(length):
            list[row] += s[i]
            if row == 0:
                direct = 1
            if row == lh - 1:
                direct = 0

            if direct == 0:
                row -= 1
            else:
                row += 1

        result = ''.join(list)
        return result


if __name__ == '__main__':
    str = 'LEETCODEISHIRING'
    # str = 'A'
    start_time = datetime.datetime.now()
    s = Solution()
    # print(s.convert(str, 1))
    result = s.convert1(str, 1)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
