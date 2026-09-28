#module2.py
def ticket_details(ticket,number):
 if ticket=="Bus":
  price=150
  available=50
 elif ticket == "Train":
  price =750
  available=100
 elif ticket=="Movie":
  price=180
  available =80
 else:
  price=0
  available=0
 if number<=available and number>0:
  total=price*number
  return price,available,total,True
 else:
  return price,available,0,False
