# function to count the number of digits
def countDigit(num,index):
  
  if (index == len(str(num))):
    return 0
    
  else:
    return 1 + countDigit(num,index+1)
    
# function to find the maximum value
def findMax(list):
  
  if len(list) == 1:
     return list[0]
    
  else:
     max = findMax(list[1:]) 
    
  if list[0] > max:
       return list[0]
  else:
       return max
    

# function to count the value of occurences
html = """<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies.</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>"""

def count_tag_occurrences(code, tag):
   
    if not code:
        return 0
      
    opening_tag = f"<{tag}>"
    closing_tag = f"</{tag}>"

    opening_index = code.find(opening_tag)

    if opening_index == -1:
        return 0

    closing_index = code.find(closing_tag, opening_index)

    if closing_index == -1:
        return 0

    count = 1

   
    remaining_html = code[closing_index + len(closing_tag):]
    count += count_tag_occurrences(remaining_html, tag)

    return count


# function to display the menu 
def displayMenu():
  print("1. Count Digits\n" + "2. Find Max\n" + "3. Count Tags\n" + "4. Exit")


displayMenu()
choice_input = int(input("Please enter your choice: "))
print("\n")
  
while (choice_input != 4): # 
    if (choice_input == 1):
      user_input = input("Please enter your number: ")
      print("The number of digits in",user_input,"is",countDigit(user_input,0))
      print("\n")

    elif (choice_input == 2):
      lst = []
      input_size = int(input("Please enter the size of the list: "))
      for i in range(input_size):
        input_element = int(input("Enter the element:"))
        lst.append(input_element)
      print(lst)
        
      print("The maximum value is:",findMax(lst)) 
      print("\n")

    elif (choice_input == 3):
      input_tag = input("Please enter your tag: ")
      print("The occurences of <",input_tag,"> is: ",count_tag_occurrences(html,input_tag))
      print("\n")
      
    else:
      print("Invalid choice")
      print("\n")
      
    displayMenu()
    choice_input = int(input("Please enter your choice: "))
    print("\n")


