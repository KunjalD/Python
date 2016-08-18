#!/usr/bin/env python
import random
class BinaryTree:
    def __init__(self,content):
        self.content = content
        self.left = None
        self.right = None
        self.depth = -1

    def __str__(self):
        return "(" + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) +"))"

def is_balance_binary(btree):
    if btree is None: return True;
    return (abs(depth(btree.left) - depth(btree.right)) <= 1) and \
        is_balance_binary(btree.left) and is_balance_binary(btree.right)

def depth(btree):
    if btree is None:
        return 0
    else:
        if btree.depth != -1:
            return btree.depth
        else:
            btree.depth = 1 + max(depth(btree.left), depth(btree.right))
            return btree.depth

def is_bal_binary_tree(btree):
    return check_balanced(btree)[0]

def check_balanced(btree):
    if btree is None: return True, 0
    left_balanced, left_depth = check_balanced(btree.left)
    right_balanced, right_depth = check_balanced(btree.right)
    btree.depth = 1 + max(left_depth, right_depth)
    return left_balanced and right_balanced and \
        (abs(depth(btree.left) - depth(btree.right)) <= 1), btree.depth


bt = BinaryTree(random.randint(0,100))
for c1 in xrange(0,19):
    bt2 = BinaryTree(random.randint(0,100))
    bt2.left = bt
    bt = bt2

unbalanced_bt=bt
#print unbalanced_bt.__str__()

def make_random_balanced_tree(depth):
    if depth > 0:
        tree = BinaryTree(random.randint(0,100))
        tree.left = make_random_balanced_tree(depth - 1)
        tree.right = make_random_balanced_tree(depth - 1)
        return tree
    else:
        return None

balanced_tree = make_random_balanced_tree(5)
print balanced_tree.__str__()
