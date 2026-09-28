# main booking file

from module1 import get_booking
from module2 import ticket_details
from module3 import payment, show_ticket

print("****************************")
print(" TICKET BOOKING SYSTEM ")
print("****************************")

# get the stuff from user
n, ph, tkt, num = get_booking()

# they cancelled?
if tkt == "None":
    print("\nBooking cancelled.")
else:
    # check price and how many left
    pr, avl, tot, ok = ticket_details(tkt, num)

    # if not ok then no tickets
    if ok == False:
        print("\nSorry, tickets are not available.")
        print("Available tickets:", avl)
    else:
        # show info
        print("\nTicket price:", pr)
        print("Available tickets:", avl)
        print("Total amount:", tot)

        # now payment
        mthd = payment(tot)

        # only if method is fine
        if mthd != "Unknown":
            show_ticket(n, ph, tkt, num, tot, mthd)
        else:
            pass   # just end
