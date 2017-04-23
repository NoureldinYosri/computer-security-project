#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 16:31:02 2017

@author: noureldin
"""

import encrypt;
import decrypt;
import random;
m = 10;
n = 50;
S = random.randint(1,10**40);
pairs,p = encrypt.encrypt(m,n,S);
print "prime = ",p;
print "all points :";
print pairs;
print;
St = decrypt.get_message(random.sample(pairs,m),p);
print "success original message == obtained message" if S == St else "fail";