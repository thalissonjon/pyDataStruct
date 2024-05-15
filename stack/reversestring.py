from stack import Stack

my_string = "abcdefgh"

def reverse_string(my_string): # Stack solution
    reversed_string= ""
    stack = Stack()

    for char in my_string:
        stack.push(char)
    
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

def reverse_string_2(my_string): # String solution
    reversed_string = ""

    for x in range(len(my_string)-1, -1, -1):
        reversed_string += my_string[x]
    
    return reversed_string
    
    
# my_string = reverse_string_2(my_string)
print(my_string)