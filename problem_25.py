# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        if head == None:
           return None
        pre_head = ListNode(0)
        pre_head.next = head
        start = pre_head
        while start.next != None:
            i = 0
            end = start
            while i<k-1:
                end = end.next
                if end.next == None:
                    return pre_head.next
                i = i+1
            [_start, _end] = self.reverse(start.next, end.next)
            start.next = _start
            start = _end
        return pre_head.next

    def reverse(self,start,end):
        nhead = ListNode(0)
        nhead.next = start
        while nhead.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = nhead.next
            nhead.next = tmp
        return [end,start]

if __name__ == "__main__":
    a = [1,2,4,6,7,8]
    k = 4
    list_head1 = ListNode(0)
    p1 = list_head1
    for i in a:
        new_node = ListNode(i)
        p1.next = new_node
        p1 = new_node
    #result,end = Solution().reverse(list_head1.next, p1)
    result = Solution().reverseKGroup(list_head1.next, k)
    while result!=None:
        print(result.val)
        result = result.next

# p = start
# while p != end:
#     print(p.val)
#     p = p.next
# import pdb;pdb.set_trace()

