#define two arrays (lists)
array1=[1,2,3,4,5]
array2=[4,5,6,7,8]
#convert arrays to sets and find intersection
commom_values= set(array1).intersection (set(array2))
#convert the result back to a list (optional)
common_values = list(commom_values)
#print the common values
print("common values between the two arrays:",common_values)
