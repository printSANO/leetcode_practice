"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        x = root
        result = []
        def recurs(x):
            if x:
                result.append(x.val)
                for i in x.children:
                    recurs(i)
        recurs(x)
        return result