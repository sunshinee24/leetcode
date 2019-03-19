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
    def mergeTwoLists(self, l1, l2):
        merged_head = ListNode(0)
        p = merged_head

        while l1 != None or l2 != None:
            if l1!=None and l2!=None:
                if l1.val <= l2.val:
                    p.next = l1
                    p = p.next
                    l1 = l1.next
                else:
                    p.next = l2
                    p = p.next
                    l2 = l2.next
            elif l1 == None:
                p.next = l2
                break
            else:
                p.next = l1
                break
        return merged_head.next

if __name__ == "__main__":
    a = [1,2,4,6,7,8]
    b = []
    list_head1 = ListNode(0)
    p1 = list_head1
    list_head2 = ListNode(0)
    p2 = list_head2
    for i in a:
        new_node = ListNode(i)
        p1.next = new_node
        p1 = new_node
    for i in b:
        new_node = ListNode(i)
        p2.next = new_node
        p2 = new_node

    result = Solution().mergeTwoLists(list_head1.next, list_head2.next)
    while result!=None:
        print(result.val)
        result = result.next
