#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findEncryptedPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING password as parameter.
#

from collections import deque

def findEncryptedPassword(password):
    chars = []
    for char in password:
        chars.append(char)
    
    chars.sort()

    palindrome = deque()
    
    i = len(chars) // 2
    if len(chars) % 2 != 0:
        middle_char = chars.pop(i)
        palindrome.append(middle_char)

    for i in range(i - 1, -1, -1):
        added = chars[i]
        palindrome.appendleft(added)
        chars.pop(i)
        
        for char in chars:
            if char == added:
                palindrome.append(char)
                chars.remove(char)
                break
    
    final_password = "".join(palindrome)
    print(final_password)

if __name__ == '__main__':

    password = input()
    findEncryptedPassword(password)
