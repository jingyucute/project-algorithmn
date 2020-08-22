'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 09:53:17
'''

# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。

# 说明：

# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:

# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:

# 输入: n = 4, k = 9
# 输出: "2314"

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    # 回溯法， 超时
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]

        def backTrack(first, path, used, ans):
            if first >= n:
                ss = ""
                for t in path:
                    ss += str(t)
                ans.append(ss)
            else:
                if len(ans) == k:
                    return
                for i in range(n):
                    if not used[i]:
                        path.append(nums[i])
                        used[i] = True
                        backTrack(first+1, path, used, ans)
                        path.pop()
                        used[i] = False
        used = [False] * n
        ans = []
        backTrack(0, [], used, ans)
        return ans[-1]

    # 官方答案
    # 不是特明白
    # 我理解的: 比如 123456 ,
    # 1、 以每个数字开头 都有 5! 种方式 , 这就是为什么需要算阶乘
    # 2、 由于是按字典排序, nums[(k-1)//5!] 就是最高位
    # 3、 选了第一个, 就要判断选择下一个(更新k), k = k - idx * 5!
    def getPermutation1(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            factorials.append(factorials[i - 1] * i)
            nums.append(str(i + 1))
        k -= 1
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            output.append(nums[idx])
            del nums[idx]

        return ''.join(output)


if __name__ == '__main__':
    n = 4
    k = 5
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.getPermutation1(n, k)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
