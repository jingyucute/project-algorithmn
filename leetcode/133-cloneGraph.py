'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-31 11:09:52
'''
# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#  

# 测试用例格式：

# 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。

# 邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

# 给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。

#  

# 示例 1：


# 输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
# 输出：[[2,4],[1,3],[2,4],[1,3]]
# 解释：
# 图中有 4 个节点。
# 节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
# 节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
# 节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
# 节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
# 示例 2：


# 输入：adjList = [[]]
# 输出：[[]]
# 解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
# 示例 3：

# 输入：adjList = []
# 输出：[]
# 解释：这个图是空的，它不含任何节点。
# 示例 4：


# 输入：adjList = [[2],[1]]
# 输出：[[2],[1]]
#  

# 提示：

# 节点数不超过 100 。
# 每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
# 无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
# 由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
# 图是连通图，你可以从给定节点访问到所有节点。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:

    # dfs
    def cloneGraph1(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs_clone(gnode):
            if not gnode:
                return
            if gnode in visited:
                return visited[gnode]
            print(gnode.val)
            clone_node = Node(gnode.val, [])
            visited[gnode] = clone_node
            for n in gnode.neighbors:
                clone_node.neighbors.append(dfs_clone(n))
            return clone_node

        return dfs_clone(node)

    # dfs
    def cloneGraph2(self, node: 'Node') -> 'Node':
        visited = {}

        def bfs_clone(gnode):
            if not gnode:
                return
            clone_node = Node(gnode.val, [])
            visited[gnode] = clone_node
            queue = []
            queue.append(node)
            while queue:
                tmp_node = queue[0]
                del queue[0]
                for n in tmp_node.neighbors:
                    if n not in visited:
                        visited[n] = Node(n.val, [])
                        queue.append(n)
                    visited[tmp_node].neighbors.append(visited[n])
            return clone_node

        return bfs_clone(node)


if __name__ == '__main__':

    node = Node(1)
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.cloneGraph1(node)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
