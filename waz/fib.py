#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def fib_iter1(n):
    pwyrazy = (0, 1)
    a, b = pwyrazy
    while n > 1:
        a, b = b, a + b 
        n -= 1
    print(b, end=" ")

fib_iter1(10)
