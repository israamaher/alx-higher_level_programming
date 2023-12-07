#!/usr/bin/python3
""" Pascal's Triangle"""


def pascal_triangle(n):
    
    triangle= []
    if n <= 0:
        return {}

    for i in range(n):
        n =[(1)]
        n.extend(n[i] + n[i+1])
        n.append[1]
    triangle.append[n]
    return triangle
