#-----------------------------
#start3.py
#Shawn Whyte
#The main file of a program
#path - \\Main2
#-----------------------------

from basic import hi #looks into the BASIC folder and imports the program hi.py

print("I'm opening the folder BASIC and importing the file hi.py")

hi.greeting("Student") #accesses the hi.py file and passes the string STUDENT into the function GREETING for printing

print("I am running", hi.file_name) #you can also access a variable directly - so I have accessed the variable file_name in hi.py