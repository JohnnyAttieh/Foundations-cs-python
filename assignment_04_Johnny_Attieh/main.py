class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.adj_list = {}

    for node in self.nodes:
      self.adj_list[node] = []

  def printAdjList(self):
    for node in self.nodes:
      if node in self.adj_list:
        print(node, ":", self.adj_list[node])
      

  def addUser(self, node):
    if node not in self.adj_list:
      self.adj_list[node] = []
      self.nodes.append(node) 
    else:
      print("This username is already taken, choose another one")
      
  def removeUser(self, node):
    if node in self.adj_list:
      del self.adj_list[node]
          
      for other_node in self.adj_list:
        connections_lst = []
        for connection in self.adj_list[other_node]:
          if connection != node:
            connections_lst.append(connection)
        self.adj_list[other_node] = connections_lst
      print(f"User '{node}' removed successfully!")
    else:
      print(f"User '{node}' does not exist. Please check the username.")

  def addConnection(self, node1, node2):
    if node1 in self.adj_list and node2 in self.adj_list:
      self.adj_list[node1].append(node2)
      self.adj_list[node2].append(node1)
      print(f"Connection added between '{node1}' and '{node2}'")
    else:
      print("One or both users do not exist. Please check the usernames.")

  def removeConnection(self, node1, node2):
    if node1 in self.adj_list and node2 in self.adj_list:
      self.adj_list[node1].remove(node2)
      self.adj_list[node2].remove(node1)
      print(f"Connection removed between '{node1}' and '{node2}'")
    else:
      print("One or both users do not exist. Please check the usernames.")

  def getFriends(self, node):
    if node in self.adj_list:
      return self.adj_list[node]
    else:
      return []

  def printUsers(self):
    for node in self.adj_list:
      print(node)

nodes = ["georgio","johnny","charbel","chris","fred"]
graph = Graph(nodes)

def displayMenu():
  print("1. Add a user to the platform.\n2. Remove a user from the platform.\n3. Send a friend request to another user.\n4. Remove a friend from your list.\n5. View your list of friends.\n6. View the list of users on the platform.\n7. Exit")

  choice = int(input("Enter your choice: "))
  
  while(choice != 7):
    if (choice == 1):
      username = input("Enter a username to add: ")
      graph.addUser(username)
      graph.printAdjList()

    elif (choice == 2):
      username2 = input("Enter a username to remove: ")
      graph.removeUser(username2)
      graph.printAdjList()

    elif (choice == 3):
      user1 = input("Enter username of first user: ")
      user2 = input("Enter username of second user: ")
      graph.addConnection(user1,user2)
      graph.printAdjList()
      
    elif (choice == 4):
      user1 = input("Enter username of first user: ")
      user2 = input("Enter username of second user: ")
      graph.removeConnection(user1, user2)
      graph.printAdjList()

    elif (choice == 5):
      user3 = input("Enter your username: ")
      print(graph.getFriends(user3))

    elif (choice == 6):
      graph.printUsers()

    else:
      print("Invalide choice")

    print("\n")
    print("1. Add a user to the platform.\n2. Remove a user from the platform.\n3. Send a friend request to another user.\n4. Remove a friend from your list.\n5. View your list of friends.\n6. View the list of users on the platform.\n7. Exit")

    choice = int(input("Enter your choice: "))
  
displayMenu()
