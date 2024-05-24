class TreeNode: # Binary Search Tree = valores menores que o nó a esquerda e valores maiores que o nó a direita 
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value) # Prosseguir iterando até achar um espaço vazio
        
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)


    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal() 
        if self.right:
            self.right.preorder_traversal()
        
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal() 
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self,value):
        if value < self.value:
            if self.left is None:
                return False # é menor entao deveria estar a esquerda do nó. se nao tem nada a esquerda, esse valor nao existe na arvore
            else:
                return self.left.find(value)
        
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)

        else: # ==
            return True
        
tree = TreeNode(10)

print('INSERINDO 1')
tree.insert(1)

print('INSERINDO 11')
tree.insert(11)


print('INSERINDO 12')
tree.insert(12)
print('INSERINDO 13')
tree.insert(13)
print('INSERINDO 9')
tree.insert(9)
print('INSERINDO 2')
tree.insert(2)
print('INSERINDO 1')
tree.insert(1)
tree.insert(0)
tree.insert(13)

tree.inorder_traversal()

print(tree.find(111))

# def level_order_traversal(self):
#         nodes = []
#         queue = deque([self.root])
        
#         while queue:
#             node = queue.popleft()
#             if node:
#                 nodes.append(node.value)
#                 queue.append(node.left)
#                 queue.append(node.right)
        
#         return nodes