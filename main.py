# defining functions to be called later. They are placeholders for now

def choice1():
  print("\n Initiate conversation about choice 1")

def choice2():
  print("\n Initiate conversation about choice 2")

def choice3():
  print("\n Initiate conversation about choice 3")


# Welcome statmeents
print("Welcome to the ELite 101 Chatbot!")
name = str(input("What is your name? "))
age = int(input("\n Nice to meet you " + name + "! How old are you? "))

print(" \n Wow! " + str(age) + " is a wonderful age to be. How can I be of assistance? ")

print("\n Please pick a choice: ")
print(" 1. Placeholder 1 \n 2. Placeholder 2 \n 3. Placeholder 3 \n 4. Exit the conversation") 

choice = input("Enter the number of your choice: ")
if choice == "1":
  choice1() # functions will call the functions defined at the top to initiate the conversation

if choice == "2":
  choice2()

if choice == "3":
  choice3()

if choice == "4": # Exit command
  print("\n Bye " + name + ", have an amazing day! ")




  


               










