# Brute force approach using BFS. Brute force only in that it uses O(N) space
# Runtime: O(N)
# Spacetime: O(N)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Initialize a queue
        # If root doesn't exist, return queue
        # Append the root node and the None value into the queue
        # Initialize the while loop for while the queue isn't empty
        # While the first element in the queue isn't None:
        # Pop the first element and set its next into the first element in the queue
        # Append its children into the queue
        # If the length of queue is 1: break
        # Else, pop and append None into the end of the array

        # return root

        if not root: return root

        queue = [root, None]
        print(queue)

        while len(queue) > 1:
            while queue[0] != None:
                popped = queue.pop(0)
                popped.next = queue[0]
                if popped.left != None:
                    queue.append(popped.left)
                    queue.append(popped.right)

            queue.pop(0)
            queue.append(None)

        return root



