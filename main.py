from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)


biders = []
def add_bider(name, bid): 
    biders.append({
      "name" : name,
      "bid" : bid,
    })
  

print("Welcome to the secret auction program.")
any_more = "yes"
while any_more == "yes":
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  any_more = input("Are there any other biders? Type 'yes' or 'no'.").lower()
  add_bider(name, bid)
  if any_more == "yes":
    clear()
  else:
    clear()
    val = []
    for bider in biders:
        val.append(bider["bid"])
    
    winning_bid = max(val)
    winning_bid_index = val.index(max(val))
    winner = biders[winning_bid_index]["name"]
    print(f"The winner is {winner} with a bid of {winning_bid}.")