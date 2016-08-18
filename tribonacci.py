#!/usr/bin/env python
#Tribonacci
# signature = [1,1,1]
# signature1 = [0,0,1]
# def tribonacci(signature, n):
#     if len(signature) < 3:
#         raise "Need atleast 3 values"
#     else:
#         while len(signature) < n:
#             signature.append(sum(signature[-3:]))
#     return signature

# print tribonacci(signature,10)
# print tribonacci(signature1,10)


# import math
# def door100():
#     for i in range(1, int(math.sqrt(100)+1)):
#         print ("%sth door is open\n" % (i*i))


# door100()


matrix=[[2,3],[4,5]]
def matrix_mult(matrix):
    daigonal=1
    for i in range(0,len(matrix)):
        daigonal = daigonal * matrix[i][i]
    print daigonal

matrix_mult(matrix)