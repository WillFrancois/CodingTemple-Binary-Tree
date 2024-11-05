class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    #Task 1
    def in_order(self, node):
        if node.left is not None:
            self.in_order(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order(node.right)

    #Task 2
    def pre_order(self, node):
        print(node.value)
        if node.left is not None:
            self.pre_order(node.left)
        if node.right is not None:
            self.pre_order(node.right)

    #Task 3
    def post_order(self, node):
        if node.left is not None:
            self.post_order(node.left)
        if node.right is not None:
            self.post_order(node.right)
        print(node.value)

head = Node(50)
head.left = Node(30)
head.right = Node(70)
head.left.left = Node(40)
head.left.right = Node(20)
head.right.left = Node(60)
head.right.right = Node(80)

print("In Order:")
head.in_order(head)
print("\nPre Order:")
head.pre_order(head)
print("\nPost Order:")
head.post_order(head)
