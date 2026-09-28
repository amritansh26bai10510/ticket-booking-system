Ticket Booking System -
This is a small Python project I made for booking tickets. You can book for bus, train or movie through the terminal.

What it does?
When you start the program it will ask your name and phone number first. After that you select Bus, Train or Movie and enter how many tickets you need. The system then checks availability, shows the total cost and gives you options to pay by Cash, UPI or Card. Once payment is done it prints the ticket confirmation. I kept the code in 3 separate files so it’s easier to manage.

Approach -
I divided the whole system into three simple modules:

module1.py – Takes user details (name, phone) and ticket choice
module2.py – Stores fixed prices and available seats for each ticket type. Also calculates total amount and checks if enough tickets are left
module3.py – Handles payment method selection and finally prints the ticket confirmation

The `main.py` file runs the whole program. It takes the details from the other three files and runs them in order. If the tickets are available, it goes to payment and then shows the ticket. If not, it stops and tells the user that tickets aren't available. I used simple conditions and functions because that's what we have used in the project.

Features -

1. Book Bus, Train or Movie tickets
2. Enter name and phone number
3. Choose number of tickets
4. Auto calculates total price
5. Checks available tickets
6. Payment options: Cash, UPI, Card
7. Shows ticket confirmation at the end

What you need -
Just Python 3. No extra libraries or packages required.

How to run -
Make sure Python is installed. Type this in terminal to check:textpython --version
Open the project folder in terminal.
Run:textpython main.py

That’s all. The program will start asking questions.
Testing
Just run it and try a few things:

1. Book normal tickets (like 2 bus tickets)
2. Try booking more than available (ex: 60 bus tickets)
3. Give wrong options for ticket type or payment
4. Complete full booking with different payment methods

You should get proper messages for success, unavailable tickets, and invalid choices.
