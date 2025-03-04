class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_post_order(self):
        result = []

        def trevers(current_node):
            if current_node.left is not None:
                trevers(current_node.left)
            if current_node.right is not None:
                trevers(current_node.right)
            result.append(current_node.value)
    
        trevers(self.root)
        return result






my_tree = BinarySearchTree()
my_tree.insert(1)
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(5)
my_tree.insert(6)
my_tree.insert(7)

print(my_tree.dfs_post_order())

# Expected output: [18, 27, 21, 52, 82, 76, 47]





                

