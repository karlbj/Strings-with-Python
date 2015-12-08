#!/usr/bin/python
# -*- coding: utf-8 -*-

str01 = raw_input("Type som characters: ") 
for c in str01:
  print c
print len(str01)
n = 0
for c in str01:
  if c =="å" or c == "Å" or c =="æ" or c == "Æ" or c =="ø" or c == "Ø" : 
    n = n + 1
print "Number of especial danish characters: ", n

 
