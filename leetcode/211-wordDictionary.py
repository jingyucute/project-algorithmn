'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-25 13:18:40
'''

# 如果数据结构中有任何与word匹配的字符串，则bool search（word）返回true，否则返回false。 单词可能包含点“。” 点可以与任何字母匹配的地方。

# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

# 实现词典类 WordDictionary ：

# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
#  

# 示例：

# 输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]

# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#  

# 提示：

# 1 <= word.length <= 500
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最调用多 50000 次 addWord 和 search

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        t = self.d
        for s in word:
            if s not in t:
                t[s] = {}
            t = t[s]
        t['end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cut = False

        def f(td, s):  # 深搜，参数为：当前子字典，当前串
            nonlocal cut
            if cut:  # 剪枝
                return True
            t = td
            for i, c in enumerate(s):
                if c == '.':
                    # 深搜扩展
                    return any(f(t[j], s[i + 1:]) for j in t if j != 'end')
                if c not in t:
                    return False
                t = t[c]
            cut = 'end' in t
            return cut
        return f(self.d, word)


if __name__ == '__main__':
    solution = WordDictionary()
    start_time = datetime.datetime.now()

    end_time = datetime.datetime.now()
    print(end_time-start_time)
