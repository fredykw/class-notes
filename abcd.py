#program: a) create a Tree
class Tree:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def insert(root, Tree):
    if root is None:
        root = Tree
    else:
        if root.data > Tree.data:
            if root.l_child is None:
                root.l_child = Tree
            else:
                insert(root.l_child, Tree)
        else:
            if root.r_child is None:
                root.r_child = Tree
            else:
                insert(root.r_child, Tree)

t = Tree(10)
insert(t, Tree(5))
insert(t, Tree(20))

#program: b) print in in,pre,post Order
def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)    

def post_order_print(root):
    if not root:
        return        
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)    
    print root.data

print "in order:"
in_order_print(t)

print "pre order"
pre_order_print(t)

print "post order"
post_order_print(t)

#program: c) count of Tree
def size(root):
    if root is None:
        return 0
    else:
        return (size(root.r_child)+ 1 + size(root.l_child))

print "Size of the tree is %d" %(size(t))

#program: d) unit testing
import unittest
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_root_r_child(self):
        self.assertEqual( size(t.r_child), 1)

    def test_numbers_root_l_child(self):
        self.assertEqual( size(t.l_child), 1)
 
    def test_total_sum(self):
        self.assertEqual( size(t.r_child)+ 1 + size(t.l_child), 3)
 
if __name__ == '__main__':
    unittest.main() 


