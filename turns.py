from constants import PLAYER


class Node:    
  def __init__(self,data):    
    self.data = data;    
    self.next = None;    


class Turns:    
  #Declaring head and tail pointer as null.    
  def __init__(self):    
    self.head = Node(None);    
    self.tail = Node(None);    
    self.head.next = self.tail;    
    self.tail.next = self.head;    
        
  #This function will add the new node at the end of the list.    
  def addTurn(self,data):    
    newNode = Node(data);    
    if self.head.data is None:    
      self.head = newNode;    
      self.tail = newNode;    
      newNode.next = self.head;    
    else:    
      self.tail.next = newNode;    
      self.tail = newNode;    
      self.tail.next = self.head;    
     
  def displayTurns(self):    
    current = self.head;    
    if self.head is None:    
      print("No players present");    
      return;    
    else:   
        print('Player Turns are as follows:') 
        print(PLAYER + str(current.data.no))
        while(current.next != self.head):    
            current = current.next;    
            print(PLAYER +str(current.data.no))
            
  def getFirstPlayer(self):
    current = self.head;    
    if self.head is None:    
        print("No players present");    
        return;    
    else:   
        return current

