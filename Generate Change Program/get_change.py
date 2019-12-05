
def main():
    item_cost = int(input("Enter the cost of the item purchased: "))
    amount_received = int(input("Enter the amount paid by the customer: "))
    calculate_remaining(item_cost, amount_received)
    
"""Calculate remaining_amount """

def calculate_remaining(item_cost, amount_received):

    remaining_amount = amount_received - item_cost
    print("Amount of remaining_amount to give back: ", remaining_amount)
    if remaining_amount >= 100:
        print("%d 100's" % (int(remaining_amount/100)))
        remaining_amount = remaining_amount - 100 * (int(remaining_amount/100))
    if remaining_amount >= 50:
        print("%d 50's" % (int(remaining_amount/50)))
        remaining_amount = remaining_amount - 50 * (int(remaining_amount/50))
    if remaining_amount >= 20:
        print("%d 20's" % (int(remaining_amount/20)))
        remaining_amount = remaining_amount - 20 * (int(remaining_amount/20))
    if remaining_amount >= 10:
        print("%d 10's" % (int(remaining_amount/10)))
        remaining_amount = remaining_amount - 10 * (int(remaining_amount/10))
    if remaining_amount >= 5:
        print("%d 5's" % (int(remaining_amount/5)))
        remaining_amount = remaining_amount - 5 * (int(remaining_amount/5))
    if remaining_amount >= 2:
        print("%d 2's" % (int(remaining_amount/2)))
        remaining_amount = remaining_amount - 2 * (int(remaining_amount/2))
    if remaining_amount >= 1:
        print("%d 1's" % (int(remaining_amount/1)))
        remaining_amount = remaining_amount - 1 * (int(remaining_amount/1))     

main()
