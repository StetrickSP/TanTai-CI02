# TreeNode 
class TreeNode: 
    def __init__(self,root):
        self.root = root
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, level=0):
        if self: 
            print(" " * level + self.root)
            for child in self.children:
                child.print_tree(level + 1)

# BinaryTreeNode
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, child):
        self.left = child

    def add_right(self, child):
        self.right = child

    def print_tree(self, level=0):
        if self:
            print(" " * level + str(self.value))
            if self.left:
                self.left.print_tree(level + 1)
            if self.right:
                self.right.print_tree(level + 1)

    def count_nodes(self):
        count = 1
        if self.left:
            count += self.left.count_nodes()
        if self.right:
            count += self.right.count_nodes()
        return count
    
    def count_leaves(self):
        if self.left is None and self.right is None:
            return 1
        leaves = 0
        if self.left:
            leaves += self.left.count_leaves()
        if self.right:
            leaves += self.right.count_leaves()
        return leaves

## Create a binary tree
root = BinaryTreeNode(50)
left_child = BinaryTreeNode(25)
right_child = BinaryTreeNode(75)

root.add_left(left_child)
root.add_right(right_child)

left_child.add_left(BinaryTreeNode(12))
left_child.add_right(BinaryTreeNode(37))

right_child.add_left(BinaryTreeNode(62))
right_child.add_right(BinaryTreeNode(87))

print("Binary Tree")
root.print_tree()
print("Number of nodes and leaves")
print("Nodes:", root.count_nodes())
print("Leaves:",root.count_leaves())




    
