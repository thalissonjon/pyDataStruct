from priorityqueue import PriorityQueue

graph2 = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'G'],
    'E': ['B', 'F'],
    'F': ['E', 'G'],
    'G': ['D', 'F']
}


def heuristic(x, y):
    pass

def fValue(g, h):
    pass

def a_star(start, goal, graph):
    pq = PriorityQueue()
    fValues = {}
    pq.put('A', 0)
    while not pq.is_empty():
        node = pq.get()
        if node == goal:
            print('Encontrado')
        else:
            for path in graph[node]:
                # fValue[path] =
                pass 


dict1 = {
    'carro1': 'ABC123'
}

print(dict1['carro1'])

vetor1 = [1,2,3,4,5]

