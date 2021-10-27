

def compressTheString(s) : 
  # initialize count variable to 1 (as every number in string shows up atleast once)
  count = 1 
# if len of string is 1, return string and len string, which is (1,1)
  if len(s) == 1:
      print((int(s),len(s)))
  else:

      # for loop staring from the 1th index to len(string)
      for i in range(1,len(s)): 
          #if current string[current index]==string[previous index]
          if s[i] == s[i-1]:
            # increasce count by 1, for loop moves onto next index
              count += 1 

          else:
            # print count and current element of string , in tuple format
              print((count,int(s[i-1])), end = " ")
              # reinitialize count varaible to 1 
              count = 1
      # at the end of the for loop , print count and current element of string, since len(s + 1) is invalid
      print((count,int(s[i])))


