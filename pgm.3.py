Python 3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #number of rows
>>> rows=6
>>> 
>>> #output loop to handle the number of rows
>>> for i in range(row,0,-1):
...     #inner loop to print the repeated number in each row
...     for j in range(rows,-1,+1):
...         print(i,end="")
...         #move to the next line after each row
