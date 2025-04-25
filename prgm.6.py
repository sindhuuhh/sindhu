#python program to print the fibonacci sequence using while loop
#number of tearms to display
n_terms=int(input("enter the number of fibonacci terms to display:"))
#first two terms
a,b=0,1
count=0
#check if the number of terms is vaild
if n_terms<=0:
     print(f"please enter a positive integer.")
elif n_terms==1:
      print(f"fibonacci sequence:")
      print(a)
else:
    print(f"fibonacci sequence:")
    while count<n_terms:
       print(a,end="")
       #update values
       a,b+b,a+b
       count+=1
          
                
