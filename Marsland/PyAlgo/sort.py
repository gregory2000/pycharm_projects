__author__ = 'g42gregory'
import random

def insertion_sort(A):
    for i in xrange(1, len(A)):
        for j in xrange(i, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
            else:
                break

if __name__ == '__main__':
    a = [random.randint(0, 1000) for k in xrange(30)]
    print(a)
    insertion_sort(a)
    print(a)
