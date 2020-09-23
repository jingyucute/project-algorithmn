'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-23 17:08:07
'''

# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

#  

# 示例 1:

# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 示例 2:

# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
#  

# 提示：

# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 主要是看有向图是否有还
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        import collections
        visited = [0] * numCourses
        edges = collections.defaultdict(list)

        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid


if __name__ == '__main__':

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
