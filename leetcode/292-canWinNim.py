'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-03 10:34:55
'''

""" 你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。

你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。

示例:

输入: 4
输出: false 
解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
     因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nim-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:
    def canWinNim(self, n: int) -> bool:

        return n % 4 != 0

        # 超出内存限制
        # if n <= 3:
        #     return True

        # dp = [False] * (n + 1)

        # dp[1], dp[2], dp[3] = True, True, True

        # for i in range(4, n+1):
        #     dp[i] = not dp[i-3] or not dp[i-2] or not dp[i-1]
        # return dp[n]


if __name__ == '__main__':
    n = 6
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.canWinNim(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
