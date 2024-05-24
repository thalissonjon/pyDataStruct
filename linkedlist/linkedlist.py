class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        cur = self.head # Iterar ate o ultimo
        while cur.next!=None:
            cur = cur.next

        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total +=1
            cur = cur.next   

        return total
    
    def display(self):
        items = []
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            print(cur.data)
            items.append(cur.data)
        
        print(items)
        return items

    def get(self, index):
        if index>=self.length():
            print('Index out of range.')
            return None
        
        cur_idx = 0
        cur_node = self.head

        while True:
            cur_node = cur_node.next
            if cur_idx==index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index>=self.length():
            print('Index out of range.')
            return 
        
        cur_idx = 0
        cur_node = self.head

        while True:
            last_node = cur_node # 1
            cur_node = cur_node.next # 2
            if cur_idx == index:
                last_node.next = cur_node.next # [1,2,3,4 ] > remove idx 2 = 3 > last_node = 2, idx = 2, cur_node = 3, last_node.next = 4 (cur_node = 3, cur_node.next = 4)
                return
            cur_idx +=1

list = LinkedList()

list.append(5)
list.append(6)
list.append(7)
list.append(3)
list.append(2)

list.display()
list.erase(2)
list.display()