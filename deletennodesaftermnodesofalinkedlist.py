class Solution:
    def linkdelete(self, head, n, m):
        # Code here
        current = head
        while current:
            for _ in range(m-1):
                if not current:
                    return head
                else:
                    current = current.next
            delete = current.next if current else None
            for _ in range(n):
                if not delete:
                    break
                else:
                    delete = delete.next
            if current:
                current.next = delete
                current = delete
        return head
