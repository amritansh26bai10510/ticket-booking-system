# module1.py

def get_booking():
 print("\n-- Booking Details --")
 name=input("Enter your name: ")
 phone =input("Enter phone number: ")
 print("\n1. Bus")
 print("2. Train")
 print("3. Movie")
 choice=int(input("Enter your choice: "))
 if choice==1:
  ticket="Bus"
 elif choice ==2:
  ticket= "Train"
 elif choice== 3:
  ticket ="Movie"
 else:
  print("Invalid choice")
  ticket="None"
 if ticket!="None":
  number=int(input("Enter number of tickets: "))
 else:
  number=0
 return name,phone,ticket,number
