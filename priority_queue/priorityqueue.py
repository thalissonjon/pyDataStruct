import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = [] # Usamos elementos inves de itens, por conta que não são apenas itens. Temos itens e suas prioridades associadas
    
    def __str__(self):
        return str(self.elements)
    
    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        return heapq.heapqpush(self.elements, (priority, item))

    def get(self):
        return heapq.heapqpop(self.elements)[1]
    
    