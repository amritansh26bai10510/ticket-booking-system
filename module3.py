def payment(total):
    print("\nPayment")
    print("Amount:", total)
    print("1. Cash")
    print("2. UPI")
    print("3. Card")

    c = int(input("Choice: "))

    if c == 1:
        m = "Cash"
    elif c == 2:
        m = "UPI"
    elif c == 3:
        m = "Card"
    else:
        m = "Invalid"

    return m


def show_ticket(name, phone, ticket, number, total, method):
    print("\nTicket Details")
    print("Name:", name)
    print("Phone:", phone)
    print("Ticket:", ticket)
    print("Number:", number)
    print("Total:", total)
    print("Payment:", method)
    print("Status:", "Confirmed")
