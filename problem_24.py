# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        pre_head = ListNode(0)
        pre_head.next = head
        pre = pre_head
        cur = head
        while cur!=None and cur.next!=None:
            pre.next = cur.next
            cur.next = pre.next.next
            pre.next.next = cur
            pre = cur
            cur = cur.next
        return pre_head.next



if __name__ == "__main__":
    a = [1,2,4,6,7,8,9]
    list_head1 = ListNode(0)
    p1 = list_head1
    for i in a:
        new_node = ListNode(i)
        p1.next = new_node
        p1 = new_node
    result = Solution().swapPairs(list_head1.next)
    while result!=None:
        print(result.val)
        result = result.next
