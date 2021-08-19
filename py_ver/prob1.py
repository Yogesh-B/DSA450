#Reverse the array
#https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/


#assume that user will give correct input and no error happens
in_arr = input("enter number separated by space:").strip()
arr = [int(num) for num in in_arr.split(" ")]

#set first value
min_val = arr[0]
max_val = arr[0]


for i in arr :
  if i < min_val :
    min_val = i
  if i > max_val :
    max_val = i

print("min - ",min_val," // max - ",max_val)