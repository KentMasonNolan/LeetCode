# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        l1List = self.listToString(l1)
        l2List = self.listToString(l2)

        l1List = reversed(l1List)
        l2List = reversed(l2List)

        intOutput = int(l1List) + int(l2List)
        intOutputStr = str(intOutput)
        reversedOutput = intOutputStr[::-1]

        return self.stringToList(reversedOutput)

    def listToString(self, head):
        output = ""
        current = head
        while current:
            output += str(current.val)
            current = current.next

        if len(output) > 0:
            return output
        else:
            return "0"

    def stringToList(self, input):
        head = None
        current = None

        for char in input:
            if head is None:
                head = ListNode(char)
                current = head
            else:
                current.next = ListNode(char)
                current = current.next
        return head



