#!/bin/env python
#-*- coding: latin-1 -*-
# 2007.4.9
#
# ガウスの公式による円周率の計算

from math import *	# 数学関数を使うためのまじない
from time import *	# 時間関数を使うためのまじない
from sys import *	# システム関数を使うためのまじない

# arctan(1/n) の小数展開
def expansion(n):
	x = ( p * q ) / n
	nn = n * n
	c = 1
	s = x
	k = 1
	while x > 0:
		x = x / nn
		k = k + 2
		c = - c
		s = s + c * ( x / k )
	return s

print '円周率を計算します。'
print '桁数を指定してください。'
prsn = input()

t0 = time()		# 開始時刻
p = 10**prsn
q = 10**10

y = 4 * ( 12 * expansion(18) + 8 * expansion(57) - 5 * expansion(239) )
y = y / q
u = y / p
v = y - u * p
t1 = time()		# 終了時刻

print "%d.%d" % (u,v)
print '計算時間 =', t1 - t0
fin = stdin.readline()	# Enter キーで終了
