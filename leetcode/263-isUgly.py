'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 09:19:08
'''

""" 编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false 
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
说明：

1 是丑数。
输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 """




import datetime
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        l = [2, 3, 5]
        while True:
            count = 0
            for n in l:
                if num % n == 0:
                    num = num // n
                    if num == 1:
                        return True
                    else:
                        break
                count += 1
            if count == 3:
                return False

        return False


if __name__ == '__main__':
    num = 1
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.isUgly(num)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
