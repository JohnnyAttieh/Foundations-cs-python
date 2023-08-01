import datetime

dict_list = []


def readFile():
  path = input("Insert your file path: ")
  file = open(path, "r") # Read the file using the file path

  for line in file: # reading the file line by line 
                    # https://favtutor.com/blogs/read-file-line-by-line-python#:~:text=We%20can%20read%20the%20file,that%20the%20file%20has%20ended.
    temp_dict = {}
    
    list_content = line.strip().split(",") # split the line at the character "," and store it in a list
    temp_dict['ticketID'] = list_content[0]      
    temp_dict['eventID'] = list_content[1]       
    temp_dict['username'] = list_content[2]      #  create a key for each value of the list and store it in a dictionary
    temp_dict['date'] = list_content[3]          
    temp_dict['priority'] = int(list_content[4]) 
    
    dict_list.append(temp_dict) # create a list of dictionaries

  file.close()



def displayStatistics(): # display the eventID with highest number of tickets
  event_count = {}
  max_key = []
  max_value = 0

  for i in dict_list: # iterate through the list of dictonaries and add 1 if the event exists or set to 1 if it does not exist
    if (i['eventID'] in event_count.keys()):
      event_count[i['eventID']] += 1
    else:
      event_count[i['eventID']] = 1
      

  for key, value in event_count.items(): # get the key of the max value
   
    if (value > max_value):
      max_value = value
      max_key = [key] # list with single element
      
    elif (value == max_value):
      max_key.append(key) # append to the list if there is more than one event with max value
  
  print("The events with highest number of tickets: ",max_key)


def getLargestID(): # get max ticked id to auto increment the ticketID of new tickets
  max = 0
  for i in dict_list:
    tick = int(i['ticketID'].replace("tick", "")) #https://realpython.com/replace-string-python/#:~:text=In%20Python%2C%20the%20.,or%20substrings%20or%20replacing%20them.
    if (tick > max):
      max = tick
  return max


def bookTicket(): # allow the admin to book a new ticket
  
  max = getLargestID() 
  
  temp_dict = {}
  
  temp_dict['eventID'] = input("Insert the EventID using the following format evXXX: ")
  temp_dict['username'] = input("Insert username: ")
  temp_dict['date'] = input("Insert date in the following format YYYYMMDD: ")
  temp_dict['priority'] = int(input("Insert priority: "))
  temp_dict['ticketID'] = "tick" + str(max + 1) # ticketID auto increment
  
  dict_list.append(temp_dict) # append the new booked dict in the original list
  
  print("The file with the new ticket: ",dict_list)
  

def mergeSort(lst,key):  # https://www.scaler.com/topics/merge-sort-in-python/
  
  if len(lst) > 1:
 
    mid = len(lst)//2
    sub_lst1 = lst[:mid]
    sub_lst2 = lst[mid:]
 
    # Sort the two halves
    mergeSort(sub_lst1,key)
    mergeSort(sub_lst2,key)
         
    # Initial values for pointers that we use to keep track of where we are in each list
    i = j = k = 0
 
    while i < len(sub_lst1) and j < len(sub_lst2):
      if sub_lst1[i][key] < sub_lst2[j][key]:
        lst[k] = sub_lst1[i]
        i += 1
      else:
        lst[k] = sub_lst2[j]
        j += 1
      k += 1
 
  # When all elements are traversed in either lst1 or lst2,
  # pick up the remaining elements and put in sorted list
    while i < len(sub_lst1):
      lst[k] = sub_lst1[i]
      i += 1
      k += 1
 
    while j < len(sub_lst2):
      lst[k] = sub_lst2[j]
      j += 1
      k += 1



def displayAllTickets(): # display tickets without old tickets
  
  temp_list = []
  today_date = datetime.date.today() # import today date: https://www.w3schools.com/python/python_datetime.asp
  
  for i in dict_list:
    
    temp_date = i['date'].strip() # .strip() to eliminate the spaces to split the date correctly
    year = int(temp_date[0:4]) # split the date into (year,month,day) and casting the string to integer, integers are comparable
    month = int(temp_date[4:6])
    day = int(temp_date[6:8])
    date = datetime.date(year, month, day)
    
    if date >= today_date:
      temp_list.append(i)
      
  mergeSort(temp_list,'date')# sorting the list per eventID
  mergeSort(temp_list,'eventID') # sorting the list per date

  print("The tickets from today's date are:\n ",temp_list)


def changeTickPriority(): # change ticket priority
  
  tick_id = input('Insert ticketID (tickXXX): ')
  priority = input('Insert priority: ')
 
  for i in dict_list:
    if (i['ticketID'] == tick_id):
      i['priority'] = priority
      
      print("\n")
      print("The file with the new priority:\n",dict_list)
      return
  print("ticket not found")


