class btree():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        self.parent= None
    def delete_a_node(self):
        if self.left or self.right:
            if self.left: self.left.

