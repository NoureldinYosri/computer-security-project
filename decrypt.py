#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:16:13 2017

@author: noureldin
"""

def multiplicative_inverse(x,p):
    return pow(x,p - 2,p);

def gaussian_elemenation(A,B,p):
    """returns coefficients of the polynomail"""
    n = len(A);
    if n == 0: raise Exception("empty matrix exception")
    if len(B) != n: raise Exception("B is not of same size as A")
    if not reduce(lambda x,y:x and y,map(lambda x:len(x)==n,A)):
        raise Exception("matrix rows are not of same size")
    
    for row in xrange(n):
        for col in xrange(n):
            A[row][col] %= p;
    
    # first pass - put in upper triangle form
    for pivot in xrange(n):
        cur = -1;
        for row in xrange(pivot,n):
            if A[row][pivot] != 0:
                cur= row;
                break;
        if cur == -1: raise Exception("singular matrix");
        # swap
        A[pivot],A[cur] = A[cur],A[pivot];
        B[pivot],B[cur] = B[cur],B[pivot];
        inv = multiplicative_inverse(A[pivot][pivot],p);
        for col in xrange(pivot,n):
            A[pivot][col] = (A[pivot][col] * inv)%p;
        B[pivot] = (B[pivot] * inv)%p;
        
        for row in xrange(pivot + 1,n):
            if A[row][pivot] != 0:
                mul = A[row][pivot];
                for col in xrange(pivot,n):
                    A[row][col] -= (mul * A[pivot][col])%p;
                    A[row][col] = (A[row][col]%p + p)%p;
                B[row] -= (mul*B[pivot])%p;
                B[row] = (B[row]%p + p)%p;
    
    # second pass 
    for row in xrange(n-1,-1,-1):
        for col in xrange(row+1,n):
            if A[row][col] != 0:
                mul = A[row][col];
                B[row] -= (mul*B[col])%p;
                B[row] = (B[row]%p + p)%p;
                A[row][col] = 0;

    return B;


def create_matrix(X,p):
    n = len(X);
    return map(lambda x:[pow(x,i,p) for i in xrange(n-1,-1,-1)],X);



def get_message(pairs,p):
    X = [pair[0] for pair in pairs];
    Y = [pair[1] for pair in pairs];
    A = create_matrix(X,p);
    return gaussian_elemenation(A,Y,p)[-1];

"""
def f(x,p):
    return (2*x**2 + x + 3)%p;

if __name__ == "__main__":
    X = [1,2,2];
    p = 11;
    B = map(lambda x:f(x,p),X);
    A = create_matrix(X,p);
    print A,B;
    print gaussian_elemenation(A,B,p);
    
 """