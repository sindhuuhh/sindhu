#Number of rows
rows=6
#outer loop to handle the number of rows
for i in range(rows,0,-1):
     #inner loop to print the repeated number in each rows
     for j in range(rows-i+1):
          print(i,end="")
          #move to the next line after each row
          print()
