#Reverse the array
#https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/



def reverseArr(arr1):
  full_len = len(arr1)
  half_len = int(len(arr1)/2)
  for i in range(half_len):
    tmp_char = arr1[i]
    arr1[i] = arr1[full_len - i - 1]
    arr1[full_len - i - 1] = tmp_char
  return arr1


if __name__ == "__main__":
  #assume that user will give correct input and no error happens
  in_arr = [int(x) for x in input("Enter numbers separated by space : ").strip().split(" ")]
  print("original : ",in_arr)
  rev_arr = reverseArr(in_arr)
  print("Reverse : ",rev_arr)