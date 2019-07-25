class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def reverse(self, head):
        prev = None
        # head不断向后遍历，将head的前一个元素作为下一个元素
        # prev不断赋值新的head
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev


class DoubleListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def reverse(self, head):
        curt = None
        # head不断向后遍历，将head的前一个元素作为下一个元素，head的后一个元素作为前一个元素
        # curt负责赋值新的head
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt
