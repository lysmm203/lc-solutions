# Optimal in terms of spacetime. Runetime is still the same though

# Runtime: O(N)
# Spacetime: O(1)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr, nxt = root, root.left if root else None

        while curr and curr.left:
            curr.left.next = curr.right

            if curr.next:
                curr.right.next = curr.next.left

            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left

        return root


