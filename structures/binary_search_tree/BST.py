class Node:
    def __init__(self, key, value, left=None, right=None):
        super().__init__()
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return '[' + str(self.key) + ';' + str(self.value) + ']'


class BinarySearchTree:
    def __init__(self, root_node):
        super().__init__()
        self.root_node = root_node

    def infix_traverse(self, consumer):
        BinarySearchTree.__infix_traverse_impl(self.root_node, consumer)

    @staticmethod
    def __infix_traverse_impl(root_node, consumer):
        if root_node is None:
            return
        BinarySearchTree.__infix_traverse_impl(root_node.left, consumer)
        consumer(root_node)
        BinarySearchTree.__infix_traverse_impl(root_node.right, consumer)

    def find(self, key):
        return BinarySearchTree.__find_internal(self.root_node, key)

    @staticmethod
    def __find_internal(root_node, key):
        if root_node is None:
            return None

        if key == root_node.key:
            return root_node

        if key < root_node.key:
            return None if root_node.left is None \
                else BinarySearchTree.__find_internal(root_node.left, key)
        else:
            return None if root_node.right is None \
                else BinarySearchTree.__find_internal(root_node.right, key)

    def insert(self, key, value):
        if key is None:
            raise ValueError('key cannot be None')
        if self.root_node is None:
            self.root_node = Node(key, value)
        else:
            BinarySearchTree.__insert_internal(self.root_node, key, value)

    @staticmethod
    def __insert_internal(root_node, key, value):
        if key == root_node.key:
            root_node.value = value
        elif key < root_node.key:
            if root_node.left is None:
                root_node.left = Node(key, value)
            else:
                BinarySearchTree.__insert_internal(root_node.left, key, value)
        elif key > root_node.key:
            if root_node.right is None:
                root_node.right = Node(key, value)
            else:
                BinarySearchTree.__insert_internal(root_node.right, key, value)

    def remove(self, key):
        pass

    def __str__(self):
        nodes = []
        self.infix_traverse(lambda x: nodes.append(str(x)))
        return ' '.join(nodes)


if __name__ == "__main__":
    left = Node(5, "b")
    right = Node(20, "c")
    root = Node(10, "a", left, right)

    tree = BinarySearchTree(root)
    print(tree.find(20))
    print(tree.find(21))
    print(tree.find(10))
    print(tree.find(5))

    print()
    print(tree)
    print()
    tree.insert(3, "d")
    tree.insert(15, "f")
    print(tree)
    print()
    print(tree.find(20).value)
