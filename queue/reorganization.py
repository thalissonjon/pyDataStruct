from queue import Queue
from collections import deque

# Complete this function by using a sequence of enqueue() and dequeue() 
# operations, so the final state of my_queue.items is
# deque(['the', 'aardvark', 'wore', 'a', 'silly', 'hat'])
def queue_challenge():
    phrase = deque(['the', 'aardvark', 'wore', 'a', 'silly', 'hat'])
    my_queue = Queue()
    word_list =  ["wore", "a", "silly", "hat", "the", "aardvark"]

    for word in word_list:
        my_queue.enqueue(word)

    while my_queue.items != phrase:
        my_queue.enqueue(my_queue.dequeue())
        print(my_queue)
        
    return my_queue.items


queue_challenge()