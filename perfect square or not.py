import math as m
n=int(input())
root = int(m.sqrt(n))
if root * root == n:
  print("Perfect square")
else:
  print("Not a perfect square")
