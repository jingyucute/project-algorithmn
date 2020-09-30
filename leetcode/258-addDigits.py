'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 01:39:29
'''
""" 
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2 
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:
    def addDigits(self, num: int) -> int:

        # O(1)
        # if num == 0:
        #     return 0
        # return (num - 1) % 9 + 1

        ans = 0

        def getSum(n):
            temp = 0
            while n:
                temp += n % 10
                n = n // 10
            return temp

        ans = getSum(num)
        while ans >= 10:
            ans = getSum(ans)

        return ans


if __name__ == '__main__':
    num = 38
    solution = Solution()
    # root = None
    start_time = datetime.datetime.now()
    result = solution.addDigits(num)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
