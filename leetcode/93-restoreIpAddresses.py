'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 09:12:42
'''
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

#  

# 示例 1：

# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：

# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：

# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 示例 4：

# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 示例 5：

# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  

# 提示：

# 0 <= s.length <= 3000
# s 仅由数字组成


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:

    # 暴力算法， 直接分成四个部分
    def restoreIpAddresses(self, s: str):
        result = []
        length = len(s)
        if length < 4 or length > 12:
            return []

        for i in range(1, min(4, length - 2)):
            # 第一个点的位置,
            for j in range(i + 1, min(i + 4, length - 1)):
                # 第二个点的位置
                for k in range(j + 1, min(j+4, length)):
                    # 第三个点的位置
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if (a[0] == '0' and a != '0') or (b[0] == '0' and b != '0') or (c[0] == '0' and c != '0') or (d[0] == '0' and d != '0'):
                        continue
                    if int(a) <= 255 and int(b) <= 255 and int(c) <= 255 and int(d) <= 255:
                        result.append(a+"."+b+"." + c+"."+d)

        return result

    # 递归回溯
    def restoreIpAddresses1(self, s: str):
        result = []
        length = len(s)
        if length < 4 or length > 12:
            return result

        def backTrack(index=0, path=[]):
            if index >= length:
                if len(path) == 4:
                    ip = ""
                    for d in path:
                        ip += d + '.'
                    result.append(ip[:-1])
            else:
                if len(path) > 4:
                    return
                if not path:
                    path.append(s[index])
                    backTrack(index+1, path)
                    path.pop()
                else:
                    if path[-1][0] == "0":
                        path.append(s[index])
                        backTrack(index+1, path)
                        path.pop()
                    else:
                        if int(path[-1] + s[index]) > 255:
                            path.append(s[index])
                            backTrack(index+1, path)
                            path.pop()
                        else:
                            path.append(s[index])
                            backTrack(index+1, path)
                            path.pop()

                            temp = path[-1]
                            path[-1] += s[index]
                            backTrack(index+1, path)
                            path[-1] = temp

        backTrack()

        return result

    # 官方答案 递归
    def restoreIpAddresses2(self, s: str):
        SEG_COUNT = 4
        ans = list()
        segments = [0] * SEG_COUNT

        def dfs(segId: int, segStart: int):
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
            if segId == SEG_COUNT:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return

            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
            if segStart == len(s):
                return

            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
            if s[segStart] == "0":
                segments[segId] = 0
                dfs(segId + 1, segStart + 1)

            # 一般情况，枚举每一种可能性并递归
            addr = 0
            for segEnd in range(segStart, len(s)):
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    s = "010010"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.restoreIpAddresses2(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
