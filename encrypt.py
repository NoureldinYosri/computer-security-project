#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 16:32:08 2017

@author: noureldin
"""

import random,sys


def gcd(a,b):
    while b: a,b = b,a%b;
    return a;

def is_probable_prime(p):
    if p <= 1: return False;
    if p <= 3: return True;
    if p%2 == 0 or p%3 == 0: return False;
    for i in xrange(1000):
        x = random.randint(1,p - 1);
        if gcd(x,p) != 1: return False;
        if pow(x,p - 1,p) != 1: return False;
    return True;

def get_prime(S):
    """returns a prime greater than S"""
    lim = S + 10**50;
    p = random.randint(S + 1,lim);
    while not is_probable_prime(p):
        p = random.randint(S + 1,lim);
    return p;    

def get_X(n,p):
    X = [];
    lst = 0;
    while len(X) < n:
        X.append(random.randint(lst + 1,p - 1 - n + len(X) - 1));
        lst = X[-1];
    return X;

def polynomial(x,C,p):
    return sum([C[i] * pow(x,len(C) - 1 - i,p) for i in xrange(len(C))]) % p;

def encrypt(m,n,S):
    """returns pairs of points and prime"""
    p = get_prime(10*max([n,S,m]));
    C = [random.randint(i==0,p-1) for i in xrange(m)];
    C[-1] = S;
    X = get_X(n,p);
    return map(lambda x:[x,polynomial(x,C,p)],X),p;


if __name__ == "__main__":
    m,n,S = map(int,str(sys.argv[1]).split());
    pairs,p = encrypt(m,n,S);
    f = file("out.out","w");
    for pair in pairs:
        f.write("%d %d\n"%(pair[0],pair[1]));
    f.write("%d\n"%p);
    f.close();
    print "this message is from encrypt.py";
