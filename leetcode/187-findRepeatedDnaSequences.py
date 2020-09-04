'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 20:04:52
'''

# 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

# 编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

#  

# 示例：

# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        L, length = 10, len(s)
        se = set()
        result = set()
        for i in range(length - L + 1):
            tmp = s[i: i + L]
            if tmp in se:
                result.add(tmp)
            se.add(tmp)
        return list(result)


if __name__ == '__main__':

    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.findRepeatedDnaSequences(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