def deleteTick():# delete ticket from file
  
  tick_id = input('Insert ticketID (tickXXX): ')
  
  for i in dict_list: # looping through the list of dictionaries to find the inserted ticketID
    if (i['ticketID'] == tick_id):
      dict_list.remove(i) # remove the dictionary of inserted ticket from the list
      print("\n")
      print("The file after disabling ticket:\n", dict_list)
      return
     # if entering a wrong ticketID
  print("ticket not found")
    

    
def runEvents(): # display today events sorted by priority
  
  temp_list = []
  temp_index_list = []
  count = 0
  
  today_date = datetime.date.today() # import today date
  
  for i in dict_list:
    temp_date = i['date'].strip() # .strip() to eliminate the spaces to split the date correctly
    year = int(temp_date[0:4])
    month = int(temp_date[4:6])
    day = int(temp_date[6:8])
    
    date = datetime.date(year, month, day) # concatunate the date of event
    
    if date == today_date:
      temp_list.append(i) # append the dictionary of events with today's date in a list
      temp_index_list.append(count) # through the loop the count increase and if it is today date we append the count in a list ,so we can use it as an index 
    count += 1
    
  for i in reversed(temp_index_list): # reversed loop because using a forward loop with .pop() will change the range of the list in each iteration: https://www.geeksforgeeks.org/backward-iteration-in-python/
    dict_list.pop(i) # using .pop() because the argument of pop should be an integer
  
  mergeSort(temp_list,'priority') # sorting per priority
  print("Tickets for today's events:\n",temp_list)


def userBookTicket(username): # let the user book a ticket
  
  max = getLargestID()
  
  temp_dict = {}
  
  temp_dict['ticketID'] = "tick" + str(max + 1) # ticketID auto incremented
  temp_dict['eventID'] = input(
    "Insert EventID using the following format evXXX: ")
  temp_dict['username'] = username # take the username from the login system
  temp_dict['date'] = input("Insert date in the following format YYYYMMDD: ")
  temp_dict['priority'] = input("Insert priority: ")

  # take priority equal 0 by default if it is not inserted
  if (temp_dict['priority'] == ''):
    temp_dict['priority'] = "0"
    
  dict_list.append(temp_dict) # add the new dictionary to the original list of dictionaries
  
 


def SaveFile(): # saving file while exit: https://www.w3schools.com/python/python_file_write.asp
  
  path = input("insert path to save to: ")
  
  file = open(path, "w")
  
  for i in dict_list:
    line = i['ticketID'] + "," + i['eventID'] + "," + i['username'] + "," + i['date'] + "," + str(i['priority']) + "\n"
   
    file.write(line)
  
  file.close()



def displayMenuAdmin(): # displays the menu for an Admin user
  print(
    "1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit"
  )
   #read input from user
  choice_input = int(input("Please enter your choice: "))
  while (choice_input != 7):
    if (choice_input == 1):
      displayStatistics()
    elif (choice_input == 2):
      bookTicket()
    elif (choice_input == 3):
      displayAllTickets()
    elif (choice_input == 4):
      changeTickPriority()
    elif (choice_input == 5):
      deleteTick()
    elif (choice_input == 6):
      runEvents()   
    else:
      print("Invalid choice")

    print("\n")
    print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")
    choice_input = int(input("Please enter your choice: "))


def displayMenuUser(username): # displays the mernu for a normal user
  print("1. Book a ticket\n2. Exit")
  
  #read input from user
  choice_input = int(input("Please enter your choice: "))
  while True:
    if (choice_input == 1):
      userBookTicket(username)
    elif (choice_input == 2):
      SaveFile()
      return # return to stop iterating while the if statment is true
    else:
      print("Invalid choice")

    print("\n")
    print("1. Book a ticket\n2. Exit")
    choice_input = int(input("Please enter your choice: "))

def askUsername():# login system and menus display
  
  readFile()
  
  print("\n")
  admin_username = "admin"
  password = "admin123123"
  
  user_input = input("Please enter your username: ").lower()# .lower() to let the user enter the username or part of the username in uppercase
  
  for i in range(5): # range 5 for maximum 5 attempts.

    if (user_input == admin_username):
      pass_input = input("Please enter your password: ")
      print("\n")
      if (pass_input == password):
        displayMenuAdmin()
        return
      else:
        print("Incorrect password")
    else:
      displayMenuUser(user_input)
      return
  
askUsername()

# weakness of code: does not check the format of all user inputs #