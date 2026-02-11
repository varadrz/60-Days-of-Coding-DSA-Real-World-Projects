class Node:
    def __init__(self, key: int, value: any):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap: key -> Node

        # Dummy head and tail to avoid edge-case checks
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # -----------------------------
    # Internal Helper Functions
    # -----------------------------

    def _remove(self, node: Node):
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        """Add node right after head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    # -----------------------------
    # Public API
    # -----------------------------

    def get(self, key: int):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move accessed node to front
        self._remove(node)
        self._add_to_front(node)

        return node.value

    def put(self, key: int, value: any):
        if key in self.cache:
            # Update value
            node = self.cache[key]
            node.value = value

            # Move to front
            self._remove(node)
            self._add_to_front(node)

        else:
            if len(self.cache) >= self.capacity:
                # Remove LRU node (node before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            # Insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def display(self):
        """Utility function to visualize cache order."""
        current = self.head.next
        result = []
        while current != self.tail:
            result.append(f"{current.key}:{current.value}")
            current = current.next
        return " <-> ".join(result)
