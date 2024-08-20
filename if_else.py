# -*- coding: utf-8 -*-
"""If Else.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N8THfdjCQGrv2JUJZFxahcd5M_EXmKpA
"""



"""https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

Task

Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if(n%2!=0):
        print('Weird')
    else:
        if 2 <= n <= 5:
            print('Not Weird')
        if 6 <= n <= 20:
            print('Weird')
        else:
            print('Not Weird')
