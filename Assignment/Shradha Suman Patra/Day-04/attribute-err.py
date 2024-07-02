#defining a class
class ARR():
  #defining object
  def __init__(self):
    #object created and value assigned
    self.first="Hello"
#driver code
OBJECT= ARR()
print(OBJECT.first)
#trying to display something that doesn't exist
print(OBJECT.second)