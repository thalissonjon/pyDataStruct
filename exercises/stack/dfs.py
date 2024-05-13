# Depth-First Search algorithm
from stack import Stack

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
stack = Stack()

def dfs(graph, stack, discovered, goal):
    traveled_path = []
    while not stack.is_empty():
        # print(f'Stack: {stack}')
        node = stack.pop()
        traveled_path.append(node)
        if node == goal:
            # print(f'Chegamos no objetivo! Caminhos descobertos {discovered}')
            print(f'Caminho percorrido: {traveled_path}')
            return True
        else:
            for path in graph[node]:
                if path not in discovered:
                    stack.push(path)
                    discovered.add(path)

    
    print(f'Não foi encontrado o objetivo. Caminhos descobertos: {discovered}')
    return False
     


start = input('Qual o caminho inicial? ')
stack.push(start)
discovered.add(start)
dfs(graph3, stack, discovered, 'D')




