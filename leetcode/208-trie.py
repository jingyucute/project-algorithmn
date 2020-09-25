'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-25 11:09:50
'''

# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

# 示例:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
# 说明:

# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for s in word:
            if s not in node.keys():
                node[s] = {}
            node = node[s]
        node['is_word'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for s in word:
            if s not in node.keys():
                return False
            node = node[s]

        if 'is_word' in node.keys():
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root

        for s in prefix:
            if s not in node.keys():
                return False
            node = node[s]

        return True


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    trie = Trie()

    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
    print(trie.root)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
