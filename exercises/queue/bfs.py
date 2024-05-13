from queue import Queue

graph1 = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

graph2 = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'G'],
    'E': ['B', 'F'],
    'F': ['E', 'G'],
    'G': ['D', 'F']
}

graph3 = {
    'A': ['B', 'F'],
    'B': ['A', 'C', 'G'],
    'C': ['B', 'D', 'H'],
    'D': ['C', 'E', 'I'],
    'E': ['D', 'J'],
    'F': ['A', 'G', 'K'],
    'G': ['B', 'F', 'H', 'L'],
    'H': ['C', 'G', 'I', 'M'],
    'I': ['D', 'H', 'J', 'N'],
    'J': ['E', 'I', 'O'],
    'K': ['F', 'L', 'P'],
    'L': ['G', 'K', 'M', 'Q'],
    'M': ['H', 'L', 'N', 'R'],
    'N': ['I', 'M', 'O', 'S'],
    'O': ['J', 'N', 'T'],
    'P': ['K', 'Q'],
    'Q': ['L', 'P', 'R'],
    'R': ['M', 'Q', 'S'],
    'S': ['N', 'R', 'T'],
    'T': ['O', 'S']
}


discovered = set()
queue = Queue()
predecessors = dict()

def bfs(graph, discovered, queue, goal):
    initial_node = queue.peek()
    while not queue.is_empty():
        print(queue)
        node = queue.dequeue()
        if node == goal:
            print('Chegamos no objetivo!')
            # print(predecessors)
            shortest_path = []
            shortest_path.append(goal)
            n = goal

            while n!= initial_node: # Precisamos voltar até o caminho inicial para encontrar o melhor caminho
                shortest_path.append(predecessors[n])
                n = predecessors[n] # Colocando o valor da chave como próxima chave. Logo, teremos outro valor dentro da nova chave até chegar no caminho inicial.

            shortest_path = shortest_path[::-1] # Inverter vetor (início > fim)
            print(f'O caminho mais curto será: {shortest_path}')
            
            return True
        else:
            for path in graph[node]:
                if path not in discovered:
                    queue.enqueue(path)
                    discovered.add(path)
                    predecessors[path] = node 

    return False
    
start = input('Qual o caminho inicial? ')
queue.enqueue(start)
discovered.add(start)

bfs(graph3, discovered, queue, 'G')

 