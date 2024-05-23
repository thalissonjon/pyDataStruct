from priorityqueue import PriorityQueue
import math

coordinates = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (1, 1),
    (2, 1),
    (3, 1)
]


def fValue(start, current, goal, g_cost):
    xStart, yStart = start
    xCurrent, yCurrent = current
    xGoal, yGoal = goal

    # gValue = abs(xCurrent - xStart) + abs(yCurrent - yStart) #manhattan distance 
    gValue = g_cost[current]
    hValue = math.sqrt((xGoal - xCurrent)**2 + (yGoal - yCurrent)**2) #euristic distance
    return gValue + hValue #f value


def a_star(start, goal, graph):
    directions = [(1,0), (-1,0), (0,1), (0,-1)] #dx dy  /  dir, esq, cima, baix
    pq = PriorityQueue()
    discovered = []
    came_from = {}
    g_cost = {start: 0}
    pq.put((0,0), 0)
    discovered.append(start)

    while not pq.is_empty():
        node = pq.get()
        discovered.append(node)

        if node == goal:
            path = []
            n = node
            while n!=start:
                path.append(n)
                n = came_from[n]
            
            path = path[::-1]
            print(f'O caminho foi {path}')
            return True
        
        else:
            for direction in directions:
                dirX, dirY = direction
                x, y = node
                new_node = (x + dirX, y + dirY)

                if new_node in graph and new_node not in discovered:
                    g_cost[new_node] = g_cost[node] + 1 
                    pq.put(new_node, fValue(start, new_node, goal, g_cost))
                    came_from[new_node] = node
                    discovered.append(new_node)

    return False #caminho nao encontrado

a_star(coordinates[0], coordinates[-1], coordinates)
