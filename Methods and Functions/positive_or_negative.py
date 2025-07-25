# -*- coding: utf-8 -*-
"""Positive or Negative

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sJYDRSJjBaVypl_6gFIjG6l0BwOCLFFY
"""

'''
Write a function called is_positive that takes a number and returns True if it is positive or zero, and False otherwise.

Inputs:
An integer (int).

Outputs:
A True value if it is positive or zero.
A False value if it is negative.

Sample Input and Output:
Sample Input 1:

5

Expected Output 1:

True

Sample Input 2:

-3

Expected Output 2:

False
'''

def is_positive(number):
    return number >= 0
print(is_positive(5))   # Output: True
print(is_positive(-3))  # Output: False