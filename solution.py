# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math

def mergeKLists(lists):
    head = None
    current = None
    for i in reversed(range(len(lists))):
        if lists[i] == None:
            lists.pop(i)
    while len(lists) > 0:
        min = (math.inf, None)
        for i, list in enumerate(lists):
            if list.val < min[0]:
                min = (list.val, i)
        lists[min[1]] = lists[min[1]].next
        if lists[min[1]] == None:
            lists.pop(min[1])
        if head == None:
            head = ListNode(min[0])
            current = head
        else:
            current.next = ListNode(min[0])
            current = current.next
    return head