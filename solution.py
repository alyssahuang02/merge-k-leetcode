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

def createLinkedLists(lists):
    res = []
    for list in lists:
        head = ListNode(list[0])
        cur = head
        for val in list[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        res.append(head)
    return res

lists = createLinkedLists([[1,4,5],[1,3,4],[2,6]])
# lists = createLinkedLists([[]])
result = mergeKLists(lists)