class bi_tree:
    def __init__(self,x):
        self.right=None
        self.left=None
        self.parent=None
        self.value=x

    def subtree_first(self):
        if self.left:
            return self.left.subTree_first()
        return self
    def subtree_last(self):
        if self.right:
            return self.right.

    #insert Node B after Node A
    def insert_after_node(self,A,B):
        if A.right:
            A=A.right.subTree_first()
            A.left,B.parent=B,A
        else:
            A.right,B.parent=B,A
    
    def insert_before_node(self,A,B):
        if A.left:
            A=A.left.subTree_last()
            A.right,B.parent=B,A
        else:
            A.left,B.parent=B,A
    




