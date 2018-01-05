#第3章    繰り返しさせる方法(反復の基礎文法)
#リスト3.1

array = [1,2,3,4,5]
for v in array:
    print(v)

'''
Python 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:25:24) [MSC v.1
900 64 bit (AMD64)]
Type "copyright", "credits" or "license" for more information.

IPython 5.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: array = [1,2,3]

In [2]: array[1]
Out[2]: 2

In [3]: array[0]
Out[3]: 1

In [4]: array[5]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-4-b10cbda823aa> in <module>()
----> 1 array[5]

IndexError: list index out of range

In [5]: array[-1]
Out[5]: 3

In [6]: array[-2]
Out[6]: 2

In [7]: array[-3]
Out[7]: 1

In [8]: array[-4]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-8-bd30e382f6b5> in <module>()
----> 1 array[-4]

IndexError: list index out of range

In [9]:
'''
