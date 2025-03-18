from typing import List, Any, Dict, Set, Generator


class StaticArray:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.array = [0] * capacity

    def set(self, index: int, value: int) -> None:
        self.array[index] = value

    def get(self, index: int) -> int:
        return self.array[index]


class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value: int) -> None:
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        del self.array[index]


    def get(self, index: int) -> int:
        return self.array[index]


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.length = 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length = 1

    def insert(self, position: int, value: int) -> None:
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.length == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node

        self.length += 1

    def delete(self, value: int) -> None:
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current.next is None:
                    self.tail = prev
                self.length -= 1
                return
            prev = current
            current = current.next
        raise ValueError

    def find(self, value: int) -> Node:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
         return self.length

    def is_empty(self) -> bool:
        return self.length == 0

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        return self.tail


class DoubleNode:
    def __init__(self, value: int, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def insert(self, position: int, value: int) -> None:
        new_node = DoubleNode(value)

        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.length == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node

        self.length += 1

    def delete(self, value: int) -> None:
        if self.head.value == value:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = self.tail = None
            self.length -= 1
            return

        current = self.head
        while current:
            if current.value == value:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.length -= 1
                return
            current = current.next

    def find(self, value: int) -> DoubleNode:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.length == 0

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")
    
    def reverse(self) -> None:
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head
    
    def get_head(self) -> DoubleNode:
        return self.head
    
    def get_tail(self) -> DoubleNode:
        return self.tail

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value: int) -> None:
        self.queue.append(value)

    def dequeue(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    def delete(self, value: int) -> None:
        if self.root is None:
            return

        current, parent = self.root, None
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif current == parent.left:
                parent.left = None
            else:
                parent.right = None

        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif current == parent.left:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif current == parent.left:
                parent.left = current.left
            else:
                parent.right = current.left

        else:
            successor = current.right
            successor_parent = current
            while successor.left:
                successor_parent = successor
                successor = successor.left

            current.value = successor.value

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def search(self, value: int) -> TreeNode:
        current = self.root
        while current:
            if current.value == value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self) -> List[int]:
        result = []
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result
    
    def size(self) -> int:
        count = 0
        current = self.root
        stack = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            count += 1
            current = current.right
        return count

    def is_empty(self) -> bool:
        return self.root is None

    def height(self) -> int:
        if self.root is None:
            return 0

        height = 0
        queue = [self.root]
        while queue:
            level_size = len(queue)
            height += 1
            for _ in range(level_size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return height

    def preorder_traversal(self) -> List[int]:
        result = []
        if self.root is None:
            return result
        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def postorder_traversal(self) -> List[int]:
        result = []
        if self.root is None:
            return result
        stack = [(self.root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.value)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return result

    def level_order_traversal(self) -> List[int]:
        result = []
        if self.root is None:
            return result
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def minimum(self) -> TreeNode:
        current = self.root
        while current and current.left:
            current = current.left
        return current

    def maximum(self) -> TreeNode:
        current = self.root
        while current and current.right:
            current = current.right
        return current
    
    def is_valid_bst(self) -> bool:
        if not self.root:
            return True
        stack = []
        current = self.root
        prev_value = float('-inf')
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.value <= prev_value:
                return False
            prev_value = current.value
            current = current.right
        return True

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

def shell_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst
def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
