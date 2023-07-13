## Assignment 1 ##

# Problem 1 #

input_number = int(input("Please Enter Your Number: n = "))

def calculateFactorial(x):
  if x < 0:
    print("The factorial is undefined for negative numbers")
  elif (x == 0):
    print("The factorial of 0 is: n! = 1")
  else:
    i = 1
    result = 1
    while (i <= x):
      result = result * i
      i += 1
    print("The factorial of your number is: n! =", result)

calculateFactorial(input_number)



# Problem 2 #
print("\n\n")
input_number2 = int(input("Please Enter Your Number: n = "))
list = []
def findDivisors(value):
  if value == 0:
    print("Zero does not have divisors")
  else:
    i1 = value
    while (i1 <= value and i1 != 0):
      remainder = value % i1
      if (remainder == 0):
        list.append(i1)
      i1 -= 1
    list.sort()
  print("The divisors of this number are:",list)
  
findDivisors(input_number2)


# Problem 3 #
print("\n\n")
input_str = input("Please Enter a string: ")

def reverseString(str):
  for i2 in range(len(str)):
    index = (len(str)-1) - i2
    print(str[index],end='')

reverseString(input_str)


# Problem 4 #
print("\n\n")
list1 = []
len_input = int(input("Please enter the length of the list: "))
for i3 in range(len_input): 
  list_input = int(input("Please enter the list element: "))
  list1.append(list_input)
print(list1)
def findEven(value2):
  list2 = []
  for i4 in range(value2):
    if (list1[i4] % 2 == 0):
      list2.append(list1[i4])
  print("The even numbers of the original list are: ",list2)
      
findEven(len_input)


# Problem 5 #
print("\n\n")
input_string = input("Please enter your password: ")

def checkPassword(value3):
  a = b = c = d = e = False
  character = ['#', '!', '$', '?']
  if (len(value3) >= 8):
      a = True
  for i4 in value3:
    if (i4.isupper()):
      b = True
      break
  for i5 in value3:
    if (i5.islower()):
      c = True
      break
  for i6 in value3:
    if (i6.isdigit()):
      d = True
      break
  for i7 in value3:
    if (i7 in character):
      e = True
  if (a == b == c == d == e == True ):
     print("strong password")
  else:
     print("weak password")
checkPassword(input_string)


# Problem 6 #
print("\n\n")
input_IP = input("Please enter your IP address: ")

def checkIPaddress(octet):
  count = 0
  char = ['.']
  valid = []
  valid_zero = []
  
  for i8 in range(len(octet)):
    count += 1 
    if (count < 4 and octet[i8] != octet[len(octet)-1]):
      if (octet[i8] in char and octet[i8+2] not in char and octet[i8] 
          < octet[len(octet)-2]):
        valid_zero.append(octet[i8+1])
      if (octet[i8] in char and octet[i8] != octet[0]):
        valid.append(i8)
        count = 0
      else:
        count = 0
        continue
    else:
      count = 0
      continue
      
  if (len(valid) == 3 and valid[0] <= 3 and valid[1] <= 7 and valid[2] 
      <= 11 and octet[0] != '0' and '0' not in valid_zero):
        
    print("Valid IPv4")
  else:
    print("Invalid IPv4")
     
checkIPaddress(input_IP)