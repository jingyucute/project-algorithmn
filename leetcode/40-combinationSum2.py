'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-19 18:12:39
'''


# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：

# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:

# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:

# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime

class Solution:
    def combinationSum2(self, candidates, target: int):
        if not candidates:
            return []
        candidates.sort()
        print(candidates)
        result = []

        # 回溯法
        def dfs(preIndex, cur_list, cur_sum):
            if cur_sum == target:
                if cur_list not in result:
                    result.append(cur_list.copy())
            else:
                for index in range(len(candidates)):
                    if preIndex >= index and cur_list:
                        continue
                    else:
                        print(preIndex, index)
                        if target - cur_sum < candidates[index]:
                            break
                        # 都是正数就好说了
                        temp_pre = preIndex
                        cur_list.append(candidates[index])
                        # print(cur_list)
                        preIndex = index
                        cur_sum += candidates[index]
                        dfs(preIndex, cur_list, cur_sum)
                        cur_sum -= candidates[index]
                        cur_list.pop()
                        preIndex = temp_pre

        dfs(0, [], 0)
        return result

    
    def combinationSum2_2(self, candidates, target: int):
        if not candidates:
            return []
        import collections
        freq = sorted(collections.Counter(candidates).items()) 
        def backTrack(index = 0, cur_sum = 0, cur_list = []):
            if cur_sum == target:
                # print(cur_list)
                ans.append(cur_list[:])
                return
            elif index >= len(freq) or cur_sum + freq[index][0] > target:
                return
            else:
                backTrack(index + 1, cur_sum, cur_list)
                # 判断 freq[index] 的数， 需要几个
                most = min( (target - cur_sum) // freq[index][0], freq[index][1])
                for i in range(1, most + 1):
                    cur_list.append(freq[index][0])
                    backTrack(index+1, cur_sum + freq[index][0] * i, cur_list)
                for i in range(most):
                    cur_list.pop()
                # 不能使用下面的 语句重新赋值
                # 使用切片修改， 重新使用一个新的变量， 也就是内存中的地址变了， 重新修改后的值，不会返回给后面用到的
                # cur_list = cur_list[:-most]
        ans = []
        backTrack()
        return ans 

if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = solution.combinationSum2_2(candidates, target)
    print(result)

    end_time = datetime.datetime.now()

    test_list = [1,2,3,4,5,6,7]
    print(id(test_list))
    test_list = test_list[:-3]
    print(id(test_list))
    print(end_time-start_time)
