from priorityqueue import PriorityQueue

def process_tasks(tasks):
    queueTasks = PriorityQueue()
    ordered_task_list = []
    
    print(f'tasks: {tasks}')
    for item, priority in tasks:
        queueTasks.put(item, priority)
    
    while not queueTasks.is_empty():
        ordered_task_list.append(queueTasks.get())

    return ordered_task_list


tasks = [('drink', 2), ('eat', 1), ('be merry', 3)]
tasks = process_tasks(tasks)

print(tasks)