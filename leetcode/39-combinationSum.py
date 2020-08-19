'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-19 17:39:18
'''

# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：

# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1：

# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2：

# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#  

# 提示：

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def combinationSum(self, candidates, target: int):
        if not candidates:
            return []
        candidates.sort()
        result = []

        # 回溯法
        def dfs(preNum, cur_list, cur_sum):
            if cur_sum == target:
                result.append(cur_list.copy())
            else:
                for num in candidates:
                    if num < preNum:
                        continue
                    else:
                        if target - cur_sum < num:
                            break
                        # 都是正数就好说了
                        temp_pre = preNum
                        cur_list.append(num)
                        # print(cur_list)
                        preNum = num
                        cur_sum += num
                        dfs(num, cur_list, cur_sum)
                        cur_sum -= num
                        cur_list.pop()
                        preNum = temp_pre

        dfs(candidates[0], [], 0)
        return result


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()

    candidates = [2, 3, 5]
    target = 8
    result = solution.combinationSum(candidates, target)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
