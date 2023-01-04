# Password Generator
# Date: Dec 6, 2022
# Author: Hiromi Honda

# Program Description: 
# Function 'four_digits_password' is a function that generates a four digits password.
# Function 'int_password' is a function that generates an n-digit integer password.
# Function 'password' is a function that generates an n-digit password using random letters and symbols.

def four_digits_password():
  import random as rd
  return rd.randint(0000, 9999)

def int_password(n):
  import random as rd
  array = [1,2,3,4,5,6,7,8,9,0]
  for i in range(n):
    print(rd.choice(array), end="")

def password(n):
  import random as rd
  array = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],['~','!','@','#','$','%','^','&','*','-','_','|','`','?','/']]
  type = []
  if n < 4:
    return
  for i in range(n):  # assign the type of character for each digits
    type.append(rd.randint(0,3))
  for i in range(n):
    if type[i] == 0:
      print(rd.randint(0,9), end="")
    elif type[i] == 1:
      print(rd.choice(array[0]), end="")
    elif type[i] == 2:
      print(rd.choice(array[1]), end="")
    else:
      print(rd.choice(array[2]), end="")
  return

four_digits_password()
int_password(10)
password(18)

# Output
# 
# 2962
# 3715236356
# ?M&5ta-C@!%79XCof9
# 
