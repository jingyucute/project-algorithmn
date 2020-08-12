'''
Description:
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-12 18:36:37
'''

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


# 示例:

# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。


import datetime


class Solution:
    def letterCombinations(self, digits: str):
        # 我靠， 我怎么写的这么复杂，虽然和官方都是递归
        d = {
            '2': "abc",
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        length = len(digits)
        sum = 0
        cur_ans = [""] * length
        result = []
        data = [
            sum, cur_ans, result
        ]

        def backTrack(index, data):
            if index >= length:
                # 到达叶子节点
                data[0] += 1
                if data[1]:
                    a = ""
                    for letter in data[1]:
                        a += letter
                    data[2].append(a)
            else:
                for sym in d[digits[index]]:
                    data[1][index] = sym
                    backTrack(index+1, data)

        backTrack(0, data)

        return data[2]

    def letterCombinations1(self, digits: str):
        # 这个是官方的解
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()
    digits = "233"

    result = solution.letterCombinations1(digits)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
