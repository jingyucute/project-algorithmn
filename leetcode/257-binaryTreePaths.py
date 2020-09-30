'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-01 01:27:40
'''

""" 给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        result = []
        # if not root:
        #     return result

        # 递归回溯
        def dfs(node=root, path=[]):
            if node:
                path.append(node.val)
                if not node.left and not node.right:
                    # 叶子结点
                    result.append("->".join('%s' % num for num in path))
                if node.left:
                    dfs(node.left, path)
                    path.pop()
                if node.right:
                    dfs(node.right, path)
                    path.pop()

        dfs(root, [])

        # print(result)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(5)
    root.left = node2
    root.right = node3
    node2.left = node4

    t = ["a", "b", 'C']

    solution = Solution()
    # root = None
    start_time = datetime.datetime.now()
    result = solution.binaryTreePaths(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
