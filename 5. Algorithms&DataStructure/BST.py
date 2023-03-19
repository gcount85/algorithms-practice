import sys

from __future__ import annotations
from typing import Any, Type

class Node:
    '''이진 검색 트리의 노드'''
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        '''생성자(constructor)'''
        self.key = key      # 키
        self.value = value  # 값
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
                return p.value

    def add(self, key: Any, value: Any, index: int) -> bool:
        '''키가 key이고 값이 value인 노드를 삽입'''


        def add_left_node(node: Node, key: Any, value: Any) -> None:
            '''node를 루트로 하는 서브트리의 왼쪽 자식에 키가 key이고 값이 value인 노드를 삽입'''
            if node.left is None:
                node.left = Node(key, value, None, None)
            else:
                add_left_node(node.left, key, value)

        def add_right_node(node: Node, key: Any, value: Any) -> None:
            '''node를 루트로 하는 서브트리에 오른쪽 자식에 키가 key이고 값이 value인 노드를 삽입'''
            if node.right is None:
                node.right = Node(key, value, None, None)
            else:
                add_right_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        # elif index == 1:
        #     return add_left_node(self.root, key, value)
        # elif index == 2:
        #     return add_right_node(self.root, key, value)

# 파이썬 rotateRight

def rotate_right(self, z):   # self라는 트리에 z를 기준으로 로테이션
	if not z: return
	x = z.left
	if x == None: return   # z자리에 올라올 x가 없다
	b = x.right
	x.parent = z.parent
	if z.parent:   # Z가 루트가 아니면
		if z.parent.left == z:
			z.parent.left = x
		else: 
			z.parent.right = x
	x.right = z
	z.parent = x
	z.left = b
	if b: b.parent = z
	if self.root == z:
		self.root = x
