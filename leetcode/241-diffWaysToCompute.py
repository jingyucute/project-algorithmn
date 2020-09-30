'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 00:58:14
'''
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

# 示例 1:

# 输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# 示例 2:

# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import datetime


class Solution:
    def diffWaysToCompute(self, input: str):
        if input.isdigit():
            return [int(input)]
        res = []
        for i, ch in enumerate(input):
            if ch in ["+", "-", "*"]:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res


if __name__ == '__main__':
    input = "2*3-4*5"
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.diffWaysToCompute(input)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
