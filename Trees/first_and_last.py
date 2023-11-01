class BinaryTree():
    def __init__(self,x):
        self.x = x
        self.parent = None
        self.left = None
        self.right = None
    
    def  subtree_first(self):
        if self.left:
            return self.left.subtree_first()
        return self
    
    def subtree_last(self):
        if self.right:
            return self.right.subtree_last()
        return self


    def successor(self):
        if self.right:
            return self.right.subtree_first()
        while self.parent and (self is self.parent.right ):
            self=self.parent
        return self.parent
        
    def predeccor(self):
        if self.left:
            return self.left.subtree_last()
        while self.left and (self is self.parent.left):
            self=self.parent
        return self.parent

