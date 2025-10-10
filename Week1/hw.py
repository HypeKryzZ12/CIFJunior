print("Hyper Rewards - Alpha")
print("Withdraw")
rewards = ["1. Roblox 1000 PTS", "2. Amazon 2000 PTS", "3. Fortnite 1000 PTS", "4. PUBG 3000 PTS", "5. Discord 500 PTS"]
for item in rewards:
    print(item)
prices = ["1000", "2000", "1000", "3000", "500"]
total = 0
buy_again = "yes"
while buy_again == "yes":
    shopping_cart = int(input("What do you want to withdraw? 1-5"))
    buy_more = int(input("How many do you want to buy?"))
    item_price = int(prices[shopping_cart-1])
    buy_again = str(input("Do you want to buy again? yes-no"))
    total = item_price*buy_more+total
discount = input("Do you have premium?")
if discount == "yes":
    total=total*0.75
print("Thank you for the purchase, please wait for the purchase to go through. Your total spent is:" ,total)
