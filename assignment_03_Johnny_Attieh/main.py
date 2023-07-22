# Sum of tuples #
def calculateTuple():
  
  tup1 = ()
  tup1_len = int(input("Enter the length of the tuples: "))
  
  list1 = list(tup1)
  
  for i in range(tup1_len):

    input_element1 = int(input("Enter the element of the FIRST tuple: "))
    list1.append(input_element1)   

  
  tup2 = ()
  list2 = list(tup2)
  
  for i in range(tup1_len):
    
    input_element2 = int(input("Enter the element of the SECOND tuple: "))
    list2.append(input_element2)
  # Let the user input the tuples and switching tuples to lists

  list3 = []

  for i in range(len(list1)):
    sum = list1[i] + list2[i]
    list3.append(sum)
  # Doing the sum of the elements having the same index

  tup3 = tuple(list3)

  return tup3


# Export Json file #
dict1 = {"name":"johnny", "age":31, "hobbies":["reading","cooking","basketball"]}

# Hardcoded the dictionnary 

def format(dict): # function to check the dictionary
  items = []
  for key, value in dict.items():
    key_str = f'"{key}"'
    value_str = check_format(value) # function to check the type of each key and value in the dictionary
    items.append(f"{key_str}: {value_str}")
  return "{" + ", ".join(items) + "}"
  


def check_format(value):
  items = []
  if type(value) == dict:
    for key, value in value.items():
      key_str = f'"{key}"'
      value_str = check_format(value)
      items.append(f"{key_str}: {value_str}")
    return "{" + ", ".join(items) + "}" # if the value is a dictionary
  elif type(value) == list:
        elements = []
        for item in value:
            elements.append(check_format(item))
        return "[" + ", ".join(elements) + "]" # if the value is list
  elif type(value) == str:
    return f'"{value}"'# if the value is string
  elif type(value) in (int, float):
    return f'"{value}"'# if the value is unt or float
  elif value is None:
    return "null" # if the value is none






def displayMenu():
  print("1.Sum Tuples\n2.Export Json\n3.Import Json\n4.Exit")
displayMenu()

input_user = int(input("Enter your choice: "))
print("\n")
while (input_user != 4):
    if (input_user == 1):
      print(calculateTuple())
      
    elif (input_user == 2):
      json_string = format(dict1)
      print(json_string)
      
    elif (input_user == 3):
      print("Option not available")
      
    else:
      print("Invalid choice")
    print("\n")
    displayMenu()
    input_user  = int(input("Enter your choice: "))
# display the menu and calling the right function for the right choice  



## Big-O notation exercise ##
  
# a. O(N^3)
# b. O(N^3)
# c. O(N!)
# d. O(NlogN)
# e. O(N)
# f. O(N^2)
# g. O(N^2)
# h. O(N!)