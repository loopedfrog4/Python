from sys import stdin
import sys

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def set_child(temp_list,index):
    if index >= len(temp_list) or temp_list[index] == None:
        return None
    temp = Node(temp_list[index])
    temp.left = set_child(temp_list, index*2+1)
    temp.right = set_child(temp_list, index*2+2)
    return (temp)

def is_binary_search_tree(root):

    def is_bst(node, min, max):
        if node.data <= min:
            return False

        if node.data >= max:
            return False

        left_ok = True
        right_ok = True

        if node.left is not None:
            left_ok = is_bst(node.left, min, node.data)
        if node.right is not None:
            right_ok = is_bst(node.right, node.data, max)

        return left_ok and right_ok

    if root is None:
        return True

    return is_bst(root, float('-inf'), float('inf'))

if __name__ == '__main__':
    flag = True
    for line in stdin:
        nums = list(line[1:-1].strip().split(","))
        nums = [int(item) if item.isnumeric() else None for item in nums]
        root = set_child(nums, 0)
        print(is_binary_search_tree(root))