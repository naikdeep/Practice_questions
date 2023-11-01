class BinaryTree():
    def __init__(self,x):
        self.parent = None
        self.right =  None
        self.left = None
        self.x=x
    
    def NaturalTraverse(self):
        if self.left:
            yield from self.left.NaturalTraverse()
        yield self
        if self.right:
            yield from self.right.NaturalTraverse()

TreeObj = BinaryTree(10)
TreeObj.left = BinaryTree(9)
TreeObj.left.right = BinaryTree(8)
TreeObj.left.left = BinaryTree(7)
TreeObj.right = BinaryTree(13)
TreeObj.right.left = BinaryTree(11)
TreeObj.right.right = BinaryTree(12)

genObjs=TreeObj.NaturalTraverse()

for i in genObjs:
    print(i.x)