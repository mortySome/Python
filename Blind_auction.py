logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def getting_highest_bid_value(bidders_dictionary):
  winner = ""
  highest_bid = 0
  for bidders in bidders_dictionary:
    bid_amount = bidders_dictionary[bidders]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidders
  print(f"The winner is {winner} with a bid of ${highest_bid}")
    
bids = {}

no_bidders = False
while not no_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your Bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    bids[name] = bid

    if others == "no":
        no_bidders = True
        getting_highest_bid_value(bids)
    elif others == "yes":
      print("\n" * 100)
