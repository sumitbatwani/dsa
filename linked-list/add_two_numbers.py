"""
Add Two Numbers (linked list digits, least-significant digit first)

This module implements `add_two_numbers(l1, l2)` which adds two numbers
represented as linked lists of digits (LeetCode #2 style). It also provides
helpers to build/inspect lists and a runnable example.

How to run:

	python3 linked-list/add_two_numbers.py

Example output:

	l1 = [2,4,3], l2 = [5,6,4] -> result = [7,0,8]

"""

from __future__ import annotations
from typing import Optional, List


class ListNode:
	def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
		self.val = val
		self.next = next

	def __repr__(self) -> str:
		return f"ListNode({self.val})"


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
	carry = 0
	dummy = ListNode(0)
	cur = dummy

	p, q = l1, l2
	while p is not None or q is not None or carry:
		x = p.val if p is not None else 0
		y = q.val if q is not None else 0
		total = x + y + carry
		carry = total // 10
		cur.next = ListNode(total % 10)
		cur = cur.next
		if p is not None:
			p = p.next
		if q is not None:
			q = q.next

	return dummy.next


def from_list(values: List[int]) -> Optional[ListNode]:
	if not values:
		return None
	dummy = ListNode(0)
	cur = dummy
	for v in values:
		cur.next = ListNode(v)
		cur = cur.next
	return dummy.next


def to_list(node: Optional[ListNode]) -> List[int]:
	out: List[int] = []
	cur = node
	while cur is not None:
		out.append(cur.val)
		cur = cur.next
	return out


if __name__ == "__main__":
	# Example from LeetCode: (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8)
	l1 = from_list([2, 4, 3])
	l2 = from_list([5, 6, 4])
	res = add_two_numbers(l1, l2)
	print("l1 =", to_list(l1), ", l2 =", to_list(l2), "-> result =", to_list(res))
