
from __future__ import annotations
from typing import Any, Type
import sys

class Node:
    '''이진 검색 트리의 노드'''
    def __init__(self, key: Any, left: Node = None, right: Node = None):
        '''생성자(constructor)'''
        self.key = key      # 키
        self.left = left    # 왼쪽 포인터
        self.right = right  # 오른쪽 포인터

class BinaryTree:
    '''이진 트리'''

    def __init__(self):
        '''초기화'''
        self.root = None
    
    def search(self, key: Any) -> Any:
        '''키가 key인 노드를 검색 '''
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.key

    def add(self, key: Any, left: Node, right: Node) -> bool:
        '''키가 key인 노드를 삽입'''

        def add_left_node(node: Node, key: Any) -> None:
            '''node를 루트로 하는 서브트리의 왼쪽 자식에 키가 key인 노드 삽입'''
            if node.left is None:
                node.left = Node(key, None, None)
            else:
                add_left_node(node.left, key)

        def add_right_node(node: Node, key: Any) -> None:
            '''node를 루트로 하는 서브트리에 오른쪽 자식에 키가 key인 노드 삽입'''
            if node.right is None:
                node.right = Node(key, None, None)
            else:
                add_right_node(node.right, key)

        if self.root is None:
            self.root = Node(key, None, None)
            return True
        elif left:
            return add_left_node(self.root, key)
        elif right:
            return add_right_node(self.root, key)



N = int(sys.stdin.readline())
tree = BinaryTree()
for i in range(N):
    node = sys.stdin.readline().split()  # [A, B, C]
    key = node[0]
    if node[1] != '.':
        left = Node(node[1])
    else:
        left = None
    if node[2] != '.':
        right = Node(node[2])
    else:
        right = None
    if i == 0:
        tree.root = Node(key, left, right)
    else:
        tree.add(Node(key), left, right)
    


