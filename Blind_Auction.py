# Blind Auction 
from clear import clear
print("Welcome to the Blind Auction\nEnter your name and bid amount when prompted")

cont_bidding = True
bidder_list = []

while cont_bidding:
    bidder = input("Bidder name:\n")
    bid_amount = float(input("How much is your bid?:\n$ "))
    bidder_dict = {'name': bidder, 'bid': bid_amount}
    bidder_list.append(bidder_dict)
    clear()
    result = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()
    if result == 'no':
        cont_bidding = False

winner = max(bidder_list, key = lambda x: x['bid'])
clear()
print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")

# If initializing a blank dictionary: 
# bidder_dict = {}
# bidder_dict[bidder] = bid_amount
# winner = max(bidder_dict, key = bidder_dict.get)